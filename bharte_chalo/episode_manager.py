#!/usr/bin/env python3
"""
BHARTE CHALO - Episode Manager

Handles episode planning, production tracking, and script management.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List
from enum import Enum


class EpisodeStatus(Enum):
    """Episode production status."""
    PLANNED = "planned"
    RESEARCHING = "researching"
    SCRIPTING = "scripting"
    RECORDING = "recording"
    EDITING = "editing"
    READY = "ready"
    RELEASED = "released"


class EpisodeManager:
    """
    Manages episode lifecycle from planning to release.

    Handles:
    - Episode planning and scheduling
    - Script generation and storage
    - Production status tracking
    - Episode metadata management
    """

    def __init__(self, base_path: Path, gemini_client=None):
        """
        Initialize episode manager.

        Args:
            base_path: Base path for episode data
            gemini_client: GeminiClient for AI generation
        """
        self.base_path = Path(base_path)
        self.episodes_path = self.base_path / "episodes"
        self.episodes_path.mkdir(parents=True, exist_ok=True)
        self.gemini = gemini_client

        # Load episode registry
        self.registry_file = self.episodes_path / "registry.json"
        self.registry = self._load_registry()

    def _load_registry(self) -> Dict[str, Any]:
        """Load episode registry."""
        if self.registry_file.exists():
            with open(self.registry_file) as f:
                return json.load(f)
        return {"episodes": {}, "last_episode_number": 0}

    def _save_registry(self):
        """Save episode registry."""
        with open(self.registry_file, "w") as f:
            json.dump(self.registry, f, indent=2, default=str)

    def create_episode(
        self,
        topic: str,
        theme: str,
        release_date: str,
        episode_number: Optional[int] = None,
        guest: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Create a new episode entry.

        Args:
            topic: Episode topic
            theme: Episode theme category
            release_date: Planned release date (YYYY-MM-DD)
            episode_number: Episode number (auto-assigned if None)
            guest: Optional guest information

        Returns:
            Episode metadata
        """
        if episode_number is None:
            self.registry["last_episode_number"] += 1
            episode_number = self.registry["last_episode_number"]

        episode_id = f"EP{episode_number:03d}"

        episode = {
            "id": episode_id,
            "number": episode_number,
            "topic": topic,
            "theme": theme,
            "release_date": release_date,
            "status": EpisodeStatus.PLANNED.value,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "guest": guest,
            "script": None,
            "recording": None,
            "social_content": None,
            "analytics": None,
            "production_notes": [],
            "listener_questions_used": [],
            "resources_mentioned": [],
            "key_takeaways": []
        }

        # Create episode directory
        episode_dir = self.episodes_path / episode_id
        episode_dir.mkdir(exist_ok=True)

        # Save episode metadata
        with open(episode_dir / "metadata.json", "w") as f:
            json.dump(episode, f, indent=2)

        # Update registry
        self.registry["episodes"][episode_id] = {
            "number": episode_number,
            "topic": topic,
            "theme": theme,
            "release_date": release_date,
            "status": episode["status"]
        }
        self._save_registry()

        return episode

    def get_episode(self, episode_id: str) -> Optional[Dict[str, Any]]:
        """Get episode by ID."""
        episode_file = self.episodes_path / episode_id / "metadata.json"
        if episode_file.exists():
            with open(episode_file) as f:
                return json.load(f)
        return None

    def update_episode_status(self, episode_id: str, status: EpisodeStatus):
        """Update episode status."""
        episode = self.get_episode(episode_id)
        if episode:
            episode["status"] = status.value
            episode["updated_at"] = datetime.now().isoformat()
            episode["production_notes"].append({
                "timestamp": datetime.now().isoformat(),
                "status_change": status.value
            })

            # Save updated metadata
            episode_dir = self.episodes_path / episode_id
            with open(episode_dir / "metadata.json", "w") as f:
                json.dump(episode, f, indent=2)

            # Update registry
            if episode_id in self.registry["episodes"]:
                self.registry["episodes"][episode_id]["status"] = status.value
                self._save_registry()

    def save_script(self, episode_id: str, script: Dict[str, Any]):
        """Save episode script."""
        episode_dir = self.episodes_path / episode_id
        episode_dir.mkdir(exist_ok=True)

        # Save script JSON
        with open(episode_dir / "script.json", "w") as f:
            json.dump(script, f, indent=2, default=str)

        # Save script markdown
        if "formatted_markdown" in script:
            with open(episode_dir / "script.md", "w") as f:
                f.write(script["formatted_markdown"])

        # Update episode metadata
        episode = self.get_episode(episode_id)
        if episode:
            episode["script"] = {
                "generated_at": datetime.now().isoformat(),
                "title": script.get("episode_title", ""),
                "duration": script.get("total_duration", "60 minutes")
            }
            episode["status"] = EpisodeStatus.SCRIPTING.value

            with open(episode_dir / "metadata.json", "w") as f:
                json.dump(episode, f, indent=2)

    def get_episodes_by_status(self, status: EpisodeStatus) -> List[Dict[str, Any]]:
        """Get all episodes with a specific status."""
        episodes = []
        for episode_id, info in self.registry["episodes"].items():
            if info["status"] == status.value:
                episode = self.get_episode(episode_id)
                if episode:
                    episodes.append(episode)
        return episodes

    def get_upcoming_episodes(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Get upcoming unreleased episodes."""
        today = datetime.now().strftime("%Y-%m-%d")
        upcoming = []

        for episode_id, info in self.registry["episodes"].items():
            if info["release_date"] >= today and info["status"] != EpisodeStatus.RELEASED.value:
                episode = self.get_episode(episode_id)
                if episode:
                    upcoming.append(episode)

        # Sort by release date
        upcoming.sort(key=lambda x: x["release_date"])
        return upcoming[:limit]

    def get_recent_episodes(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recently released episodes."""
        released = self.get_episodes_by_status(EpisodeStatus.RELEASED)
        released.sort(key=lambda x: x["release_date"], reverse=True)
        return released[:limit]

    def add_production_note(self, episode_id: str, note: str):
        """Add a production note to an episode."""
        episode = self.get_episode(episode_id)
        if episode:
            episode["production_notes"].append({
                "timestamp": datetime.now().isoformat(),
                "note": note
            })
            episode_dir = self.episodes_path / episode_id
            with open(episode_dir / "metadata.json", "w") as f:
                json.dump(episode, f, indent=2)

    def set_recording_info(self, episode_id: str, recording_info: Dict[str, Any]):
        """Set recording information for an episode."""
        episode = self.get_episode(episode_id)
        if episode:
            episode["recording"] = {
                "recorded_at": datetime.now().isoformat(),
                **recording_info
            }
            episode["status"] = EpisodeStatus.RECORDING.value

            episode_dir = self.episodes_path / episode_id
            with open(episode_dir / "metadata.json", "w") as f:
                json.dump(episode, f, indent=2)

    def mark_released(self, episode_id: str, release_info: Optional[Dict[str, Any]] = None):
        """Mark an episode as released."""
        episode = self.get_episode(episode_id)
        if episode:
            episode["status"] = EpisodeStatus.RELEASED.value
            episode["released_at"] = datetime.now().isoformat()
            if release_info:
                episode["release_info"] = release_info

            episode_dir = self.episodes_path / episode_id
            with open(episode_dir / "metadata.json", "w") as f:
                json.dump(episode, f, indent=2)

            # Update registry
            if episode_id in self.registry["episodes"]:
                self.registry["episodes"][episode_id]["status"] = EpisodeStatus.RELEASED.value
                self._save_registry()

    def generate_episode_report(self, episode_id: str) -> str:
        """Generate a production report for an episode."""
        episode = self.get_episode(episode_id)
        if not episode:
            return f"Episode {episode_id} not found."

        report = []
        report.append(f"# Episode Report: {episode['id']}")
        report.append(f"\n## {episode['topic']}")
        report.append(f"\n**Theme:** {episode['theme']}")
        report.append(f"**Status:** {episode['status']}")
        report.append(f"**Release Date:** {episode['release_date']}")

        if episode.get("guest"):
            report.append(f"\n### Guest")
            report.append(f"- Name: {episode['guest'].get('name', 'TBD')}")
            report.append(f"- Background: {episode['guest'].get('background', 'TBD')}")

        if episode.get("script"):
            report.append(f"\n### Script")
            report.append(f"- Title: {episode['script'].get('title', 'TBD')}")
            report.append(f"- Generated: {episode['script'].get('generated_at', 'TBD')}")

        if episode.get("key_takeaways"):
            report.append(f"\n### Key Takeaways")
            for takeaway in episode["key_takeaways"]:
                report.append(f"- {takeaway}")

        if episode.get("production_notes"):
            report.append(f"\n### Production Notes")
            for note in episode["production_notes"][-5:]:  # Last 5 notes
                report.append(f"- [{note.get('timestamp', '')}] {note.get('note', note.get('status_change', ''))}")

        return "\n".join(report)

    def get_production_board(self) -> Dict[str, List[Dict[str, Any]]]:
        """Get Kanban-style production board."""
        board = {
            "planned": [],
            "researching": [],
            "scripting": [],
            "recording": [],
            "editing": [],
            "ready": [],
            "released": []
        }

        for episode_id, info in self.registry["episodes"].items():
            status = info["status"]
            if status in board:
                episode = self.get_episode(episode_id)
                if episode:
                    board[status].append({
                        "id": episode_id,
                        "number": episode["number"],
                        "topic": episode["topic"],
                        "release_date": episode["release_date"]
                    })

        # Sort each column by release date
        for status in board:
            board[status].sort(key=lambda x: x["release_date"])

        return board

    def print_production_board(self):
        """Print production board to console."""
        board = self.get_production_board()

        print("\n" + "=" * 80)
        print("📋 BHARTE CHALO - PRODUCTION BOARD")
        print("=" * 80)

        for status, episodes in board.items():
            if episodes:
                print(f"\n{'─' * 40}")
                print(f"📌 {status.upper()} ({len(episodes)})")
                print(f"{'─' * 40}")
                for ep in episodes[:5]:  # Show max 5 per column
                    print(f"  [{ep['id']}] {ep['topic'][:30]}...")
                    print(f"          Release: {ep['release_date']}")
