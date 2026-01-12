#!/usr/bin/env python3
"""
BHARTE CHALO - Command Line Interface

Complete CLI for managing the Bharte Chalo radio show.
"""

import sys
from datetime import datetime
from pathlib import Path

from .show_manager import ShowManager
from .episode_manager import EpisodeManager, EpisodeStatus
from .guest_manager import GuestManager, GuestStatus
from .listener_manager import ListenerManager
from .social_manager import SocialMediaManager
from .calendar_manager import CalendarManager


def print_header():
    """Print CLI header."""
    print("""
╔══════════════════════════════════════════════════════════════════╗
║   🎙️  BHARTE CHALO - بڑھتے چلو                                   ║
║   Pakistan's AI, IT, Leadership & Innovation Radio Show          ║
║   "Sochein Behtar, Faisla Karein Smarter, Aagey Barhein"         ║
╚══════════════════════════════════════════════════════════════════╝
""")


def print_help():
    """Print help message."""
    print_header()
    print("""
USAGE:
    python -m bharte_chalo <command> [options]

COMMANDS:

  📊 SHOW MANAGEMENT
    dashboard           Show complete dashboard
    status             Show current show status
    week               Show this week's tasks

  📋 EPISODE MANAGEMENT
    episode new <topic> <theme>    Create new episode
    episode list                   List all episodes
    episode board                  Show production board
    episode script <id>            Generate script for episode

  🎤 GUEST MANAGEMENT
    guest add <name>               Add guest to pipeline
    guest list                     List all guests
    guest pipeline                 Show guest pipeline
    guest email <id>               Generate outreach email

  👥 LISTENER ENGAGEMENT
    question add <question>        Add listener question
    question list                  List pending questions
    listener stats                 Show engagement stats

  📅 CALENDAR
    calendar month [YYYY] [MM]     Show month calendar
    calendar plan <month> <theme>  Plan a month
    calendar week                  Show this week's tasks

  📱 SOCIAL MEDIA
    social pack <episode_id>       Generate social media pack
    social calendar <episode_id>   Show posting schedule

  🚀 QUICK ACTIONS
    next                 Show what's next to do
    record <episode_id>  Mark episode as recorded
    release <episode_id> Mark episode as released

EXAMPLES:
    python -m bharte_chalo dashboard
    python -m bharte_chalo episode new "What is AI" "AI Fundamentals"
    python -m bharte_chalo guest add "Dr. Ahmad"
    python -m bharte_chalo question add "AI kya hai?"
    python -m bharte_chalo calendar month 2024 3
""")


