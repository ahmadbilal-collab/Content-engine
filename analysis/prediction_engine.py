"""
PREDICTION ENGINE
Generates and tracks predictions about AI, design, and technology.
Maintains prediction log for accountability and content generation.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path
import json


# JSON schema for predictions
PREDICTION_SCHEMA = {
    "type": "object",
    "properties": {
        "prediction": {"type": "string"},
        "category": {
            "type": "string",
            "enum": [
                "ai_interfaces",
                "vibe_coding",
                "tools",
                "industry",
                "society",
                "design_practice"
            ]
        },
        "timeframe": {
            "type": "string",
            "enum": ["3_months", "6_months", "1_year", "2_years", "5_years"]
        },
        "confidence": {
            "type": "string",
            "enum": ["high", "medium", "low"]
        },
        "reasoning": {"type": "string"},
        "signals_to_watch": {"type": "array", "items": {"type": "string"}},
        "what_could_prove_wrong": {"type": "string"},
        "content_angle": {"type": "string"}
    }
}


class PredictionEngine:
    """
    Generates and tracks predictions for thought leadership content.
    Maintains accountability through prediction logging.
    """

    def __init__(self, gemini_client, data_dir: str = "data"):
        """
        Initialize the prediction engine.

        Args:
            gemini_client: Configured GeminiClient instance
            data_dir: Directory for storing prediction data
        """
        self.gemini = gemini_client
        self.data_dir = Path(data_dir)
        self.predictions_file = self.data_dir / "predictions_log.json"
        self._ensure_data_dir()

    def _ensure_data_dir(self):
        """Ensure data directory exists."""
        self.data_dir.mkdir(parents=True, exist_ok=True)
        if not self.predictions_file.exists():
            self._save_predictions([])

    def _load_predictions(self) -> List[Dict[str, Any]]:
        """Load predictions database."""
        if self.predictions_file.exists():
            with open(self.predictions_file, "r") as f:
                return json.load(f)
        return []

    def _save_predictions(self, predictions: List[Dict[str, Any]]):
        """Save predictions database."""
        with open(self.predictions_file, "w") as f:
            json.dump(predictions, f, indent=2)

    def generate_predictions(
        self,
        research_context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate predictions based on current research context.

        Args:
            research_context: Recent research/news data

        Returns:
            Set of predictions across categories
        """
        prompt = f"""
        Based on this research context:
        {json.dumps(research_context, indent=2) if research_context else "General AI industry knowledge"}

        And Ahmad Bilal's positioning as someone actively building AI interfaces,
        generate 5-7 predictions across different timeframes and categories:

        ## PREDICTION CATEGORIES

        ### 1. AI INTERFACES (Ahmad's core area)
        - How will people interact with AI in 1 year? 3 years?
        - What interface paradigm will win?
        - What will die?
        - What new patterns will emerge?

        ### 2. VIBE CODING / AI DEVELOPMENT
        - Will prompt-to-product become mainstream?
        - What happens to traditional development?
        - Which tools will win/lose?
        - How will this change who can build software?

        ### 3. DESIGN PRACTICE
        - How will designer roles change?
        - What skills become more/less valuable?
        - What new roles emerge?
        - How will design education adapt?

        ### 4. INDUSTRY STRUCTURE
        - Which companies are positioned well/poorly?
        - Where's disruption coming from?
        - What will consolidate?
        - New categories that will emerge?

        ### 5. BIGGER PICTURE
        - Human-AI relationship evolution
        - Societal implications
        - What kind of future are we building?
        - The unintended consequences

        ## FOR EACH PREDICTION

        - prediction: Make it specific and falsifiable
        - category: Which category
        - timeframe: 3_months, 6_months, 1_year, 2_years, or 5_years
        - confidence: high/medium/low with reasoning
        - reasoning: Why you predict this
        - signals_to_watch: What would confirm/deny it
        - what_could_prove_wrong: Steel-man the counter case
        - content_angle: How to write about this for thought leadership

        ## PREDICTION QUALITY RULES
        - Be bold but reasoned
        - Avoid obvious predictions everyone makes
        - Connect to Ahmad's hands-on experience
        - Include at least one contrarian prediction
        - Include at least one long-term (5-year) prediction

        Return as JSON array of predictions.
        """

        schema = {
            "type": "object",
            "properties": {
                "predictions": {
                    "type": "array",
                    "items": PREDICTION_SCHEMA
                },
                "meta": {
                    "type": "object",
                    "properties": {
                        "generated_date": {"type": "string"},
                        "context_summary": {"type": "string"},
                        "boldest_prediction": {"type": "string"},
                        "most_controversial": {"type": "string"}
                    }
                }
            }
        }

        result = self.gemini.generate_structured(prompt, schema)

        # Log predictions
        if "predictions" in result:
            self._log_predictions(result["predictions"])

        result["generated_at"] = datetime.now().isoformat()
        return result

    def _log_predictions(self, new_predictions: List[Dict[str, Any]]):
        """Log new predictions to the database."""
        predictions = self._load_predictions()

        for pred in new_predictions:
            pred["id"] = f"pred_{datetime.now().strftime('%Y%m%d%H%M%S')}_{len(predictions)}"
            pred["created_at"] = datetime.now().isoformat()
            pred["status"] = "active"
            pred["updates"] = []
            predictions.append(pred)

        self._save_predictions(predictions)

    def update_prediction(
        self,
        prediction_id: str,
        update_type: str,
        notes: str,
        new_confidence: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Update a prediction with new information.

        Args:
            prediction_id: ID of the prediction
            update_type: Type of update (evidence_for, evidence_against, refinement)
            notes: Update notes
            new_confidence: Optional new confidence level

        Returns:
            Updated prediction
        """
        predictions = self._load_predictions()

        for pred in predictions:
            if pred.get("id") == prediction_id:
                pred["updates"].append({
                    "date": datetime.now().isoformat(),
                    "type": update_type,
                    "notes": notes,
                    "confidence_change": new_confidence
                })
                if new_confidence:
                    pred["original_confidence"] = pred.get("confidence")
                    pred["confidence"] = new_confidence
                self._save_predictions(predictions)
                return pred

        return {"error": f"Prediction {prediction_id} not found"}

    def check_predictions(self) -> Dict[str, Any]:
        """
        Check status of all active predictions using search grounding.

        Returns:
            Prediction status update
        """
        predictions = self._load_predictions()
        active = [p for p in predictions if p.get("status") == "active"]

        if not active:
            return {"message": "No active predictions to check"}

        prompt = f"""
        Check the status of these predictions by searching for current evidence:

        {json.dumps(active, indent=2)}

        For each prediction:
        1. Search for current news/evidence relevant to the prediction
        2. Assess if evidence supports or contradicts the prediction
        3. Suggest confidence adjustment if warranted
        4. Identify if prediction can be marked as confirmed/denied

        Return as JSON:
        {{
            "prediction_updates": [
                {{
                    "id": "...",
                    "prediction": "...",
                    "evidence_found": [...],
                    "evidence_direction": "supports/contradicts/neutral",
                    "confidence_adjustment": "increase/decrease/same",
                    "new_confidence": "...",
                    "can_resolve": true/false,
                    "resolution": "confirmed/denied/null",
                    "notes": "..."
                }}
            ],
            "check_date": "...",
            "content_opportunities": [...]
        }}
        """

        result = self.gemini.research_with_search(prompt)

        # Apply updates if any
        if "prediction_updates" in result:
            for update in result["prediction_updates"]:
                if update.get("id"):
                    self.update_prediction(
                        update["id"],
                        "status_check",
                        update.get("notes", ""),
                        update.get("new_confidence")
                    )

        return result

    def generate_prediction_content(
        self,
        prediction: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate content based on a prediction.

        Args:
            prediction: Prediction to create content from

        Returns:
            Content pieces for different channels
        """
        prompt = f"""
        Create thought leadership content based on this prediction:

        {json.dumps(prediction, indent=2)}

        ## GENERATE CONTENT FOR:

        ### 1. LINKEDIN POST
        - Hook that captures attention
        - The prediction clearly stated
        - Reasoning in accessible language
        - What to watch for
        - Discussion prompt
        - 1200-1800 characters

        ### 2. TWITTER THREAD (5-7 tweets)
        - Opening hook
        - The prediction
        - Key reasoning points
        - What could prove it wrong (intellectual honesty)
        - What to watch
        - Engagement prompt

        ### 3. NEWSLETTER SECTION
        - Longer exploration of the prediction
        - More nuance and caveats
        - Connection to broader patterns
        - Personal perspective

        ## TONE
        - Confident but not arrogant
        - Intellectually honest (acknowledge uncertainty)
        - Connect to Ahmad's hands-on experience
        - Make it actionable for readers

        Return as JSON with content for each channel.
        """

        return self.gemini.generate_structured(prompt, {
            "type": "object",
            "properties": {
                "linkedin": {
                    "type": "object",
                    "properties": {
                        "hook": {"type": "string"},
                        "body": {"type": "string"},
                        "cta": {"type": "string"},
                        "hashtags": {"type": "array"}
                    }
                },
                "twitter_thread": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "newsletter_section": {"type": "string"}
            }
        })

    def generate_prediction_update_content(
        self,
        prediction_id: str
    ) -> Dict[str, Any]:
        """
        Generate content for a prediction update (was I right/wrong?).

        Args:
            prediction_id: ID of the prediction

        Returns:
            Update content
        """
        predictions = self._load_predictions()
        prediction = next((p for p in predictions if p.get("id") == prediction_id), None)

        if not prediction:
            return {"error": f"Prediction {prediction_id} not found"}

        prompt = f"""
        Generate a prediction update/accountability post:

        ## ORIGINAL PREDICTION
        {json.dumps(prediction, indent=2)}

        ## GENERATE
        A post that:
        1. Reminds readers of the original prediction
        2. Shares what has happened since
        3. Honestly assesses: was I right, wrong, or too early to tell?
        4. What I learned from being right/wrong
        5. Refined prediction if applicable

        ## TONE
        - Intellectually honest
        - Not defensive if wrong
        - Not gloating if right
        - Learning orientation
        - Builds credibility through accountability

        Return as JSON with LinkedIn post and key learnings.
        """

        return self.gemini.generate_structured(prompt, {
            "type": "object",
            "properties": {
                "linkedin_post": {"type": "string"},
                "assessment": {"type": "string", "enum": ["correct", "incorrect", "partially_correct", "too_early"]},
                "key_learnings": {"type": "array", "items": {"type": "string"}},
                "refined_prediction": {"type": "string"}
            }
        })

    def get_due_predictions(self) -> List[Dict[str, Any]]:
        """
        Get predictions that are due for checking based on timeframe.

        Returns:
            List of predictions due for review
        """
        predictions = self._load_predictions()
        now = datetime.now()
        due = []

        timeframe_days = {
            "3_months": 90,
            "6_months": 180,
            "1_year": 365,
            "2_years": 730,
            "5_years": 1825
        }

        for pred in predictions:
            if pred.get("status") != "active":
                continue

            created = datetime.fromisoformat(pred["created_at"])
            timeframe = pred.get("timeframe", "1_year")
            days = timeframe_days.get(timeframe, 365)

            # Check if we're past 80% of the timeframe
            elapsed = (now - created).days
            if elapsed >= days * 0.8:
                pred["check_reason"] = f"Approaching {timeframe} timeframe"
                due.append(pred)

        return due

    def get_prediction_stats(self) -> Dict[str, Any]:
        """
        Get statistics on predictions for content/credibility.

        Returns:
            Prediction statistics
        """
        predictions = self._load_predictions()

        stats = {
            "total": len(predictions),
            "by_status": {},
            "by_category": {},
            "by_confidence": {},
            "by_timeframe": {},
            "accuracy_rate": None,
            "recent_predictions": [],
            "upcoming_checks": []
        }

        resolved = []
        for pred in predictions:
            status = pred.get("status", "active")
            category = pred.get("category", "unknown")
            confidence = pred.get("confidence", "unknown")
            timeframe = pred.get("timeframe", "unknown")

            stats["by_status"][status] = stats["by_status"].get(status, 0) + 1
            stats["by_category"][category] = stats["by_category"].get(category, 0) + 1
            stats["by_confidence"][confidence] = stats["by_confidence"].get(confidence, 0) + 1
            stats["by_timeframe"][timeframe] = stats["by_timeframe"].get(timeframe, 0) + 1

            if status in ["confirmed", "denied"]:
                resolved.append(pred)

        # Calculate accuracy
        if resolved:
            correct = sum(1 for p in resolved if p.get("status") == "confirmed")
            stats["accuracy_rate"] = correct / len(resolved)

        # Get recent predictions
        sorted_preds = sorted(predictions, key=lambda x: x.get("created_at", ""), reverse=True)
        stats["recent_predictions"] = sorted_preds[:5]

        # Get upcoming checks
        stats["upcoming_checks"] = self.get_due_predictions()

        return stats
