"""
TWITTER/X CONTENT GENERATOR
Creates Twitter content for real-time commentary and thought leadership.
Threads, hot takes, and engagement content.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
import json


# Tweet schema
TWEET_SCHEMA = {
    "type": "object",
    "properties": {
        "content": {"type": "string"},
        "char_count": {"type": "integer"},
        "type": {
            "type": "string",
            "enum": ["standalone", "thread_start", "reply", "quote"]
        },
        "engagement_hook": {"type": "string"},
        "hashtags": {"type": "array", "items": {"type": "string"}}
    }
}

THREAD_SCHEMA = {
    "type": "object",
    "properties": {
        "topic": {"type": "string"},
        "hook": {"type": "string"},
        "tweets": {"type": "array", "items": {"type": "string"}},
        "total_tweets": {"type": "integer"},
        "call_to_action": {"type": "string"}
    }
}


class TwitterGenerator:
    """
    Generates Twitter/X content for Ahmad Bilal.
    Real-time commentary, threads, and engagement content.
    """

    def __init__(self, gemini_client):
        """
        Initialize the Twitter generator.

        Args:
            gemini_client: Configured GeminiClient instance
        """
        self.gemini = gemini_client
        self.max_chars = 280

    def generate_daily_content(
        self,
        research: Dict[str, Any],
        num_tweets: int = 5
    ) -> Dict[str, Any]:
        """
        Generate daily Twitter content.

        Args:
            research: Research context from news scanner
            num_tweets: Number of standalone tweets

        Returns:
            Daily Twitter content package
        """
        prompt = f"""
        Generate Twitter content for Ahmad Bilal (AI Interface Architect).

        ## CONTEXT
        {json.dumps(research, indent=2) if research else "Use general AI knowledge"}

        ## GENERATE

        ### {num_tweets} STANDALONE TWEETS
        Each should be:
        - Under 280 characters
        - Punchy and memorable
        - Provoke thought or engagement
        - Mix of types: insight, hot take, question, prediction

        Tweet types to include:
        1. HOT TAKE: Contrarian but substantive
        2. OBSERVATION: Pattern or insight from practice
        3. QUESTION: Thought-provoking question
        4. PREDICTION: Brief, bold prediction
        5. QUOTE-WORTHY: Something memorable/shareable

        ### 1 THREAD (5-7 tweets)
        Topic: Based on most interesting news/trend
        Structure:
        - Tweet 1: Hook that creates curiosity
        - Tweets 2-5: Develop the insight
        - Tweet 6: Implication or prediction
        - Tweet 7: Call to action / question

        ## AHMAD'S TWITTER VOICE
        - Sharper than LinkedIn
        - More real-time, more opinionated
        - Still substantive, not shitposty
        - Accessible to tech-curious, not just designers
        - Global perspective

        ## RULES
        - Every tweet under 280 characters
        - No generic advice
        - Specific > vague
        - Personality > corporate

        Return as JSON with standalone tweets and thread.
        """

        return self.gemini.generate_structured(prompt, {
            "type": "object",
            "properties": {
                "standalone_tweets": {
                    "type": "array",
                    "items": TWEET_SCHEMA
                },
                "thread": THREAD_SCHEMA,
                "generated_at": {"type": "string"}
            }
        })

    def generate_thread(
        self,
        topic: str,
        angle: str,
        length: int = 7
    ) -> Dict[str, Any]:
        """
        Generate a Twitter thread on a specific topic.

        Args:
            topic: Topic for the thread
            angle: Specific angle or perspective
            length: Number of tweets in thread

        Returns:
            Thread content
        """
        prompt = f"""
        Generate a Twitter thread for Ahmad Bilal:

        TOPIC: {topic}
        ANGLE: {angle}
        LENGTH: {length} tweets

        ## THREAD STRUCTURE

        Tweet 1 (HOOK):
        - Create curiosity
        - Promise value
        - Make people want to click "Show this thread"
        - Examples:
          - "I've tested every vibe coding tool. Here's my honest ranking: 🧵"
          - "The AI interface we're all building wrong: 🧵"
          - "Nobody is talking about this AI design pattern. But it's everywhere: 🧵"

        Tweets 2-{length-2} (BODY):
        - One idea per tweet
        - Each tweet should stand alone somewhat
        - Build toward conclusion
        - Include specific examples

        Tweet {length-1} (IMPLICATION):
        - So what?
        - What does this mean?
        - Prediction or call to action

        Tweet {length} (ENGAGEMENT):
        - Question to audience
        - Invitation to share
        - "What would you add?"

        ## RULES
        - Every tweet under 280 characters
        - Use 🧵 only in first tweet
        - Numbered if helpful (1/, 2/, etc.)
        - Substance over style

        Return as thread schema.
        """

        result = self.gemini.generate_structured(prompt, THREAD_SCHEMA)
        result["topic"] = topic
        result["angle"] = angle
        result["generated_at"] = datetime.now().isoformat()
        return result

    def generate_news_reaction(
        self,
        news_item: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate quick reaction tweet to breaking news.

        Args:
            news_item: News to react to

        Returns:
            Reaction tweet(s)
        """
        prompt = f"""
        Generate Ahmad's reaction to this news:

        NEWS: {news_item.get('headline', 'Unknown')}
        DETAILS: {news_item.get('summary', '')}

        ## GENERATE

        1. QUICK TAKE (single tweet):
        - Immediate reaction
        - Unique angle
        - Under 280 chars

        2. FOLLOW-UP (if warranted):
        - Deeper thought
        - Prediction
        - Question

        ## AHMAD'S NEWS REACTION VOICE
        - Not just repeating the news
        - Practitioner perspective
        - What others are missing
        - What this means for design/AI interfaces

        Return as JSON with tweets.
        """

        return self.gemini.generate_structured(prompt, {
            "type": "object",
            "properties": {
                "quick_take": TWEET_SCHEMA,
                "follow_up": TWEET_SCHEMA,
                "quote_tweet_angle": {"type": "string"}
            }
        })

    def generate_engagement_tweets(
        self,
        num_tweets: int = 5
    ) -> Dict[str, Any]:
        """
        Generate tweets designed to drive engagement/discussion.

        Args:
            num_tweets: Number of tweets to generate

        Returns:
            Engagement-focused tweets
        """
        prompt = f"""
        Generate {num_tweets} engagement-focused tweets for Ahmad Bilal.

        ## ENGAGEMENT TWEET TYPES

        1. CONTROVERSIAL QUESTION
        "Hot take: [controversial opinion]. Am I wrong?"

        2. UNPOPULAR OPINION
        "Unpopular opinion: [opinion that goes against conventional wisdom]"

        3. AGREE/DISAGREE
        "Agree or disagree: [statement]"

        4. PREDICTION POLL
        "[Prediction]. Over/under?"

        5. FILL IN THE BLANK
        "The biggest mistake in AI interfaces right now is ___"

        6. THIS OR THAT
        "[Option A] or [Option B] for [use case]?"

        7. CONFESSION
        "Confession: I still [thing that's supposedly outdated]"

        ## RULES
        - Each under 280 characters
        - Genuinely interesting, not engagement bait
        - Related to AI, design, interfaces
        - Ahmad's authentic voice

        Return as JSON array of tweets.
        """

        return self.gemini.generate_structured(prompt, {
            "type": "object",
            "properties": {
                "engagement_tweets": {
                    "type": "array",
                    "items": TWEET_SCHEMA
                }
            }
        })

    def generate_tool_take_tweets(
        self,
        tool_name: str,
        verdict: str
    ) -> Dict[str, Any]:
        """
        Generate tweets about a specific tool.

        Args:
            tool_name: Name of the tool
            verdict: Overall assessment

        Returns:
            Tool-focused tweets
        """
        prompt = f"""
        Generate tweets about {tool_name} for Ahmad Bilal.

        TOOL: {tool_name}
        AHMAD'S VERDICT: {verdict}

        ## GENERATE

        1. HOT TAKE TWEET:
        Sharp, memorable take on this tool

        2. MINI THREAD (3-4 tweets):
        - What it does well
        - What it doesn't
        - Who should use it
        - Verdict

        3. COMPARISON TWEET:
        Compare to alternatives

        ## VOICE
        - Honest, not promotional
        - Practitioner tested
        - Specific observations

        Return as JSON.
        """

        return self.gemini.generate_structured(prompt, {
            "type": "object",
            "properties": {
                "hot_take": TWEET_SCHEMA,
                "mini_thread": {"type": "array", "items": {"type": "string"}},
                "comparison": TWEET_SCHEMA
            }
        })

    def optimize_tweet(self, draft: str) -> Dict[str, Any]:
        """
        Optimize a draft tweet for impact.

        Args:
            draft: Draft tweet text

        Returns:
            Optimized versions
        """
        prompt = f"""
        Optimize this tweet for Ahmad Bilal:

        DRAFT: {draft}
        CURRENT LENGTH: {len(draft)} characters

        ## GENERATE

        1. PUNCHIER VERSION:
        Same idea, more impact, under 280 chars

        2. THREAD-WORTHY VERSION:
        If this could be a thread, what's the hook?

        3. ENGAGEMENT VERSION:
        Rephrase to invite response

        4. QUOTABLE VERSION:
        Make it screenshot-worthy

        Return all versions with character counts.
        """

        return self.gemini.generate_structured(prompt, {
            "type": "object",
            "properties": {
                "original": {"type": "string"},
                "punchier": TWEET_SCHEMA,
                "thread_hook": TWEET_SCHEMA,
                "engagement": TWEET_SCHEMA,
                "quotable": TWEET_SCHEMA
            }
        })

    def format_thread_for_publishing(self, thread: Dict[str, Any]) -> str:
        """
        Format thread for easy publishing.

        Args:
            thread: Thread object

        Returns:
            Formatted thread text
        """
        output = []
        tweets = thread.get("tweets", [])

        for i, tweet in enumerate(tweets, 1):
            output.append(f"--- Tweet {i}/{len(tweets)} ---")
            output.append(tweet)
            output.append(f"[{len(tweet)} chars]")
            output.append("")

        return "\n".join(output)
