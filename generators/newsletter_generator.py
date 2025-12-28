"""
NEWSLETTER GENERATOR
"Dispatches from the AI Design Frontier"
Weekly newsletter with exclusive insights, lab notes, and predictions.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
import json


# Newsletter schema
NEWSLETTER_SCHEMA = {
    "type": "object",
    "properties": {
        "subject_line": {"type": "string"},
        "preview_text": {"type": "string"},
        "opening_hook": {"type": "string"},
        "main_insight": {
            "type": "object",
            "properties": {
                "headline": {"type": "string"},
                "body": {"type": "string"},
                "takeaway": {"type": "string"}
            }
        },
        "from_the_lab": {
            "type": "object",
            "properties": {
                "what_i_tested": {"type": "string"},
                "what_i_learned": {"type": "string"},
                "recommendation": {"type": "string"}
            }
        },
        "prediction_corner": {
            "type": "object",
            "properties": {
                "prediction": {"type": "string"},
                "reasoning": {"type": "string"},
                "confidence": {"type": "string"}
            }
        },
        "links_worth_your_time": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "url": {"type": "string"},
                    "why_it_matters": {"type": "string"}
                }
            }
        },
        "one_question": {"type": "string"},
        "closing": {"type": "string"}
    }
}


class NewsletterGenerator:
    """
    Generates weekly newsletter content.
    "Dispatches from the AI Design Frontier"
    """

    def __init__(self, gemini_client):
        """
        Initialize the newsletter generator.

        Args:
            gemini_client: Configured GeminiClient instance
        """
        self.gemini = gemini_client
        self.newsletter_name = "Dispatches from the AI Design Frontier"

    def generate_weekly_newsletter(
        self,
        weekly_research: Dict[str, Any],
        lab_notes: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Generate the weekly newsletter.

        Args:
            weekly_research: Aggregated research from the week
            lab_notes: Ahmad's personal testing notes

        Returns:
            Complete newsletter content
        """
        prompt = f"""
        Generate this week's newsletter: "{self.newsletter_name}"

        ## NEWSLETTER VIBE
        - Like a letter from a friend who's deep in the arena
        - Practitioner insights, not industry analysis
        - Personal voice, philosophical depth
        - Exclusive—stuff not in the LinkedIn posts
        - Worth subscribing to

        ## THIS WEEK'S CONTEXT
        Research: {json.dumps(weekly_research, indent=2) if weekly_research else "Use current AI knowledge"}
        Lab Notes: {json.dumps(lab_notes, indent=2) if lab_notes else "Based on typical week of testing"}

        ## SECTIONS TO GENERATE

        ### 1. SUBJECT LINE
        - Curiosity-inducing
        - Not clickbait
        - Hints at main insight
        - Under 50 characters

        ### 2. PREVIEW TEXT
        - Complements subject line
        - Creates urgency to open
        - Under 100 characters

        ### 3. OPENING HOOK (2-3 paragraphs)
        Start with something surprising, personal, or provocative from the week.
        NOT: "This week in AI..."
        NOT: "Welcome to another issue..."
        YES: "I broke three vibe coding tools this week trying to..."
        YES: "A conversation with a government minister made me rethink..."
        YES: "I was wrong about something. Let me explain..."

        ### 4. MAIN INSIGHT (400-600 words)
        One big idea, well developed. This is the flagship content.
        - What pattern did you notice?
        - What changed your mind?
        - What prediction would you make?
        - Connect tactical to philosophical
        - Include specific examples
        - Make it actionable or thought-provoking

        ### 5. FROM THE LAB (200-300 words)
        What you actually tested/built this week.
        - Specific tool or approach
        - What worked / what didn't
        - Would you recommend it?
        - Raw, honest practitioner notes
        - Not a formal review—lab notes

        ### 6. PREDICTION CORNER (100-150 words)
        One prediction with reasoning.
        - Bold but thoughtful
        - Include timeframe
        - Include confidence level
        - What would prove you wrong

        ### 7. LINKS WORTH YOUR TIME (3-5 links)
        Curated, not comprehensive.
        For each:
        - Title of the piece
        - Source/URL placeholder
        - Why it matters (2-3 sentences)
        - Your one-line take

        ### 8. ONE QUESTION
        Leave them with a question to ponder.
        Something that doesn't have an easy answer.
        Makes them think throughout the week.

        ### 9. CLOSING
        Personal, warm, forward-looking.
        What you're excited about for next week.
        Not "until next time" generic.

        ## VOICE
        - Personal, not corporate
        - Opinionated, not neutral
        - Practitioner, not pundit
        - Thoughtful, not rushed
        - Exclusive, not recycled

        ## WORD COUNT
        Total newsletter: 1000-1500 words
        Should take 5-7 minutes to read

        Return as complete newsletter schema.
        """

        result = self.gemini.generate_structured(prompt, NEWSLETTER_SCHEMA, model="pro")
        result["generated_at"] = datetime.now().isoformat()
        result["newsletter_name"] = self.newsletter_name
        return result

    def generate_special_edition(
        self,
        topic: str,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate a special edition newsletter on a specific topic.

        Args:
            topic: Special topic to cover
            context: Relevant context/research

        Returns:
            Special edition newsletter
        """
        prompt = f"""
        Generate a special edition newsletter on: {topic}

        ## CONTEXT
        {json.dumps(context, indent=2)}

        ## SPECIAL EDITION FORMAT

        This is a deeper dive than usual:

        1. SUBJECT LINE
        "[Special Edition] {topic}"

        2. OPENING
        Why this deserves a special edition
        What prompted this deep dive

        3. THE DEEP DIVE (800-1200 words)
        Comprehensive but accessible exploration:
        - What's happening
        - Why it matters
        - Ahmad's unique perspective
        - Implications for practitioners
        - Predictions

        4. PRACTICAL TAKEAWAYS
        3-5 actionable insights

        5. WHAT I'M STILL FIGURING OUT
        Honest about uncertainties

        6. CLOSING
        What this means for the future

        Return as newsletter schema with expanded main_insight.
        """

        result = self.gemini.generate_structured(prompt, NEWSLETTER_SCHEMA, model="pro")
        result["edition_type"] = "special"
        result["topic"] = topic
        result["generated_at"] = datetime.now().isoformat()
        return result

    def generate_prediction_review(
        self,
        predictions: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Generate quarterly prediction review newsletter.

        Args:
            predictions: List of predictions to review

        Returns:
            Prediction review newsletter
        """
        prompt = f"""
        Generate a prediction review newsletter:

        ## PREDICTIONS TO REVIEW
        {json.dumps(predictions, indent=2)}

        ## FORMAT

        1. SUBJECT LINE
        "Prediction Check: Where I Was Right (and Wrong)"

        2. OPENING
        Set up the accountability angle
        Why tracking predictions matters

        3. PREDICTIONS REVIEWED
        For each prediction:
        - What I predicted
        - What actually happened
        - Was I right/wrong/too early?
        - What I learned

        4. OVERALL ACCURACY
        Honest assessment
        Patterns in what I get right/wrong

        5. REFINED PREDICTIONS
        Updated predictions based on learning

        6. CLOSING
        Intellectual honesty builds credibility

        Return as newsletter format.
        """

        return self.gemini.generate_structured(prompt, NEWSLETTER_SCHEMA, model="pro")

    def format_newsletter_markdown(self, newsletter: Dict[str, Any]) -> str:
        """
        Format newsletter as markdown for publishing.

        Args:
            newsletter: Newsletter object

        Returns:
            Markdown-formatted newsletter
        """
        md = []

        # Header
        md.append(f"# {self.newsletter_name}")
        md.append("")

        # Subject line for reference
        if newsletter.get("subject_line"):
            md.append(f"**Subject:** {newsletter['subject_line']}")
            md.append(f"**Preview:** {newsletter.get('preview_text', '')}")
            md.append("")
            md.append("---")
            md.append("")

        # Opening
        if newsletter.get("opening_hook"):
            md.append(newsletter["opening_hook"])
            md.append("")

        # Main insight
        if newsletter.get("main_insight"):
            insight = newsletter["main_insight"]
            md.append(f"## {insight.get('headline', 'This Week\\'s Insight')}")
            md.append("")
            md.append(insight.get("body", ""))
            md.append("")
            if insight.get("takeaway"):
                md.append(f"**Key Takeaway:** {insight['takeaway']}")
                md.append("")

        # From the lab
        if newsletter.get("from_the_lab"):
            lab = newsletter["from_the_lab"]
            md.append("## From the Lab")
            md.append("")
            md.append(f"**What I Tested:** {lab.get('what_i_tested', '')}")
            md.append("")
            md.append(f"**What I Learned:** {lab.get('what_i_learned', '')}")
            md.append("")
            md.append(f"**Recommendation:** {lab.get('recommendation', '')}")
            md.append("")

        # Prediction corner
        if newsletter.get("prediction_corner"):
            pred = newsletter["prediction_corner"]
            md.append("## Prediction Corner")
            md.append("")
            md.append(f"**Prediction:** {pred.get('prediction', '')}")
            md.append("")
            md.append(f"**Reasoning:** {pred.get('reasoning', '')}")
            md.append("")
            md.append(f"**Confidence:** {pred.get('confidence', '')}")
            md.append("")

        # Links
        if newsletter.get("links_worth_your_time"):
            md.append("## Links Worth Your Time")
            md.append("")
            for link in newsletter["links_worth_your_time"]:
                md.append(f"### [{link.get('title', 'Link')}]({link.get('url', '#')})")
                md.append(link.get("why_it_matters", ""))
                md.append("")

        # One question
        if newsletter.get("one_question"):
            md.append("## One Question")
            md.append("")
            md.append(f"*{newsletter['one_question']}*")
            md.append("")

        # Closing
        if newsletter.get("closing"):
            md.append("---")
            md.append("")
            md.append(newsletter["closing"])
            md.append("")

        return "\n".join(md)

    def format_newsletter_html(self, newsletter: Dict[str, Any]) -> str:
        """
        Format newsletter as basic HTML for email.

        Args:
            newsletter: Newsletter object

        Returns:
            HTML-formatted newsletter
        """
        # Convert markdown to basic HTML
        md = self.format_newsletter_markdown(newsletter)

        # Simple markdown to HTML conversion
        html = md
        html = html.replace("## ", "<h2>").replace("\n\n", "</h2>\n\n<p>")
        html = html.replace("### ", "<h3>").replace("\n\n", "</h3>\n\n<p>")
        html = html.replace("**", "<strong>").replace("**", "</strong>")
        html = html.replace("*", "<em>").replace("*", "</em>")
        html = html.replace("---", "<hr>")

        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>{newsletter.get('subject_line', self.newsletter_name)}</title>
        </head>
        <body style="font-family: Georgia, serif; max-width: 600px; margin: 0 auto; padding: 20px;">
            {html}
        </body>
        </html>
        """
