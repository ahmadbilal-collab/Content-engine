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

    # Show segments configuration
    SEGMENTS = {
        "opening": {
            "duration": "2-3 minutes",
            "purpose": "Hook listeners, set energy, introduce topic",
            "urdu_name": "Aghaz"
        },
        "tech_spotlight": {
            "duration": "5-7 minutes",
            "purpose": "Deep dive into one AI/IT concept or tool",
            "urdu_name": "Tech ki Duniya"
        },
        "leadership_lens": {
            "duration": "4-5 minutes",
            "purpose": "Leadership insight connected to tech topic",
            "urdu_name": "Leadership ka Sabaq"
        },
        "pakistan_perspective": {
            "duration": "3-4 minutes",
            "purpose": "Local context, opportunities, success stories",
            "urdu_name": "Hamara Pakistan"
        },
        "action_steps": {
            "duration": "3-4 minutes",
            "purpose": "Practical takeaways listeners can apply today",
            "urdu_name": "Aaj Hi Karein"
        },
        "closing": {
            "duration": "2-3 minutes",
            "purpose": "Inspire, preview next episode, call to action",
            "urdu_name": "Alvida"
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
GENERATE SCRIPT WITH THESE SEGMENTS
═══════════════════════════════════════════════════════════════════

1. AGHAZ / OPENING (2-3 minutes)
   - Start with energetic "Assalam-u-Alaikum!"
   - Show signature and tagline
   - Hook with relatable Pakistani scenario
   - Introduce topic with "Aaj hum baat karenge..."
   - Why this matters: "Yeh aapke liye kyun zaroori hai..."

2. TECH KI DUNIYA / TECH SPOTLIGHT (5-7 minutes)
   - Explain concept in simple Urdu first, then English terms
   - Use Pakistani analogies: "Jaise chai ki tapri pe...", "Jaise Sunday bazaar mein..."
   - Real examples from Pakistani context
   - Break jargon: "Machine Learning, yaani computer ko seekhna sikhaana"

3. LEADERSHIP KA SABAQ / LEADERSHIP LENS (4-5 minutes)
   - Connect to Pakistani leadership context
   - Reference Pakistani business leaders' mindset
   - Decision frameworks for our culture
   - "Ek acha leader kaise sochta hai..."

4. HAMARA PAKISTAN / PAKISTAN PERSPECTIVE (3-4 minutes)
   - Specific opportunities in Pakistan
   - Success stories: "Ek bhai Faisalabad se..."
   - Challenges we face honestly: "Haan, mushkilaat hain, lekin..."
   - Call to build Pakistan through tech

5. AAJ HI KAREIN / ACTION STEPS (3-4 minutes)
   - 3 specific actions in Urdu/English mix
   - Free resources (consider Pakistani internet/budget constraints)
   - Small experiments: "Aaj raat try karein..."
   - Accountability: "Apne aap se waada karein..."

6. ALVIDA / CLOSING (2-3 minutes)
   - Key takeaway in one Urdu sentence
   - Motivational close: "Yaad rakhein, Pakistan ka mustaqbil..."
   - Call to action: Share, subscribe
   - Signature sign-off: "Bharte chalo, seekhte raho, aagey barhte raho!"
   - "Allah Hafiz, phir milenge!"

═══════════════════════════════════════════════════════════════════
OUTPUT FORMAT
═══════════════════════════════════════════════════════════════════

Return as JSON:
{{
    "episode_title": "Catchy bilingual title",
    "episode_title_urdu": "Title in Roman Urdu",
    "episode_number": {episode_number or "null"},
    "theme": "{theme}",
    "theme_urdu": "{urdu_theme}",
    "topic": "{topic}",
    "total_duration": "20-25 minutes",
    "language_mix": "{language_balance}",
    "segments": {{
        "opening": {{
            "urdu_name": "Aghaz",
            "duration": "2-3 minutes",
            "script": "Full bilingual script with natural English-Urdu mix",
            "music_cues": ["Energetic Pakistani-fusion intro music", "fade under"],
            "key_urdu_phrases": ["phrases used"]
        }},
        "tech_spotlight": {{
            "urdu_name": "Tech ki Duniya",
            "duration": "5-7 minutes",
            "script": "Full bilingual script",
            "music_cues": [],
            "key_urdu_phrases": []
        }},
        "leadership_lens": {{
            "urdu_name": "Leadership ka Sabaq",
            "duration": "4-5 minutes",
            "script": "Full bilingual script",
            "music_cues": [],
            "key_urdu_phrases": []
        }},
        "pakistan_perspective": {{
            "urdu_name": "Hamara Pakistan",
            "duration": "3-4 minutes",
            "script": "Full bilingual script",
            "music_cues": ["Soft patriotic music under"],
            "key_urdu_phrases": []
        }},
        "action_steps": {{
            "urdu_name": "Aaj Hi Karein",
            "duration": "3-4 minutes",
            "script": "Full bilingual script",
            "music_cues": [],
            "key_urdu_phrases": []
        }},
        "closing": {{
            "urdu_name": "Alvida",
            "duration": "2-3 minutes",
            "script": "Full bilingual script",
            "music_cues": ["Show theme music swells", "fade out"],
            "key_urdu_phrases": []
        }}
    }},
    "key_phrases_urdu": ["All memorable Urdu phrases with translations"],
    "technical_terms_explained": [
        {{"term": "AI", "urdu_explanation": "Computer ko insaan ki tarah sochna"}}
    ],
    "pakistan_references": ["All Pakistan-specific examples used"],
    "quotable_moments": ["Tweetable bilingual quotes"],
    "resources_mentioned": ["Resources considering Pakistani access/budget"]
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
        output.append(f"**Language Mix:** {script.get('language_mix', 'Balanced English-Urdu')}")
        output.append(f"**Generated:** {script.get('generated_at', 'N/A')}")
        output.append("")
        output.append("---")
        output.append("")

        # Segments
        segments = script.get("segments", {})
        segment_order = [
            "opening", "tech_spotlight", "leadership_lens",
            "pakistan_perspective", "action_steps", "closing"
        ]

        for seg_name in segment_order:
            seg = segments.get(seg_name, {})
            if seg:
                urdu_name = seg.get('urdu_name', '')
                output.append(f"## {seg_name.upper().replace('_', ' ')} ({urdu_name})")
                output.append(f"*Duration: {seg.get('duration', 'N/A')}*")
                output.append("")

                if seg.get("music_cues"):
                    output.append(f"**🎵 Music Cues:** {', '.join(seg['music_cues'])}")
                    output.append("")

                if seg.get("key_urdu_phrases"):
                    output.append(f"**Key Urdu Phrases:** {', '.join(seg['key_urdu_phrases'])}")
                    output.append("")

                output.append("### Script")
                output.append("")
                output.append(seg.get("script", ""))
                output.append("")
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

        # Footer
        output.append("---")
        output.append(f"*{self.show_name} - {self.tagline}*")
        output.append("*Bharte Chalo, Seekhte Raho, Aagey Barhte Raho!*")

        return "\n".join(output)
