"""
AUDIENCES CONFIGURATION
Target audience definitions for Ahmad Bilal's thought leadership.
"""

# Target audience tiers - the 5-year game
AUDIENCE_TIERS = {
    "tier_1": {
        "name": "Decision Makers",
        "who": [
            "CEOs and C-suite executives",
            "Government ministers and policymakers",
            "VCs and investors",
            "Policy makers and regulators",
        ],
        "why_they_matter": "They hire advisors, fund initiatives, set policy",
        "channels": [
            "Harvard Business Review",
            "Keynote speeches",
            "Books",
            "Executive podcasts",
            "World Economic Forum",
            "Davos",
        ],
        "content_approach": "Big picture, strategic implications, business impact",
        "tone": "Authoritative, strategic, forward-looking",
    },

    "tier_2": {
        "name": "Amplifiers",
        "who": [
            "Tech journalists",
            "Academics and researchers",
            "Conference organizers",
            "Podcast hosts",
            "Newsletter writers",
        ],
        "why_they_matter": "They amplify and legitimize ideas",
        "channels": [
            "Press relationships",
            "Academic papers and collaborations",
            "Major conference talks",
            "Podcast appearances",
        ],
        "content_approach": "Quotable insights, unique angles, research-backed",
        "tone": "Expert, accessible, newsworthy",
    },

    "tier_3": {
        "name": "Industry Leaders",
        "who": [
            "Design leaders and directors",
            "Product leaders",
            "Engineering leaders",
            "Startup founders",
        ],
        "why_they_matter": "They implement ideas and evangelize to teams",
        "channels": [
            "LinkedIn",
            "Industry conferences (Config, Figma, etc.)",
            "Workshops and masterclasses",
            "Design/product communities",
        ],
        "content_approach": "Practical insights, frameworks, case studies",
        "tone": "Practitioner, peer-to-peer, actionable",
    },

    "tier_4": {
        "name": "Practitioners & Students",
        "who": [
            "Designers (all levels)",
            "Product managers",
            "Developers interested in AI",
            "Design students",
            "Career changers",
        ],
        "why_they_matter": "They spread ideas, become future decision-makers",
        "channels": [
            "Social media (LinkedIn, Twitter)",
            "Courses and tutorials",
            "Accessible content",
            "Community engagement",
        ],
        "content_approach": "Educational, inspiring, accessible",
        "tone": "Mentor, encouraging, clear",
    },
}


