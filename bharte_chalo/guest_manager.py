#!/usr/bin/env python3
"""
BHARTE CHALO - Guest Manager

Manages guest pipeline, outreach, and interview scheduling.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List
from enum import Enum


class GuestStatus(Enum):
    """Guest pipeline status."""
    WISHLIST = "wishlist"
    CONTACTED = "contacted"
    CONFIRMED = "confirmed"
    SCHEDULED = "scheduled"
    RECORDED = "recorded"
    RELEASED = "released"


class GuestManager:
    """
    Manages guest pipeline for Bharte Chalo.

    Handles:
    - Guest wishlist and research
    - Outreach tracking
    - Interview scheduling
    - Guest prep materials
    """

    def __init__(self, base_path: Path):
        """
        Initialize guest manager.

        Args:
            base_path: Base path for guest data
        """
        self.base_path = Path(base_path)
        self.guests_path = self.base_path / "guests"
        self.guests_path.mkdir(parents=True, exist_ok=True)

        # Load guest registry
        self.registry_file = self.guests_path / "registry.json"
        self.registry = self._load_registry()

    def _load_registry(self) -> Dict[str, Any]:
        """Load guest registry."""
        if self.registry_file.exists():
            with open(self.registry_file) as f:
                return json.load(f)
        return {"guests": {}, "guest_count": 0}

    def _save_registry(self):
        """Save guest registry."""
        with open(self.registry_file, "w") as f:
            json.dump(self.registry, f, indent=2, default=str)

    def add_guest(
        self,
        name: str,
        background: str,
        expertise: List[str],
        contact_info: Optional[Dict[str, str]] = None,
        why_invite: str = "",
        topic_ideas: Optional[List[str]] = None,
        status: GuestStatus = GuestStatus.WISHLIST
    ) -> Dict[str, Any]:
        """
        Add a guest to the pipeline.

        Args:
            name: Guest name
            background: Guest background/bio
            expertise: Areas of expertise
            contact_info: Contact information
            why_invite: Why this guest would be good
            topic_ideas: Potential episode topics with this guest
            status: Initial status

        Returns:
            Guest record
        """
        self.registry["guest_count"] += 1
        guest_id = f"G{self.registry['guest_count']:03d}"

        guest = {
            "id": guest_id,
            "name": name,
            "background": background,
            "expertise": expertise,
            "contact_info": contact_info or {},
            "why_invite": why_invite,
            "topic_ideas": topic_ideas or [],
            "status": status.value,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "outreach_history": [],
            "scheduled_episode": None,
            "interview_notes": None,
            "follow_up_notes": []
        }

        # Save guest file
        guest_file = self.guests_path / f"{guest_id}.json"
        with open(guest_file, "w") as f:
            json.dump(guest, f, indent=2)

        # Update registry
        self.registry["guests"][guest_id] = {
            "name": name,
            "status": status.value,
            "expertise": expertise[:3]  # First 3 for quick reference
        }
        self._save_registry()

        return guest

    def get_guest(self, guest_id: str) -> Optional[Dict[str, Any]]:
        """Get guest by ID."""
        guest_file = self.guests_path / f"{guest_id}.json"
        if guest_file.exists():
            with open(guest_file) as f:
                return json.load(f)
        return None

    def update_guest_status(self, guest_id: str, status: GuestStatus, notes: str = ""):
        """Update guest status."""
        guest = self.get_guest(guest_id)
        if guest:
            guest["status"] = status.value
            guest["updated_at"] = datetime.now().isoformat()
            if notes:
                guest["follow_up_notes"].append({
                    "timestamp": datetime.now().isoformat(),
                    "status": status.value,
                    "notes": notes
                })

            guest_file = self.guests_path / f"{guest_id}.json"
            with open(guest_file, "w") as f:
                json.dump(guest, f, indent=2)

            # Update registry
            if guest_id in self.registry["guests"]:
                self.registry["guests"][guest_id]["status"] = status.value
                self._save_registry()

    def log_outreach(
        self,
        guest_id: str,
        method: str,
        message: str,
        response: Optional[str] = None
    ):
        """Log an outreach attempt."""
        guest = self.get_guest(guest_id)
        if guest:
            guest["outreach_history"].append({
                "timestamp": datetime.now().isoformat(),
                "method": method,
                "message": message,
                "response": response
            })

            if guest["status"] == GuestStatus.WISHLIST.value:
                guest["status"] = GuestStatus.CONTACTED.value

            guest_file = self.guests_path / f"{guest_id}.json"
            with open(guest_file, "w") as f:
                json.dump(guest, f, indent=2)

            self.registry["guests"][guest_id]["status"] = guest["status"]
            self._save_registry()

    def schedule_guest(self, guest_id: str, episode_id: str, recording_date: str):
        """Schedule a guest for an episode."""
        guest = self.get_guest(guest_id)
        if guest:
            guest["status"] = GuestStatus.SCHEDULED.value
            guest["scheduled_episode"] = {
                "episode_id": episode_id,
                "recording_date": recording_date,
                "scheduled_at": datetime.now().isoformat()
            }

            guest_file = self.guests_path / f"{guest_id}.json"
            with open(guest_file, "w") as f:
                json.dump(guest, f, indent=2)

            self.registry["guests"][guest_id]["status"] = GuestStatus.SCHEDULED.value
            self._save_registry()

    def get_guests_by_status(self, status: GuestStatus) -> List[Dict[str, Any]]:
        """Get all guests with a specific status."""
        guests = []
        for guest_id, info in self.registry["guests"].items():
            if info["status"] == status.value:
                guest = self.get_guest(guest_id)
                if guest:
                    guests.append(guest)
        return guests

    def get_guest_pipeline(self) -> Dict[str, List[Dict[str, Any]]]:
        """Get guest pipeline organized by status."""
        pipeline = {
            "wishlist": [],
            "contacted": [],
            "confirmed": [],
            "scheduled": [],
            "recorded": [],
            "released": []
        }

        for guest_id, info in self.registry["guests"].items():
            status = info["status"]
            if status in pipeline:
                pipeline[status].append({
                    "id": guest_id,
                    "name": info["name"],
                    "expertise": info["expertise"]
                })

        return pipeline

    def generate_outreach_email(self, guest_id: str) -> str:
        """Generate outreach email template for a guest."""
        guest = self.get_guest(guest_id)
        if not guest:
            return ""

        topics = ", ".join(guest["topic_ideas"][:2]) if guest["topic_ideas"] else "AI and technology"

        email = f"""Subject: Invitation to Bharte Chalo Radio Show

