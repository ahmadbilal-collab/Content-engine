"""
HOT TAKE GENERATOR
Generates Ahmad's unique angles on news, trends, and industry events.
Creates contrarian but well-reasoned perspectives backed by experience.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
import json

# JSON schema for hot takes
HOT_TAKE_SCHEMA = {
    "type": "object",
    "properties": {
        "news_item": {"type": "string"},
        "conventional_take": {"type": "string"},
        "ahmad_angle": {"type": "string"},
        "supporting_experience": {"type": "string"},
        "contrarian_element": {"type": "string"},
        "philosophical_connection": {"type": "string"},
        "content_hook": {"type": "string"},
        "content_type": {
            "type": "string",
            "enum": ["linkedin_post", "twitter_thread", "article", "talk_topic"]
        },
        "confidence": {
            "type": "string",
            "enum": ["high", "medium", "low"]
        },
        "urgency": {
            "type": "string",
            "enum": ["post_today", "this_week", "whenever"]
        }
    }
}


class HotTakeGenerator:
    """
    Generates Ahmad Bilal's unique perspectives on AI news and trends.
    Creates hot takes that are contrarian but substantive.
    """

    def __init__(self, gemini_client):
        """
        Initialize the hot take generator.

        Args:
            gemini_client: Configured GeminiClient instance
        """
        self.gemini = gemini_client

    def generate_hot_take(self, news_item: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate Ahmad's unique take on a news item.

        Args:
            news_item: Dict with headline, summary, source

        Returns:
            Hot take with unique angle and content hook
        """
        prompt = f"""
        Generate Ahmad Bilal's unique take on this news:

        NEWS: {news_item.get('headline', 'Unknown headline')}
        DETAILS: {news_item.get('summary', 'No details provided')}
        SOURCE: {news_item.get('source', 'Unknown source')}

        ## AHMAD'S CONTEXT
        - He's actively building AI interfaces daily
        - He's tested most vibe coding tools hands-on
        - He has 10+ industry experience (gov, mobility, automotive, etc.)
        - He thinks about philosophy, not just tactics
        - His signature concept is "The Intent Layer"
        - He's not a Silicon Valley insider - global perspective

        ## GENERATE

        1. CONVENTIONAL TAKE: What most people will say about this

        2. AHMAD'S ANGLE: What unique perspective can he offer?
           - Connect to his hands-on experience
           - What pattern does this fit that others miss?
           - What's the second-order implication?
           - What does this mean for designers/practitioners?

        3. CONTRARIAN ELEMENT: Where might he respectfully disagree
           with the mainstream narrative? (Only if authentic and substantive)

        4. PHILOSOPHICAL CONNECTION: What bigger question does this raise?
           - Human agency implications
           - The future of design/development
           - Ethical dimensions
           - What kind of future are we building?

        5. CONTENT HOOK: A compelling first line for a post about this
           - NOT: "Here's my take on..."
           - YES: Something that stops the scroll and makes people think

        6. SUPPORTING EXPERIENCE: Specific experience from Ahmad's background
           that makes his take credible

        7. CONFIDENCE: How confident in this take (high/medium/low)

        8. URGENCY: When to post (post_today/this_week/whenever)

        Be specific. Don't be generic. Make it sound like Ahmad, not a bot.
        Don't force controversy - only be contrarian when there's genuine substance.
        """

        result = self.gemini.generate_structured(prompt, HOT_TAKE_SCHEMA)
        result["generated_at"] = datetime.now().isoformat()
        result["source_news"] = news_item
        return result

    def generate_contrarian_take(self, popular_opinion: str) -> Dict[str, Any]:
        """
        Generate a thoughtful contrarian perspective on a popular opinion.

        Args:
            popular_opinion: The mainstream view to potentially counter

        Returns:
            Contrarian take with supporting reasoning
        """
        prompt = f"""
        The popular opinion in tech/design right now is:
        "{popular_opinion}"

        Generate Ahmad Bilal's contrarian take. Rules:
        - Only be contrarian if there's genuine substance
        - Back it up with experience or evidence
        - Be respectful, not inflammatory
        - Aim to add nuance, not just disagree
        - Connect to bigger themes
        - Don't be contrarian for its own sake

        ## AHMAD'S BACKGROUND FOR CREDIBILITY
        - 10+ years across automotive, government, education, mobility
        - Currently building AI interfaces hands-on
        - Tested major vibe coding tools extensively
        - MENA + global perspective (not just Silicon Valley)

        ## STRUCTURE YOUR RESPONSE

        1. ACKNOWLEDGE: What's TRUE in the popular opinion

        2. COMPLICATE: What's being missed or oversimplified

        3. COUNTER: Ahmad's alternative view with evidence

        4. EXPERIENCE: Specific experience that informs this view

        5. LARGER PRINCIPLE: The bigger truth this reveals

        6. HOOK: How to open a post about this

        7. AUTHENTICITY CHECK: Is this genuinely contrarian or forced?
           If forced, say so and provide a "nuanced addition" instead

        Return as JSON matching the hot take schema.
        """

        result = self.gemini.generate_structured(prompt, HOT_TAKE_SCHEMA)
        result["type"] = "contrarian"
        result["original_opinion"] = popular_opinion
        result["generated_at"] = datetime.now().isoformat()
        return result

    def generate_pattern_recognition(
        self,
        observations: List[str],
        context: str = ""
    ) -> Dict[str, Any]:
        """
        Generate a hot take based on pattern recognition across observations.

        Args:
            observations: List of things observed/noticed
            context: Additional context

        Returns:
            Pattern-based insight
        """
        observations_str = "\n".join(f"- {obs}" for obs in observations)

        prompt = f"""
        Ahmad has noticed these patterns/observations:

        {observations_str}

        Additional context: {context}

        ## GENERATE PATTERN-BASED INSIGHT

        1. THE PATTERN: What connects these observations?

        2. WHY OTHERS MISS IT: Why isn't this obvious to everyone?

        3. IMPLICATIONS: What does this pattern suggest about:
           - The future of AI interfaces
           - What designers should do differently
           - What companies are getting wrong/right

        4. PREDICTION: Based on this pattern, what happens next?

        5. AHMAD'S UNIQUE VIEW: Why is he positioned to see this pattern?
           (Experience across industries, hands-on testing, etc.)

        6. CONTENT ANGLE: How to present this as thought leadership

        7. HOOK: Opening line that captures the insight

        Return as JSON with these fields plus standard hot take fields.
        """

        schema = {
            **HOT_TAKE_SCHEMA,
            "properties": {
                **HOT_TAKE_SCHEMA["properties"],
                "pattern": {"type": "string"},
                "implications": {"type": "array", "items": {"type": "string"}},
                "prediction": {"type": "string"},
            }
        }

        result = self.gemini.generate_structured(prompt, schema)
        result["type"] = "pattern_recognition"
        result["source_observations"] = observations
        result["generated_at"] = datetime.now().isoformat()
        return result

    def generate_philosophical_angle(
        self,
        topic: str,
        tactical_observation: str
    ) -> Dict[str, Any]:
        """
        Elevate a tactical observation to philosophical insight.

        Args:
            topic: The topic area
            tactical_observation: The practical/tactical observation

        Returns:
            Philosophical hot take
        """
        prompt = f"""
        Topic: {topic}
        Tactical observation: {tactical_observation}

        ## ELEVATE TO PHILOSOPHY

        Ahmad doesn't just comment on tactics - he connects to bigger meaning.
        Take this tactical observation and find the philosophical depth.

        1. THE TACTICAL: What's the practical observation?

        2. THE QUESTION: What bigger question does this raise?
           - About human agency
           - About creativity and authorship
           - About the future of work
           - About what we're choosing to build
           - About human-AI relationship

        3. THE TENSION: What fundamental tension does this reveal?

        4. AHMAD'S POSITION: Where does he stand on this tension?
           (Not wishy-washy - a clear, defensible position)

        5. THE STAKES: Why should non-designers care?
           (Connect to broader human experience)

        6. CONTENT APPROACH: How to write about this
           - For LinkedIn leaders
           - For a keynote
           - For a major publication

        7. SIGNATURE CONNECTION: How does this connect to
           "The Intent Layer" or other Ahmad signature concepts?

        Return as JSON with philosophical depth.
        """

        schema = {
            **HOT_TAKE_SCHEMA,
            "properties": {
                **HOT_TAKE_SCHEMA["properties"],
                "bigger_question": {"type": "string"},
                "tension": {"type": "string"},
                "position": {"type": "string"},
                "stakes": {"type": "string"},
            }
        }

        result = self.gemini.generate_structured(prompt, schema)
        result["type"] = "philosophical"
        result["source_tactical"] = tactical_observation
        result["topic"] = topic
        result["generated_at"] = datetime.now().isoformat()
        return result

    def batch_generate_hot_takes(
        self,
        news_items: List[Dict[str, Any]],
        max_takes: int = 5
    ) -> List[Dict[str, Any]]:
        """
        Generate hot takes for multiple news items.

        Args:
            news_items: List of news items
            max_takes: Maximum number of takes to generate

        Returns:
            List of hot takes, prioritized
        """
        # First, prioritize which items deserve hot takes
        prompt = f"""
        Review these news items and select the top {max_takes} that deserve
        Ahmad Bilal's hot take:

        {json.dumps(news_items, indent=2)}

        ## SELECTION CRITERIA
        1. Relevance to AI interfaces / design
        2. Opportunity for unique angle
        3. Timeliness / urgency
        4. Potential for philosophical depth
        5. Connection to Ahmad's experience

        Return indices of top {max_takes} items with brief reasoning.
        """

        # Get prioritized indices
        priority_result = self.gemini.generate_structured(prompt, {
            "type": "object",
            "properties": {
                "selected_indices": {"type": "array", "items": {"type": "integer"}},
                "reasoning": {"type": "array", "items": {"type": "string"}}
            }
        })

        # Generate hot takes for selected items
        hot_takes = []
        selected = priority_result.get("selected_indices", [])[:max_takes]

        for idx in selected:
            if idx < len(news_items):
                take = self.generate_hot_take(news_items[idx])
                hot_takes.append(take)

        return hot_takes

    def refine_hot_take(
        self,
        draft_take: Dict[str, Any],
        feedback: str
    ) -> Dict[str, Any]:
        """
        Refine a hot take based on feedback.

        Args:
            draft_take: The initial hot take
            feedback: Feedback for refinement

        Returns:
            Refined hot take
        """
        prompt = f"""
        Refine this hot take based on feedback:

        ## ORIGINAL TAKE
        {json.dumps(draft_take, indent=2)}

        ## FEEDBACK
        {feedback}

        ## REFINEMENT INSTRUCTIONS
        - Keep what's working
        - Address the feedback specifically
        - Maintain Ahmad's voice
        - Don't lose the contrarian edge (if appropriate)
        - Ensure it's still actionable as content

        Return refined hot take as JSON.
        """

        result = self.gemini.generate_structured(prompt, HOT_TAKE_SCHEMA)
        result["refined_from"] = draft_take
        result["feedback_addressed"] = feedback
        result["generated_at"] = datetime.now().isoformat()
        return result