# Detailed audience personas
TARGET_AUDIENCES = {
    "executive_leader": {
        "name": "The Executive",
        "tier": "tier_1",
        "job_titles": ["CEO", "CTO", "Chief Digital Officer", "VP of Product"],
        "goals": [
            "Understand AI's strategic implications",
            "Make informed AI investment decisions",
            "Lead AI transformation initiatives",
        ],
        "pain_points": [
            "Overwhelmed by AI hype",
            "Unclear on practical implementation",
            "Need trusted advisors",
        ],
        "content_they_want": [
            "Strategic frameworks",
            "Case studies with business impact",
            "Clear predictions with reasoning",
            "Executive briefings",
        ],
        "where_they_are": ["LinkedIn", "Executive podcasts", "HBR", "Conferences"],
        "what_makes_them_share": "Insights they can bring to board meetings",
    },

    "tech_journalist": {
        "name": "The Tech Journalist",
        "tier": "tier_2",
        "job_titles": ["Tech Reporter", "AI Correspondent", "Editor"],
        "goals": [
            "Find unique angles on AI stories",
            "Get expert commentary",
            "Break news and trends",
        ],
        "pain_points": [
            "Everyone has the same hot takes",
            "Hard to find practitioners (not just commentators)",
            "Need clear, quotable insights",
        ],
        "content_they_want": [
            "Contrarian but well-reasoned takes",
            "Practitioner perspective",
            "Predictions they can reference",
            "Original frameworks",
        ],
        "where_they_are": ["Twitter/X", "Tech publications", "Newsletters"],
        "what_makes_them_share": "Unique angle they haven't seen elsewhere",
    },

    "design_leader": {
        "name": "The Design Leader",
        "tier": "tier_3",
        "job_titles": ["Head of Design", "Design Director", "VP Design"],
        "goals": [
            "Lead team through AI transition",
            "Stay ahead of industry changes",
            "Build AI-ready design practice",
        ],
        "pain_points": [
            "Uncertain how AI changes team structure",
            "Need to upskill team",
            "Balancing AI tools with craft",
        ],
        "content_they_want": [
            "Frameworks for AI-era design",
            "Team strategy insights",
            "Tool recommendations",
            "Leadership perspectives",
        ],
        "where_they_are": ["LinkedIn", "Design conferences", "Slack communities"],
        "what_makes_them_share": "Insights they can use with their teams",
    },

    "product_leader": {
        "name": "The Product Leader",
        "tier": "tier_3",
        "job_titles": ["Head of Product", "VP Product", "CPO"],
        "goals": [
            "Build AI-powered products",
            "Understand AI UX patterns",
            "Make build vs. buy decisions",
        ],
        "pain_points": [
            "Moving fast without sacrificing quality",
            "Understanding what's possible vs. hype",
            "Designing AI that users trust",
        ],
        "content_they_want": [
            "AI product patterns",
            "Implementation insights",
            "Trust and safety considerations",
            "Competitive analysis",
        ],
        "where_they_are": ["LinkedIn", "Product conferences", "Substack"],
        "what_makes_them_share": "Product insights backed by experience",
    },

    "practicing_designer": {
        "name": "The Practicing Designer",
        "tier": "tier_4",
        "job_titles": ["Product Designer", "UX Designer", "UI Designer"],
        "goals": [
            "Stay relevant in AI era",
            "Learn AI tools effectively",
            "Grow career with AI skills",
        ],
        "pain_points": [
            "Fear of being replaced",
            "Overwhelmed by new tools",
            "Unclear career path",
        ],
        "content_they_want": [
            "Practical tool reviews",
            "Career guidance",
            "Skill development advice",
            "Inspiring examples",
        ],
        "where_they_are": ["LinkedIn", "Twitter", "YouTube", "Design communities"],
        "what_makes_them_share": "Content that makes them look thoughtful",
    },

    "developer_curious": {
        "name": "The AI-Curious Developer",
        "tier": "tier_4",
        "job_titles": ["Frontend Developer", "Full-stack Developer", "Engineer"],
        "goals": [
            "Use AI tools effectively",
            "Understand vibe coding",
            "Build AI-powered features",
        ],
        "pain_points": [
            "Evaluating which tools actually work",
            "Understanding AI limitations",
            "Bridging design and development",
        ],
        "content_they_want": [
            "Tool comparisons",
            "Technical insights from design perspective",
            "Implementation patterns",
        ],
        "where_they_are": ["Twitter", "Dev.to", "GitHub", "Tech blogs"],
        "what_makes_them_share": "Technical insights they haven't seen elsewhere",
    },
}


# Channel-specific strategies
CHANNEL_STRATEGIES = {
    "linkedin": {
        "primary_audiences": ["design_leader", "product_leader", "executive_leader"],
        "content_types": ["thought_leadership", "predictions", "frameworks", "hot_takes"],
        "posting_frequency": "3-5x per week",
        "best_times": ["Tuesday-Thursday mornings", "Sunday evenings"],
        "engagement_approach": "Respond thoughtfully, ask questions, build relationships",
    },

    "twitter": {
        "primary_audiences": ["tech_journalist", "practicing_designer", "developer_curious"],
        "content_types": ["hot_takes", "tool_reviews", "quick_insights", "threads"],
        "posting_frequency": "Daily",
        "engagement_approach": "Real-time commentary, engage with news, build network",
    },

    "newsletter": {
        "primary_audiences": ["design_leader", "product_leader", "practicing_designer"],
        "content_types": ["deep_insights", "lab_notes", "predictions", "curated_links"],
        "posting_frequency": "Weekly",
        "approach": "Exclusive insights not shared elsewhere, personal voice",
    },

    "articles": {
        "primary_audiences": ["executive_leader", "tech_journalist"],
        "content_types": ["strategic_analysis", "predictions", "frameworks"],
        "target_publications": [
            "Harvard Business Review",
            "Wired",
            "MIT Technology Review",
            "Fast Company",
            "TechCrunch",
        ],
        "approach": "Pitch unique angles, build editor relationships",
    },

    "speaking": {
        "primary_audiences": ["all_tiers"],
        "content_types": ["keynotes", "panels", "workshops"],
        "target_events": [
            "Config (Figma)",
            "Clarity",
            "IXDA",
            "Product conferences",
            "AI conferences",
        ],
        "approach": "Build speaking reel, start smaller and grow",
    },
}
