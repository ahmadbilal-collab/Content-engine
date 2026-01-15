# Bharte Chalo - Reference Data

This directory contains reference data, templates, and examples for the Bharte Chalo radio show content generation agent.

## Directory Structure

```
reference_data/
├── csv/                          # CSV databases
│   ├── pakistani_tech_analogies.csv    # Tech concepts with Pakistani analogies
│   ├── urdu_phrases_by_context.csv     # Urdu phrases organized by usage context
│   ├── skills_rotation.csv             # 12-week skill rotation with resources
│   ├── careers_rotation.csv            # 12-week career rotation with salaries
│   ├── example_stories_template.csv    # Story structure examples
│   ├── tips_and_tricks.csv             # Mobile, computer, hardware tips
│   ├── tech_myths.csv                  # Common tech myths to bust
│   ├── tech_trivia.csv                 # Trivia questions with answers
│   ├── hot_takes.csv                   # Controversial opinions with reasoning
│   ├── listener_questions_examples.csv # Example Q&A content
│   ├── global_tech_tour_countries.csv  # Countries for global segment
│   └── sach_ya_jhoot_facts.csv         # True/false facts for game
│
├── templates/                    # Templates and guides
│   ├── episode_script_template.md      # Full episode script template
│   ├── research_sources.txt            # List of research sources
│   └── style_guide_quick_ref.txt       # Quick style reference
│
└── examples/                     # Example content (to be added)
    └── (sample episodes, scripts)
```

## CSV Files Description

### pakistani_tech_analogies.csv
- **Purpose:** Translate tech concepts into Pakistani daily life analogies
- **Columns:** tech_term, english_meaning, urdu_analogy, roman_urdu, context_example
- **Usage:** Use when explaining technical concepts simply

### urdu_phrases_by_context.csv
- **Purpose:** Provide appropriate Urdu phrases for different situations
- **Columns:** context, urdu_phrase, roman_urdu, english_translation, when_to_use
- **Usage:** Select phrases based on the segment/mood

### skills_rotation.csv
- **Purpose:** 12-week skill spotlight content guide
- **Columns:** week, skill_name, urdu_name, category, difficulty, free_learning_resources, youtube_channels, earning_potential_pkr_monthly, earning_potential_usd_hourly, thirty_day_challenge, pakistan_demand, tools_needed
- **Usage:** Reference for Tuesday Skill Spotlight segment

### careers_rotation.csv
- **Purpose:** 12-week career focus content guide
- **Columns:** week, career_name, urdu_name, category, entry_salary_pkr, mid_salary_pkr, senior_salary_pkr, remote_usd_yearly, required_skills, education_needed, certifications_helpful, day_in_life, first_step_today, pakistan_companies_hiring, growth_outlook
- **Usage:** Reference for Friday Career in IT segment

### example_stories_template.csv
- **Purpose:** Story structure examples for Kahani segment
- **Columns:** story_type, person_name, city, background, starting_point, challenge_1, challenge_2, turning_point, current_achievement, lesson_1, lesson_2, lesson_3, advice_quote, category
- **Usage:** Template for structuring success/failure stories

### tips_and_tricks.csv
- **Purpose:** Ready-to-use tips content
- **Columns:** category, tip_title, urdu_title, problem_it_solves, step_by_step, why_it_works, pakistan_context, tools_needed, difficulty
- **Usage:** Source material for Tips & Tricks segment

### tech_myths.csv
- **Purpose:** Common tech myths with debunking
- **Columns:** myth_urdu, myth_english, truth_urdu, truth_english, explanation, source_type, common_belief_percentage
- **Usage:** Content for Tech Myth Busters game segment

### tech_trivia.csv
- **Purpose:** Trivia questions for game segment
- **Columns:** question_urdu, question_english, answer, options_if_mcq, fun_fact, difficulty, category
- **Usage:** Content for Tech Trivia game segment

### hot_takes.csv
- **Purpose:** Controversial opinions with reasoning
- **Columns:** hot_take_urdu, hot_take_english, reasoning, counter_argument, conclusion, controversy_level, category
- **Usage:** Content for Hot Take game segment

### listener_questions_examples.csv
- **Purpose:** Example Q&A content
- **Columns:** question_urdu, question_english, listener_name, listener_city, category, answer_key_points, resources_to_mention, difficulty_level
- **Usage:** Reference for Q&A segment structure

### global_tech_tour_countries.csv
- **Purpose:** Country profiles for Global Tech Tour
- **Columns:** country, urdu_name, tech_strength, key_initiatives, what_pakistan_can_learn, opportunities_for_pakistanis, visa_options, notable_companies, fun_fact
- **Usage:** Content for Tuesday Global Tech Tour segment

### sach_ya_jhoot_facts.csv
- **Purpose:** Facts for Sach ya Jhoot game
- **Columns:** fact_urdu, fact_english, is_true, explanation, source, surprise_level
- **Usage:** Content for Sach ya Jhoot game segment

## How to Use This Reference Data

### For the Agent:
1. Load relevant CSV files based on the segment being generated
2. Use analogies.csv when explaining technical concepts
3. Use phrases.csv for appropriate bilingual expressions
4. Reference skill/career rotation based on episode week number
5. Use story templates as structural guide (not copy)
6. Verify all current data through live research - CSVs are templates only

### Important Notes:
- CSV data provides STRUCTURE and EXAMPLES, not live statistics
- All salary figures, user counts, and time-sensitive data must be researched fresh
- Stories can be used as templates - adapt or create new based on research
- Tips and myths should be verified for current accuracy
- Always add Pakistan-specific context when using any reference

## Updating This Data

- Add new analogies as tech evolves
- Update skill/career rotations quarterly
- Add new stories as they are researched
- Refresh tips based on OS/app updates
- Add new trivia and myths regularly
