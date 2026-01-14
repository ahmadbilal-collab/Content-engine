#!/usr/bin/env python3
"""
BHARTE CHALO - Radio Show Script Generator

Generates engaging bilingual (English + Urdu) radio show scripts for Pakistan's
future-focused show on AI, IT, leadership, and innovation.

Target: Pakistani audience across all cities and backgrounds
Language: Bilingual - English with natural Roman Urdu integration
"""

from typing import Dict, Any, Optional, List
from datetime import datetime


class RadioScriptGenerator:
    """
    Generates radio show scripts for Bharte Chalo.

    Show Philosophy:
    - Educate everyone in Pakistan on AI, IT, leadership, and innovation
    - Help listeners think better, decide smarter, and move forward
    - Make complex topics accessible and actionable
    - Inspire forward momentum ("Bharte Chalo" = Keep Moving Forward)
    - Bilingual delivery: English + Roman Urdu for maximum reach
    """

    # Pakistan context for scripts
    PAKISTAN_CONTEXT = {
        "cities": [
            "Karachi", "Lahore", "Islamabad", "Rawalpindi", "Faisalabad",
            "Multan", "Peshawar", "Quetta", "Sialkot", "Gujranwala"
        ],
        "tech_hubs": [
            "NSTP Islamabad", "Arfa Tower Lahore", "NIC Karachi",
            "Plan9 Lahore", "Daftarkhwan Islamabad"
        ],
        "industries": [
            "IT exports", "freelancing", "e-commerce", "fintech",
            "agritech", "edtech", "healthtech", "textiles", "manufacturing"
        ],
        "challenges": [
            "load shedding", "internet connectivity", "dollar rate",
            "brain drain", "skill gaps", "funding access"
        ],
        "opportunities": [
            "young population", "growing IT exports", "remote work boom",
            "startup ecosystem", "digital banking", "e-commerce growth"
        ],
        "success_stories": [
            "Pakistani unicorns", "top Upwork freelancers",
            "Silicon Valley Pakistanis", "local tech startups"
        ]
    }

    # Common Urdu phrases for natural integration
    URDU_PHRASES = {
        "greetings": [
            "Assalam-u-Alaikum",
            "Khush aamdeed",
            "Kya haal hai aap sab ka"
        ],
        "encouragement": [
            "Bharte chalo",
            "Aagey barhein",
            "Himmat na harein",
            "Koshish jaari rakhein",
            "Aap kar sakte hain",
            "Mushkil zaroor hai, lekin namumkin nahi"
        ],
        "transitions": [
            "Ab baat karte hain",
            "Aur suniye",
            "Sochiye zara",
            "Yeh hai dilchasp baat",
            "Ek aur zaroori baat",
            "Chalein aagey barhte hain"
        ],
        "emphasis": [
            "Yeh bohat zaroori hai",
            "Dhyan se suniye",
            "Yaad rakhein",
            "Bilkul sahi baat",
            "Yeh samajhna zaroori hai"
        ],
        "closing": [
            "Shukriya",
            "Allah Hafiz",
            "Phir milenge",
            "Agli baar tak",
            "Apna khayal rakhein"
        ],
        "motivational": [
            "Pakistan ka mustaqbil roshan hai",
            "Hum sab mil kar kar sakte hain",
            "Apni capability pe bharosa rakhein",
            "Seekhna kabhi band na karein"
        ]
    }

    # Show configuration
    SHOW_CONFIG = {
        "show_name": "Bharte Chalo",
        "episodes_per_week": 2,
        "episode_duration": "90 minutes",
        "release_days": ["Tuesday", "Friday"]
    }

    # Show segments configuration (NEW 90-minute format with diverse segments)
    # Opening (10) + Tech Samjho (10) + Tips (8) + Skill/Career (10) + Kahani (10) +
    # Game (5) + News (12) + Q&A (10) + Global (7) + Conclusion (8) = 90 min
    SEGMENTS = {
        "opening": {
            "duration": "8-10 minutes",
            "purpose": "Show opening, energy, host intro, audience connection",
            "urdu_name": "Aghaz",
            "subsections": [
                {
                    "name": "Signature Opening",
                    "urdu_name": "Aghaz-e-Show",
                    "duration": "2 minutes",
                    "content": [
                        "Show jingle (15 seconds)",
                        "Energetic 'Assalam-u-Alaikum Pakistan!'",
                        "Show tagline: 'Sochein Behtar, Faisla Karein Smarter, Aagey Barhein!'",
                        "Today's date and episode number",
                        "Quick energy hook: 'Aaj ka episode aapko...'"
                    ]
                },
                {
                    "name": "Host's Corner",
                    "urdu_name": "Mezbaan ki Baat",
                    "duration": "2-3 minutes",
                    "content": [
                        "Personal touch - What's on host's mind",
                        "Something interesting from the week",
                        "Connect with current Pakistani context",
                        "Why today's topic matters personally"
                    ]
                },
                {
                    "name": "Episode Preview",
                    "urdu_name": "Aaj ka Agenda",
                    "duration": "2 minutes",
                    "content": [
                        "What's coming in today's episode",
                        "Why each segment matters",
                        "Special mentions (guests, features)"
                    ]
                },
                {
                    "name": "Listener Shoutouts",
                    "urdu_name": "Saameen ke Naam",
                    "duration": "2-3 minutes",
                    "content": [
                        "Shoutouts by city (Karachi, Lahore, Islamabad, etc.)",
                        "New listener welcomes",
                        "Community highlights and achievements"
                    ]
                }
            ]
        },
        "tech_samjho": {
            "duration": "10 minutes",
            "purpose": "Tech explained for ordinary people - accessible, simple, relevant",
            "urdu_name": "Tech Samjho",
            "subsections": [
                {
                    "name": "Aam Aadmi ki Tech",
                    "urdu_name": "عام آدمی کی ٹیک",
                    "duration": "4 minutes",
                    "content": [
                        "Tech news explained simply for non-tech people",
                        "What happened this week in simple words",
                        "Why should a regular person care?"
                    ]
                },
                {
                    "name": "Yeh Kaise Kaam Karta Hai",
                    "urdu_name": "یہ کیسے کام کرتا ہے",
                    "duration": "3 minutes",
                    "content": [
                        "One tech concept explained with Pakistani analogies",
                        "Chai, cricket, bazaar examples",
                        "Simple enough for grandparents to understand"
                    ]
                },
                {
                    "name": "Aapke Kaam Ki Baat",
                    "urdu_name": "آپ کے کام کی بات",
                    "duration": "3 minutes",
                    "content": [
                        "How this tech affects daily life in Pakistan",
                        "Practical implications",
                        "What to do with this knowledge"
                    ]
                }
            ]
        },
        "tips_tricks": {
            "duration": "8 minutes",
            "purpose": "Practical tips for mobile, computer, hardware, software",
            "urdu_name": "Totke",
            "subsections": [
                {
                    "name": "Mobile Totka",
                    "urdu_name": "موبائل ٹوٹکا",
                    "duration": "3 minutes",
                    "content": [
                        "Phone tips, apps, battery saving",
                        "Storage management",
                        "Hidden features",
                        "Free apps that work like paid ones"
                    ]
                },
                {
                    "name": "Computer/Laptop Tip",
                    "urdu_name": "کمپیوٹر ٹپ",
                    "duration": "3 minutes",
                    "content": [
                        "PC/laptop speed hacks",
                        "Keyboard shortcuts",
                        "Maintenance tips",
                        "Free software recommendations"
                    ]
                },
                {
                    "name": "Hardware/Software Hack",
                    "urdu_name": "ہارڈویئر/سافٹویئر ہیک",
                    "duration": "2 minutes",
                    "content": [
                        "Solutions for common tech problems",
                        "DIY fixes",
                        "When to repair vs replace",
                        "Budget-friendly solutions"
                    ]
                }
            ]
        },
        "skill_career": {
            "duration": "10 minutes",
            "purpose": "Career guidance and skill development - rotates between skill spotlight and career path",
            "urdu_name": "Skill ya Career",
            "rotation": ["skill_spotlight", "career_in_it"],
            "subsections": [
                {
                    "name": "Skill Spotlight",
                    "urdu_name": "Hunar ki Baat",
                    "duration": "10 minutes",
                    "content": [
                        "What is this skill? (2 min)",
                        "Why is it in demand? Market numbers (2 min)",
                        "How to learn FREE? Resources (3 min)",
                        "Earning potential in Pakistan (2 min)",
                        "30-Day Learning Challenge (1 min)"
                    ],
                    "example_skills": [
                        "Prompt Engineering",
                        "Excel/Data Analysis",
                        "Video Editing",
                        "Graphic Design",
                        "Content Writing",
                        "Web Development",
                        "Digital Marketing"
                    ]
                },
                {
                    "name": "Career in IT",
                    "urdu_name": "IT mein Career",
                    "duration": "10 minutes",
                    "content": [
                        "What is this career? (2 min)",
                        "Day in the life - what do they do? (2 min)",
                        "How to enter - education, skills (3 min)",
                        "Salary ranges - Pakistan + remote (2 min)",
                        "First step to take TODAY (1 min)"
                    ],
                    "example_careers": [
                        "Software Developer",
                        "Data Analyst",
                        "UI/UX Designer",
                        "DevOps Engineer",
                        "Product Manager",
                        "QA Engineer",
                        "AI/ML Engineer"
                    ]
                }
            ]
        },
        "kahani": {
            "duration": "10 minutes",
            "purpose": "Inspirational narrative storytelling - success and failure stories",
            "urdu_name": "Kahani",
            "subsections": [
                {
                    "name": "Story Introduction",
                    "urdu_name": "Kahani Shuru",
                    "duration": "2 minutes",
                    "content": [
                        "Hook the listener",
                        "Person intro - name, city, background",
                        "'Aaj ki kahani shuru hoti hai...'"
                    ]
                },
                {
                    "name": "The Journey",
                    "urdu_name": "Safar",
                    "duration": "3 minutes",
                    "content": [
                        "Where they started",
                        "Struggles and challenges",
                        "The turning point moment"
                    ]
                },
                {
                    "name": "The Achievement",
                    "urdu_name": "Manzil",
                    "duration": "2 minutes",
                    "content": [
                        "Where they are now",
                        "Numbers and achievements",
                        "Impact on their life"
                    ]
                },
                {
                    "name": "Lessons Learned",
                    "urdu_name": "Sabaq",
                    "duration": "2 minutes",
                    "content": [
                        "3 key lessons from their journey",
                        "What they wish they knew earlier",
                        "Mistakes to avoid"
                    ]
                },
                {
                    "name": "Their Advice",
                    "urdu_name": "Unka Mashwara",
                    "duration": "1 minute",
                    "content": [
                        "Direct message for listeners",
                        "How to connect with them",
                        "'Agar main kar sakta hoon, toh aap bhi...'"
                    ]
                }
            ],
            "story_types": {
                "success": "Kamyabi ki Kahani - 3 episodes",
                "failure": "Haar se Seekho - 1 episode (to normalize failure)"
            }
        },
        "game_segment": {
            "duration": "5 minutes",
            "purpose": "Interactive fun segment - rotates weekly",
            "urdu_name": "Khel",
            "rotation": ["sach_ya_jhoot", "tech_myth_busters", "tech_trivia", "hot_take"],
            "subsections": [
                {
                    "name": "Sach ya Jhoot (2 Truths & A Lie)",
                    "urdu_name": "سچ یا جھوٹ",
                    "duration": "5 minutes",
                    "content": [
                        "Present 3 tech 'facts'",
                        "Listeners guess which is false",
                        "Reveal answer with explanation",
                        "Winner shoutout next episode"
                    ]
                },
                {
                    "name": "Tech Myth Busters",
                    "urdu_name": "Sach ya Afsana",
                    "duration": "5 minutes",
                    "content": [
                        "Present common tech myth",
                        "'Yeh sach hai ya afsana?'",
                        "Reveal truth with proof",
                        "Pakistani context"
                    ],
                    "example_myths": [
                        "Raat ko phone charge karna battery kharab karta hai",
                        "Incognito mode mein koi track nahi kar sakta",
                        "Zyada RAM = zyada fast phone",
                        "Mac mein virus nahi aata"
                    ]
                },
                {
                    "name": "Tech Trivia",
                    "urdu_name": "Tech Muqabla",
                    "duration": "5 minutes",
                    "content": [
                        "3 quick trivia questions",
                        "WhatsApp answers",
                        "Points and leaderboard",
                        "Monthly winner prize"
                    ]
                },
                {
                    "name": "Hot Take",
                    "urdu_name": "Seedhi Baat",
                    "duration": "5 minutes",
                    "content": [
                        "Host's controversial tech opinion",
                        "Reasoning explained",
                        "'Aap agree karte ho?'",
                        "Read responses next episode"
                    ],
                    "example_hot_takes": [
                        "Pakistan mein AI se zyada Excel seekhna zaroori hai",
                        "Degree se zyada portfolio important hai",
                        "Remote work har Pakistani ke liye nahi hai"
                    ]
                }
            ]
        },
        "tech_news": {
            "duration": "12 minutes",
            "purpose": "Weekly tech news roundup with tool review",
            "urdu_name": "Tech Khabrain",
            "subsections": [
                {
                    "name": "Top 5 Headlines",
                    "urdu_name": "Paanch Khabrain",
                    "duration": "5 minutes",
                    "content": [
                        "Top 5 tech news of the week",
                        "Quick summary of each",
                        "Host's take on each story",
                        "Which matters most for Pakistan"
                    ]
                },
                {
                    "name": "Pakistan Tech News",
                    "urdu_name": "Pakistan ki Khabrain",
                    "duration": "3 minutes",
                    "content": [
                        "Local tech ecosystem updates",
                        "Government announcements",
                        "Pakistani startup news",
                        "IT export and freelancing stats"
                    ]
                },
                {
                    "name": "AI/Tool Update",
                    "urdu_name": "AI Update",
                    "duration": "2 minutes",
                    "content": [
                        "New AI tools released",
                        "ChatGPT, Gemini, Claude updates",
                        "How to use new features"
                    ]
                },
                {
                    "name": "Software/Tool Review",
                    "urdu_name": "Hafte ka Tool",
                    "duration": "2 minutes",
                    "content": [
                        "One tool reviewed in detail",
                        "What it does",
                        "Free vs Paid features",
                        "Works in Pakistan? Data usage?",
                        "Host's rating (out of 5 stars)"
                    ]
                }
            ]
        },
        "your_questions": {
            "duration": "10 minutes",
            "purpose": "Listener engagement through Q&A",
            "urdu_name": "Aap ke Sawaal",
            "subsections": [
                {
                    "name": "Question 1",
                    "urdu_name": "Pehla Sawaal",
                    "duration": "3 minutes",
                    "content": [
                        "Read question with listener name/city",
                        "Detailed answer",
                        "Resources to learn more"
                    ]
                },
                {
                    "name": "Question 2",
                    "urdu_name": "Doosra Sawaal",
                    "duration": "3 minutes",
                    "content": [
                        "Different topic or skill level",
                        "Practical answer",
                        "Action steps"
                    ]
                },
                {
                    "name": "Question 3",
                    "urdu_name": "Teesra Sawaal",
                    "duration": "3 minutes",
                    "content": [
                        "Career or practical question",
                        "Honest advice",
                        "Personal experience if relevant"
                    ]
                },
                {
                    "name": "Quick Fire",
                    "urdu_name": "Jaldi Jaldi",
                    "duration": "1 minute",
                    "content": [
                        "2-3 quick yes/no questions",
                        "Rapid answers",
                        "Fun and fast-paced"
                    ]
                }
            ]
        },
        "global_opportunities": {
            "duration": "7 minutes",
            "purpose": "Global perspective and job opportunities - rotates",
            "urdu_name": "Global Nazar",
            "rotation": ["global_tech_tour", "rate_card_jobs"],
            "subsections": [
                {
                    "name": "Global Tech Tour",
                    "urdu_name": "Duniya ka Chakkar",
                    "duration": "7 minutes",
                    "content": [
                        "One country's tech scene spotlight (3 min)",
                        "What Pakistan can learn (2 min)",
                        "Opportunities for Pakistanis there (2 min)"
                    ],
                    "countries": [
                        "UAE/Dubai", "India", "Estonia", "Singapore",
                        "Germany", "China", "USA", "UK", "Canada"
                    ]
                },
                {
                    "name": "Rate Card + Job Board",
                    "urdu_name": "Paisa aur Naukri",
                    "duration": "7 minutes",
                    "content": [
                        "Rate Card: Salaries, freelance rates, pricing tips (3 min)",
                        "Job Board: 3-5 real job opportunities (3 min)",
                        "How to Apply: Quick application tips (1 min)"
                    ]
                }
            ]
        },
        "conclusion": {
            "duration": "8-10 minutes",
            "purpose": "Summary, takeaways, IT tips, and closing",
            "urdu_name": "Khulaasa aur Alvida",
            "subsections": [
                {
                    "name": "Episode Summary",
                    "urdu_name": "Aaj Humne Seekha",
                    "duration": "2 minutes",
                    "content": [
                        "Quick recap of all segments",
                        "Key highlights",
                        "'Aaj humne seekha...'"
                    ]
                },
                {
                    "name": "3 Key Takeaways",
                    "urdu_name": "Teen Zaroori Baatein",
                    "duration": "2 minutes",
                    "content": [
                        "3 actionable points from the episode",
                        "What to remember",
                        "What to do"
                    ]
                },
                {
                    "name": "Weekly Challenge",
                    "urdu_name": "Hafte ka Challenge",
                    "duration": "1 minute",
                    "content": [
                        "One thing to do before next episode",
                        "Hashtag to share results",
                        "Winner featured next episode"
                    ]
                },
                {
                    "name": "IT Problem/Solution",
                    "urdu_name": "Masla aur Hal",
                    "duration": "2 minutes",
                    "content": [
                        "Common IT problem",
                        "Quick solution explained",
                        "Troubleshooting tip"
                    ]
                },
                {
                    "name": "Closing",
                    "urdu_name": "Alvida",
                    "duration": "2-3 minutes",
                    "content": [
                        "Next episode teaser",
                        "How to reach out (WhatsApp, email, social)",
                        "Motivational closing: 'Bharte Chalo!'",
                        "'Allah Hafiz Pakistan!'",
                        "Closing jingle"
                    ]
                }
            ]
        }
    }

    # Episode themes with Urdu names
    THEMES = {
        "AI Fundamentals": "AI ki Bunyaad",
        "Leadership in Digital Age": "Digital Daur mein Leadership",
        "Innovation Mindset": "Jadeed Soch",
        "Career in Tech": "Tech mein Career",
        "Entrepreneurship": "Apna Karobar",
        "Digital Transformation": "Digital Tabdeeli",
        "Future of Work": "Kaam ka Mustaqbil",
        "Tech for Social Good": "Tech se Samaj ki Khidmat",
        "Learning & Upskilling": "Seekhna aur Taraqi",
        "Building Tech Teams": "Tech Teams Banana",
        "Freelancing Success": "Freelancing mein Kamyabi",
        "Pakistan Tech Ecosystem": "Pakistan ka Tech Mahaul"
    }

    def __init__(self, gemini_client):
        """
        Initialize the radio script generator.

        Args:
            gemini_client: GeminiClient instance for AI generation
        """
        self.gemini = gemini_client
        self.show_name = "Bharte Chalo"
        self.tagline = "Sochein Behtar, Faisla Karein Smarter, Aagey Barhein"
        self.tagline_english = "Think Better, Decide Smarter, Move Forward"

    def generate_episode_script(
        self,
        topic: str,
        theme: str = "AI Fundamentals",
        guest_name: Optional[str] = None,
        episode_number: Optional[int] = None,
        include_urdu_phrases: bool = True,
        language_balance: str = "balanced"  # "balanced", "urdu_heavy", "english_heavy"
    ) -> Dict[str, Any]:
        """
        Generate a complete bilingual episode script.

        Args:
            topic: Main topic for the episode
            theme: Episode theme category
            guest_name: Optional guest name
            episode_number: Episode number
            include_urdu_phrases: Whether to include Urdu phrases
            language_balance: How to balance English and Urdu

        Returns:
            Complete episode script with all segments
        """
        urdu_theme = self.THEMES.get(theme, theme)

        language_instruction = {
            "balanced": "Use a 60% English, 40% Roman Urdu mix. Switch naturally between languages as Pakistanis do in daily conversation.",
            "urdu_heavy": "Use 40% English, 60% Roman Urdu. More Urdu for emotional and motivational parts.",
            "english_heavy": "Use 75% English, 25% Roman Urdu. Urdu for greetings, emphasis, and key phrases."
        }.get(language_balance, "balanced")

        prompt = f"""
You are a scriptwriter for "Bharte Chalo" (بڑھتے چلو - Keep Moving Forward),
Pakistan's most popular bilingual radio show educating listeners on AI, IT,
leadership, and innovation.

═══════════════════════════════════════════════════════════════════
SHOW IDENTITY
═══════════════════════════════════════════════════════════════════
Name: Bharte Chalo (بڑھتے چلو)
Tagline: "Sochein Behtar, Faisla Karein Smarter, Aagey Barhein"
         (سوچیں بہتر، فیصلہ کریں اسمارٹر، آگے بڑھیں)
         Translation: Think Better, Decide Smarter, Move Forward

Target Audience:
- Pakistani professionals in Karachi, Lahore, Islamabad, and beyond
- University students exploring tech careers
- Entrepreneurs and startup founders
- Business leaders navigating digital transformation
- Freelancers building global careers from Pakistan
- Parents guiding children in tech education
- Anyone curious about AI and the future

═══════════════════════════════════════════════════════════════════
BILINGUAL STYLE GUIDE
═══════════════════════════════════════════════════════════════════
{language_instruction}

KEY RULES:
1. Write Urdu in ROMAN SCRIPT (not Arabic/Nastaliq) for radio host to read
2. Mix languages naturally like educated Pakistanis speak
3. Use Urdu for:
   - Greetings and warmth: "Assalam-u-Alaikum", "Khush aamdeed"
   - Emotional connection: "Dil se baat karte hain"
   - Emphasis: "Yeh bohat zaroori hai"
   - Encouragement: "Aap zaroor kar sakte hain"
   - Cultural references: "Jaise hamare ghar mein..."
4. Use English for:
   - Technical terms (with Urdu explanation)
   - Global concepts
   - Data and statistics
5. Always explain technical terms in simple Urdu after introducing them

EXAMPLE SCRIPT STYLE:
"Assalam-u-Alaikum doston! Aaj hum baat karenge Artificial Intelligence ki -
jo basically computers ko insaan ki tarah sochne ki power deti hai. Ab aap
soch rahe honge ke yeh mujhe kaise help karega? Suniye, agar aap freelancer
hain Upwork pe, toh AI tools aapka kaam 10 guna fast kar sakte hain..."

═══════════════════════════════════════════════════════════════════
EPISODE DETAILS
═══════════════════════════════════════════════════════════════════
Topic: {topic}
Theme: {theme} ({urdu_theme})
Episode Number: {episode_number or "TBD"}
Guest: {guest_name or "No guest - solo episode"}

═══════════════════════════════════════════════════════════════════
PAKISTAN CONTEXT TO WEAVE IN
═══════════════════════════════════════════════════════════════════
Tech Ecosystem:
- IT exports crossing $3 billion
- Freelancing hub - top country on platforms like Upwork
- Growing startup scene in Lahore, Karachi, Islamabad
- Challenges: load shedding, dollar rates, connectivity

Real Examples to Reference:
- Pakistani developers working for global companies
- Local startups solving Pakistani problems
- Freelancers earning in dollars, building careers from home
- University students building tech skills

Cultural Context:
- Family support and expectations
- Balancing tradition with innovation
- Making parents proud through tech careers
- Community and helping others succeed

═══════════════════════════════════════════════════════════════════
SHOW FORMAT: 90 MINUTE EPISODE WITH 10 DIVERSE SEGMENTS
═══════════════════════════════════════════════════════════════════

GENERATE COMPREHENSIVE HIGH-CONTENT RADIO SCRIPT WITH THESE 10 SEGMENTS.
WRITE FULL SCRIPTS FOR EVERY SEGMENT. This format includes rotating segments
for variety across episodes.

══════════════════════════════════════════════════════════════
SEGMENT 1: AGHAZ / OPENING (8-10 minutes)
══════════════════════════════════════════════════════════════

1.1 SIGNATURE OPENING (Aghaz-e-Show) - 2 min
- Show jingle (15 seconds)
- Energetic "Assalam-u-Alaikum Pakistan!"
- Show tagline: "Sochein Behtar, Faisla Karein Smarter, Aagey Barhein!"
- Today's date and episode number

1.2 HOST'S CORNER (Mezbaan ki Baat) - 2-3 min
- Personal touch - What's on host's mind
- Something interesting from the week
- Pakistani context connection

1.3 EPISODE PREVIEW (Aaj ka Agenda) - 2 min
- What's coming in today's episode
- Why each segment matters

1.4 LISTENER SHOUTOUTS (Saameen ke Naam) - 2-3 min
- Shoutouts by city (Karachi, Lahore, Islamabad, etc.)
- Community highlights

══════════════════════════════════════════════════════════════
SEGMENT 2: TECH SAMJHO / TECH FOR EVERYONE (10 minutes)
══════════════════════════════════════════════════════════════

2.1 AAM AADMI KI TECH (عام آدمی کی ٹیک) - 4 min
- Tech news explained simply for non-tech people
- What happened this week in simple words

2.2 YEH KAISE KAAM KARTA HAI (یہ کیسے کام کرتا ہے) - 3 min
- One tech concept explained with Pakistani analogies
- Chai, cricket, bazaar examples

2.3 AAPKE KAAM KI BAAT (آپ کے کام کی بات) - 3 min
- How this tech affects daily life in Pakistan
- Practical implications

══════════════════════════════════════════════════════════════
SEGMENT 3: TOTKE / TIPS & TRICKS (8 minutes)
══════════════════════════════════════════════════════════════

3.1 MOBILE TOTKA (موبائل ٹوٹکا) - 3 min
- Phone tips, apps, battery saving, storage management
- Hidden features, free apps

3.2 COMPUTER/LAPTOP TIP (کمپیوٹر ٹپ) - 3 min
- PC/laptop speed hacks, shortcuts
- Maintenance tips, free software

3.3 HARDWARE/SOFTWARE HACK (ہارڈویئر/سافٹویئر) - 2 min
- Solutions for common tech problems
- Budget-friendly solutions

══════════════════════════════════════════════════════════════
SEGMENT 4: SKILL YA CAREER / SKILL OR CAREER (10 minutes)
[ROTATING: Skill Spotlight on Tuesdays, Career in IT on Fridays]
══════════════════════════════════════════════════════════════

Option A - SKILL SPOTLIGHT (Hunar ki Baat):
- What is this skill? (2 min)
- Why is it in demand? (2 min)
- How to learn FREE? (3 min)
- Earning potential in Pakistan (2 min)
- 30-Day Learning Challenge (1 min)

Option B - CAREER IN IT (IT mein Career):
- What is this career? (2 min)
- Day in the life (2 min)
- How to enter - education, skills (3 min)
- Salary ranges - Pakistan + remote (2 min)
- First step to take TODAY (1 min)

══════════════════════════════════════════════════════════════
SEGMENT 5: KAHANI / STORY (10 minutes)
══════════════════════════════════════════════════════════════

5.1 STORY INTRO (Kahani Shuru) - 2 min
- Hook the listener
- Person intro - name, city, background

5.2 THE JOURNEY (Safar) - 3 min
- Where they started
- Struggles and challenges
- The turning point

5.3 THE ACHIEVEMENT (Manzil) - 2 min
- Where they are now
- Numbers and achievements

5.4 LESSONS (Sabaq) - 2 min
- 3 key lessons from their journey

5.5 THEIR ADVICE (Unka Mashwara) - 1 min
- Direct message for listeners

══════════════════════════════════════════════════════════════
SEGMENT 6: KHEL / GAME SEGMENT (5 minutes)
[ROTATING: Week 1: Sach ya Jhoot, Week 2: Tech Myth Busters,
           Week 3: Tech Trivia, Week 4: Hot Take]
══════════════════════════════════════════════════════════════

Option A - SACH YA JHOOT (2 Truths & A Lie):
- Present 3 tech "facts"
- Listeners guess which is false
- Reveal answer with explanation

Option B - TECH MYTH BUSTERS (Sach ya Afsana):
- Present common tech myth
- "Yeh sach hai ya afsana?"
- Reveal truth with proof

Option C - TECH TRIVIA (Tech Muqabla):
- 3 quick trivia questions
- WhatsApp answers
- Points and leaderboard

Option D - HOT TAKE (Seedhi Baat):
- Host's controversial tech opinion
- Reasoning explained
- "Aap agree karte ho?"

══════════════════════════════════════════════════════════════
SEGMENT 7: TECH KHABRAIN / NEWS (12 minutes)
══════════════════════════════════════════════════════════════

7.1 TOP 5 HEADLINES (Paanch Khabrain) - 5 min
- Top 5 tech news of the week
- Host's take on each story

7.2 PAKISTAN TECH NEWS (Pakistan ki Khabrain) - 3 min
- Local tech ecosystem updates
- Government announcements, startup news

7.3 AI/TOOL UPDATE (AI Update) - 2 min
- New AI tools released
- ChatGPT, Gemini, Claude updates

7.4 SOFTWARE/TOOL REVIEW (Hafte ka Tool) - 2 min
- One tool reviewed in detail
- Free vs Paid, Works in Pakistan?
- Host's rating (out of 5 stars)

══════════════════════════════════════════════════════════════
SEGMENT 8: AAP KE SAWAAL / YOUR QUESTIONS (10 minutes)
══════════════════════════════════════════════════════════════

8.1 QUESTION 1 (Pehla Sawaal) - 3 min
- Read question with listener name/city
- Detailed answer with resources

8.2 QUESTION 2 (Doosra Sawaal) - 3 min
- Different topic or skill level
- Practical answer

8.3 QUESTION 3 (Teesra Sawaal) - 3 min
- Career or practical question
- Honest advice

8.4 QUICK FIRE (Jaldi Jaldi) - 1 min
- 2-3 quick yes/no questions
- Rapid answers

══════════════════════════════════════════════════════════════
SEGMENT 9: GLOBAL NAZAR / GLOBAL OPPORTUNITIES (7 minutes)
[ROTATING: Global Tech Tour on Tuesdays, Rate Card + Jobs on Fridays]
══════════════════════════════════════════════════════════════

Option A - GLOBAL TECH TOUR (Duniya ka Chakkar):
- One country's tech scene spotlight (3 min)
- What Pakistan can learn (2 min)
- Opportunities for Pakistanis there (2 min)

Option B - RATE CARD + JOB BOARD (Paisa aur Naukri):
- Rate Card: Salaries, freelance rates, pricing tips (3 min)
- Job Board: 3-5 real job opportunities (3 min)
- How to Apply: Quick application tips (1 min)

══════════════════════════════════════════════════════════════
SEGMENT 10: KHULAASA & ALVIDA / CONCLUSION & CLOSING (8-10 minutes)
══════════════════════════════════════════════════════════════

10.1 EPISODE SUMMARY (Aaj Humne Seekha) - 2 min
- Quick recap of all segments
- Key highlights

10.2 THREE KEY TAKEAWAYS (Teen Zaroori Baatein) - 2 min
- 3 actionable points from the episode

10.3 WEEKLY CHALLENGE (Hafte ka Challenge) - 1 min
- One thing to do before next episode
- Hashtag to share results

10.4 IT PROBLEM/SOLUTION (Masla aur Hal) - 2 min
- Common IT problem
- Quick solution explained

10.5 CLOSING (Alvida) - 2-3 min
- Next episode teaser
- Contact info (WhatsApp, email, social)
- "Bharte Chalo!"
- "Allah Hafiz Pakistan!"
- Closing jingle

═══════════════════════════════════════════════════════════════════
OUTPUT FORMAT (HIGH-CONTENT 90-MINUTE EPISODE)
═══════════════════════════════════════════════════════════════════

IMPORTANT: Generate FULL DETAILED SCRIPTS for EVERY segment. Each segment
should have complete, broadcast-ready content. This is radio content that will be
read on air - make it engaging, informative, and bilingual throughout.

Return as JSON:
{{
    "episode_title": "Catchy bilingual title",
    "episode_title_urdu": "Title in Roman Urdu",
    "episode_number": {episode_number or "null"},
    "theme": "{theme}",
    "theme_urdu": "{urdu_theme}",
    "topic": "{topic}",
    "total_duration": "90 minutes",
    "episode_day": "Tuesday or Friday",
    "language_mix": "{language_balance}",
    "segments": {{
        "opening": {{
            "urdu_name": "Aghaz",
            "duration": "8-10 minutes",
            "subsegments": {{
                "signature_opening": {{
                    "name": "Signature Opening",
                    "urdu_name": "Aghaz-e-Show",
                    "duration": "2 minutes",
                    "script": "FULL script with jingle cue, energetic greeting, tagline, date"
                }},
                "hosts_corner": {{
                    "name": "Host's Corner",
                    "urdu_name": "Mezbaan ki Baat",
                    "duration": "2-3 minutes",
                    "script": "FULL script with personal touch and weekly observation"
                }},
                "episode_preview": {{
                    "name": "Episode Preview",
                    "urdu_name": "Aaj ka Agenda",
                    "duration": "2 minutes",
                    "script": "FULL script previewing all 10 segments"
                }},
                "listener_shoutouts": {{
                    "name": "Listener Shoutouts",
                    "urdu_name": "Saameen ke Naam",
                    "duration": "2-3 minutes",
                    "script": "FULL script with city shoutouts"
                }}
            }},
            "music_cues": ["Signature jingle - 15 sec", "fade under"]
        }},
        "tech_samjho": {{
            "urdu_name": "Tech Samjho",
            "duration": "10 minutes",
            "subsegments": {{
                "aam_aadmi_tech": {{
                    "name": "Aam Aadmi ki Tech",
                    "urdu_name": "عام آدمی کی ٹیک",
                    "duration": "4 minutes",
                    "script": "FULL script with tech news explained simply for non-tech people"
                }},
                "yeh_kaise_kaam": {{
                    "name": "Yeh Kaise Kaam Karta Hai",
                    "urdu_name": "یہ کیسے کام کرتا ہے",
                    "duration": "3 minutes",
                    "script": "FULL script explaining tech concept with Pakistani analogies"
                }},
                "aapke_kaam_ki_baat": {{
                    "name": "Aapke Kaam Ki Baat",
                    "urdu_name": "آپ کے کام کی بات",
                    "duration": "3 minutes",
                    "script": "FULL script on how this affects daily life in Pakistan"
                }}
            }},
            "music_cues": ["Transition sound"]
        }},
        "tips_tricks": {{
            "urdu_name": "Totke",
            "duration": "8 minutes",
            "subsegments": {{
                "mobile_totka": {{
                    "name": "Mobile Totka",
                    "urdu_name": "موبائل ٹوٹکا",
                    "duration": "3 minutes",
                    "script": "FULL script with phone tips, apps, battery, storage"
                }},
                "computer_tip": {{
                    "name": "Computer/Laptop Tip",
                    "urdu_name": "کمپیوٹر ٹپ",
                    "duration": "3 minutes",
                    "script": "FULL script with PC speed hacks and shortcuts"
                }},
                "hardware_software_hack": {{
                    "name": "Hardware/Software Hack",
                    "urdu_name": "ہارڈویئر/سافٹویئر ہیک",
                    "duration": "2 minutes",
                    "script": "FULL script with common problem solutions"
                }}
            }},
            "music_cues": ["Practical music bed"]
        }},
        "skill_career": {{
            "urdu_name": "Skill ya Career",
            "duration": "10 minutes",
            "rotation_type": "skill_spotlight or career_in_it",
            "script": "FULL script for either Skill Spotlight OR Career in IT based on episode day",
            "skill_spotlight": {{
                "name": "Skill Spotlight",
                "urdu_name": "Hunar ki Baat",
                "featured_skill": "Skill name (e.g., Prompt Engineering)",
                "what_is_it": "2 min explanation",
                "why_in_demand": "2 min market demand",
                "how_to_learn_free": "3 min free resources",
                "earning_potential": "2 min Pakistan salaries",
                "thirty_day_challenge": "1 min challenge"
            }},
            "career_in_it": {{
                "name": "Career in IT",
                "urdu_name": "IT mein Career",
                "featured_career": "Career name (e.g., Data Analyst)",
                "what_is_it": "2 min career explanation",
                "day_in_life": "2 min what they do",
                "how_to_enter": "3 min skills needed",
                "salary_ranges": "2 min Pakistan + remote",
                "first_step_today": "1 min actionable step"
            }}
        }},
        "kahani": {{
            "urdu_name": "Kahani",
            "duration": "10 minutes",
            "story_type": "success or failure",
            "subsegments": {{
                "story_intro": {{
                    "name": "Story Introduction",
                    "urdu_name": "Kahani Shuru",
                    "duration": "2 minutes",
                    "script": "FULL script introducing person - name, city, hook"
                }},
                "journey": {{
                    "name": "The Journey",
                    "urdu_name": "Safar",
                    "duration": "3 minutes",
                    "script": "FULL script with struggles and turning point"
                }},
                "achievement": {{
                    "name": "The Achievement",
                    "urdu_name": "Manzil",
                    "duration": "2 minutes",
                    "script": "FULL script with where they are now"
                }},
                "lessons": {{
                    "name": "Lessons Learned",
                    "urdu_name": "Sabaq",
                    "duration": "2 minutes",
                    "script": "FULL script with 3 key lessons"
                }},
                "advice": {{
                    "name": "Their Advice",
                    "urdu_name": "Unka Mashwara",
                    "duration": "1 minute",
                    "script": "FULL script with direct message"
                }}
            }},
            "featured_person": {{"name": "Name", "city": "City", "achievement": "Achievement"}}
        }},
        "game_segment": {{
            "urdu_name": "Khel",
            "duration": "5 minutes",
            "rotation_type": "sach_ya_jhoot, tech_myth_busters, tech_trivia, or hot_take",
            "script": "FULL script for the selected game type",
            "game_content": {{
                "type": "Game type for this episode",
                "items": ["Item 1", "Item 2", "Item 3"],
                "answer": "Correct answer or host's opinion",
                "explanation": "Why this is true/false"
            }}
        }},
        "tech_news": {{
            "urdu_name": "Tech Khabrain",
            "duration": "12 minutes",
            "subsegments": {{
                "top_headlines": {{
                    "name": "Top 5 Headlines",
                    "urdu_name": "Paanch Khabrain",
                    "duration": "5 minutes",
                    "script": "FULL script with 5 news items and host's take",
                    "news_items": [
                        {{"headline": "news 1", "category": "AI", "pakistan_relevance": "relevance"}},
                        {{"headline": "news 2", "category": "Tech", "pakistan_relevance": "relevance"}},
                        {{"headline": "news 3", "category": "Pakistan", "pakistan_relevance": "relevance"}},
                        {{"headline": "news 4", "category": "Startups", "pakistan_relevance": "relevance"}},
                        {{"headline": "news 5", "category": "Global", "pakistan_relevance": "relevance"}}
                    ]
                }},
                "pakistan_tech_news": {{
                    "name": "Pakistan Tech News",
                    "urdu_name": "Pakistan ki Khabrain",
                    "duration": "3 minutes",
                    "script": "FULL script with local ecosystem updates"
                }},
                "ai_update": {{
                    "name": "AI/Tool Update",
                    "urdu_name": "AI Update",
                    "duration": "2 minutes",
                    "script": "FULL script with AI tool updates"
                }},
                "tool_review": {{
                    "name": "Software/Tool Review",
                    "urdu_name": "Hafte ka Tool",
                    "duration": "2 minutes",
                    "script": "FULL script reviewing featured tool",
                    "featured_tool": {{"name": "Tool name", "free_paid": "Free/Paid", "rating": "4/5"}}
                }}
            }},
            "music_cues": ["News jingle"]
        }},
        "your_questions": {{
            "urdu_name": "Aap ke Sawaal",
            "duration": "10 minutes",
            "subsegments": {{
                "question_1": {{
                    "name": "Question 1",
                    "urdu_name": "Pehla Sawaal",
                    "duration": "3 minutes",
                    "listener_name": "Name",
                    "listener_city": "City",
                    "question": "The question",
                    "script": "FULL answer script"
                }},
                "question_2": {{
                    "name": "Question 2",
                    "urdu_name": "Doosra Sawaal",
                    "duration": "3 minutes",
                    "listener_name": "Name",
                    "listener_city": "City",
                    "question": "The question",
                    "script": "FULL answer script"
                }},
                "question_3": {{
                    "name": "Question 3",
                    "urdu_name": "Teesra Sawaal",
                    "duration": "3 minutes",
                    "listener_name": "Name",
                    "listener_city": "City",
                    "question": "The question",
                    "script": "FULL answer script"
                }},
                "quick_fire": {{
                    "name": "Quick Fire",
                    "urdu_name": "Jaldi Jaldi",
                    "duration": "1 minute",
                    "script": "FULL script with 2-3 quick questions and answers"
                }}
            }}
        }},
        "global_opportunities": {{
            "urdu_name": "Global Nazar",
            "duration": "7 minutes",
            "rotation_type": "global_tech_tour or rate_card_jobs",
            "script": "FULL script for either Global Tech Tour OR Rate Card + Jobs",
            "global_tech_tour": {{
                "name": "Global Tech Tour",
                "urdu_name": "Duniya ka Chakkar",
                "featured_country": "Country name",
                "tech_scene": "3 min country spotlight",
                "pakistan_lessons": "2 min what Pakistan can learn",
                "opportunities": "2 min opportunities for Pakistanis"
            }},
            "rate_card_jobs": {{
                "name": "Rate Card + Job Board",
                "urdu_name": "Paisa aur Naukri",
                "rate_card": "3 min salaries and freelance rates",
                "job_board": [
                    {{"title": "Job 1", "company": "Company", "salary": "Range", "how_to_apply": "Link/method"}},
                    {{"title": "Job 2", "company": "Company", "salary": "Range", "how_to_apply": "Link/method"}},
                    {{"title": "Job 3", "company": "Company", "salary": "Range", "how_to_apply": "Link/method"}}
                ],
                "application_tips": "1 min quick tips"
            }}
        }},
        "conclusion": {{
            "urdu_name": "Khulaasa aur Alvida",
            "duration": "8-10 minutes",
            "subsegments": {{
                "episode_summary": {{
                    "name": "Episode Summary",
                    "urdu_name": "Aaj Humne Seekha",
                    "duration": "2 minutes",
                    "script": "FULL script recap of all segments"
                }},
                "key_takeaways": {{
                    "name": "3 Key Takeaways",
                    "urdu_name": "Teen Zaroori Baatein",
                    "duration": "2 minutes",
                    "takeaways": ["Takeaway 1", "Takeaway 2", "Takeaway 3"],
                    "script": "FULL script with actionable points"
                }},
                "weekly_challenge": {{
                    "name": "Weekly Challenge",
                    "urdu_name": "Hafte ka Challenge",
                    "duration": "1 minute",
                    "challenge": "The challenge",
                    "hashtag": "#BharteChalo",
                    "script": "FULL script"
                }},
                "it_problem_solution": {{
                    "name": "IT Problem/Solution",
                    "urdu_name": "Masla aur Hal",
                    "duration": "2 minutes",
                    "problem": "Common IT problem",
                    "solution": "Quick solution",
                    "script": "FULL script"
                }},
                "closing": {{
                    "name": "Closing",
                    "urdu_name": "Alvida",
                    "duration": "2-3 minutes",
                    "next_episode_teaser": "What's coming next",
                    "script": "FULL closing script with contact info and Allah Hafiz Pakistan"
                }}
            }},
            "music_cues": ["Closing theme music", "Closing jingle"]
        }}
    }},
    "key_phrases_urdu": ["All memorable Urdu phrases with translations"],
    "technical_terms_explained": [
        {{"term": "AI", "urdu_explanation": "Computer ko insaan ki tarah sochna"}}
    ],
    "pakistan_references": ["All Pakistan-specific examples used"],
    "quotable_moments": ["Tweetable bilingual quotes - at least 5"],
    "resources_mentioned": ["All resources with Pakistani access notes"],
    "listener_engagement": {{
        "questions_to_ask": ["Questions to collect from listeners"],
        "challenge_of_week": "Weekly challenge",
        "social_hashtag": "#BharteChalo"
    }}
}}
"""

        response = self.gemini.generate_json(prompt)

        # Add metadata
        response["generated_at"] = datetime.now().isoformat()
        response["show_name"] = self.show_name
        response["show_tagline"] = self.tagline

        return response

    def generate_segment_script(
        self,
        segment_type: str,
        topic: str,
        context: Optional[str] = None,
        language_balance: str = "balanced"
    ) -> Dict[str, Any]:
        """
        Generate a single bilingual segment script.

        Args:
            segment_type: Type of segment (opening, tech_spotlight, etc.)
            topic: Topic for the segment
            context: Additional context
            language_balance: How to balance languages

        Returns:
            Segment script
        """
        segment_config = self.SEGMENTS.get(segment_type)
        if not segment_config:
            raise ValueError(f"Unknown segment type: {segment_type}")

        prompt = f"""
Generate a BILINGUAL radio script segment for "Bharte Chalo", Pakistan's show
on AI, IT, leadership, and innovation.

SEGMENT: {segment_type.upper().replace("_", " ")} ({segment_config['urdu_name']})
DURATION: {segment_config['duration']}
PURPOSE: {segment_config['purpose']}
TOPIC: {topic}
{f"ADDITIONAL CONTEXT: {context}" if context else ""}

LANGUAGE STYLE:
- Mix English and Roman Urdu naturally (60-40 split)
- Use Urdu for warmth, emphasis, and connection
- Use English for technical terms (but explain in Urdu)
- Write like educated Pakistanis actually speak

PAKISTAN FOCUS:
- Reference Pakistani cities, challenges, opportunities
- Use local analogies (chai, bazaar, family, etc.)
- Consider Pakistani constraints (budget, internet, power)

Write script with:
- Clear host directions in [brackets]
- [MUSIC CUE], [PAUSE], [EMPHASIS] markers
- Natural language switching

Return as JSON:
{{
    "segment_type": "{segment_type}",
    "segment_name_urdu": "{segment_config['urdu_name']}",
    "duration": "estimated time",
    "script": "Full bilingual script with natural mix",
    "urdu_phrases": ["key phrases with English translations"],
    "pakistan_references": ["local references made"],
    "key_points": ["main points covered"]
}}
"""

        return self.gemini.generate_json(prompt)

    def generate_topic_series(
        self,
        main_topic: str,
        num_episodes: int = 4
    ) -> Dict[str, Any]:
        """
        Generate a bilingual series outline for Pakistan audience.

        Args:
            main_topic: Overarching topic for the series
            num_episodes: Number of episodes in series

        Returns:
            Series outline with episode summaries
        """
        prompt = f"""
Create a {num_episodes}-episode series outline for "Bharte Chalo", Pakistan's
bilingual radio show on AI, IT, leadership, and innovation.

MAIN TOPIC: {main_topic}

PAKISTAN-FIRST APPROACH:
- Every episode must have strong Pakistani context
- Consider challenges: internet speed, power issues, dollar rates
- Highlight opportunities: freelancing, IT exports, young population
- Reference local success stories
- Make actionable for Pakistani listeners

BILINGUAL TITLES:
- Give each episode both English and Roman Urdu title
- Titles should be catchy and memorable

For each episode, provide:
1. Episode title (English + Urdu)
2. Specific focus with Pakistan angle
3. Key concepts (with Urdu explanations)
4. Local examples and stories to include
5. Guest suggestion (Pakistani expert type)
6. Teaser hook (bilingual)

Return as JSON:
{{
    "series_title": "English title",
    "series_title_urdu": "Roman Urdu title",
    "main_topic": "{main_topic}",
    "num_episodes": {num_episodes},
    "series_description": "Bilingual 2-3 sentence overview",
    "target_audience_pakistan": "Specific Pakistani audience segments",
    "episodes": [
        {{
            "episode_number": 1,
            "title": "English title",
            "title_urdu": "Roman Urdu title",
            "focus": "specific focus",
            "pakistan_angle": "how this applies to Pakistan",
            "key_concepts": [
                {{"english": "concept", "urdu_explanation": "explanation"}}
            ],
            "local_examples": ["Pakistani examples to use"],
            "suggested_guest_type": "type of Pakistani expert",
            "teaser": "bilingual promotional hook"
        }}
    ],
    "series_arc": "how series builds knowledge for Pakistani context"
}}
"""

        return self.gemini.generate_json(prompt)

    def generate_pakistan_success_story(
        self,
        story_type: str = "freelancer",
        industry: str = "tech"
    ) -> Dict[str, Any]:
        """
        Generate a Pakistani success story segment.

        Args:
            story_type: Type of success story (freelancer, startup, developer, etc.)
            industry: Industry context

        Returns:
            Success story segment script
        """
        prompt = f"""
Create a "Hamari Kahani" (Our Story) segment for Bharte Chalo radio show.

This segment celebrates Pakistani success in tech. Generate a REALISTIC but
INSPIRING story template that could represent many Pakistanis.

STORY TYPE: {story_type}
INDUSTRY: {industry}

Create a bilingual (English + Roman Urdu) script featuring:

1. INTRODUCTION (Hook the listener)
   - "Aaj ki kahani hai..." format
   - Relatable starting point (small city, modest background)

2. THE JOURNEY
   - Challenges faced (Pakistani-specific: load shedding, connectivity, family pressure)
   - Turning point (discovering tech opportunity)
   - How they learned (free resources, YouTube, etc.)

3. THE SUCCESS
   - Where they are now
   - Impact on family and community
   - Numbers that inspire (but realistic for Pakistan)

4. THE LESSON
   - Key takeaway for listeners
   - "Agar woh kar sakte hain, toh aap bhi..."
   - Specific first step to take

STYLE:
- Emotional but not melodramatic
- Honest about challenges
- Celebratory of Pakistani potential
- Natural Urdu-English mix

Return as JSON:
{{
    "segment_name": "Hamari Kahani",
    "segment_name_english": "Our Story",
    "duration": "4-5 minutes",
    "story_type": "{story_type}",
    "story_location": "Pakistani city",
    "script": "Full bilingual script",
    "key_urdu_phrases": ["emotional phrases used"],
    "challenges_shown": ["Pakistani challenges referenced"],
    "inspiration_points": ["motivational elements"],
    "call_to_action": "What listener should do"
}}
"""

        return self.gemini.generate_json(prompt)

    def generate_tech_explainer(
        self,
        tech_term: str,
        difficulty: str = "beginner"
    ) -> Dict[str, Any]:
        """
        Generate a bilingual tech explainer segment.

        Args:
            tech_term: Technology term to explain
            difficulty: Target difficulty level

        Returns:
            Tech explainer segment
        """
        prompt = f"""
Create a "Tech Samjhiye" (Understand Tech) segment for Bharte Chalo.

TERM TO EXPLAIN: {tech_term}
DIFFICULTY LEVEL: {difficulty}

Create a bilingual explanation that:

1. HOOKS with relatable scenario
   - "Kabhi socha hai..." or "Jab aap [everyday action]..."
   - Pakistani daily life example

2. EXPLAINS in layers
   - One-line Urdu definition first
   - English technical term introduced
   - Deeper explanation with Pakistani analogy
   - How it affects Pakistani listeners specifically

3. SHOWS real use
   - Example from Pakistani context
   - How Pakistani freelancers/companies use it
   - Job opportunities in Pakistan

4. MAKES IT ACTIONABLE
   - Free resource to learn more
   - Simple experiment to try
   - "5 minute mein samjho" summary

PAKISTANI ANALOGIES TO USE:
- Chai making process
- Cricket match strategy
- Bazaar/shopping dynamics
- Family WhatsApp group
- Load shedding workarounds
- Rickshaw navigation

Return as JSON:
{{
    "segment_name": "Tech Samjhiye",
    "tech_term": "{tech_term}",
    "one_line_urdu": "Simple Urdu definition",
    "duration": "3-4 minutes",
    "script": "Full bilingual script",
    "pakistani_analogy": "The main analogy used",
    "local_examples": ["Pakistani examples"],
    "learn_more": ["Free resources accessible in Pakistan"],
    "job_relevance": "How this skill helps in Pakistani job market"
}}
"""

        return self.gemini.generate_json(prompt)

    def generate_quick_segment(
        self,
        segment_name: str,
        content: str,
        duration: str = "2-3 minutes"
    ) -> Dict[str, Any]:
        """
        Generate a quick custom bilingual segment.

        Args:
            segment_name: Name of the segment
            content: What to cover
            duration: Target duration

        Returns:
            Segment script
        """
        prompt = f"""
Write a quick BILINGUAL radio segment for "Bharte Chalo" show.

SEGMENT: {segment_name}
CONTENT: {content}
DURATION: {duration}

Create an engaging script that:
- Uses natural English-Urdu mix (Roman script for Urdu)
- Is perfect for Pakistani radio listeners across all cities
- Uses simple, clear language
- Has energy, warmth, and Pakistani flavor
- Includes local references and analogies

Return as JSON:
{{
    "segment_name": "{segment_name}",
    "duration": "{duration}",
    "script": "Full bilingual script",
    "urdu_phrases": ["key phrases with English meaning"],
    "pakistan_references": ["local references made"]
}}
"""

        return self.gemini.generate_json(prompt)

    def generate_news_commentary(
        self,
        news_items: List[Dict[str, Any]],
        max_items: int = 3
    ) -> Dict[str, Any]:
        """
        Generate bilingual commentary on AI/tech news.

        Args:
            news_items: List of news items to comment on
            max_items: Maximum items to cover

        Returns:
            News commentary segment
        """
        news_summary = "\n".join([
            f"- {item.get('title', item)}: {item.get('summary', '')}"
            for item in news_items[:max_items]
        ])

        prompt = f"""
Create a bilingual "Tech Khabrain" (Tech News) segment for Bharte Chalo.

NEWS ITEMS:
{news_summary}

For each news item, provide BILINGUAL commentary:

1. HEADLINE in simple Urdu first
   - "Aaj ki bari khabar yeh hai ke..."

2. EXPLANATION
   - What happened (mix of English-Urdu)
   - Why it matters globally

3. PAKISTAN ANGLE (most important!)
   - "Ab Pakistan ke liye iska matlab..."
   - How this affects Pakistani tech workers, freelancers, startups
   - Opportunities or threats for Pakistan

4. LISTENER TAKEAWAY
   - One action they can take
   - "Aap yeh kar sakte hain..."

STYLE:
- Conversational, not formal news-anchor style
- Include personal opinion and perspective
- Connect everything to Pakistani context
- Natural language mixing

Return as JSON:
{{
    "segment_title": "Tech Khabrain",
    "segment_title_english": "Tech News",
    "duration": "5-7 minutes",
    "intro_script": "Bilingual opening for segment",
    "news_coverage": [
        {{
            "headline_urdu": "Simple Urdu headline",
            "headline_english": "English headline",
            "script": "Full bilingual commentary",
            "pakistan_impact": "Specific impact on Pakistan",
            "listener_action": "What to do with this info"
        }}
    ],
    "closing_script": "Bilingual wrap up"
}}
"""

        return self.gemini.generate_json(prompt)

    def generate_guest_interview_guide(
        self,
        guest_name: str,
        guest_background: str,
        interview_topic: str
    ) -> Dict[str, Any]:
        """
        Generate bilingual interview guide for Pakistani guest.

        Args:
            guest_name: Name of the guest
            guest_background: Guest's background/expertise
            interview_topic: Main topic to discuss

        Returns:
            Interview guide with questions and flow
        """
        prompt = f"""
Create a bilingual interview guide for "Bharte Chalo" radio show.

GUEST: {guest_name}
BACKGROUND: {guest_background}
TOPIC: {interview_topic}

Generate a BILINGUAL interview guide that:

1. GUEST INTRODUCTION (Warm, respectful, Pakistani style)
   - "Aaj hamare saath hain..."
   - Build credibility while staying humble
   - Connect guest's journey to Pakistani context

2. MAIN QUESTIONS (8-10, bilingual)
   - Mix of professional and personal
   - Questions about their Pakistani journey
   - Challenges they faced in Pakistan specifically
   - Advice for Pakistani listeners

3. PAKISTAN-SPECIFIC QUESTIONS
   - "Pakistan mein tech ka future..."
   - "Nayi generation ke liye aapka message..."
   - "Kya challenges hain aur kaise overcome karein..."

4. RAPID-FIRE (Fun, light, Pakistani flavor)
   - Favorite Pakistani food
   - Chai or coffee?
   - One Pakistani city everyone should visit
   - Parhai ke waqt ka favorite subject

5. CLOSING
   - Guest's message for Pakistani youth
   - How to connect with guest
   - Celebrate the guest's contribution

STYLE:
- Respectful but warm (Pakistani hospitality)
- Natural English-Urdu switching
- Draw out stories, not just facts
- Make guest comfortable with Urdu phrases

Return as JSON:
{{
    "guest_name": "{guest_name}",
    "segment_duration": "15-20 minutes",
    "introduction_script": "Bilingual warm intro",
    "main_questions": [
        {{
            "question": "Bilingual question",
            "purpose": "Why asking this",
            "follow_ups": ["Potential follow-ups in both languages"]
        }}
    ],
    "pakistan_specific": ["Questions about Pakistan journey/context"],
    "rapid_fire": ["Fun quick questions with Pakistani flavor"],
    "closing_script": "Bilingual thank you and celebration",
    "pre_interview_notes": "Tips for host including cultural considerations"
}}
"""

        return self.gemini.generate_json(prompt)

    def generate_listener_qa(
        self,
        questions: List[str]
    ) -> Dict[str, Any]:
        """
        Generate a listener Q&A segment.

        Args:
            questions: List of listener questions

        Returns:
            Q&A segment script
        """
        questions_text = "\n".join([f"- {q}" for q in questions])

        prompt = f"""
Create a bilingual "Aap ke Sawaal" (Your Questions) segment for Bharte Chalo.

LISTENER QUESTIONS:
{questions_text}

For each question:

1. READ THE QUESTION
   - Acknowledge the listener: "Yeh sawaal aaya hai [city] se..."
   - Read question (in whatever language it was asked)

2. ANSWER
   - Start with empathy: "Yeh bohat acha sawaal hai..."
   - Give practical answer with Pakistani context
   - Include specific resources/next steps
   - Keep it actionable

3. ENCOURAGE
   - Thank the listener
   - Invite more questions

STYLE:
- Warm and encouraging
- Practical, not preachy
- Pakistan-focused advice
- Natural bilingual mix

Return as JSON:
{{
    "segment_name": "Aap ke Sawaal",
    "segment_name_english": "Your Questions",
    "duration": "5-7 minutes",
    "intro_script": "Segment opening",
    "qa_pairs": [
        {{
            "question": "Original question",
            "listener_city": "Pakistani city (can be made up)",
            "answer_script": "Full bilingual answer",
            "resources": ["Helpful links/resources"],
            "encouragement": "Closing words for this listener"
        }}
    ],
    "closing_script": "How to send more questions"
}}
"""

        return self.gemini.generate_json(prompt)

    def format_script_markdown(self, script: Dict[str, Any]) -> str:
        """
        Format a script as readable bilingual markdown.

        Args:
            script: Script dictionary

        Returns:
            Formatted markdown string
        """
        output = []

        # Header
        output.append(f"# 🎙️ {self.show_name} (بڑھتے چلو)")
        output.append(f"## {script.get('episode_title', 'Episode Script')}")
        if script.get('episode_title_urdu'):
            output.append(f"### {script.get('episode_title_urdu')}")
        output.append("")
        output.append(f"**Tagline:** {self.tagline}")
        output.append("")
        output.append(f"**Theme:** {script.get('theme', 'N/A')} ({script.get('theme_urdu', '')})")
        output.append(f"**Topic:** {script.get('topic', 'N/A')}")
        output.append(f"**Duration:** {script.get('total_duration', 'N/A')}")
        output.append(f"**Episode Day:** {script.get('episode_day', 'N/A')}")
        output.append(f"**Language Mix:** {script.get('language_mix', 'Balanced English-Urdu')}")
        output.append(f"**Generated:** {script.get('generated_at', 'N/A')}")
        output.append("")
        output.append("---")
        output.append("")

        # Segments (90-minute format with 10 segments)
        segments = script.get("segments", {})
        segment_order = [
            "opening", "tech_samjho", "tips_tricks", "skill_career", "kahani",
            "game_segment", "tech_news", "your_questions", "global_opportunities", "conclusion"
        ]

        segment_numbers = {
            "opening": "1",
            "tech_samjho": "2",
            "tips_tricks": "3",
            "skill_career": "4",
            "kahani": "5",
            "game_segment": "6",
            "tech_news": "7",
            "your_questions": "8",
            "global_opportunities": "9",
            "conclusion": "10"
        }

        segment_display_names = {
            "opening": "AGHAZ / OPENING",
            "tech_samjho": "TECH SAMJHO / TECH FOR EVERYONE",
            "tips_tricks": "TOTKE / TIPS & TRICKS",
            "skill_career": "SKILL YA CAREER",
            "kahani": "KAHANI / STORY",
            "game_segment": "KHEL / GAME",
            "tech_news": "TECH KHABRAIN / NEWS",
            "your_questions": "AAP KE SAWAAL / YOUR QUESTIONS",
            "global_opportunities": "GLOBAL NAZAR / GLOBAL",
            "conclusion": "KHULAASA & ALVIDA / CONCLUSION"
        }

        for seg_name in segment_order:
            seg = segments.get(seg_name, {})
            if seg:
                urdu_name = seg.get('urdu_name', '')
                seg_num = segment_numbers.get(seg_name, '')
                display_name = segment_display_names.get(seg_name, seg_name.upper())
                output.append(f"## SEGMENT {seg_num}: {display_name} ({urdu_name})")
                output.append(f"*Duration: {seg.get('duration', 'N/A')}*")
                output.append("")

                if seg.get("music_cues"):
                    output.append(f"**🎵 Music Cues:** {', '.join(seg['music_cues'])}")
                    output.append("")

                # Handle rotation type segments
                if seg.get("rotation_type"):
                    output.append(f"**Rotation Type:** {seg['rotation_type']}")
                    output.append("")

                # Handle main script (for rotating segments)
                if seg.get("script") and not seg.get("subsegments"):
                    output.append(seg["script"])
                    output.append("")

                # Handle story type for kahani
                if seg.get("story_type"):
                    output.append(f"**Story Type:** {seg['story_type'].title()}")
                    output.append("")

                # Handle featured person
                if seg.get("featured_person"):
                    person = seg["featured_person"]
                    output.append(f"**Featured Person:** {person.get('name', 'N/A')} from {person.get('city', 'N/A')}")
                    if person.get("achievement"):
                        output.append(f"**Achievement:** {person['achievement']}")
                    output.append("")

                # Handle game content
                if seg.get("game_content"):
                    game = seg["game_content"]
                    output.append(f"**Game Type:** {game.get('type', 'N/A')}")
                    if game.get("items"):
                        output.append("**Items:**")
                        for item in game["items"]:
                            output.append(f"- {item}")
                    if game.get("answer"):
                        output.append(f"**Answer:** {game['answer']}")
                    if game.get("explanation"):
                        output.append(f"**Explanation:** {game['explanation']}")
                    output.append("")

                # Handle skill spotlight / career in IT
                if seg.get("skill_spotlight"):
                    skill = seg["skill_spotlight"]
                    output.append(f"### Skill Spotlight: {skill.get('featured_skill', 'N/A')}")
                    for key in ["what_is_it", "why_in_demand", "how_to_learn_free", "earning_potential", "thirty_day_challenge"]:
                        if skill.get(key):
                            output.append(f"- **{key.replace('_', ' ').title()}:** {skill[key]}")
                    output.append("")

                if seg.get("career_in_it"):
                    career = seg["career_in_it"]
                    output.append(f"### Career in IT: {career.get('featured_career', 'N/A')}")
                    for key in ["what_is_it", "day_in_life", "how_to_enter", "salary_ranges", "first_step_today"]:
                        if career.get(key):
                            output.append(f"- **{key.replace('_', ' ').title()}:** {career[key]}")
                    output.append("")

                # Handle global tech tour / rate card
                if seg.get("global_tech_tour"):
                    tour = seg["global_tech_tour"]
                    output.append(f"### Global Tech Tour: {tour.get('featured_country', 'N/A')}")
                    for key in ["tech_scene", "pakistan_lessons", "opportunities"]:
                        if tour.get(key):
                            output.append(f"- **{key.replace('_', ' ').title()}:** {tour[key]}")
                    output.append("")

                if seg.get("rate_card_jobs"):
                    jobs = seg["rate_card_jobs"]
                    output.append("### Rate Card + Job Board")
                    if jobs.get("rate_card"):
                        output.append(f"**Rate Card:** {jobs['rate_card']}")
                    if jobs.get("job_board"):
                        output.append("**Job Board:**")
                        for job in jobs["job_board"]:
                            if isinstance(job, dict):
                                output.append(f"- **{job.get('title', 'N/A')}** at {job.get('company', 'N/A')}")
                                output.append(f"  - Salary: {job.get('salary', 'N/A')}")
                                output.append(f"  - Apply: {job.get('how_to_apply', 'N/A')}")
                    if jobs.get("application_tips"):
                        output.append(f"**Application Tips:** {jobs['application_tips']}")
                    output.append("")

                # Handle sub-segments
                subsegments = seg.get("subsegments", {})
                if subsegments:
                    subseg_num = 1
                    for subseg_key, subseg in subsegments.items():
                        if isinstance(subseg, dict):
                            subseg_name = subseg.get('name', subseg_key.replace('_', ' ').title())
                            subseg_urdu = subseg.get('urdu_name', '')
                            subseg_duration = subseg.get('duration', '')

                            output.append(f"### {seg_num}.{subseg_num} {subseg_name} ({subseg_urdu})")
                            if subseg_duration:
                                output.append(f"*Duration: {subseg_duration}*")
                            output.append("")

                            # Output question info for Q&A segment
                            if subseg.get("listener_name") and subseg.get("listener_city"):
                                output.append(f"**From:** {subseg['listener_name']} from {subseg['listener_city']}")
                            if subseg.get("question"):
                                output.append(f"**Question:** {subseg['question']}")
                                output.append("")

                            # Output the script
                            if subseg.get("script"):
                                output.append(subseg["script"])
                                output.append("")

                            # Output featured items
                            if subseg.get("featured_person"):
                                person = subseg["featured_person"]
                                output.append(f"**Featured:** {person.get('name', 'N/A')} from {person.get('city', 'N/A')}")
                                output.append("")

                            if subseg.get("featured_tool"):
                                tool = subseg["featured_tool"]
                                output.append(f"**Featured Tool:** {tool.get('name', 'N/A')} - {tool.get('free_paid', '')} - Rating: {tool.get('rating', 'N/A')}")
                                output.append("")

                            if subseg.get("news_items"):
                                output.append("**News Items:**")
                                for item in subseg["news_items"]:
                                    if isinstance(item, dict):
                                        output.append(f"- **{item.get('headline', '')}** [{item.get('category', '')}]")
                                        if item.get('pakistan_relevance'):
                                            output.append(f"  - Pakistan Relevance: {item['pakistan_relevance']}")
                                output.append("")

                            if subseg.get("takeaways"):
                                output.append("**Key Takeaways:**")
                                for takeaway in subseg["takeaways"]:
                                    output.append(f"- {takeaway}")
                                output.append("")

                            if subseg.get("challenge"):
                                output.append(f"**Challenge:** {subseg['challenge']}")
                                if subseg.get("hashtag"):
                                    output.append(f"**Hashtag:** {subseg['hashtag']}")
                                output.append("")

                            if subseg.get("problem") and subseg.get("solution"):
                                output.append(f"**Problem:** {subseg['problem']}")
                                output.append(f"**Solution:** {subseg['solution']}")
                                output.append("")

                            if subseg.get("next_episode_teaser"):
                                output.append(f"**Next Episode:** {subseg['next_episode_teaser']}")
                                output.append("")

                            subseg_num += 1

                output.append("---")
                output.append("")

        # Technical terms explained
        if script.get("technical_terms_explained"):
            output.append("## 📚 Technical Terms Explained")
            for term in script["technical_terms_explained"]:
                if isinstance(term, dict):
                    output.append(f"- **{term.get('term', '')}**: {term.get('urdu_explanation', '')}")
                else:
                    output.append(f"- {term}")
            output.append("")

        # Pakistan references
        if script.get("pakistan_references"):
            output.append("## 🇵🇰 Pakistan References Used")
            for ref in script["pakistan_references"]:
                output.append(f"- {ref}")
            output.append("")

        # Urdu phrases
        if script.get("key_phrases_urdu"):
            output.append("## 🗣️ Key Urdu Phrases")
            for phrase in script["key_phrases_urdu"]:
                output.append(f"- {phrase}")
            output.append("")

        # Quotable moments
        if script.get("quotable_moments"):
            output.append("## 💬 Quotable Moments")
            for quote in script["quotable_moments"]:
                output.append(f"> {quote}")
                output.append("")

        # Resources
        if script.get("resources_mentioned"):
            output.append("## 📖 Resources Mentioned")
            for resource in script["resources_mentioned"]:
                output.append(f"- {resource}")
            output.append("")

        # Listener engagement
        if script.get("listener_engagement"):
            engagement = script["listener_engagement"]
            output.append("## 🎯 Listener Engagement")
            if engagement.get("challenge_of_week"):
                output.append(f"**Challenge of the Week:** {engagement['challenge_of_week']}")
            if engagement.get("social_hashtag"):
                output.append(f"**Hashtag:** {engagement['social_hashtag']}")
            if engagement.get("questions_to_ask"):
                output.append("**Questions to Collect:**")
                for q in engagement["questions_to_ask"]:
                    output.append(f"- {q}")
            output.append("")

        # Footer
        output.append("---")
        output.append(f"*{self.show_name} - {self.tagline}*")
        output.append("*Bharte Chalo, Seekhte Raho, Aagey Barhte Raho!*")

        return "\n".join(output)
