#!/usr/bin/env python3
"""
AI THOUGHT LEADERSHIP ENGINE
Main orchestrator for Ahmad Bilal's content generation system.

Commands:
    python main.py daily      - Daily content generation
    python main.py weekly     - Weekly deep content (newsletter, article)
    python main.py scan       - Quick AI news scan
    python main.py predict    - Generate predictions
    python main.py review     - Generate tool reviews
    python main.py radio      - Generate Bharte Chalo radio script
    python main.py show       - Bharte Chalo show management
    python main.py help       - Show this help

BHARTE CHALO SHOW COMMANDS:
    python main.py show dashboard    - Show complete dashboard
    python main.py show episode new <topic> <theme>  - Create episode
    python main.py show episode list - List episodes
    python main.py show guest add <name>  - Add guest
    python main.py show question add <question>  - Add listener question
    python main.py show calendar month  - Show month calendar
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from core.gemini_client import GeminiClient
from research.ai_news_scanner import AINewsScanner
from research.tool_tracker import ToolTracker
from analysis.hot_take_generator import HotTakeGenerator
from analysis.prediction_engine import PredictionEngine
from generators.linkedin_generator import LinkedInGenerator
from generators.twitter_generator import TwitterGenerator
from generators.newsletter_generator import NewsletterGenerator
from generators.article_generator import ArticleGenerator
from generators.radio_script_generator import RadioScriptGenerator


class AIThoughtLeadershipEngine:
    """
    Main orchestrator for the AI Thought Leadership Engine.
    Coordinates research, analysis, and content generation.
    """

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the engine with all components.

        Args:
            api_key: Optional Gemini API key
        """
        print("🚀 Initializing AI Thought Leadership Engine...")

        # Core client
        self.gemini = GeminiClient(api_key)

        # Research modules
        self.news_scanner = AINewsScanner(self.gemini)
        self.tool_tracker = ToolTracker(self.gemini)

        # Analysis modules
        self.hot_take_gen = HotTakeGenerator(self.gemini)
        self.prediction_engine = PredictionEngine(self.gemini)

        # Content generators
        self.linkedin_gen = LinkedInGenerator(self.gemini)
        self.twitter_gen = TwitterGenerator(self.gemini)
        self.newsletter_gen = NewsletterGenerator(self.gemini)
        self.article_gen = ArticleGenerator(self.gemini)
        self.radio_gen = RadioScriptGenerator(self.gemini)

        # Setup directories
        self.setup_directories()

        print("✅ Engine initialized successfully")

    def setup_directories(self):
        """Create necessary output directories."""
        dirs = [
            "output/daily",
            "output/weekly",
            "output/monthly",
            "output/radio",
            "data",
        ]
        for d in dirs:
            Path(d).mkdir(parents=True, exist_ok=True)

    def save_json(self, path: Path, data: Dict[str, Any]):
        """Save data as JSON."""
        with open(path, "w") as f:
            json.dump(data, f, indent=2, default=str)

    def save_markdown(self, path: Path, content: str):
        """Save content as markdown."""
        with open(path, "w") as f:
            f.write(content)

    def format_linkedin(self, posts: Dict[str, Any]) -> str:
        """Format LinkedIn posts as markdown."""
        output = []
        output.append("# LinkedIn Posts")
        output.append(f"Generated: {datetime.now().isoformat()}")
        output.append("")

        for i, post in enumerate(posts.get("posts", []), 1):
            output.append(f"---")
            output.append(f"## Post #{i}")
            output.append(f"**Type:** {post.get('type', 'N/A')}")
            output.append(f"**Target:** {post.get('target_audience', 'N/A')}")
            output.append(f"**Characters:** {post.get('char_count', 'N/A')}")
            output.append("")
            output.append("### Content")
            output.append("```")

            # Format the post content
            if post.get("hook"):
                output.append(post["hook"])
                output.append("")
            if post.get("body"):
                output.append(post["body"])
                output.append("")
            if post.get("cta"):
                output.append(post["cta"])
                output.append("")
            if post.get("hashtags"):
                output.append(" ".join(post["hashtags"]))

            output.append("```")
            output.append("")

            if post.get("philosophical_layer"):
                output.append(f"**Philosophical Layer:** {post['philosophical_layer']}")
                output.append("")

        return "\n".join(output)

    def format_twitter(self, content: Dict[str, Any]) -> str:
        """Format Twitter content as markdown."""
        output = []
        output.append("# Twitter Content")
        output.append(f"Generated: {datetime.now().isoformat()}")
        output.append("")

        # Standalone tweets
        output.append("## Standalone Tweets")
        for i, tweet in enumerate(content.get("standalone_tweets", []), 1):
            output.append(f"### Tweet #{i}")
            output.append(f"```")
            output.append(tweet.get("content", str(tweet)))
            output.append(f"```")
            if isinstance(tweet, dict) and tweet.get("char_count"):
                output.append(f"*{tweet['char_count']} characters*")
            output.append("")

        # Thread
        if content.get("thread"):
            thread = content["thread"]
            output.append("## Thread")
            output.append(f"**Topic:** {thread.get('topic', 'N/A')}")
            output.append("")
            for i, tweet in enumerate(thread.get("tweets", []), 1):
                output.append(f"### {i}/{len(thread.get('tweets', []))}")
                output.append(f"```")
                output.append(tweet)
                output.append(f"```")
                output.append("")

        return "\n".join(output)

    def format_media_hooks(self, hooks: Dict[str, Any]) -> str:
        """Format media opportunities as markdown."""
        output = []
        output.append("# Media Opportunities")
        output.append(f"Generated: {datetime.now().isoformat()}")
        output.append("")
        output.append(json.dumps(hooks, indent=2, default=str))
        return "\n".join(output)

    def run_daily(self) -> Dict[str, Any]:
        """
        Run daily content generation workflow.

        Returns:
            Generated content and research
        """
        print("\n" + "=" * 60)
        print("🚀 AI Thought Leadership Engine - DAILY RUN")
        print("=" * 60)

        today = datetime.now().strftime("%Y-%m-%d")
        output_path = Path(f"output/daily/{today}")
        output_path.mkdir(parents=True, exist_ok=True)

        results = {}

        # ========================================
        # PHASE 1: RESEARCH
        # ========================================
        print("\n📡 PHASE 1: Scanning AI landscape...")

        try:
            # Scan AI news
            print("  → Scanning AI news...")
            ai_news = self.news_scanner.scan_daily_ai_news()
            print("  ✓ AI news scanned")
            results["ai_news"] = ai_news
        except Exception as e:
            print(f"  ⚠ AI news scan failed: {e}")
            ai_news = {}

        try:
            # Scan vibe coding ecosystem
            print("  → Scanning vibe coding ecosystem...")
            vibe_coding = self.news_scanner.scan_vibe_coding_ecosystem()
            print("  ✓ Vibe coding ecosystem scanned")
            results["vibe_coding"] = vibe_coding
        except Exception as e:
            print(f"  ⚠ Vibe coding scan failed: {e}")
            vibe_coding = {}

        # Combine research
        research = {
            "date": today,
            "ai_news": ai_news,
            "vibe_coding": vibe_coding,
        }

        self.save_json(output_path / "research_digest.json", research)
        print("  ✓ Research digest saved")

        # ========================================
        # PHASE 2: ANALYSIS
        # ========================================
        print("\n🔍 PHASE 2: Generating insights...")

        hot_takes = []
        try:
            # Generate hot takes on top news
            top_stories = ai_news.get("top_stories", [])[:3]
            if top_stories:
                for item in top_stories:
                    take = self.hot_take_gen.generate_hot_take(item)
                    hot_takes.append(take)
                print(f"  ✓ Generated {len(hot_takes)} hot takes")
            else:
                print("  ⚠ No top stories for hot takes")
        except Exception as e:
            print(f"  ⚠ Hot take generation failed: {e}")

        results["hot_takes"] = hot_takes
        self.save_json(output_path / "hot_takes.json", hot_takes)

        # ========================================
        # PHASE 3: CONTENT GENERATION
        # ========================================
        print("\n✍️ PHASE 3: Generating content...")

        try:
            # LinkedIn posts
            print("  → Generating LinkedIn posts...")
            linkedin = self.linkedin_gen.generate_daily_posts(research, num_posts=3)
            self.save_markdown(output_path / "linkedin_posts.md",
                              self.format_linkedin(linkedin))
            self.save_json(output_path / "linkedin_posts.json", linkedin)
            print("  ✓ LinkedIn posts generated")
            results["linkedin"] = linkedin
        except Exception as e:
            print(f"  ⚠ LinkedIn generation failed: {e}")

        try:
            # Twitter content
            print("  → Generating Twitter content...")
            twitter = self.twitter_gen.generate_daily_content(research)
            self.save_markdown(output_path / "twitter_content.md",
                              self.format_twitter(twitter))
            self.save_json(output_path / "twitter_content.json", twitter)
            print("  ✓ Twitter content generated")
            results["twitter"] = twitter
        except Exception as e:
            print(f"  ⚠ Twitter generation failed: {e}")

        # Summary
        print("\n" + "=" * 60)
        print(f"🎉 Daily run complete!")
        print(f"📁 Output: {output_path}")
        print("=" * 60)

        # Print quick summary
        if results.get("linkedin", {}).get("posts"):
            print(f"\n📌 LinkedIn: {len(results['linkedin']['posts'])} posts ready")
        if results.get("twitter", {}).get("standalone_tweets"):
            print(f"🐦 Twitter: {len(results['twitter']['standalone_tweets'])} tweets + 1 thread")
        if hot_takes:
            print(f"🔥 Hot takes: {len(hot_takes)} generated")

        return results

    def run_weekly(self) -> Dict[str, Any]:
        """
        Run weekly deep content generation.

        Returns:
            Generated content
        """
        print("\n" + "=" * 60)
        print("🚀 AI Thought Leadership Engine - WEEKLY RUN")
        print("=" * 60)

        week = datetime.now().strftime("week-%W-%Y")
        output_path = Path(f"output/weekly/{week}")
        output_path.mkdir(parents=True, exist_ok=True)

        results = {}

        # Compile weekly research
        print("\n📊 Compiling weekly research...")
        try:
            weekly_research = self.news_scanner.scan_daily_ai_news()
            self.save_json(output_path / "weekly_research.json", weekly_research)
            results["research"] = weekly_research
        except Exception as e:
            print(f"  ⚠ Research compilation failed: {e}")
            weekly_research = {}

        # Generate newsletter
        print("\n📧 Generating newsletter...")
        try:
            newsletter = self.newsletter_gen.generate_weekly_newsletter(
                weekly_research,
                None  # Lab notes would come from manual input
            )
            md_content = self.newsletter_gen.format_newsletter_markdown(newsletter)
            self.save_markdown(output_path / "newsletter.md", md_content)
            self.save_json(output_path / "newsletter.json", newsletter)
            print("  ✓ Newsletter generated")
            results["newsletter"] = newsletter
        except Exception as e:
            print(f"  ⚠ Newsletter generation failed: {e}")

        # Generate article draft
        print("\n📝 Generating article draft...")
        try:
            # Select a topic based on research
            article = self.article_gen.generate_article_for_publication(
                "The design patterns emerging in AI interfaces",
                "wired",
                weekly_research
            )
            md_content = self.article_gen.format_article_markdown(article)
            self.save_markdown(output_path / "article_draft.md", md_content)
            self.save_json(output_path / "article_draft.json", article)
            print("  ✓ Article draft generated")
            results["article"] = article
        except Exception as e:
            print(f"  ⚠ Article generation failed: {e}")

        # Generate predictions
        print("\n🔮 Generating predictions...")
        try:
            predictions = self.prediction_engine.generate_predictions(weekly_research)
            self.save_json(output_path / "predictions.json", predictions)
            print("  ✓ Predictions generated")
            results["predictions"] = predictions
        except Exception as e:
            print(f"  ⚠ Prediction generation failed: {e}")

        print("\n" + "=" * 60)
        print(f"🎉 Weekly run complete!")
        print(f"📁 Output: {output_path}")
        print("=" * 60)

        return results

    def run_scan(self) -> Dict[str, Any]:
        """
        Run quick news scan only.

        Returns:
            Scan results
        """
        print("\n📡 Running quick AI news scan...")

        results = {}

        try:
            news = self.news_scanner.scan_daily_ai_news()
            results["ai_news"] = news
            print(json.dumps(news, indent=2, default=str))
        except Exception as e:
            print(f"Error: {e}")

        return results

    def run_predict(self) -> Dict[str, Any]:
        """
        Generate predictions.

        Returns:
            Predictions
        """
        print("\n🔮 Generating predictions...")

        try:
            predictions = self.prediction_engine.generate_predictions({})
            print(json.dumps(predictions, indent=2, default=str))
            return predictions
        except Exception as e:
            print(f"Error: {e}")
            return {}

    def run_tool_review(self, tool_name: str) -> Dict[str, Any]:
        """
        Generate a tool review.

        Args:
            tool_name: Name of tool to review

        Returns:
            Review content
        """
        print(f"\n🔧 Generating review for {tool_name}...")

        try:
            # Research the tool
            research = self.tool_tracker.research_tool(tool_name)

            # Generate review
            review = self.linkedin_gen.generate_tool_review_post(
                tool_name,
                research
            )

            print("\n" + "=" * 60)
            print(f"TOOL REVIEW: {tool_name}")
            print("=" * 60)
            print(f"\n{review.get('hook', '')}")
            print(f"\n{review.get('body', '')}")

            return review
        except Exception as e:
            print(f"Error: {e}")
            return {}

    def run_radio(
        self,
        topic: str,
        theme: str = "AI Fundamentals",
        episode_number: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Generate a Bharte Chalo radio show script.

        Args:
            topic: Main topic for the episode
            theme: Episode theme category
            episode_number: Optional episode number

        Returns:
            Generated script
        """
        print("\n" + "=" * 60)
        print("🎙️ BHARTE CHALO - Radio Script Generator")
        print("=" * 60)
        print(f"\n📝 Topic: {topic}")
        print(f"🎯 Theme: {theme}")

        today = datetime.now().strftime("%Y-%m-%d")
        output_path = Path(f"output/radio/{today}")
        output_path.mkdir(parents=True, exist_ok=True)

        results = {}

        try:
            # Generate full episode script
            print("\n🎬 Generating episode script...")
            script = self.radio_gen.generate_episode_script(
                topic=topic,
                theme=theme,
                episode_number=episode_number,
                include_urdu_phrases=True
            )
            results["script"] = script

            # Save outputs
            safe_topic = "".join(c if c.isalnum() else "_" for c in topic[:30])
            self.save_json(output_path / f"script_{safe_topic}.json", script)

            md_content = self.radio_gen.format_script_markdown(script)
            self.save_markdown(output_path / f"script_{safe_topic}.md", md_content)

            print("  ✓ Episode script generated")

            # Print summary
            print("\n" + "=" * 60)
            print(f"🎉 Script generated successfully!")
            print(f"📁 Output: {output_path}")
            print("=" * 60)

            # Show episode title
            if script.get("episode_title"):
                print(f"\n📺 Episode: {script['episode_title']}")
            if script.get("total_duration"):
                print(f"⏱️ Duration: {script['total_duration']}")

            # Show quotable moments
            if script.get("quotable_moments"):
                print("\n💬 Quotable Moments:")
                for quote in script["quotable_moments"][:3]:
                    print(f"   > {quote}")

        except Exception as e:
            print(f"  ⚠ Script generation failed: {e}")
            import traceback
            traceback.print_exc()

        return results

    def run_radio_series(
        self,
        main_topic: str,
        num_episodes: int = 4
    ) -> Dict[str, Any]:
        """
        Generate a series outline for Bharte Chalo.

        Args:
            main_topic: Overarching topic for the series
            num_episodes: Number of episodes in series

        Returns:
            Series outline
        """
        print("\n" + "=" * 60)
        print("🎙️ BHARTE CHALO - Series Planner")
        print("=" * 60)
        print(f"\n📚 Main Topic: {main_topic}")
        print(f"📻 Episodes: {num_episodes}")

        today = datetime.now().strftime("%Y-%m-%d")
        output_path = Path(f"output/radio/{today}")
        output_path.mkdir(parents=True, exist_ok=True)

        try:
            print("\n📋 Generating series outline...")
            series = self.radio_gen.generate_topic_series(
                main_topic=main_topic,
                num_episodes=num_episodes
            )

            safe_topic = "".join(c if c.isalnum() else "_" for c in main_topic[:30])
            self.save_json(output_path / f"series_{safe_topic}.json", series)

            print("  ✓ Series outline generated")
            print(f"\n📁 Output: {output_path}")

            # Show series overview
            if series.get("series_title"):
                print(f"\n📺 Series: {series['series_title']}")
            if series.get("episodes"):
                print("\n📋 Episodes:")
                for ep in series["episodes"]:
                    print(f"   {ep.get('episode_number', '?')}. {ep.get('title', 'TBD')}")

            return series

        except Exception as e:
            print(f"  ⚠ Series generation failed: {e}")
            return {}


def print_help():
    """Print help message."""
    help_text = """
╔══════════════════════════════════════════════════════════════╗
║     AI THOUGHT LEADERSHIP ENGINE                             ║
║     For Ahmad Bilal - AI Interface Architect                 ║
╚══════════════════════════════════════════════════════════════╝

USAGE:
    python main.py <command> [options]

COMMANDS:
    daily       Run daily content generation
                - Scans AI news
                - Generates hot takes
                - Creates LinkedIn posts
                - Creates Twitter content

    weekly      Run weekly deep content generation
                - Compiles weekly research
                - Generates newsletter
                - Creates article draft
                - Generates predictions

    scan        Quick AI news scan
                - Scans current AI landscape
                - Returns JSON output

    predict     Generate predictions
                - AI interfaces predictions
                - Vibe coding predictions
                - Industry predictions

    review      Generate tool review
                Usage: python main.py review <tool_name>

    radio       Generate Bharte Chalo radio show script
                Usage: python main.py radio <topic> [theme]
                Themes: AI Fundamentals, Leadership in Digital Age,
                        Innovation Mindset, Career in Tech, etc.

    radio-series Generate episode series outline
                Usage: python main.py radio-series <topic> [num_episodes]

    help        Show this help message

EXAMPLES:
    python main.py daily
    python main.py weekly
    python main.py scan
    python main.py predict
    python main.py review "Cursor"
    python main.py radio "What is AI and Why Should You Care"
    python main.py radio "ChatGPT for Beginners" "AI Fundamentals"
    python main.py radio-series "Understanding AI" 4

SETUP:
    1. Create .env file with GEMINI_API_KEY
    2. pip install -r requirements.txt
    3. Run desired command

OUTPUT:
    - Daily output: output/daily/YYYY-MM-DD/
    - Weekly output: output/weekly/week-WW-YYYY/
    - Radio scripts: output/radio/YYYY-MM-DD/
"""
    print(help_text)


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1].lower()

    if command == "help":
        print_help()
        return

    # Initialize engine
    try:
        engine = AIThoughtLeadershipEngine()
    except ValueError as e:
        print(f"❌ Initialization failed: {e}")
        print("\nMake sure you have set GEMINI_API_KEY in your .env file")
        return
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("\nRun: pip install -r requirements.txt")
        return

    # Execute command
    if command == "daily":
        engine.run_daily()
    elif command == "weekly":
        engine.run_weekly()
    elif command == "scan":
        engine.run_scan()
    elif command == "predict":
        engine.run_predict()
    elif command == "review":
        if len(sys.argv) < 3:
            print("Usage: python main.py review <tool_name>")
            return
        tool_name = sys.argv[2]
        engine.run_tool_review(tool_name)
    elif command == "radio":
        if len(sys.argv) < 3:
            print("Usage: python main.py radio <topic> [theme]")
            print("\nThemes: AI Fundamentals, Leadership in Digital Age,")
            print("        Innovation Mindset, Career in Tech, Entrepreneurship,")
            print("        Future of Work, Pakistan Tech Ecosystem")
            return
        topic = sys.argv[2]
        theme = sys.argv[3] if len(sys.argv) > 3 else "AI Fundamentals"
        engine.run_radio(topic, theme)
    elif command == "radio-series":
        if len(sys.argv) < 3:
            print("Usage: python main.py radio-series <topic> [num_episodes]")
            return
        topic = sys.argv[2]
        num_episodes = int(sys.argv[3]) if len(sys.argv) > 3 else 4
        engine.run_radio_series(topic, num_episodes)
    elif command == "show":
        # Bharte Chalo Show Management
        from bharte_chalo.cli import BharteChaloCLI
        cli = BharteChaloCLI(gemini_client=engine.gemini)
        cli.run(sys.argv[2:])
    else:
        print(f"Unknown command: {command}")
        print_help()


if __name__ == "__main__":
    main()
