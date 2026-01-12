#!/usr/bin/env python3
"""
BHARTE CHALO - Calendar Manager

Manages content calendar, scheduling, and production planning.
"""

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any, Optional, List
from calendar import monthcalendar, month_name


class CalendarManager:
    """
    Manages content calendar for Bharte Chalo.

    Handles:
    - Episode scheduling
    - Production timeline
    - Monthly/quarterly planning
    - Theme scheduling
    """

    # Release days (Tuesday=1, Friday=4)
    RELEASE_DAYS = [1, 4]  # 0=Monday, 1=Tuesday, etc.

    # Production lead times (days before release)
    PRODUCTION_TIMELINE = {
        "research": 3,
        "script": 2,
        "record": 1,
        "edit": 0  # Same day as release
    }

    def __init__(self, base_path: Path):
        """
        Initialize calendar manager.

        Args:
            base_path: Base path for calendar data
        """
        self.base_path = Path(base_path)
        self.calendar_path = self.base_path / "calendar"
        self.calendar_path.mkdir(parents=True, exist_ok=True)

        # Load calendar data
        self.data_file = self.calendar_path / "calendar_data.json"
        self.data = self._load_data()

    def _load_data(self) -> Dict[str, Any]:
        """Load calendar data."""
        if self.data_file.exists():
            with open(self.data_file) as f:
                return json.load(f)
        return {
            "scheduled_episodes": {},
            "themes": {},
            "special_dates": {},
            "quarterly_themes": {}
        }

    def _save_data(self):
        """Save calendar data."""
        with open(self.data_file, "w") as f:
            json.dump(self.data, f, indent=2, default=str)

    def get_release_dates(
        self,
        start_date: datetime,
        num_episodes: int = 8
    ) -> List[datetime]:
        """
        Get upcoming release dates.

        Args:
            start_date: Start date to calculate from
            num_episodes: Number of episodes to schedule

        Returns:
            List of release dates
        """
        dates = []
        current = start_date

        while len(dates) < num_episodes:
            if current.weekday() in self.RELEASE_DAYS:
                dates.append(current)
            current += timedelta(days=1)

        return dates

    def schedule_episode(
        self,
        release_date: str,
        topic: str,
        theme: str,
        episode_type: str = "solo",
        guest_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Schedule an episode.

        Args:
            release_date: Release date (YYYY-MM-DD)
            topic: Episode topic
            theme: Episode theme
            episode_type: Type (solo, guest, qa, news)
            guest_id: Optional guest ID

        Returns:
            Scheduled episode info
        """
        release = datetime.strptime(release_date, "%Y-%m-%d")

        scheduled = {
            "release_date": release_date,
            "topic": topic,
            "theme": theme,
            "episode_type": episode_type,
            "guest_id": guest_id,
            "production_dates": {
                "research": (release - timedelta(days=self.PRODUCTION_TIMELINE["research"])).strftime("%Y-%m-%d"),
                "script": (release - timedelta(days=self.PRODUCTION_TIMELINE["script"])).strftime("%Y-%m-%d"),
                "record": (release - timedelta(days=self.PRODUCTION_TIMELINE["record"])).strftime("%Y-%m-%d"),
                "edit_release": release_date
            },
            "status": "scheduled",
            "created_at": datetime.now().isoformat()
        }

        self.data["scheduled_episodes"][release_date] = scheduled
        self._save_data()

        return scheduled

    def get_month_schedule(
        self,
        year: int,
        month: int
    ) -> Dict[str, Any]:
        """
        Get schedule for a specific month.

        Args:
            year: Year
            month: Month (1-12)

        Returns:
            Monthly schedule
        """
        schedule = {
            "year": year,
            "month": month,
            "month_name": month_name[month],
            "weeks": [],
            "episodes": []
        }

        # Get all dates in month
        weeks = monthcalendar(year, month)

        for week_num, week in enumerate(weeks, 1):
            week_data = {
                "week": week_num,
                "days": []
            }

            for day_num, day in enumerate(week):
                if day == 0:
                    continue

                date_str = f"{year}-{month:02d}-{day:02d}"
                day_data = {
                    "date": date_str,
                    "day": day,
                    "weekday": day_num,
                    "is_release_day": day_num in self.RELEASE_DAYS,
                    "scheduled_episode": self.data["scheduled_episodes"].get(date_str),
                    "special": self.data["special_dates"].get(date_str)
                }
                week_data["days"].append(day_data)

                if day_data["scheduled_episode"]:
                    schedule["episodes"].append(day_data["scheduled_episode"])

            schedule["weeks"].append(week_data)

        return schedule

    def set_quarterly_theme(
        self,
        year: int,
        quarter: int,
        theme: str,
        focus_areas: List[str]
    ):
        """
        Set theme for a quarter.

        Args:
            year: Year
            quarter: Quarter (1-4)
            theme: Main theme
            focus_areas: Focus areas for the quarter
        """
        key = f"{year}-Q{quarter}"
        self.data["quarterly_themes"][key] = {
            "theme": theme,
            "focus_areas": focus_areas,
            "set_at": datetime.now().isoformat()
        }
        self._save_data()

    def add_special_date(
        self,
        date: str,
        name: str,
        description: str,
        content_ideas: Optional[List[str]] = None
    ):
        """
        Add a special date to the calendar.

        Args:
            date: Date (YYYY-MM-DD)
            name: Name of the occasion
            description: Description
            content_ideas: Episode ideas for this date
        """
        self.data["special_dates"][date] = {
            "name": name,
            "description": description,
            "content_ideas": content_ideas or []
        }
        self._save_data()

    def get_week_tasks(self, week_start: datetime) -> Dict[str, List[Dict[str, Any]]]:
        """
        Get all tasks for a week.

        Args:
            week_start: Start of the week (Monday)

        Returns:
            Tasks organized by day
        """
        tasks = {}

        for i in range(7):
            date = week_start + timedelta(days=i)
            date_str = date.strftime("%Y-%m-%d")
            day_name = date.strftime("%A")

            tasks[day_name] = []

            # Check for scheduled episode release
            if date_str in self.data["scheduled_episodes"]:
                ep = self.data["scheduled_episodes"][date_str]
                tasks[day_name].append({
                    "type": "release",
                    "priority": "high",
                    "task": f"Release Episode: {ep['topic']}",
                    "details": "Edit in AM, Release at 6 PM, Promote on socials"
                })

            # Check for production tasks
            for release_date, ep in self.data["scheduled_episodes"].items():
                prod_dates = ep.get("production_dates", {})

                if prod_dates.get("research") == date_str:
                    tasks[day_name].append({
                        "type": "research",
                        "priority": "medium",
                        "task": f"Research: {ep['topic']}",
                        "for_episode": release_date
                    })

                if prod_dates.get("script") == date_str:
                    tasks[day_name].append({
                        "type": "script",
                        "priority": "high",
                        "task": f"Generate Script: {ep['topic']}",
                        "for_episode": release_date
                    })

                if prod_dates.get("record") == date_str:
                    tasks[day_name].append({
                        "type": "record",
                        "priority": "high",
                        "task": f"Record Episode: {ep['topic']}",
                        "for_episode": release_date
                    })

        return tasks

    def generate_month_plan(
        self,
        year: int,
        month: int,
        monthly_theme: str,
        topics: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Generate a complete month plan.

        Args:
            year: Year
            month: Month
            monthly_theme: Theme for the month
            topics: List of topics with themes

        Returns:
            Complete month plan
        """
        # Get release dates for the month
        start = datetime(year, month, 1)
        if month == 12:
            end = datetime(year + 1, 1, 1) - timedelta(days=1)
        else:
            end = datetime(year, month + 1, 1) - timedelta(days=1)

        release_dates = []
        current = start
        while current <= end:
            if current.weekday() in self.RELEASE_DAYS:
                release_dates.append(current)
            current += timedelta(days=1)

        # Schedule episodes
        plan = {
            "year": year,
            "month": month,
            "month_name": month_name[month],
            "monthly_theme": monthly_theme,
            "episodes": []
        }

        for i, release_date in enumerate(release_dates):
            if i < len(topics):
                topic_info = topics[i]
                episode = self.schedule_episode(
                    release_date=release_date.strftime("%Y-%m-%d"),
                    topic=topic_info.get("topic", f"Topic {i+1}"),
                    theme=topic_info.get("theme", monthly_theme),
                    episode_type=topic_info.get("type", "solo"),
                    guest_id=topic_info.get("guest_id")
                )
                plan["episodes"].append(episode)

        return plan

    def print_month_calendar(self, year: int, month: int):
        """Print visual calendar for a month."""
        schedule = self.get_month_schedule(year, month)

        print("\n" + "=" * 70)
        print(f"📅 BHARTE CHALO - {schedule['month_name'].upper()} {year}")
        print("=" * 70)
        print()
        print("   Mon        Tue        Wed        Thu        Fri        Sat        Sun")
        print("   " + "-" * 65)

        for week in schedule["weeks"]:
            row = "   "
            for day_num in range(7):
                day_data = next((d for d in week["days"] if d["weekday"] == day_num), None)

                if day_data:
                    day = str(day_data["day"]).rjust(2)
                    if day_data["scheduled_episode"]:
                        row += f"[{day}]🎙️    "
                    elif day_data["is_release_day"]:
                        row += f" {day} 📻    "
                    else:
                        row += f" {day}       "
                else:
                    row += "          "

            print(row)

        print()
        print("   Legend: 🎙️ = Episode Scheduled, 📻 = Release Day")

        if schedule["episodes"]:
            print("\n   📋 SCHEDULED EPISODES:")
            for ep in schedule["episodes"]:
                print(f"      {ep['release_date']}: {ep['topic'][:40]}")

    def print_week_tasks(self, week_start: Optional[datetime] = None):
        """Print tasks for the current/specified week."""
        if week_start is None:
            today = datetime.now()
            week_start = today - timedelta(days=today.weekday())

        tasks = self.get_week_tasks(week_start)

        print("\n" + "=" * 60)
        print(f"📋 WEEK OF {week_start.strftime('%B %d, %Y')}")
        print("=" * 60)

        for day, day_tasks in tasks.items():
            date = week_start + timedelta(days=list(tasks.keys()).index(day))
            print(f"\n{'─' * 40}")
            print(f"📆 {day} ({date.strftime('%m/%d')})")

            if day_tasks:
                for task in day_tasks:
                    priority_icon = "🔴" if task["priority"] == "high" else "🟡"
                    print(f"   {priority_icon} {task['task']}")
                    if task.get("details"):
                        print(f"      {task['details']}")
            else:
                print("   No scheduled tasks")

    def initialize_pakistan_special_dates(self, year: int):
        """Initialize Pakistani special dates for a year."""
        special_dates = [
            ("03-23", "Pakistan Day", "Celebrate Pakistan's tech achievements", ["Pakistan Tech Journey", "Pakistani Innovators"]),
            ("08-14", "Independence Day", "Pakistan's tech independence and future", ["Pakistan Tech Vision", "Building Digital Pakistan"]),
            ("09-06", "Defence Day", "Defending Pakistan's digital future", ["Cybersecurity for Pakistan", "Digital Defense"]),
            ("11-09", "Iqbal Day", "Innovation and Vision like Iqbal", ["Visionary Thinking", "Pakistan's Tech Philosophy"]),
            ("12-25", "Quaid Day", "Leadership lessons from Quaid", ["Leadership Masterclass", "Building with Purpose"])
        ]

        for date_str, name, desc, ideas in special_dates:
            full_date = f"{year}-{date_str}"
            self.add_special_date(full_date, name, desc, ideas)

        print(f"✅ Added {len(special_dates)} Pakistani special dates for {year}")
