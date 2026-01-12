#!/usr/bin/env python3
"""
BHARTE CHALO - Show Manager

Central orchestrator for the entire radio show infrastructure.
Manages episodes, guests, listeners, content calendar, and analytics.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any, Optional, List


class ShowManager:
    """
    Central manager for Bharte Chalo radio show.

    Coordinates all aspects of show production:
    - Episode planning and generation
    - Guest management
    - Listener engagement
    - Content calendar
    - Social media content
    - Analytics tracking
    """

    # Show configuration
    CONFIG = {
        "show_name": "Bharte Chalo",
        "show_name_urdu": "بڑھتے چلو",
        "tagline": "Sochein Behtar, Faisla Karein Smarter, Aagey Barhein",
        "tagline_english": "Think Better, Decide Smarter, Move Forward",
        "episodes_per_week": 2,
        "episode_duration_minutes": 60,
        "release_days": ["Tuesday", "Friday"],
        "release_time": "18:00",  # 6 PM PKT
        "timezone": "Asia/Karachi",
        "languages": ["English", "Urdu"],
        "social_hashtag": "#BharteChalo",
        "segments": 9
    }

    def __init__(self, base_path: str = None, gemini_client=None):
        """
        Initialize the show manager.

        Args:
            base_path: Base path for show data
            gemini_client: GeminiClient for AI generation
        """
        self.base_path = Path(base_path or "bharte_chalo")
        self.gemini = gemini_client

        # Initialize paths
        self.paths = {
            "episodes": self.base_path / "episodes",
            "guests": self.base_path / "guests",
            "listeners": self.base_path / "listeners",
            "social": self.base_path / "social",
            "analytics": self.base_path / "analytics",
            "assets": self.base_path / "assets",
            "calendar": self.base_path / "calendar",
            "output": Path("output/radio")
        }

        # Create directories
        for path in self.paths.values():
            path.mkdir(parents=True, exist_ok=True)

        # Load or initialize show state
        self.state_file = self.base_path / "show_state.json"
        self.state = self._load_state()

    def _load_state(self) -> Dict[str, Any]:
        """Load show state from file."""
        if self.state_file.exists():
            with open(self.state_file) as f:
                return json.load(f)
        return {
            "current_episode_number": 0,
            "total_episodes": 0,
            "current_season": 1,
            "show_started": None,
            "last_episode_date": None,
            "upcoming_topics": [],
            "guest_pipeline": [],
            "listener_questions": [],
            "weekly_challenge": None
        }

    def _save_state(self):
        """Save show state to file."""
        with open(self.state_file, "w") as f:
            json.dump(self.state, f, indent=2, default=str)

    def get_next_episode_number(self) -> int:
        """Get the next episode number."""
        self.state["current_episode_number"] += 1
        self._save_state()
        return self.state["current_episode_number"]

    def get_next_release_date(self) -> datetime:
        """Calculate the next release date based on schedule."""
        today = datetime.now()
        release_days = {"Tuesday": 1, "Friday": 4}  # Monday = 0

        current_weekday = today.weekday()

        # Find next release day
        days_ahead = None
        for day_name, day_num in release_days.items():
            diff = day_num - current_weekday
            if diff <= 0:
                diff += 7
            if days_ahead is None or diff < days_ahead:
                days_ahead = diff

        next_date = today + timedelta(days=days_ahead)
        return next_date.replace(hour=18, minute=0, second=0, microsecond=0)

    def get_show_status(self) -> Dict[str, Any]:
        """Get current show status."""
        return {
            "show_name": self.CONFIG["show_name"],
            "current_episode": self.state["current_episode_number"],
            "total_episodes": self.state["total_episodes"],
            "current_season": self.state["current_season"],
            "next_release": self.get_next_release_date().isoformat(),
            "upcoming_topics": self.state["upcoming_topics"][:5],
            "pending_questions": len(self.state["listener_questions"]),
            "guest_pipeline": len(self.state["guest_pipeline"]),
            "weekly_challenge": self.state["weekly_challenge"]
        }

    def add_topic_to_queue(self, topic: str, theme: str, priority: int = 5):
        """Add a topic to the upcoming topics queue."""
        self.state["upcoming_topics"].append({
            "topic": topic,
            "theme": theme,
            "priority": priority,
            "added_date": datetime.now().isoformat(),
            "status": "queued"
        })
        # Sort by priority
        self.state["upcoming_topics"].sort(key=lambda x: x["priority"], reverse=True)
        self._save_state()

    def get_next_topic(self) -> Optional[Dict[str, Any]]:
        """Get the next topic from queue."""
        if self.state["upcoming_topics"]:
            topic = self.state["upcoming_topics"].pop(0)
            topic["status"] = "in_production"
            self._save_state()
            return topic
        return None

    def add_listener_question(
        self,
        question: str,
        listener_name: str = "Anonymous",
        city: str = "Pakistan",
        contact: str = None
    ):
        """Add a listener question to the queue."""
        self.state["listener_questions"].append({
            "question": question,
            "listener_name": listener_name,
            "city": city,
            "contact": contact,
            "received_date": datetime.now().isoformat(),
            "status": "pending",
            "answered_in_episode": None
        })
        self._save_state()

    def get_pending_questions(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Get pending listener questions."""
        pending = [q for q in self.state["listener_questions"] if q["status"] == "pending"]
        return pending[:limit]

    def set_weekly_challenge(self, challenge: str, episode_number: int):
        """Set the weekly challenge."""
        self.state["weekly_challenge"] = {
            "challenge": challenge,
            "set_in_episode": episode_number,
            "date": datetime.now().isoformat()
        }
        self._save_state()

    def generate_weekly_plan(self) -> Dict[str, Any]:
        """Generate a weekly production plan."""
        next_tuesday = self.get_next_release_date()
        # Adjust to get both Tuesday and Friday
        if next_tuesday.weekday() == 4:  # Friday
            tuesday = next_tuesday + timedelta(days=4)
            friday = next_tuesday
        else:
            tuesday = next_tuesday
            friday = tuesday + timedelta(days=3)

        return {
            "week_of": tuesday.strftime("%Y-%m-%d"),
            "episode_1": {
                "release_date": tuesday.strftime("%Y-%m-%d"),
                "release_day": "Tuesday",
                "production_schedule": {
                    "research": (tuesday - timedelta(days=3)).strftime("%Y-%m-%d"),
                    "script": (tuesday - timedelta(days=2)).strftime("%Y-%m-%d"),
                    "record": (tuesday - timedelta(days=1)).strftime("%Y-%m-%d"),
                    "edit_release": tuesday.strftime("%Y-%m-%d")
                },
                "topic": self.state["upcoming_topics"][0] if self.state["upcoming_topics"] else None
            },
            "episode_2": {
                "release_date": friday.strftime("%Y-%m-%d"),
                "release_day": "Friday",
                "production_schedule": {
                    "research": tuesday.strftime("%Y-%m-%d"),
                    "script": (tuesday + timedelta(days=1)).strftime("%Y-%m-%d"),
                    "record": (tuesday + timedelta(days=2)).strftime("%Y-%m-%d"),
                    "edit_release": friday.strftime("%Y-%m-%d")
                },
                "topic": self.state["upcoming_topics"][1] if len(self.state["upcoming_topics"]) > 1 else None
            },
            "pending_questions": len(self.state["listener_questions"]),
            "guests_available": len(self.state["guest_pipeline"])
        }

    def print_dashboard(self):
        """Print show dashboard to console."""
        status = self.get_show_status()
        plan = self.generate_weekly_plan()

        print("\n" + "=" * 70)
        print(f"🎙️  {self.CONFIG['show_name']} ({self.CONFIG['show_name_urdu']}) DASHBOARD")
        print("=" * 70)
        print(f"\n📊 SHOW STATUS")
        print(f"   Episodes Produced: {status['total_episodes']}")
        print(f"   Current Episode: #{status['current_episode']}")
        print(f"   Season: {status['current_season']}")
        print(f"   Next Release: {status['next_release']}")

        print(f"\n📅 THIS WEEK'S PRODUCTION")
        print(f"   Episode 1 (Tuesday): {plan['episode_1']['topic']['topic'] if plan['episode_1']['topic'] else 'TBD'}")
        print(f"   Episode 2 (Friday): {plan['episode_2']['topic']['topic'] if plan['episode_2']['topic'] else 'TBD'}")

        print(f"\n📝 CONTENT QUEUE")
        print(f"   Upcoming Topics: {len(self.state['upcoming_topics'])}")
        print(f"   Pending Questions: {status['pending_questions']}")
        print(f"   Guests in Pipeline: {status['guest_pipeline']}")

        if status['weekly_challenge']:
            print(f"\n🎯 WEEKLY CHALLENGE")
            print(f"   {status['weekly_challenge']['challenge']}")

        print("\n" + "=" * 70)
