#!/usr/bin/env python3
"""
BHARTE CHALO - Listener Manager

Manages listener engagement, questions, feedback, and community.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List
from enum import Enum


class QuestionStatus(Enum):
    """Question status."""
    PENDING = "pending"
    SELECTED = "selected"
    ANSWERED = "answered"
    ARCHIVED = "archived"


class ListenerManager:
    """
    Manages listener engagement for Bharte Chalo.

    Handles:
    - Listener questions collection
    - Question selection for episodes
    - Feedback tracking
    - Community challenges
    - Listener shoutouts
    """

    def __init__(self, base_path: Path):
        """
        Initialize listener manager.

        Args:
            base_path: Base path for listener data
        """
        self.base_path = Path(base_path)
        self.listeners_path = self.base_path / "listeners"
        self.listeners_path.mkdir(parents=True, exist_ok=True)

        # Load listener data
        self.data_file = self.listeners_path / "listener_data.json"
        self.data = self._load_data()

    def _load_data(self) -> Dict[str, Any]:
        """Load listener data."""
        if self.data_file.exists():
            with open(self.data_file) as f:
                return json.load(f)
        return {
            "questions": [],
            "feedback": [],
            "challenges": [],
            "shoutouts": [],
            "subscribers": [],
            "stats": {
                "total_questions": 0,
                "questions_answered": 0,
                "total_feedback": 0,
                "challenges_completed": 0
            }
        }

    def _save_data(self):
        """Save listener data."""
        with open(self.data_file, "w") as f:
            json.dump(self.data, f, indent=2, default=str)

    def add_question(
        self,
        question: str,
        listener_name: str = "Anonymous",
        city: str = "Pakistan",
        contact: Optional[str] = None,
        topic_area: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Add a listener question.

        Args:
            question: The question text
            listener_name: Name of listener
            city: City in Pakistan
            contact: Optional contact info
            topic_area: Related topic area

        Returns:
            Question record
        """
        self.data["stats"]["total_questions"] += 1
        question_id = f"Q{self.data['stats']['total_questions']:04d}"

        question_record = {
            "id": question_id,
            "question": question,
            "listener_name": listener_name,
            "city": city,
            "contact": contact,
            "topic_area": topic_area,
            "status": QuestionStatus.PENDING.value,
            "received_at": datetime.now().isoformat(),
            "answered_in_episode": None,
            "answer_summary": None,
            "priority": 5  # Default priority (1-10)
        }

        self.data["questions"].append(question_record)
        self._save_data()

        return question_record

    def get_pending_questions(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get pending questions sorted by priority."""
        pending = [
            q for q in self.data["questions"]
            if q["status"] == QuestionStatus.PENDING.value
        ]
        # Sort by priority (high first) then by date (oldest first)
        pending.sort(key=lambda x: (-x.get("priority", 5), x["received_at"]))
        return pending[:limit]

    def get_questions_by_topic(self, topic: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Get questions related to a topic."""
        related = []
        topic_lower = topic.lower()

        for q in self.data["questions"]:
            if q["status"] == QuestionStatus.PENDING.value:
                if (topic_lower in q["question"].lower() or
                    (q.get("topic_area") and topic_lower in q["topic_area"].lower())):
                    related.append(q)

        return related[:limit]

    def select_questions_for_episode(
        self,
        episode_id: str,
        question_ids: List[str]
    ):
        """Select questions for an episode."""
        for q in self.data["questions"]:
            if q["id"] in question_ids:
                q["status"] = QuestionStatus.SELECTED.value
                q["answered_in_episode"] = episode_id
        self._save_data()

    def mark_question_answered(
        self,
        question_id: str,
        answer_summary: str
    ):
        """Mark a question as answered."""
        for q in self.data["questions"]:
            if q["id"] == question_id:
                q["status"] = QuestionStatus.ANSWERED.value
                q["answer_summary"] = answer_summary
                q["answered_at"] = datetime.now().isoformat()
                self.data["stats"]["questions_answered"] += 1
                break
        self._save_data()

    def set_question_priority(self, question_id: str, priority: int):
        """Set question priority (1-10)."""
        for q in self.data["questions"]:
            if q["id"] == question_id:
                q["priority"] = max(1, min(10, priority))
                break
        self._save_data()

    def add_feedback(
        self,
        episode_id: str,
        rating: int,
        comment: str,
        listener_name: str = "Anonymous",
        city: str = "Pakistan"
    ):
        """Add listener feedback for an episode."""
        feedback = {
            "id": f"F{len(self.data['feedback']) + 1:04d}",
            "episode_id": episode_id,
            "rating": max(1, min(5, rating)),
            "comment": comment,
            "listener_name": listener_name,
            "city": city,
            "received_at": datetime.now().isoformat()
        }

        self.data["feedback"].append(feedback)
        self.data["stats"]["total_feedback"] += 1
        self._save_data()

        return feedback

    def get_episode_feedback(self, episode_id: str) -> List[Dict[str, Any]]:
        """Get all feedback for an episode."""
        return [
            f for f in self.data["feedback"]
            if f["episode_id"] == episode_id
        ]

    def create_challenge(
        self,
        challenge: str,
        episode_id: str,
        deadline: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create a weekly challenge."""
        challenge_record = {
            "id": f"C{len(self.data['challenges']) + 1:03d}",
            "challenge": challenge,
            "episode_id": episode_id,
            "created_at": datetime.now().isoformat(),
            "deadline": deadline,
            "completions": []
        }

        self.data["challenges"].append(challenge_record)
        self._save_data()

        return challenge_record

    def log_challenge_completion(
        self,
        challenge_id: str,
        listener_name: str,
        city: str,
        proof: str = ""
    ):
        """Log a challenge completion."""
        for c in self.data["challenges"]:
            if c["id"] == challenge_id:
                c["completions"].append({
                    "listener_name": listener_name,
                    "city": city,
                    "proof": proof,
                    "completed_at": datetime.now().isoformat()
                })
                self.data["stats"]["challenges_completed"] += 1
                break
        self._save_data()

    def add_shoutout(
        self,
        listener_name: str,
        city: str,
        reason: str,
        episode_id: str
    ):
        """Add a listener shoutout."""
        shoutout = {
            "listener_name": listener_name,
            "city": city,
            "reason": reason,
            "episode_id": episode_id,
            "created_at": datetime.now().isoformat()
        }

        self.data["shoutouts"].append(shoutout)
        self._save_data()

    def get_shoutouts_for_episode(self, episode_id: str) -> List[Dict[str, Any]]:
        """Get shoutouts for an episode."""
        return [
            s for s in self.data["shoutouts"]
            if s["episode_id"] == episode_id
        ]

    def get_engagement_stats(self) -> Dict[str, Any]:
        """Get listener engagement statistics."""
        pending_questions = len([
            q for q in self.data["questions"]
            if q["status"] == QuestionStatus.PENDING.value
        ])

        # City distribution
        cities = {}
        for q in self.data["questions"]:
            city = q["city"]
            cities[city] = cities.get(city, 0) + 1

        return {
            "total_questions": self.data["stats"]["total_questions"],
            "questions_answered": self.data["stats"]["questions_answered"],
            "pending_questions": pending_questions,
            "total_feedback": self.data["stats"]["total_feedback"],
            "challenges_completed": self.data["stats"]["challenges_completed"],
            "top_cities": sorted(cities.items(), key=lambda x: x[1], reverse=True)[:5],
            "active_challenge": self.data["challenges"][-1] if self.data["challenges"] else None
        }

    def generate_qa_segment_content(
        self,
        question_ids: List[str]
    ) -> List[Dict[str, Any]]:
        """Generate content for Q&A segment."""
        content = []

        for q in self.data["questions"]:
            if q["id"] in question_ids:
                content.append({
                    "question": q["question"],
                    "listener_name": q["listener_name"],
                    "city": q["city"],
                    "intro_script": f"Yeh sawaal aaya hai {q['city']} se, {q['listener_name']} ki taraf se...",
                    "question_id": q["id"]
                })

        return content

    def print_dashboard(self):
        """Print listener engagement dashboard."""
        stats = self.get_engagement_stats()

        print("\n" + "=" * 60)
        print("👥 BHARTE CHALO - LISTENER ENGAGEMENT")
        print("=" * 60)

        print(f"\n📊 STATISTICS")
        print(f"   Total Questions: {stats['total_questions']}")
        print(f"   Answered: {stats['questions_answered']}")
        print(f"   Pending: {stats['pending_questions']}")
        print(f"   Total Feedback: {stats['total_feedback']}")
        print(f"   Challenges Completed: {stats['challenges_completed']}")

        if stats["top_cities"]:
            print(f"\n🏙️ TOP CITIES")
            for city, count in stats["top_cities"]:
                print(f"   {city}: {count} questions")

        if stats["active_challenge"]:
            print(f"\n🎯 ACTIVE CHALLENGE")
            print(f"   {stats['active_challenge']['challenge']}")
            print(f"   Completions: {len(stats['active_challenge']['completions'])}")

        # Show pending questions
        pending = self.get_pending_questions(5)
        if pending:
            print(f"\n❓ PENDING QUESTIONS (Top 5)")
            for q in pending:
                print(f"   [{q['id']}] {q['question'][:50]}...")
                print(f"          From: {q['listener_name']}, {q['city']}")
