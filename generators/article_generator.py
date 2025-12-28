"""
ARTICLE GENERATOR
For major publications: HBR, Wired, MIT Tech Review, Fast Company, etc.
Creates pitch-ready articles with editor outreach.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
import json


# Article schema
ARTICLE_SCHEMA = {
    "type": "object",
    "properties": {
        "headline": {"type": "string"},
        "subhead": {"type": "string"},
        "target_publication": {"type": "string"},
        "word_count": {"type": "integer"},
        "thesis": {"type": "string"},
        "why_now": {"type": "string"},
        "outline": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "section": {"type": "string"},
                    "key_points": {"type": "array", "items": {"type": "string"}},
                    "evidence_needed": {"type": "string"}
                }
            }
        },
        "draft": {"type": "string"},
        "key_quotes": {"type": "array", "items": {"type": "string"}},
        "pitch_email": {"type": "string"},
        "social_hooks": {"type": "array", "items": {"type": "string"}}
    }
}


# Publication guidelines
PUBLICATION_GUIDELINES = {
    "hbr": {
        "name": "Harvard Business Review",
        "style": "Business focus, executive audience, actionable frameworks",
        "word_count": (2000, 3000),
        "tone": "Authoritative, research-backed, strategic",
        "audience": "C-suite, business leaders, MBA students",
        "what_they_want": "Original frameworks, business implications, case studies",
    },
    "wired": {
        "name": "Wired",
        "style": "Tech-forward, cultural implications, narrative style",
        "word_count": (1500, 2500),
        "tone": "Smart, curious, slightly irreverent",
        "audience": "Tech-curious, early adopters, culture watchers",
        "what_they_want": "Big ideas, trend identification, cultural impact",
    },
    "mit_tech_review": {
        "name": "MIT Technology Review",
        "style": "Technical depth, research-backed, future implications",
        "word_count": (2000, 2500),
        "tone": "Expert, analytical, forward-looking",
        "audience": "Technologists, researchers, innovation leaders",
        "what_they_want": "Technical insight, research connections, predictions",
    },
    "fast_company": {
        "name": "Fast Company",
        "style": "Innovation focus, business impact, accessible",
        "word_count": (1200, 1800),
        "tone": "Energetic, optimistic, design-forward",
        "audience": "Creative professionals, entrepreneurs, innovators",
        "what_they_want": "Innovation stories, design thinking, future of work",
    },
    "techcrunch": {
        "name": "TechCrunch",
        "style": "Startup/VC focus, industry analysis, trend spotting",
        "word_count": (1000, 1500),
        "tone": "Insider, analytical, opinionated",
        "audience": "Startup founders, VCs, tech industry",
        "what_they_want": "Market analysis, predictions, insider perspective",
    },
}


class ArticleGenerator:
    """
    Generates articles for major publications.
    Creates pitch-ready content with editor outreach materials.
    """

    def __init__(self, gemini_client):
        """
        Initialize the article generator.

        Args:
            gemini_client: Configured GeminiClient instance
        """
        self.gemini = gemini_client
        self.publications = PUBLICATION_GUIDELINES

    def generate_article_for_publication(
        self,
        topic: str,
        publication: str,
        research: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate a full article draft for a specific publication.

        Args:
            topic: Topic to write about
            publication: Target publication (hbr, wired, etc.)
            research: Research context

        Returns:
            Complete article with pitch materials
        """
        pub_info = self.publications.get(
            publication.lower(),
            {"name": publication, "style": "General publication", "word_count": (1500, 2000)}
        )

        prompt = f"""
        Generate an article for {pub_info['name']} on: {topic}

        ## PUBLICATION GUIDELINES
        Name: {pub_info['name']}
        Style: {pub_info.get('style', 'General')}
        Word Count: {pub_info.get('word_count', (1500, 2000))}
        Tone: {pub_info.get('tone', 'Professional')}
        Audience: {pub_info.get('audience', 'General readers')}
        What They Want: {pub_info.get('what_they_want', 'Quality insights')}

        ## RESEARCH CONTEXT
        {json.dumps(research, indent=2) if research else "Use current AI industry knowledge"}

        ## AHMAD'S POSITIONING
        - AI Interface Architect actively building in this space
        - Can speak from direct experience (10+ industries)
        - Has philosophical depth beyond tactics
        - Global perspective (not just Silicon Valley)
        - Signature concept: "The Intent Layer"

        ## ARTICLE REQUIREMENTS

        ### THESIS
        One clear, arguable claim. NOT "AI is changing design" (obvious).
        Something like:
        - "The companies winning at AI aren't building better algorithms—they're designing better behaviors"
        - "Vibe coding won't replace developers. It will expose which developers were just translators"
        - "The AI interface war won't be won by the best model—it will be won by the best understanding of intent"

        ### WHY NOW
        Why is this article timely? What recent event or trend makes this relevant?
        Editors want to know why readers need this NOW.

        ### STRUCTURE
        1. HOOK: Opening that captures attention (anecdote, surprising fact, provocative question)
        2. THESIS: Clear statement of your argument
        3. EVIDENCE: 3-4 supporting points with examples
        4. IMPLICATIONS: What this means for readers
        5. FORWARD-LOOKING CLOSE: What happens next

        ### VOICE
        - Authoritative but not arrogant
        - Specific, not vague
        - Global perspective
        - Accessible depth
        - Match the publication's tone

        ## GENERATE

        1. HEADLINE: Compelling, specific, shareable

        2. SUBHEAD: Expands on headline, adds context

        3. THESIS: One sentence summary of argument

        4. OUTLINE: Section-by-section plan with key points

        5. FULL DRAFT: Complete article at target word count

        6. KEY QUOTES: 5 pull-worthy quotes from the article

        7. PITCH EMAIL: Email to editor (under 200 words)
           - Why this piece matters
           - Why you're the right person to write it
           - Why now
           - Brief bio

        8. SOCIAL HOOKS: 3 ways to promote on social media

        The draft should be ready for editing, not a rough outline.
        """

        result = self.gemini.generate_structured(prompt, ARTICLE_SCHEMA, model="pro")
        result["publication"] = publication
        result["topic"] = topic
        result["generated_at"] = datetime.now().isoformat()
        return result

    def generate_op_ed(
        self,
        topic: str,
        position: str,
        hook_news: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate an opinion piece / op-ed.

        Args:
            topic: Topic to address
            position: Ahmad's position on the topic
            hook_news: Optional news hook

        Returns:
            Op-ed article
        """
        prompt = f"""
        Generate an op-ed for Ahmad Bilal:

        TOPIC: {topic}
        AHMAD'S POSITION: {position}
        NEWS HOOK: {hook_news or "General timeliness"}

        ## OP-ED FORMAT (700-900 words)

        1. HOOK (1-2 paragraphs)
        - Timely connection to news/events
        - Why readers should care now

        2. THESIS (1 paragraph)
        - Clear, bold statement of position
        - What you're arguing for/against

        3. ARGUMENT (3-4 paragraphs)
        - Your best evidence/reasoning
        - Acknowledge counterarguments
        - Personal experience that informs this

        4. STAKES (1 paragraph)
        - What happens if we get this wrong/right
        - Why this matters beyond the immediate

        5. CALL TO ACTION (1 paragraph)
        - What should readers/leaders do
        - Specific, actionable

        ## VOICE
        - Opinionated but reasoned
        - Personal but not self-indulgent
        - Accessible to general readers
        - Ahmad's practitioner credibility

        Return as article schema.
        """

        result = self.gemini.generate_structured(prompt, ARTICLE_SCHEMA, model="pro")
        result["article_type"] = "op_ed"
        result["generated_at"] = datetime.now().isoformat()
        return result

    def generate_article_outline(
        self,
        topic: str,
        publication: str
    ) -> Dict[str, Any]:
        """
        Generate just an article outline (for planning).

        Args:
            topic: Topic to outline
            publication: Target publication

        Returns:
            Detailed outline
        """
        pub_info = self.publications.get(publication.lower(), {})

        prompt = f"""
        Generate a detailed article outline for {pub_info.get('name', publication)}:

        TOPIC: {topic}

        ## OUTLINE FORMAT

        1. HEADLINE OPTIONS (3 options)

        2. THESIS: Core argument in one sentence

        3. SECTION-BY-SECTION:
        For each section:
        - Section title
        - Key points (3-5 bullets)
        - Evidence/examples needed
        - Approximate word count

        4. RESEARCH NEEDED:
        What additional research/data would strengthen this?

        5. AHMAD'S UNIQUE ANGLE:
        What perspective can he bring that others can't?

        6. POTENTIAL CHALLENGES:
        What might be weak in this argument?

        Return as JSON outline.
        """

        return self.gemini.generate_structured(prompt, {
            "type": "object",
            "properties": {
                "headline_options": {"type": "array", "items": {"type": "string"}},
                "thesis": {"type": "string"},
                "sections": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "title": {"type": "string"},
                            "key_points": {"type": "array"},
                            "evidence_needed": {"type": "string"},
                            "word_count": {"type": "integer"}
                        }
                    }
                },
                "research_needed": {"type": "array", "items": {"type": "string"}},
                "unique_angle": {"type": "string"},
                "potential_challenges": {"type": "array", "items": {"type": "string"}}
            }
        })

    def generate_pitch_for_publication(
        self,
        topic: str,
        publication: str,
        angle: str
    ) -> Dict[str, Any]:
        """
        Generate just a pitch email for a publication.

        Args:
            topic: Topic to pitch
            publication: Target publication
            angle: Specific angle

        Returns:
            Pitch email and materials
        """
        pub_info = self.publications.get(publication.lower(), {})

        prompt = f"""
        Generate a pitch email for {pub_info.get('name', publication)}:

        TOPIC: {topic}
        ANGLE: {angle}

        ## AHMAD'S CREDENTIALS
        - AI Interface Architect & Innovation Philosopher
        - Principal Product Designer at AutoLeap (US)
        - Head of Product Design at Hyphenn (MENA)
        - 10+ industries (automotive, government, mobility, education)
        - Actively building AI interfaces

        ## PITCH EMAIL FORMAT

        Subject line: [Compelling subject]

        Body (under 200 words):
        - Hook: Why this matters now
        - Thesis: What the piece will argue
        - Why Ahmad: Unique qualifications
        - Brief bio: One sentence
        - Call to action: Request to discuss

        ## ADDITIONAL MATERIALS

        1. HEADLINE OPTIONS (3)

        2. BRIEF OUTLINE (5 bullets)

        3. SAMPLE OPENING (100 words)

        4. SIMILAR PIECES (if known)
        What this publication has run that's similar

        Return as JSON.
        """

        return self.gemini.generate_structured(prompt, {
            "type": "object",
            "properties": {
                "subject_line": {"type": "string"},
                "pitch_email": {"type": "string"},
                "headline_options": {"type": "array", "items": {"type": "string"}},
                "brief_outline": {"type": "array", "items": {"type": "string"}},
                "sample_opening": {"type": "string"},
                "publication_fit": {"type": "string"}
            }
        })

    def identify_publication_opportunities(
        self,
        research: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Identify which publications might want which stories.

        Args:
            research: Current research context

        Returns:
            Publication opportunities mapped to topics
        """
        prompt = f"""
        Based on this research context:
        {json.dumps(research, indent=2) if research else "Current AI industry trends"}

        And Ahmad Bilal's positioning as AI Interface Architect,
        identify publication opportunities:

        ## FOR EACH MAJOR PUBLICATION

        ### Harvard Business Review
        - Best topic angle for HBR
        - Why it fits their audience
        - Timeliness

        ### Wired
        - Best topic angle for Wired
        - Why it fits their style
        - Timeliness

        ### MIT Technology Review
        - Best topic angle for MIT Tech Review
        - Why it fits their depth
        - Timeliness

        ### Fast Company
        - Best topic angle for Fast Company
        - Why it fits their focus
        - Timeliness

        ### TechCrunch
        - Best topic angle for TechCrunch
        - Why it fits their audience
        - Timeliness

        ## PRIORITY RANKING
        Rank the opportunities by:
        1. Likelihood of acceptance
        2. Timeliness/urgency
        3. Impact for Ahmad's positioning

        Return as JSON with opportunities per publication.
        """

        return self.gemini.generate_structured(prompt, {
            "type": "object",
            "properties": {
                "opportunities": {
                    "type": "object",
                    "additionalProperties": {
                        "type": "object",
                        "properties": {
                            "topic": {"type": "string"},
                            "angle": {"type": "string"},
                            "fit_score": {"type": "integer"},
                            "timeliness": {"type": "string"}
                        }
                    }
                },
                "priority_ranking": {"type": "array", "items": {"type": "string"}}
            }
        })

    def format_article_markdown(self, article: Dict[str, Any]) -> str:
        """
        Format article as markdown.

        Args:
            article: Article object

        Returns:
            Markdown-formatted article
        """
        md = []

        # Metadata
        md.append(f"# {article.get('headline', 'Untitled')}")
        md.append("")
        if article.get("subhead"):
            md.append(f"*{article['subhead']}*")
            md.append("")

        md.append(f"**Publication:** {article.get('target_publication', 'TBD')}")
        md.append(f"**Word Count:** {article.get('word_count', 'N/A')}")
        md.append(f"**Generated:** {article.get('generated_at', 'N/A')}")
        md.append("")
        md.append("---")
        md.append("")

        # Thesis
        if article.get("thesis"):
            md.append("## Thesis")
            md.append(article["thesis"])
            md.append("")

        # Why now
        if article.get("why_now"):
            md.append("## Why Now")
            md.append(article["why_now"])
            md.append("")

        # Draft
        if article.get("draft"):
            md.append("---")
            md.append("")
            md.append(article["draft"])
            md.append("")

        # Key quotes
        if article.get("key_quotes"):
            md.append("---")
            md.append("## Key Quotes")
            for quote in article["key_quotes"]:
                md.append(f"> {quote}")
                md.append("")

        # Pitch email
        if article.get("pitch_email"):
            md.append("---")
            md.append("## Pitch Email")
            md.append("```")
            md.append(article["pitch_email"])
            md.append("```")
            md.append("")

        return "\n".join(md)