class BharteChaloCLI:
    """CLI for Bharte Chalo show management."""

    def __init__(self, base_path: str = "bharte_chalo", gemini_client=None):
        """Initialize CLI with all managers."""
        self.base_path = Path(base_path)
        self.gemini = gemini_client

        # Initialize managers
        self.show = ShowManager(self.base_path, gemini_client)
        self.episodes = EpisodeManager(self.base_path, gemini_client)
        self.guests = GuestManager(self.base_path)
        self.listeners = ListenerManager(self.base_path)
        self.social = SocialMediaManager(self.base_path, gemini_client)
        self.calendar = CalendarManager(self.base_path)

    def run(self, args: list):
        """Run CLI command."""
        if not args:
            print_help()
            return

        command = args[0].lower()

        # Dashboard
        if command == "dashboard":
            self.show_dashboard()

        elif command == "status":
            self.show.print_dashboard()

        elif command == "week":
            self.calendar.print_week_tasks()

        # Episode commands
        elif command == "episode":
            self.handle_episode(args[1:])

        # Guest commands
        elif command == "guest":
            self.handle_guest(args[1:])

        # Question/Listener commands
        elif command == "question":
            self.handle_question(args[1:])

        elif command == "listener":
            if len(args) > 1 and args[1] == "stats":
                self.listeners.print_dashboard()

        # Calendar commands
        elif command == "calendar":
            self.handle_calendar(args[1:])

        # Social commands
        elif command == "social":
            self.handle_social(args[1:])

        # Quick actions
        elif command == "next":
            self.show_next_action()

        elif command == "record":
            if len(args) > 1:
                self.episodes.update_episode_status(args[1], EpisodeStatus.RECORDING)
                print(f"✅ Episode {args[1]} marked as recording")

        elif command == "release":
            if len(args) > 1:
                self.episodes.mark_released(args[1])
                print(f"✅ Episode {args[1]} marked as released")

        elif command == "help":
            print_help()

        else:
            print(f"Unknown command: {command}")
            print("Use 'help' to see available commands")

    def show_dashboard(self):
        """Show complete dashboard."""
        print_header()

        # Show status
        status = self.show.get_show_status()
        print("📊 SHOW STATUS")
        print(f"   Current Episode: #{status['current_episode']}")
        print(f"   Next Release: {status['next_release']}")

        # Production board summary
        board = self.episodes.get_production_board()
        print("\n📋 PRODUCTION BOARD")
        for status_name, eps in board.items():
            if eps:
                print(f"   {status_name.title()}: {len(eps)}")

        # Engagement
        stats = self.listeners.get_engagement_stats()
        print("\n👥 LISTENER ENGAGEMENT")
        print(f"   Pending Questions: {stats['pending_questions']}")

        # Guest pipeline
        pipeline = self.guests.get_guest_pipeline()
        confirmed = len(pipeline.get("confirmed", [])) + len(pipeline.get("scheduled", []))
        print(f"\n🎤 GUESTS")
        print(f"   Confirmed/Scheduled: {confirmed}")
        print(f"   In Pipeline: {len(pipeline.get('contacted', []))}")

        # This week
        print("\n📅 THIS WEEK")
        plan = self.show.generate_weekly_plan()
        ep1 = plan["episode_1"]["topic"]["topic"] if plan["episode_1"]["topic"] else "TBD"
        ep2 = plan["episode_2"]["topic"]["topic"] if plan["episode_2"]["topic"] else "TBD"
        print(f"   Tuesday: {ep1[:40]}")
        print(f"   Friday: {ep2[:40]}")

    def handle_episode(self, args: list):
        """Handle episode commands."""
        if not args:
            print("Usage: episode <new|list|board|script> [options]")
            return

        subcommand = args[0].lower()

        if subcommand == "new":
            if len(args) < 3:
                print("Usage: episode new <topic> <theme>")
                return
            topic = args[1]
            theme = args[2]
            release_date = self.show.get_next_release_date().strftime("%Y-%m-%d")

            episode = self.episodes.create_episode(
                topic=topic,
                theme=theme,
                release_date=release_date
            )
            print(f"✅ Created episode: {episode['id']}")
            print(f"   Topic: {topic}")
            print(f"   Release: {release_date}")

        elif subcommand == "list":
            upcoming = self.episodes.get_upcoming_episodes(10)
            print("\n📋 UPCOMING EPISODES")
            for ep in upcoming:
                print(f"   [{ep['id']}] {ep['topic'][:40]}")
                print(f"          Release: {ep['release_date']} | Status: {ep['status']}")

        elif subcommand == "board":
            self.episodes.print_production_board()

        elif subcommand == "script":
            if len(args) < 2:
                print("Usage: episode script <episode_id>")
                return
            episode_id = args[1]
            episode = self.episodes.get_episode(episode_id)
            if episode:
                print(f"📝 Generate script for: {episode['topic']}")
                print("   (Use radio generator with topic)")
            else:
                print(f"Episode {episode_id} not found")

    def handle_guest(self, args: list):
        """Handle guest commands."""
        if not args:
            print("Usage: guest <add|list|pipeline|email> [options]")
            return

        subcommand = args[0].lower()

        if subcommand == "add":
            if len(args) < 2:
                print("Usage: guest add <name>")
                return
            name = " ".join(args[1:])
            guest = self.guests.add_guest(
                name=name,
                background="TBD - Add background",
                expertise=["Tech"],
                why_invite="Great potential guest"
            )
            print(f"✅ Added guest: {guest['id']} - {name}")

        elif subcommand == "list":
            pipeline = self.guests.get_guest_pipeline()
            print("\n🎤 ALL GUESTS")
            for status, guests in pipeline.items():
                if guests:
                    print(f"\n   {status.upper()}")
                    for g in guests:
                        print(f"      [{g['id']}] {g['name']}")

        elif subcommand == "pipeline":
            self.guests.print_pipeline()

        elif subcommand == "email":
            if len(args) < 2:
                print("Usage: guest email <guest_id>")
                return
            email = self.guests.generate_outreach_email(args[1])
            print(email)

    def handle_question(self, args: list):
        """Handle question commands."""
        if not args:
            print("Usage: question <add|list> [options]")
            return

        subcommand = args[0].lower()

        if subcommand == "add":
            if len(args) < 2:
                print("Usage: question add <question>")
                return
            question = " ".join(args[1:])
            q = self.listeners.add_question(question)
            print(f"✅ Added question: {q['id']}")

        elif subcommand == "list":
            pending = self.listeners.get_pending_questions(10)
            print("\n❓ PENDING QUESTIONS")
            for q in pending:
                print(f"   [{q['id']}] {q['question'][:50]}...")
                print(f"          From: {q['listener_name']}, {q['city']}")

    def handle_calendar(self, args: list):
        """Handle calendar commands."""
        if not args:
            print("Usage: calendar <month|plan|week> [options]")
            return

        subcommand = args[0].lower()

        if subcommand == "month":
            year = int(args[1]) if len(args) > 1 else datetime.now().year
            month = int(args[2]) if len(args) > 2 else datetime.now().month
            self.calendar.print_month_calendar(year, month)

        elif subcommand == "week":
            self.calendar.print_week_tasks()

        elif subcommand == "plan":
            print("Use: calendar plan <year> <month> <theme>")

    def handle_social(self, args: list):
        """Handle social media commands."""
        if not args:
            print("Usage: social <pack|calendar> <episode_id>")
            return

        subcommand = args[0].lower()

        if subcommand == "calendar" and len(args) > 1:
            episode_id = args[1]
            episode = self.episodes.get_episode(episode_id)
            if episode:
                self.social.print_social_calendar(episode_id, episode["release_date"])
            else:
                print(f"Episode {episode_id} not found")

    def show_next_action(self):
        """Show the next recommended action."""
        print("\n🎯 NEXT RECOMMENDED ACTIONS:")

        # Check production board
        board = self.episodes.get_production_board()

        if board["scripting"]:
            ep = board["scripting"][0]
            print(f"   1. 📝 Record episode: {ep['topic'][:40]}")

        if board["planned"]:
            ep = board["planned"][0]
            print(f"   2. 🔍 Research for: {ep['topic'][:40]}")

        # Check pending questions
        pending = self.listeners.get_pending_questions(1)
        if pending:
            print(f"   3. ❓ Review pending questions ({len(pending)})")

        # Check guest pipeline
        pipeline = self.guests.get_guest_pipeline()
        if pipeline.get("wishlist"):
            print(f"   4. 📧 Reach out to guests ({len(pipeline['wishlist'])} in wishlist)")


def main():
    """Main entry point for CLI."""
    cli = BharteChaloCI()
    cli.run(sys.argv[1:])


if __name__ == "__main__":
    main()
