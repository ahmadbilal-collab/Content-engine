"""
CONTENT DIMENSIONS CONFIGURATION
The territory Ahmad Bilal owns in AI thought leadership.
"""

# Six core content dimensions
CONTENT_DIMENSIONS = {
    "ai_interface_paradigms": {
        "name": "AI Interface Paradigms",
        "description": "Primary arena - how humans interact with AI systems",
        "priority": 1,
        "topics": {
            "chat_interfaces": {
                "description": "ChatGPT, Claude, Gemini patterns",
                "subtopics": [
                    "Current state of chat UX",
                    "Limitations and failure modes",
                    "What's next beyond chat",
                    "Memory and context patterns",
                ],
            },
            "copilots": {
                "description": "AI assistance embedded in workflows",
                "subtopics": [
                    "GitHub Copilot patterns",
                    "Figma AI, Cursor patterns",
                    "When copilots help vs. hinder",
                    "The 'copilot UX' design language",
                ],
            },
            "ai_agents": {
                "description": "Autonomous AI systems",
                "subtopics": [
                    "Devin, Claude Computer Use, Operator",
                    "Trust and control design",
                    "Human-in-the-loop patterns",
                    "When to give agents autonomy",
                    "Supervision interfaces",
                ],
            },
            "ambient_ai": {
                "description": "Always-on, background AI",
                "subtopics": [
                    "Post-screen interaction",
                    "Humane, Rabbit, future wearables",
                    "Always-on AI assistants",
                    "Privacy and attention implications",
                ],
            },
            "generative_ui": {
                "description": "AI-created interfaces",
                "subtopics": [
                    "AI creates interfaces on-the-fly",
                    "End of design systems?",
                    "Personalization at scale",
                    "The 'UI of One'",
                ],
            },
            "multimodal": {
                "description": "Voice + vision + text + gesture",
                "subtopics": [
                    "Fluid modality switching",
                    "Accessibility implications",
                    "Cross-modal interaction patterns",
                ],
            },
        },
    },

    "vibe_coding": {
        "name": "Vibe Coding Deep Dive",
        "description": "Ahmad's vibe coding lab - hands-on tool testing",
        "priority": 2,
        "topics": {
            "tools": {
                "description": "AI development tools ecosystem",
                "tools_list": [
                    {"name": "v0", "company": "Vercel", "focus": "React/Next.js generation"},
                    {"name": "Bolt.new", "company": "StackBlitz", "focus": "Full-stack in browser"},
                    {"name": "Lovable", "company": "Lovable", "focus": "Product development"},
                    {"name": "Replit Agent", "company": "Replit", "focus": "Autonomous development"},
                    {"name": "Claude Artifacts", "company": "Anthropic", "focus": "Interactive components"},
                    {"name": "Cursor", "company": "Cursor", "focus": "AI-native IDE"},
                    {"name": "Windsurf", "company": "Codeium", "focus": "AI-native IDE"},
                    {"name": "GitHub Copilot", "company": "GitHub/Microsoft", "focus": "Code completion"},
                    {"name": "Figma AI", "company": "Figma", "focus": "Design-to-code"},
                ],
            },
            "key_questions": [
                "Quality ceiling: Can vibe-coded products be excellent?",
                "Designer as director: New creative workflow",
                "The stack collapse: Frontend/backend/design → intent",
                "Speed vs. depth tradeoffs",
                "When to vibe code vs. traditional",
                "Debugging AI-generated code",
                "Prompt engineering patterns that work",
            ],
            "hot_takes": [
                "Vibe coding isn't killing designers—it's exposing pixel pushers",
                "The best vibe coders aren't coders—they're clear thinkers",
                "We're not automating development—we're automating translation",
                "Prompt engineering is the new programming literacy",
            ],
        },
    },

    "ai_native_design": {
        "name": "AI-Native Design Principles",
        "description": "New frameworks for designing AI systems",
        "priority": 3,
        "topics": {
            "paradigm_shifts": {
                "description": "Traditional vs AI-native design",
                "shifts": [
                    ("Design the interface", "Design the behavior"),
                    ("Static layouts", "Adaptive, generative layouts"),
                    ("User flows", "Possibility spaces"),
                    ("Edge cases", "Emergent behaviors"),
                    ("Design systems", "Prompt libraries + guardrails"),
                    ("Consistency", "Contextual intelligence"),
                    ("User testing", "Model evaluation"),
                ],
            },
            "frameworks": {
                "intent_first_design": {
                    "description": "Start with user goals, not UI",
                    "principles": [
                        "Let AI figure out the how",
                        "Design the boundaries, not the paths",
                        "Focus on outcomes, not interactions",
                    ],
                },
                "graceful_autonomy": {
                    "description": "When and how AI takes control",
                    "principles": [
                        "When AI should take control",
                        "When AI should ask permission",
                        "Escalation and de-escalation patterns",
                        "Trust calibration over time",
                    ],
                },
                "transparent_intelligence": {
                    "description": "Making AI decisions legible",
                    "principles": [
                        "Explainability in UX",
                        "Building trust through transparency",
                        "Confidence communication",
                    ],
                },
                "failure_mode_design": {
                    "description": "Designing for AI errors",
                    "principles": [
                        "What happens when AI is wrong?",
                        "Confident errors are worse than uncertain ones",
                        "Recovery and correction patterns",
                        "Maintaining trust after failure",
                    ],
                },
            },
        },
    },

    "philosophy_ethics": {
        "name": "Philosophy & Ethics Layer",
        "description": "Big questions about human-AI interaction",
        "priority": 4,
        "topics": {
            "human_agency": [
                "What happens to agency when AI predicts our needs?",
                "Should AI make us capable or dependent?",
                "The centaur model: Human + AI > either alone",
                "Preserving meaningful human choice",
            ],
            "creativity_authorship": [
                "If AI generates it, who created it?",
                "Is prompting a creative act?",
                "What does 'original' mean now?",
                "The human premium for handcrafted",
            ],
            "designer_identity": [
                "If AI can design, what's our value?",
                "From craftsperson → curator → conductor",
                "Skills that remain human: judgment, taste, ethics",
                "The case for human designers in AI era",
            ],
            "bias_representation": [
                "Whose values are encoded in AI?",
                "AI design through non-Western lens",
                "MENA and Global South perspective",
                "Designing for the next billion users",
            ],
            "endgame_questions": [
                "Are we designing ourselves out of relevance?",
                "What do humans do when AI does everything?",
                "Designing for flourishing, not just efficiency",
                "The future we're choosing to build",
            ],
        },
    },

    "predictions_futures": {
        "name": "Predictions & Futures",
        "description": "Forward-looking analysis and predictions",
        "priority": 5,
        "topics": {
            "near_term_2025_2026": [
                "Design tools market collapse (Figma AI = everything?)",
                "Vibe coding goes mainstream",
                "First AI-designed mass-market products",
                "Copilot fatigue and pushback",
                "EU AI Act impacts on design",
                "AI agents reach consumer products",
            ],
            "medium_term_2027_2029": [
                "Death of apps (agents do everything)",
                "Personalized interfaces at scale",
                "Human premium for handcrafted products",
                "Design education crisis/reinvention",
                "New job titles emerge, old ones die",
                "First AI-native design superstars",
            ],
            "long_term_2030_plus": [
                "Brain-computer interfaces go consumer",
                "AI indistinguishable from human in creative tasks",
                "'User experience' completely transforms",
                "Post-work design economy?",
                "The Intent Layer becomes standard",
            ],
            "prediction_categories": [
                "What's inevitable vs. hype",
                "Happening faster than expected",
                "Happening slower than expected",
                "What nobody is talking about yet",
            ],
        },
    },

    "tactical_technical": {
        "name": "Tactical/Technical Depth",
        "description": "Technical concepts designers need to know",
        "priority": 6,
        "topics": {
            "models_capabilities": [
                "GPT-4/4o vs Claude vs Gemini for design tasks",
                "When to use which model",
                "Context windows implications for design",
                "Multimodal capabilities (vision, audio, code)",
                "Local vs cloud models",
                "Cost and latency considerations",
            ],
            "tools_ecosystem": [
                "Figma AI capabilities and limits",
                "Adobe Firefly / Canva AI",
                "v0, Bolt, Lovable comparisons",
                "Cursor vs Windsurf vs GitHub Copilot",
                "AI prototyping tools",
                "The emerging AI-native stack",
            ],
            "technical_concepts": [
                "Prompt engineering principles",
                "RAG (retrieval augmented generation)",
                "Fine-tuning vs prompting tradeoffs",
                "Hallucination design patterns",
                "Evaluation and testing AI outputs",
                "Tokens, context, memory design",
            ],
            "implementation_patterns": [
                "AI-first vs AI-augmented strategy",
                "Build vs buy AI features",
                "Designing for AI errors gracefully",
                "Progressive disclosure of AI capabilities",
                "Human-in-the-loop patterns",
                "Feedback loops and learning systems",
            ],
        },
    },
}


# Quick access to all topic areas
TOPIC_AREAS = []
for dimension_key, dimension in CONTENT_DIMENSIONS.items():
    for topic_key in dimension.get("topics", {}):
        TOPIC_AREAS.append({
            "dimension": dimension_key,
            "dimension_name": dimension["name"],
            "topic": topic_key,
            "priority": dimension["priority"],
        })
