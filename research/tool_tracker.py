"""
TOOL TRACKER
Tracks and analyzes AI tools, especially vibe coding and design tools.
Maintains a database of tools tested and generates review content.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path
import json


# Tool categories and their focus areas
TOOL_CATEGORIES = {
    "vibe_coding": {
        "description": "Prompt-to-product development tools",
        "tools": ["v0", "bolt.new", "lovable", "replit_agent", "claude_artifacts"],
    },
    "ai_ide": {
        "description": "AI-native development environments",
        "tools": ["cursor", "windsurf", "github_copilot"],
    },
    "design_ai": {
        "description": "AI-powered design tools",
        "tools": ["figma_ai", "framer_ai", "galileo_ai", "uizard"],
    },
    "image_generation": {
        "description": "AI image generation for design",
        "tools": ["midjourney", "dall_e", "stable_diffusion", "firefly"],
    },
    "llm_interfaces": {
        "description": "Large language model interfaces",
        "tools": ["chatgpt", "claude", "gemini", "perplexity"],
    },
}


class ToolTracker:
    """
    Tracks AI tools and generates review/comparison content.
    """

    def __init__(self, gemini_client, data_dir: str = "data"):
        """
        Initialize the tool tracker.

        Args:
            gemini_client: Configured GeminiClient instance
            data_dir: Directory for storing tool data
        """
        self.gemini = gemini_client
        self.data_dir = Path(data_dir)
        self.tools_file = self.data_dir / "tools_tested.json"
        self._ensure_data_dir()

    def _ensure_data_dir(self):
        """Ensure data directory exists."""
        self.data_dir.mkdir(parents=True, exist_ok=True)
        if not self.tools_file.exists():
            self._save_tools({})

    def _load_tools(self) -> Dict[str, Any]:
        """Load tools database."""
        if self.tools_file.exists():
            with open(self.tools_file, "r") as f:
                return json.load(f)
        return {}

    def _save_tools(self, tools: Dict[str, Any]):
        """Save tools database."""
        with open(self.tools_file, "w") as f:
            json.dump(tools, f, indent=2)

    def scan_new_tools(self) -> Dict[str, Any]:
        """
        Scan for newly launched AI tools.

        Returns:
            Dict with new tools and their details
        """
        prompt = """
        Search for AI tools launched in the last 30 days, focusing on:

        ## CATEGORIES TO SEARCH
        1. Vibe coding / prompt-to-product tools
        2. AI-native IDEs and code editors
        3. Design + AI tools
        4. Prototyping and wireframing AI
        5. AI agents for development/design

        ## FOR EACH TOOL FOUND
        - name: Tool name
        - company: Company/creator
        - category: [vibe_coding, ai_ide, design_ai, prototyping, ai_agent]
        - launch_date: When launched (approximate)
        - description: What it does (2-3 sentences)
        - unique_angle: What makes it different
        - target_user: Who it's for
        - pricing: Free/paid/pricing model
        - early_reception: How people are responding
        - ahmad_review_priority: [high, medium, low] - should Ahmad review this?
        - why_review: Why or why not to review

        Focus on tools relevant to designers and developers.

        Return as JSON:
        {
            "scan_date": "YYYY-MM-DD",
            "new_tools": [...],
            "notable_updates": [...],
            "review_priorities": [...]
        }
        """

        result = self.gemini.research_with_search(prompt)
        result["scan_timestamp"] = datetime.now().isoformat()
        return result

    def research_tool(self, tool_name: str) -> Dict[str, Any]:
        """
        Deep research on a specific tool.

        Args:
            tool_name: Name of the tool to research

        Returns:
            Comprehensive tool research
        """
        prompt = f"""
        Research the AI tool "{tool_name}" comprehensively:

        ## BASIC INFO
        - Official name and company
        - Website and pricing
        - Launch date
        - Current version/state

        ## CAPABILITIES
        - What can it do?
        - What are its main features?
        - What technology does it use?
        - Integration options

        ## USER EXPERIENCE
        - How do users interact with it?
        - Learning curve
        - Documentation quality
        - Community/support

        ## REAL USER FEEDBACK
        - What do users love about it?
        - What frustrates users?
        - Common use cases
        - Success stories
        - Failure stories

        ## COMPETITIVE POSITION
        - Main competitors
        - Unique advantages
        - Key weaknesses
        - Market positioning

        ## AHMAD'S REVIEW ANGLES
        - What unique perspective can Ahmad bring?
        - Connection to AI Interface Architect positioning
        - Potential hot takes
        - Philosophical questions this tool raises

        Return as detailed JSON with all sections.
        """

        result = self.gemini.research_with_search(prompt)
        result["tool_name"] = tool_name
        result["research_date"] = datetime.now().isoformat()
        return result

    def compare_tools(self, tools: List[str]) -> Dict[str, Any]:
        """
        Generate tool comparison analysis.

        Args:
            tools: List of tool names to compare

        Returns:
            Comparison analysis
        """
        tools_str = ", ".join(tools)
        prompt = f"""
        Compare these AI tools: {tools_str}

        ## COMPARISON DIMENSIONS

        ### 1. CAPABILITIES
        - What each tool can do
        - Feature overlap
        - Unique capabilities

        ### 2. USER EXPERIENCE
        - Ease of use
        - Learning curve
        - Interface quality

        ### 3. OUTPUT QUALITY
        - Quality of generated code/design
        - Consistency
        - Customization options

        ### 4. USE CASES
        - Best for what scenarios
        - When to use which
        - Not suitable for

        ### 5. PRICING & VALUE
        - Cost comparison
        - Value proposition
        - Best for budget considerations

        ### 6. AHMAD'S RECOMMENDATION
        - For designers: which to use
        - For developers: which to use
        - For learning: which to start with
        - Overall winner and why

        ### 7. CONTENT ANGLES
        - Hot take comparison could generate
        - Unique insight to share
        - Prediction about these tools

        Return as JSON with comparison matrix and recommendations.
        """

        result = self.gemini.research_with_search(prompt)
        result["tools_compared"] = tools
        result["comparison_date"] = datetime.now().isoformat()
        return result

    def log_tool_test(
        self,
        tool_name: str,
        test_date: str,
        test_type: str,
        notes: str,
        rating: int,
        would_recommend: bool,
    ) -> Dict[str, Any]:
        """
        Log a tool testing session.

        Args:
            tool_name: Name of the tool
            test_date: Date of testing
            test_type: Type of test (quick_test, deep_dive, comparison)
            notes: Testing notes
            rating: Rating 1-10
            would_recommend: Would recommend to others

        Returns:
            Updated tool entry
        """
        tools = self._load_tools()

        if tool_name not in tools:
            tools[tool_name] = {
                "name": tool_name,
                "first_tested": test_date,
                "test_logs": [],
                "overall_rating": None,
                "content_created": [],
            }

        tools[tool_name]["test_logs"].append({
            "date": test_date,
            "type": test_type,
            "notes": notes,
            "rating": rating,
            "would_recommend": would_recommend,
        })

        # Update overall rating (average)
        ratings = [log["rating"] for log in tools[tool_name]["test_logs"]]
        tools[tool_name]["overall_rating"] = sum(ratings) / len(ratings)
        tools[tool_name]["last_tested"] = test_date

        self._save_tools(tools)
        return tools[tool_name]

    def generate_tool_review(self, tool_name: str) -> Dict[str, Any]:
        """
        Generate a tool review based on research and testing notes.

        Args:
            tool_name: Tool to review

        Returns:
            Generated review content
        """
        tools = self._load_tools()
        tool_data = tools.get(tool_name, {})

        # Get fresh research
        research = self.research_tool(tool_name)

        prompt = f"""
        Generate a tool review for Ahmad Bilal's thought leadership.

        ## TOOL: {tool_name}

        ## RESEARCH DATA
        {json.dumps(research, indent=2)}

        ## AHMAD'S TESTING NOTES (if available)
        {json.dumps(tool_data.get('test_logs', []), indent=2)}

        ## GENERATE REVIEW

        ### FORMAT: LinkedIn Post
        - Hook that captures attention
        - Honest assessment (not promotional)
        - Specific observations
        - Who should/shouldn't use it
        - Philosophical reflection on what this tool represents
        - Prediction about this tool's future

        ### TONE
        - Practitioner perspective ("I tested this...")
        - Honest, balanced (not fanboy, not hater)
        - Connect to bigger AI interface trends
        - Ahmad's signature voice

        ### STRUCTURE
        1. Opening hook
        2. What I tested and how
        3. What works well
        4. What doesn't work
        5. Who this is for
        6. The bigger picture
        7. My recommendation
        8. Discussion prompt

        Return as JSON:
        {{
            "tool_name": "{tool_name}",
            "review_type": "linkedin_post",
            "hook": "...",
            "body": "...",
            "recommendation": "...",
            "hashtags": [...],
            "char_count": ...,
            "hot_take": "...",
            "philosophical_angle": "..."
        }}
        """

        result = self.gemini.generate_structured(prompt, {
            "type": "object",
            "properties": {
                "tool_name": {"type": "string"},
                "review_type": {"type": "string"},
                "hook": {"type": "string"},
                "body": {"type": "string"},
                "recommendation": {"type": "string"},
                "hashtags": {"type": "array", "items": {"type": "string"}},
                "char_count": {"type": "integer"},
                "hot_take": {"type": "string"},
                "philosophical_angle": {"type": "string"},
            }
        })

        # Log content creation
        if tool_name in tools:
            tools[tool_name]["content_created"].append({
                "date": datetime.now().isoformat(),
                "type": "linkedin_review",
            })
            self._save_tools(tools)

        return result

    def get_review_priorities(self) -> Dict[str, Any]:
        """
        Determine which tools should be reviewed next.

        Returns:
            Prioritized list of tools to review
        """
        tools = self._load_tools()

        # Scan for new tools
        new_tools = self.scan_new_tools()

        prompt = f"""
        Prioritize which AI tools Ahmad should review next.

        ## TOOLS ALREADY REVIEWED
        {json.dumps(list(tools.keys()), indent=2)}

        ## NEW TOOLS DISCOVERED
        {json.dumps(new_tools, indent=2)}

        ## PRIORITIZATION CRITERIA
        1. Relevance to AI interfaces / vibe coding
        2. Buzz/attention in the community
        3. Unique capabilities worth exploring
        4. Gap in Ahmad's coverage
        5. Potential for strong hot take

        ## GENERATE
        - Top 5 tools to review with reasoning
        - What angle to take for each
        - Urgency level

        Return as JSON with prioritized list.
        """

        return self.gemini.generate_structured(prompt, {
            "type": "object",
            "properties": {
                "review_priorities": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "tool_name": {"type": "string"},
                            "priority": {"type": "integer"},
                            "reasoning": {"type": "string"},
                            "angle": {"type": "string"},
                            "urgency": {"type": "string"},
                        }
                    }
                }
            }
        })
