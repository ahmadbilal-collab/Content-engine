"""
LINKEDIN THOUGHT LEADERSHIP GENERATOR
Creates LinkedIn posts at thought leadership scale.
Not tips and tricks—big ideas and real insights.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
import json


# LinkedIn post schema
LINKEDIN_POST_SCHEMA = {
    "type": "object",
    "properties": {
        "type": {
            "type": "string",
            "enum": [
                "practitioner_insight",
                "prediction",
                "contrarian",
                "philosophy",
                "pattern_recognition",
                "tool_take",
                "industry_commentary"
            ]
        },
        "dimension": {"type": "string"},
        "hook": {"type": "string"},
        "body": {"type": "string"},
        "philosophical_layer": {"type": "string"},
        "cta": {"type": "string"},
        "hashtags": {"type": "array", "items": {"type": "string"}},
        "target_audience": {"type": "string"},
        "potential_reach": {
            "type": "string",
            "enum": ["practitioners", "leaders", "general_tech", "mainstream"]
        },
        "char_count": {"type": "integer"}
    }
}

LINKEDIN_BATCH_SCHEMA = {
    "type": "object",
    "properties": {
        "posts": {
            "type": "array",
            "items": LINKEDIN_POST_SCHEMA
        }
    }
}


class LinkedInGenerator:
    """
    Generates thought leadership LinkedIn posts for Ahmad Bilal.
    Creates content that resonates from Davos to design teams.
    """

    def __init__(self, gemini_client):
        """
        Initialize the LinkedIn generator.

        Args:
            gemini_client: Configured GeminiClient instance
        """
        self.gemini = gemini_client

    def generate_daily_posts(
        self,
        research: Dict[str, Any],
        num_posts: int = 3
    ) -> Dict[str, Any]:
        """
        Generate thought leadership LinkedIn posts for the day.

        Args:
            research: Research context from news scanner
            num_posts: Number of posts to generate

        Returns:
            Generated posts with variety
        """
        prompt = f"""
        Generate {num_posts} LinkedIn posts for Ahmad Bilal.

        ## AHMAD'S POSITIONING
        - AI Interface Architect & Innovation Philosopher
        - Actively building AI interfaces and testing vibe coding tools
        - Signature concept: "The Intent Layer"
        - Not a commentator—a practitioner with philosophical depth
        - 10+ industries experience (gov, mobility, automotive, education)
        - Global perspective (MENA + US), not Silicon Valley centric

        ## TODAY'S RESEARCH CONTEXT
        {json.dumps(research, indent=2) if research else "Use general AI industry knowledge"}

        ## POST REQUIREMENTS

        ### VARIETY (use different types across the {num_posts} posts):
        1. PRACTITIONER INSIGHT: "I tested/built/discovered this week..."
           - Specific hands-on experience
           - What worked, what didn't
           - Lessons for other practitioners

        2. PREDICTION: "Here's what I think happens next..."
           - Bold but reasoned
           - Include signals to watch
           - Connect to experience

        3. CONTRARIAN: "Everyone says X, but actually..."
           - Only if genuinely substantive
           - Respectful disagreement
           - Evidence-based

        4. PHILOSOPHY: "The bigger question nobody's asking..."
           - Elevate from tactical to meaning
           - Human agency, creativity, future
           - Accessible depth

        5. PATTERN RECOGNITION: "Seeing this across industries..."
           - Cross-industry insight
           - Connect disparate trends
           - Unique perspective

        6. TOOL TAKE: "Spent a week with [tool]. Honest thoughts..."
           - Specific tool experience
           - Balanced assessment
           - Who it's for/not for

        ### STRUCTURE FOR EACH POST:

        HOOK (First 2-3 lines):
        - Must stop executives AND practitioners scrolling
        - NOT: "10 tips for..." or "Here's my take on..."
        - YES: "I've been building AI interfaces for 8 months. Here's what nobody tells you."
        - YES: "The vibe coding hype is missing something crucial."
        - YES: "We're asking the wrong question about AI and jobs."

        BODY:
        - Lead with insight, not setup
        - Include specific experience/evidence
        - Connect tactical to philosophical
        - One big idea, well developed
        - 1200-1800 characters total (including hook)

        PHILOSOPHICAL LAYER:
        Every post should gesture toward bigger meaning:
        - What does this mean for human agency?
        - What future are we choosing?
        - What's the ethical dimension?
        - What pattern does this reveal?

        CTA (Call to action):
        - Spark genuine discussion
        - NOT: "Like and share!" or "What do you think?"
        - YES: "What are you seeing differently?"
        - YES: "Is this matching your experience?"
        - YES: "Where am I wrong here?"

        HASHTAGS:
        - 3-5 relevant hashtags
        - Mix of broad (#AI, #ProductDesign) and specific (#AIDesign, #VibeCoding)

        ### TONE:
        - Confident but curious
        - Practitioner credibility
        - Accessible depth
        - Global perspective (not Silicon Valley centric)
        - Optimistic but clear-eyed

        ### AUDIENCE TARGETING:
        - At least one post should resonate with executives/leaders
        - At least one should spark practitioner discussion
        - Avoid being too niche (remember: 5-year game to thought leadership)

        Generate posts that could be shared at Davos or discussed in design teams.
        Each post should be ready to copy-paste to LinkedIn.
        """

        result = self.gemini.generate_structured(prompt, LINKEDIN_BATCH_SCHEMA, model="pro")

        # Add metadata
        result["generated_at"] = datetime.now().isoformat()
        result["research_context"] = bool(research)

        return result

    def generate_post_from_hot_take(
        self,
        hot_take: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate a LinkedIn post from a hot take.

        Args:
            hot_take: Hot take from HotTakeGenerator

        Returns:
            Formatted LinkedIn post
        """
        prompt = f"""
        Transform this hot take into a LinkedIn post:

        {json.dumps(hot_take, indent=2)}

        ## FORMAT AS LINKEDIN POST

        Structure:
        1. HOOK: Attention-grabbing opening (2-3 lines)
        2. BODY: Develop the insight with evidence
        3. PHILOSOPHICAL: Connect to bigger meaning
        4. CTA: Spark discussion

        Requirements:
        - 1200-1800 characters total
        - Ahmad's practitioner voice
        - Specific, not vague
        - Include the contrarian element if present
        - End with engaging question

        Return as LinkedIn post schema.
        """

        result = self.gemini.generate_structured(prompt, LINKEDIN_POST_SCHEMA)
        result["source"] = "hot_take"
        result["generated_at"] = datetime.now().isoformat()
        return result

    def generate_post_from_prediction(
        self,
        prediction: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate a LinkedIn post from a prediction.

        Args:
            prediction: Prediction from PredictionEngine

        Returns:
            Formatted LinkedIn post
        """
        prompt = f"""
        Transform this prediction into a LinkedIn post:

        {json.dumps(prediction, indent=2)}

        ## FORMAT AS LINKEDIN PREDICTION POST

        Structure:
        1. HOOK: Make readers curious about what you're predicting
        2. THE PREDICTION: State it clearly and boldly
        3. WHY I THINK THIS: Your reasoning
        4. WHAT TO WATCH: Signals that would confirm/deny
        5. THE STAKES: Why this matters
        6. CTA: Invite agreement/disagreement

        Requirements:
        - 1200-1800 characters
        - Confident but intellectually honest
        - Include what could prove you wrong
        - Connect to hands-on experience
        - Make it memorable

        Return as LinkedIn post schema with type: "prediction"
        """

        result = self.gemini.generate_structured(prompt, LINKEDIN_POST_SCHEMA)
        result["source"] = "prediction"
        result["generated_at"] = datetime.now().isoformat()
        return result

    def generate_tool_review_post(
        self,
        tool_name: str,
        research: Dict[str, Any],
        testing_notes: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate a tool review LinkedIn post.

        Args:
            tool_name: Name of the tool
            research: Research data about the tool
            testing_notes: Ahmad's personal testing notes

        Returns:
            Tool review post
        """
        prompt = f"""
        Generate a tool review LinkedIn post for {tool_name}:

        ## RESEARCH
        {json.dumps(research, indent=2)}

        ## AHMAD'S TESTING NOTES
        {testing_notes or "Based on hands-on testing experience"}

        ## POST FORMAT

        Structure:
        1. HOOK: "I spent [time] with {tool_name}. Here's the honest truth..."
        2. WHAT IT DOES: Brief explanation
        3. WHAT WORKS: Specific positives
        4. WHAT DOESN'T: Honest limitations
        5. WHO IT'S FOR: Specific recommendations
        6. THE BIGGER PICTURE: What this tool represents
        7. VERDICT: Clear recommendation
        8. CTA: Ask about others' experiences

        Requirements:
        - Not a fanboy review or hit piece
        - Balanced, practitioner perspective
        - Connect to AI interface trends
        - Specific examples from testing
        - 1200-1800 characters

        Return as LinkedIn post schema with type: "tool_take"
        """

        result = self.gemini.generate_structured(prompt, LINKEDIN_POST_SCHEMA)
        result["source"] = "tool_review"
        result["tool"] = tool_name
        result["generated_at"] = datetime.now().isoformat()
        return result

    def generate_response_to_news(
        self,
        news_item: Dict[str, Any],
        urgency: str = "same_day"
    ) -> Dict[str, Any]:
        """
        Generate a LinkedIn post responding to breaking news.

        Args:
            news_item: News item to respond to
            urgency: How quickly to post (same_day, this_week)

        Returns:
            News response post
        """
        prompt = f"""
        Generate a LinkedIn post responding to this news:

        NEWS: {news_item.get('headline', 'Unknown')}
        DETAILS: {news_item.get('summary', 'No details')}
        SOURCE: {news_item.get('source', 'Unknown')}

        ## AHMAD'S RESPONSE FORMAT

        For urgent news response:
        1. HOOK: Acknowledge the news, hint at unique take
        2. CONVENTIONAL WISDOM: What everyone will say
        3. AHMAD'S ANGLE: Your unique perspective
        4. WHY THIS MATTERS: Beyond the headline
        5. WHAT TO WATCH: What happens next
        6. CTA: Invite perspectives

        Requirements:
        - Don't just summarize the news
        - Add unique practitioner perspective
        - Be timely but thoughtful
        - Connect to bigger patterns
        - 800-1200 characters (shorter for news response)

        Return as LinkedIn post schema with type: "industry_commentary"
        """

        result = self.gemini.generate_structured(prompt, LINKEDIN_POST_SCHEMA)
        result["source"] = "news_response"
        result["news"] = news_item
        result["urgency"] = urgency
        result["generated_at"] = datetime.now().isoformat()
        return result

    def format_post_for_publishing(self, post: Dict[str, Any]) -> str:
        """
        Format a post object into publishable text.

        Args:
            post: Post object with hook, body, cta, hashtags

        Returns:
            Formatted text ready to paste into LinkedIn
        """
        parts = []

        if post.get("hook"):
            parts.append(post["hook"])

        if post.get("body"):
            parts.append("\n\n" + post["body"])

        if post.get("cta"):
            parts.append("\n\n" + post["cta"])

        if post.get("hashtags"):
            parts.append("\n\n" + " ".join(post["hashtags"]))

        return "".join(parts)

    def generate_weekly_content_calendar(
        self,
        research: Dict[str, Any],
        posts_per_day: int = 1
    ) -> Dict[str, Any]:
        """
        Generate a week's worth of LinkedIn content.

        Args:
            research: Research context
            posts_per_day: Posts per day

        Returns:
            Weekly content calendar
        """
        prompt = f"""
        Generate a week's LinkedIn content calendar for Ahmad Bilal.

        ## CONTEXT
        {json.dumps(research, indent=2) if research else "Use general AI knowledge"}

        ## GENERATE 7 DAYS OF CONTENT

        For each day, create {posts_per_day} post(s):

        - Monday: Practitioner insight (start week strong)
        - Tuesday: Hot take or contrarian view
        - Wednesday: Tool review or comparison
        - Thursday: Prediction or future-focused
        - Friday: Philosophical / bigger picture
        - Saturday: Pattern recognition or cross-industry
        - Sunday: Reflection or preparation for week ahead

        ## VARIETY REQUIREMENTS
        - Mix of post types
        - Different audience segments
        - Varying lengths (some shorter, some longer)
        - Different engagement styles

        Return as JSON with day-by-day posts.
        """

        return self.gemini.generate_structured(prompt, {
            "type": "object",
            "properties": {
                "week_of": {"type": "string"},
                "daily_content": {
                    "type": "object",
                    "properties": {
                        "monday": {"type": "array", "items": LINKEDIN_POST_SCHEMA},
                        "tuesday": {"type": "array", "items": LINKEDIN_POST_SCHEMA},
                        "wednesday": {"type": "array", "items": LINKEDIN_POST_SCHEMA},
                        "thursday": {"type": "array", "items": LINKEDIN_POST_SCHEMA},
                        "friday": {"type": "array", "items": LINKEDIN_POST_SCHEMA},
                        "saturday": {"type": "array", "items": LINKEDIN_POST_SCHEMA},
                        "sunday": {"type": "array", "items": LINKEDIN_POST_SCHEMA}
                    }
                }
            }
        }, model="pro")