Assalam-u-Alaikum {guest['name'].split()[0]} Sahab/Sahiba,

I hope this message finds you well. I'm reaching out from "Bharte Chalo" -
Pakistan's radio show dedicated to educating our awaam on AI, IT, leadership,
and innovation.

{guest['why_invite']}

We believe your insights on {topics} would greatly benefit our listeners
across Pakistan - from students in Lahore to entrepreneurs in Karachi.

Episode Details:
- Format: 15-20 minute conversation within our 1-hour show
- Topics: Your journey, expertise, and advice for Pakistani youth
- Audience: Professionals, students, entrepreneurs across Pakistan
- Schedule: We release 2 episodes per week (Tuesday & Friday)

Would you be available for a recording in the next 2-3 weeks? We're flexible
with timing and can conduct the interview remotely.

Looking forward to your response.

With respect,
[Host Name]
Bharte Chalo - بڑھتے چلو
"Sochein Behtar, Faisla Karein Smarter, Aagey Barhein"

#BharteChalo
"""
        return email

    def generate_interview_prep(self, guest_id: str) -> Dict[str, Any]:
        """Generate interview preparation materials."""
        guest = self.get_guest(guest_id)
        if not guest:
            return {}

        prep = {
            "guest_name": guest["name"],
            "background_summary": guest["background"],
            "expertise_areas": guest["expertise"],
            "suggested_questions": [
                f"Aap ki journey kaise shuru hui {guest['expertise'][0] if guest['expertise'] else 'tech'} mein?",
                "Pakistan mein aapko sabse bara challenge kya laga?",
                "Nayi generation ke liye aapka kya message hai?",
                "Agar aap dobara start karein, toh kya differently karenge?",
                "Pakistan ka tech future aap kaise dekhte hain?"
            ],
            "pakistan_specific_questions": [
                "Pakistani students ko kya skills seekhni chahiye?",
                "Pakistan mein opportunities kahan hain?",
                "Brain drain ke baare mein aapka kya khayal hai?"
            ],
            "rapid_fire": [
                "Chai ya coffee?",
                "Favorite Pakistani food?",
                "Ek Pakistani city jo sabko visit karni chahiye?",
                "Early bird ya night owl?"
            ],
            "topics_to_cover": guest["topic_ideas"],
            "pre_interview_notes": [
                "Research guest's recent work/posts",
                "Find common ground with Pakistani context",
                "Prepare 2-3 personal anecdotes to share",
                "Have backup questions ready"
            ]
        }

        return prep

    def print_pipeline(self):
        """Print guest pipeline to console."""
        pipeline = self.get_guest_pipeline()

        print("\n" + "=" * 60)
        print("🎤 BHARTE CHALO - GUEST PIPELINE")
        print("=" * 60)

        for status, guests in pipeline.items():
            if guests:
                print(f"\n{'─' * 40}")
                print(f"📌 {status.upper()} ({len(guests)})")
                print(f"{'─' * 40}")
                for guest in guests[:5]:
                    expertise_str = ", ".join(guest["expertise"][:2])
                    print(f"  [{guest['id']}] {guest['name']}")
                    print(f"          {expertise_str}")
