#!/usr/bin/env python3
"""
BHARTE CHALO - Radio Show Script Generator

Generates engaging radio show scripts for Pakistan's future-focused
show on AI, IT, leadership, and innovation.
"""

from typing import Dict, Any, Optional, List
from datetime import datetime


class RadioScriptGenerator:
    """
    Generates radio show scripts for Bharte Chalo.

    Show Philosophy:
    - Educate everyone in Pakistan on AI, IT, leadership, and innovation
    - Help listeners think better, decide smarter, and move forward
    - Make complex topics accessible and actionable
    - Inspire forward momentum ("Bharte Chalo" = Keep Moving Forward)
    """

    # Show segments configuration
    SEGMENTS = {
        "opening": {
            "duration": "2-3 minutes",
            "purpose": "Hook listeners, set energy, introduce topic"
        },
        "tech_spotlight": {
            "duration": "5-7 minutes",
            "purpose": "Deep dive into one AI/IT concept or tool"
        },
        "leadership_lens": {
            "duration": "4-5 minutes",
            "purpose": "Leadership insight connected to tech topic"
        },
        "pakistan_perspective": {
            "duration": "3-4 minutes",
            "purpose": "Local context, opportunities, success stories"
        },
        "action_steps": {
            "duration": "3-4 minutes",
            "purpose": "Practical takeaways listeners can apply today"
        },
        "closing": {
            "duration": "2-3 minutes",
            "purpose": "Inspire, preview next episode, call to action"
        }
    }

    # Episode themes
    THEMES = [
        "AI Fundamentals",
        "Leadership in Digital Age",
        "Innovation Mindset",
        "Career in Tech",
        "Entrepreneurship",
        "Digital Transformation",
        "Future of Work",
        "Tech for Social Good",
        "Learning & Upskilling",
        "Building Tech Teams"
    ]

    def __init__(self, gemini_client):
        """
        Initialize the radio script generator.

        Args:
            gemini_client: GeminiClient instance for AI generation
        """
        self.gemini = gemini_client
        self.show_name = "Bharte Chalo"
        self.tagline = "Sochein Behtar, Faisla Karein Smarter, Aagey Barhein"

    def generate_episode_script(
        self,
        topic: str,
        theme: str = "AI Fundamentals",
        guest_name: Optional[str] = None,
        episode_number: Optional[int] = None,
        include_urdu_phrases: bool = True
    ) -> Dict[str, Any]:
        """
        Generate a complete episode script.

        Args:
            topic: Main topic for the episode
            theme: Episode theme category
            guest_name: Optional guest name
            episode_number: Episode number
            include_urdu_phrases: Whether to include Urdu phrases

        Returns:
            Complete episode script with all segments
        """
        prompt = f"""
You are a scriptwriter for "Bharte Chalo" (meaning "Keep Moving Forward"),
a popular Pakistani radio show that educates listeners on AI, IT, leadership,
and innovation.

SHOW IDENTITY:
- Name: Bharte Chalo
- Tagline: "Sochein Behtar, Faisla Karein Smarter, Aagey Barhein"
  (Think Better, Decide Smarter, Move Forward)
- Audience: Pakistani professionals, students, entrepreneurs, and curious minds
- Tone: Warm, encouraging, educational but not preachy, conversational
- Style: Mix of English with natural Urdu phrases (Roman Urdu)

EPISODE DETAILS:
- Topic: {topic}
- Theme: {theme}
- Episode Number: {episode_number or "TBD"}
- Guest: {guest_name or "No guest - solo episode"}

Generate a complete radio script with these segments:

1. OPENING (2-3 minutes)
   - Energetic greeting with show signature
   - Hook that grabs attention
   - Episode topic introduction
   - Why this matters to Pakistani listeners

2. TECH SPOTLIGHT (5-7 minutes)
   - Explain the core concept/technology
   - Use relatable analogies for Pakistani context
   - Real-world examples
   - Break down complexity into simple terms

3. LEADERSHIP LENS (4-5 minutes)
   - Connect technology to leadership skills
   - Decision-making frameworks
   - How leaders should think about this topic

4. PAKISTAN PERSPECTIVE (3-4 minutes)
   - Local opportunities and challenges
   - Pakistani success stories or potential
   - How this applies to Pakistan's growth

5. ACTION STEPS (3-4 minutes)
   - 3 specific things listeners can do TODAY
   - Free resources to explore
   - Small experiments to try

6. CLOSING (2-3 minutes)
   - Key takeaway summary
   - Inspirational close
   - Call to action (share, subscribe, apply)
   - Preview hint for next episode

{"Include natural Urdu phrases in Roman script throughout the script" if include_urdu_phrases else "Keep the script primarily in English"}

Format the script with clear speaker directions, timing notes, and natural
conversational flow. Include [MUSIC CUE], [PAUSE], [EMPHASIS] markers where appropriate.

Return as JSON with structure:
{{
    "episode_title": "catchy title",
    "episode_number": number,
    "theme": "theme",
    "topic": "topic",
    "total_duration": "estimated minutes",
    "segments": {{
        "opening": {{
            "duration": "X minutes",
            "script": "full script text",
            "music_cues": ["list of music/sound cues"]
        }},
        "tech_spotlight": {{ ... }},
        "leadership_lens": {{ ... }},
        "pakistan_perspective": {{ ... }},
        "action_steps": {{ ... }},
        "closing": {{ ... }}
    }},
    "key_phrases_urdu": ["memorable Urdu phrases used"],
    "quotable_moments": ["tweetable quotes from the episode"],
    "resources_mentioned": ["links/resources mentioned"]
}}
"""

        response = self.gemini.generate_json(prompt)

        # Add metadata
        response["generated_at"] = datetime.now().isoformat()
        response["show_name"] = self.show_name

        return response

    def generate_segment_script(
        self,
        segment_type: str,
        topic: str,
        context: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate a single segment script.

        Args:
            segment_type: Type of segment (opening, tech_spotlight, etc.)
            topic: Topic for the segment
            context: Additional context

        Returns:
            Segment script
        """
        segment_config = self.SEGMENTS.get(segment_type)
        if not segment_config:
            raise ValueError(f"Unknown segment type: {segment_type}")

        prompt = f"""
Generate a radio script segment for "Bharte Chalo", Pakistan's show on AI,
IT, leadership, and innovation.

SEGMENT: {segment_type.upper().replace("_", " ")}
DURATION: {segment_config['duration']}
PURPOSE: {segment_config['purpose']}
TOPIC: {topic}
{f"ADDITIONAL CONTEXT: {context}" if context else ""}

Write an engaging, conversational script that:
- Speaks directly to Pakistani listeners
- Uses simple language for complex topics
- Includes 2-3 natural Urdu phrases (Roman script)
- Has clear speaker directions
- Includes [MUSIC CUE], [PAUSE], [EMPHASIS] markers

Return as JSON:
{{
    "segment_type": "{segment_type}",
    "duration": "estimated time",
    "script": "full script with directions",
    "urdu_phrases": ["phrases used with translations"],
    "key_points": ["main points covered"]
}}
"""

        return self.gemini.generate_json(prompt)

    def generate_topic_series(
        self,
        main_topic: str,
        num_episodes: int = 4
    ) -> Dict[str, Any]:
        """
        Generate a series of episode outlines on a main topic.

        Args:
            main_topic: Overarching topic for the series
            num_episodes: Number of episodes in series

        Returns:
            Series outline with episode summaries
        """
        prompt = f"""
Create a {num_episodes}-episode series outline for "Bharte Chalo" radio show.

MAIN TOPIC: {main_topic}

For each episode, provide:
1. Episode title (catchy, memorable)
2. Specific focus within the main topic
3. Key concepts to cover
4. Pakistan-specific angle
5. Guest suggestion (type of expert, not specific names)
6. Teaser hook for promotion

The series should:
- Progress logically from basics to advanced
- Build on previous episodes
- Be accessible to beginners but valuable for experts
- Connect to Pakistani context throughout

Return as JSON:
{{
    "series_title": "catchy series name",
    "main_topic": "{main_topic}",
    "num_episodes": {num_episodes},
    "series_description": "2-3 sentence overview",
    "episodes": [
        {{
            "episode_number": 1,
            "title": "title",
            "focus": "specific focus",
            "key_concepts": ["concept1", "concept2"],
            "pakistan_angle": "local relevance",
            "suggested_guest_type": "type of expert",
            "teaser": "promotional hook"
        }}
    ],
    "series_arc": "how the series builds knowledge"
}}
"""

        return self.gemini.generate_json(prompt)

    def generate_quick_segment(
        self,
        segment_name: str,
        content: str,
        duration: str = "2-3 minutes"
    ) -> Dict[str, Any]:
        """
        Generate a quick custom segment.

        Args:
            segment_name: Name of the segment
            content: What to cover
            duration: Target duration

        Returns:
            Segment script
        """
        prompt = f"""
Write a quick radio segment for "Bharte Chalo" show.

SEGMENT: {segment_name}
CONTENT: {content}
DURATION: {duration}

Create an engaging, conversational script that:
- Is perfect for Pakistani radio listeners
- Uses simple, clear language
- Includes 1-2 Urdu phrases naturally
- Has energy and warmth

Return as JSON:
{{
    "segment_name": "{segment_name}",
    "duration": "{duration}",
    "script": "full script",
    "urdu_phrases": ["phrases with translations"]
}}
"""

        return self.gemini.generate_json(prompt)

    def generate_news_commentary(
        self,
        news_items: List[Dict[str, Any]],
        max_items: int = 3
    ) -> Dict[str, Any]:
        """
        Generate commentary on AI/tech news for the show.

        Args:
            news_items: List of news items to comment on
            max_items: Maximum items to cover

        Returns:
            News commentary segment
        """
        news_summary = "\n".join([
            f"- {item.get('title', item)}: {item.get('summary', '')}"
            for item in news_items[:max_items]
        ])

        prompt = f"""
Create a news commentary segment for "Bharte Chalo" radio show.

NEWS ITEMS:
{news_summary}

For each news item, provide:
1. Simple explanation of what happened
2. Why it matters globally
3. What it means for Pakistan specifically
4. One actionable insight for listeners

Style:
- Conversational, not news-anchor formal
- Include perspective and opinion
- Connect to Pakistani context
- Use 1-2 Urdu phrases naturally

Return as JSON:
{{
    "segment_title": "This Week in Tech",
    "duration": "5-7 minutes",
    "intro_script": "opening for the segment",
    "news_coverage": [
        {{
            "headline": "simplified headline",
            "script": "full commentary script",
            "pakistan_relevance": "why it matters here",
            "listener_takeaway": "what to do with this info"
        }}
    ],
    "closing_script": "wrap up the segment"
}}
"""

        return self.gemini.generate_json(prompt)

    def generate_guest_interview_guide(
        self,
        guest_name: str,
        guest_background: str,
        interview_topic: str
    ) -> Dict[str, Any]:
        """
        Generate an interview guide for a guest segment.

        Args:
            guest_name: Name of the guest
            guest_background: Guest's background/expertise
            interview_topic: Main topic to discuss

        Returns:
            Interview guide with questions and flow
        """
        prompt = f"""
Create an interview guide for "Bharte Chalo" radio show.

GUEST: {guest_name}
BACKGROUND: {guest_background}
TOPIC: {interview_topic}

Generate:
1. Guest introduction script (warm, respectful)
2. 8-10 interview questions (mix of professional and personal)
3. Follow-up prompts for deeper discussion
4. Pakistan-specific questions
5. Rapid-fire fun questions for personality
6. Closing that celebrates the guest

Style:
- Respectful but not formal
- Curious and genuine
- Draw out stories, not just facts
- Connect expertise to Pakistani context

Return as JSON:
{{
    "guest_name": "{guest_name}",
    "segment_duration": "15-20 minutes",
    "introduction_script": "warm intro for the guest",
    "main_questions": [
        {{
            "question": "the question",
            "purpose": "why asking this",
            "follow_ups": ["potential follow-up questions"]
        }}
    ],
    "pakistan_specific": ["questions about Pakistan context"],
    "rapid_fire": ["quick fun questions"],
    "closing_script": "thank you and celebration",
    "pre_interview_notes": "tips for the host"
}}
"""

        return self.gemini.generate_json(prompt)

    def format_script_markdown(self, script: Dict[str, Any]) -> str:
        """
        Format a script as readable markdown.

        Args:
            script: Script dictionary

        Returns:
            Formatted markdown string
        """
        output = []

        # Header
        output.append(f"# {self.show_name}")
        output.append(f"## {script.get('episode_title', 'Episode Script')}")
        output.append("")
        output.append(f"**Theme:** {script.get('theme', 'N/A')}")
        output.append(f"**Topic:** {script.get('topic', 'N/A')}")
        output.append(f"**Duration:** {script.get('total_duration', 'N/A')}")
        output.append(f"**Generated:** {script.get('generated_at', 'N/A')}")
        output.append("")
        output.append("---")
        output.append("")

        # Segments
        segments = script.get("segments", {})
        segment_order = [
            "opening", "tech_spotlight", "leadership_lens",
            "pakistan_perspective", "action_steps", "closing"
        ]

        for seg_name in segment_order:
            seg = segments.get(seg_name, {})
            if seg:
                output.append(f"## {seg_name.upper().replace('_', ' ')}")
                output.append(f"*Duration: {seg.get('duration', 'N/A')}*")
                output.append("")

                if seg.get("music_cues"):
                    output.append(f"**Music Cues:** {', '.join(seg['music_cues'])}")
                    output.append("")

                output.append("### Script")
                output.append("")
                output.append(seg.get("script", ""))
                output.append("")
                output.append("---")
                output.append("")

        # Extras
        if script.get("key_phrases_urdu"):
            output.append("## Urdu Phrases Used")
            for phrase in script["key_phrases_urdu"]:
                output.append(f"- {phrase}")
            output.append("")

        if script.get("quotable_moments"):
            output.append("## Quotable Moments")
            for quote in script["quotable_moments"]:
                output.append(f"> {quote}")
                output.append("")

        if script.get("resources_mentioned"):
            output.append("## Resources Mentioned")
            for resource in script["resources_mentioned"]:
                output.append(f"- {resource}")
            output.append("")

        return "\n".join(output)
