#!/usr/bin/env python3
"""
BHARTE CHALO - Social Media Manager

Generates and manages social media content for episode promotion.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List


class SocialMediaManager:
    """
    Manages social media content for Bharte Chalo.

    Handles:
    - Episode promotion content
    - Quote cards generation
    - Clip suggestions
    - Cross-platform content adaptation
    """

    PLATFORMS = {
        "twitter": {
            "name": "Twitter/X",
            "max_chars": 280,
            "best_times": ["9:00", "12:00", "18:00"],
            "hashtags": ["#BharteChalo", "#PakistanTech", "#AI", "#TechPakistan"]
        },
        "linkedin": {
            "name": "LinkedIn",
            "max_chars": 3000,
            "best_times": ["8:00", "12:00", "17:00"],
            "hashtags": ["#BharteChalo", "#AILeadership", "#PakistanIT", "#TechCareers"]
        },
        "facebook": {
            "name": "Facebook",
            "max_chars": 5000,
            "best_times": ["9:00", "13:00", "16:00"],
            "hashtags": ["#BharteChalo", "#PakistanTech"]
        },
        "instagram": {
            "name": "Instagram",
            "max_chars": 2200,
            "best_times": ["11:00", "14:00", "19:00"],
            "hashtags": ["#BharteChalo", "#TechPakistan", "#AIEducation", "#PakistaniYouth"]
        },
        "whatsapp": {
            "name": "WhatsApp",
            "max_chars": 1000,
            "best_times": ["10:00", "18:00"],
            "hashtags": []
        }
    }

    def __init__(self, base_path: Path, gemini_client=None):
        """
        Initialize social media manager.

        Args:
            base_path: Base path for social media data
            gemini_client: GeminiClient for AI generation
        """
        self.base_path = Path(base_path)
        self.social_path = self.base_path / "social"
        self.social_path.mkdir(parents=True, exist_ok=True)
        self.gemini = gemini_client

    def generate_episode_social_pack(
        self,
        episode: Dict[str, Any],
        script: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate complete social media pack for an episode.

        Args:
            episode: Episode metadata
            script: Episode script

        Returns:
            Social media content pack
        """
        episode_id = episode.get("id", "EP000")
        topic = episode.get("topic", "")
        theme = episode.get("theme", "")

        # Extract quotable moments from script
        quotes = script.get("quotable_moments", [])

        pack = {
            "episode_id": episode_id,
            "topic": topic,
            "generated_at": datetime.now().isoformat(),
            "pre_release": self._generate_pre_release_content(episode, script),
            "release_day": self._generate_release_day_content(episode, script),
            "post_release": self._generate_post_release_content(episode, script),
            "quote_cards": self._generate_quote_cards(quotes, topic),
            "clip_suggestions": self._generate_clip_suggestions(script),
            "stories": self._generate_story_content(episode, script)
        }

        # Save social pack
        pack_file = self.social_path / f"{episode_id}_social_pack.json"
        with open(pack_file, "w") as f:
            json.dump(pack, f, indent=2, default=str)

        return pack

    def _generate_pre_release_content(
        self,
        episode: Dict[str, Any],
        script: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Generate pre-release teaser content."""
        topic = episode.get("topic", "")
        release_date = episode.get("release_date", "")

        return {
            "twitter": [
                {
                    "type": "teaser",
                    "text": f"🎙️ Naya episode aa raha hai!\n\n\"{topic}\"\n\n📅 {release_date} ko 6 PM\n\nTayyar ho? 🚀\n\n#BharteChalo #PakistanTech",
                    "timing": "2 days before"
                },
                {
                    "type": "countdown",
                    "text": f"⏰ Kal milte hain!\n\nBharte Chalo ka naya episode:\n\"{topic}\"\n\nKya seekhenge:\n✅ {script.get('segments', {}).get('main_topic_part1', {}).get('concepts_covered', ['Concept'])[0] if script.get('segments') else 'New concepts'}\n\n#BharteChalo",
                    "timing": "1 day before"
                }
            ],
            "linkedin": [
                {
                    "type": "announcement",
                    "text": f"""🎙️ New Episode Coming: "{topic}"

Bharte Chalo ka naya episode is {release_date} ko release ho raha hai.

Is episode mein:
📌 {script.get('theme', 'AI & Technology')} pe deep dive
📌 Pakistani success story
📌 Practical action steps jo aap aaj se apply kar sakte hain

Notification on karein taake miss na ho!

#BharteChalo #AILeadership #PakistanIT""",
                    "timing": "2 days before"
                }
            ],
            "whatsapp": [
                {
                    "type": "group_message",
                    "text": f"""🎙️ *Bharte Chalo - New Episode Alert*

📌 Topic: {topic}
📅 Release: {release_date}, 6 PM

Apne friends ko bhi batayein! Forward karein ➡️

_Sochein Behtar, Faisla Karein Smarter, Aagey Barhein_""",
                    "timing": "1 day before"
                }
            ]
        }

    def _generate_release_day_content(
        self,
        episode: Dict[str, Any],
        script: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Generate release day content."""
        topic = episode.get("topic", "")
        episode_number = episode.get("number", "")

        key_takeaways = script.get("segments", {}).get("closing", {}).get("key_takeaways", [])
        takeaways_text = "\n".join([f"✅ {t}" for t in key_takeaways[:3]])

        return {
            "twitter": [
                {
                    "type": "release_announcement",
                    "text": f"""🎙️ NEW EPISODE OUT NOW!

EP{episode_number}: "{topic}"

⏱️ 1 hour of learning
🇵🇰 Pakistan-focused insights
🎯 5 action steps

Link in bio! 👆

#BharteChalo #BharteChaloPodcast""",
                    "timing": "Release time"
                },
                {
                    "type": "thread_start",
                    "text": f"""🧵 Thread: Key takeaways from today's Bharte Chalo episode on "{topic}"

Let's go! 👇""",
                    "timing": "1 hour after release"
                }
            ],
            "linkedin": [
                {
                    "type": "release_post",
                    "text": f"""🎙️ New Episode Released: "{topic}"

Bharte Chalo Episode {episode_number} is now live!

Key Takeaways:
{takeaways_text}

This 1-hour episode covers:
- Concepts explained with Pakistani context
- Real success story from Pakistan
- Leadership insights
- 5 practical action steps

Listen now and take your first step forward today.

#BharteChalo #PakistanTech #AIEducation #Leadership""",
                    "timing": "Release time"
                }
            ],
            "instagram": [
                {
                    "type": "carousel_caption",
                    "text": f"""🎙️ NEW EPISODE: "{topic}"

Swipe karein key insights ke liye ➡️

Is episode mein:
🔹 Deep dive into {episode.get('theme', 'technology')}
🔹 Pakistani success story
🔹 5 practical steps

Full episode ka link bio mein hai!

.
.
#BharteChalo #TechPakistan #AIEducation #PakistaniYouth #Motivation #TechCareer #Freelancing #Pakistan""",
                    "timing": "Release time"
                }
            ],
            "whatsapp": [
                {
                    "type": "release_message",
                    "text": f"""🎙️ *BHARTE CHALO - NEW EPISODE*

*EP{episode_number}: {topic}*

🎯 Key Takeaways:
{takeaways_text}

📻 Ab sunein! [Link]

_Forward karein apne network ko!_""",
                    "timing": "Release time"
                }
            ]
        }

    def _generate_post_release_content(
        self,
        episode: Dict[str, Any],
        script: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Generate post-release engagement content."""
        topic = episode.get("topic", "")

        return {
            "twitter": [
                {
                    "type": "engagement",
                    "text": f"""Aaj ka Bharte Chalo episode suna?

"{topic}"

Aapka favorite takeaway kya tha? 👇

#BharteChalo""",
                    "timing": "Next day"
                },
                {
                    "type": "question",
                    "text": """Agli episode ke liye aapka sawaal?

Reply karein - best questions episode mein answer honge! 🎙️

#BharteChalo #AapKeSawaal""",
                    "timing": "2 days after"
                }
            ],
            "linkedin": [
                {
                    "type": "discussion",
                    "text": f"""Weekend reflection:

This week's Bharte Chalo episode on "{topic}" got amazing response.

Question for you: Is topic se aapne kya seekha jo aap apni work/life mein apply kar sakte hain?

Share your thoughts below! 👇

#BharteChalo #WeekendLearning""",
                    "timing": "Weekend after release"
                }
            ]
        }

    def _generate_quote_cards(
        self,
        quotes: List[str],
        topic: str
    ) -> List[Dict[str, Any]]:
        """Generate quote card specifications."""
        cards = []

        for i, quote in enumerate(quotes[:5]):  # Max 5 quote cards
            cards.append({
                "quote_id": f"QC{i+1}",
                "quote_text": quote,
                "topic": topic,
                "design_specs": {
                    "background": "gradient_green_blue",
                    "font": "bold_urdu_english",
                    "logo": "bharte_chalo_logo",
                    "hashtag": "#BharteChalo"
                },
                "platforms": ["instagram", "twitter", "linkedin"]
            })

        return cards

    def _generate_clip_suggestions(
        self,
        script: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Suggest audio/video clips from the episode."""
        segments = script.get("segments", {})

        suggestions = []

        # Opening hook
        if segments.get("opening"):
            suggestions.append({
                "clip_id": "CLIP_HOOK",
                "segment": "opening",
                "description": "Episode hook - first 60 seconds",
                "duration": "60 seconds",
                "purpose": "Teaser for social media",
                "platforms": ["instagram_reels", "twitter", "tiktok"]
            })

        # Success story highlight
        if segments.get("hamari_kahani"):
            suggestions.append({
                "clip_id": "CLIP_STORY",
                "segment": "hamari_kahani",
                "description": "Most inspiring moment from success story",
                "duration": "90 seconds",
                "purpose": "Inspirational content",
                "platforms": ["instagram_reels", "youtube_shorts", "facebook"]
            })

        # Key insight
        if segments.get("main_topic_part1"):
            suggestions.append({
                "clip_id": "CLIP_INSIGHT",
                "segment": "main_topic_part1",
                "description": "Core concept explanation with analogy",
                "duration": "2 minutes",
                "purpose": "Educational content",
                "platforms": ["linkedin", "youtube_shorts"]
            })

        # Action steps
        if segments.get("action_steps"):
            suggestions.append({
                "clip_id": "CLIP_ACTIONS",
                "segment": "action_steps",
                "description": "5 action steps summary",
                "duration": "90 seconds",
                "purpose": "Practical value",
                "platforms": ["instagram_reels", "twitter"]
            })

        return suggestions

    def _generate_story_content(
        self,
        episode: Dict[str, Any],
        script: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Generate Instagram/Facebook story content."""
        topic = episode.get("topic", "")
        key_takeaways = script.get("segments", {}).get("closing", {}).get("key_takeaways", [])

        return {
            "story_sequence": [
                {
                    "slide": 1,
                    "type": "announcement",
                    "text": f"🎙️ NEW EPISODE\n\n{topic}",
                    "cta": "Swipe up to listen"
                },
                {
                    "slide": 2,
                    "type": "takeaway",
                    "text": f"Key Insight #1\n\n{key_takeaways[0] if key_takeaways else 'Coming soon'}",
                    "cta": None
                },
                {
                    "slide": 3,
                    "type": "takeaway",
                    "text": f"Key Insight #2\n\n{key_takeaways[1] if len(key_takeaways) > 1 else ''}",
                    "cta": None
                },
                {
                    "slide": 4,
                    "type": "question",
                    "text": "Aapka favorite takeaway?\n\nPoll below 👇",
                    "cta": "Poll sticker"
                },
                {
                    "slide": 5,
                    "type": "cta",
                    "text": "Full episode\nLink in Bio! 🔗",
                    "cta": "Link sticker"
                }
            ]
        }

    def get_posting_schedule(
        self,
        episode_id: str,
        release_date: str
    ) -> List[Dict[str, Any]]:
        """Generate posting schedule for an episode."""
        from datetime import datetime, timedelta

        release = datetime.strptime(release_date, "%Y-%m-%d")

        schedule = [
            {
                "date": (release - timedelta(days=2)).strftime("%Y-%m-%d"),
                "time": "10:00",
                "platform": "twitter",
                "content_type": "teaser",
                "status": "scheduled"
            },
            {
                "date": (release - timedelta(days=2)).strftime("%Y-%m-%d"),
                "time": "12:00",
                "platform": "linkedin",
                "content_type": "announcement",
                "status": "scheduled"
            },
            {
                "date": (release - timedelta(days=1)).strftime("%Y-%m-%d"),
                "time": "18:00",
                "platform": "whatsapp",
                "content_type": "group_message",
                "status": "scheduled"
            },
            {
                "date": release_date,
                "time": "18:00",
                "platform": "all",
                "content_type": "release_announcement",
                "status": "scheduled"
            },
            {
                "date": (release + timedelta(days=1)).strftime("%Y-%m-%d"),
                "time": "12:00",
                "platform": "twitter",
                "content_type": "engagement",
                "status": "scheduled"
            }
        ]

        return schedule

    def print_social_calendar(self, episode_id: str, release_date: str):
        """Print social media calendar for an episode."""
        schedule = self.get_posting_schedule(episode_id, release_date)

        print("\n" + "=" * 60)
        print(f"📱 SOCIAL MEDIA CALENDAR - {episode_id}")
        print("=" * 60)

        current_date = ""
        for post in schedule:
            if post["date"] != current_date:
                current_date = post["date"]
                print(f"\n📅 {current_date}")

            platform = self.PLATFORMS.get(post["platform"], {}).get("name", post["platform"])
            print(f"   {post['time']} | {platform} | {post['content_type']}")
