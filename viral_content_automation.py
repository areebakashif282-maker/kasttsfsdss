#!/usr/bin/env python3
"""
🚀 VIRAL CONTENT AUTOMATION SYSTEM
Automatically generates: Titles → Outlines → Full Scripts

Author: AI Automation System
Version: 1.0
"""

import os
import json
from datetime import datetime
from typing import List, Dict
import anthropic

# ============================================================================
# CONFIGURATION
# ============================================================================

# Add your Anthropic API key here
API_KEY = "your-api-key-here"  # ⚠️ REPLACE THIS WITH YOUR ACTUAL API KEY

# Output directory structure
OUTPUT_DIR = "viral_content_output"
TITLES_DIR = os.path.join(OUTPUT_DIR, "1_titles")
OUTLINES_DIR = os.path.join(OUTPUT_DIR, "2_outlines")
SCRIPTS_DIR = os.path.join(OUTPUT_DIR, "3_scripts")

# ============================================================================
# PROMPTS
# ============================================================================

TITLE_GENERATION_PROMPT = """🚀 READY-TO-USE VIRAL TITLE GENERATOR PROMPT (COPY PASTE BELOW)
OBJECTIVE:
 You are an expert YouTube political title strategist.
 Your job is to analyze the competitor titles I provide and generate new, highly clickable, FOMO-driven, non-generic, emotionally charged political titles in the exact structure, rhythm, and style as my competitors — and every title MUST end with "— Kamala Harris".
Match the following competitor triggers:
"Most People Don't Realise…"
"Most People Have NO IDEA…"
"You Won't Believe…"
"Nobody Saw This Coming…"
Breaking news tone
Shock, urgency, curiosity gap
Trump, Supreme Court, Congress, scandals
High CTR emotional style
Same format, NOT copied

INPUT INSTRUCTIONS:
7 competitor titles.
Most People Don't Realise What Marjorie Taylor Greene Just Did To Donald Trump — Kamala Harris
 Most People Don't Know Trump's Tariffs Just Took a MASSIVE Hit in the Supreme Court — Kamala Harris
Most People Have NO IDEA What Trump Just Did To SNAP Benefits, He's a Disgrace! — Kamala Harris
 Most People Don't Realize What Trump Just Did To BLOCK Mamdani — Kamala Harris
 Most People Don't Realise What Supreme Court Justice Did To Donald Trump — Kamala Harris
 Most People Have NO IDEA What Trump Just Unveiled — Kamala Harris
 You Won't Believe What Chuck Schumer Just Did To The Government Shutdown — Kamala Harris

 Analyze:
Hook structure
Emotional triggers
Placement of political figures
Word patterns
Shock factor
Topic direction
 Then create new titles in the same style.

OUTPUT INSTRUCTIONS:
Produce 10 new viral political titles that:
 ✔ Match competitor emotional style
 ✔ Use FOMO, shock, urgency
 ✔ Are NOT generic
 ✔ Sound like real breaking news
 ✔ Fit U.S. political drama niche
 ✔ Follow the competitor cadence
 ✔ End with "— Kamala Harris"
 ✔ No explanation — just titles

FORMAT:
OUTPUT:
 10 viral titles
 Each must end with: — Kamala Harris"""

OUTLINE_GENERATION_PROMPT = """OBJECTIVE:
 You are an expert political script strategist who writes long-form, high-retention YouTube scripts in the style of authoritative, moral-voice U.S. political commentators (the "Kamala Harris" style competitor). Your task is to create a 5000-word script outline divided into up to 10 logical sections. Each section must include: section name, exact word allocation, a 1–2 sentence summary of the section, and a 1-line transition instruction describing how to move smoothly to the next section. The outlines must reflect the competitor's tone: authoritative, morally urgent, empathetic to victims, legally/constitutionally informed, and designed to trigger FOMO/engagement. Use contrast framing throughout (e.g., "what was vs what is", "promise vs reality", "authority vs accountability").
INPUT INSTRUCTIONS (what I will give you):
 I will provide only one input: the video title (single line). Do not ask for anything else.
CONSTRAINTS / RULES:
The total words across all sections must be exactly 5000 words (sum of the per-section allocations = 5000).
The outline must contain between 8 and 10 sections (you decide exact number for best logical flow).
Provide section names that are action/impact oriented (e.g., "Hook: The Hidden Threat — 250 words").
For each section include:
Section name
Word allocation (integer, e.g., 620 words)
Short summary (1–2 sentences; what to write in that section)
Transition cue (one short sentence explaining how to bridge to the next section)
Include contrast framing at least once in every section summary (show the contrast that will be written about).
Match the competitor audience profile: politically engaged, left-leaning/moderate, age 25–54, motivated by rule-of-law & social justice. Explicitly state the audience focus line at the top of the outline.
Keep section lengths realistic — vary short punchy sections (50–200 words) and deep analytical sections (400–900 words) so the reader/viewer pacing mirrors competitor style.
Make transitions logical and lead the viewer step-by-step to a mobilizing CTA in the final section (organize, call reps, vote, donate, comment).
Output only the outline (no full script text). Do not write the 5000-word full script here — only the section-by-section blueprint.

OUTPUT FORMAT (exactly):
 Start with a one-line Audience Focus description. Then list the sections numbered 1..N (N = 8–10) in this exact pattern:
Audience Focus: [one-line audience description]

1) Section Title — [XXX words]
Summary: [1–2 sentence summary; include contrast framing]
Transition: [one short sentence telling how to move to Section 2]

2) Section Title — [XXX words]
Summary: ...
Transition: ...

...
N) Section Title — [XXX words]
Summary: ...
Transition/CTA: [one short sentence that ends with the exact mobilizing call to action to be expanded in the full script]

ADDITIONAL NOTES FOR THE OUTLINE:
Ensure the first section is a strong 8–12 second hook equivalent (allocate enough words to craft a high-impact opening).
Include a section that translates legal/judicial details into simple, shareable lines (one-liners for thumbnails).
Include at least one human vignette section (real-person empathy anchor).
Reserve the last section for a practical mobilization plan + direct CTAs (phone scripts, tweet copy, comment prompt).
Tag places where on-screen text / B-roll should be inserted (as short parenthetical cues in the section summaries).
Maintain moral-authority voice and psychological triggers (surprise, injustice, urgency) across summaries.

Now WAIT FOR INPUT:
 When I paste the video title, generate the outline per above immediately."""

SCRIPT_GENERATION_PROMPT = """OBJECTIVE:
 You are an expert political scriptwriter who writes long-form, emotionally resonant, high-retention YouTube scripts in the authoritative narrative style of U.S. political commentary channels (the "Kamala Harris voice" competitor style).
 Your task is to take the outline I provide and expand it into a fully polished, 5000-word script following the emotional, structural, psychological, and stylistic patterns of my top-performing competitors.

INPUT (What I Will Provide):
I will paste the entire outline generated from Prompt #1.
 The outline will include:
Section titles
Word allocations
Section summaries
Transition cues
Total words = 5000
You must follow it exactly.

EXPANSION RULES (MUST FOLLOW):
1. Follow the outline EXACTLY
Each section must match the word allocation you see in the outline (±3% maximum).
Always follow the summary + transition cue.

2. Match Competitor Tone & Voice
The script must use the following competitor traits:
Moral authority (prosecutor/AG/VP tone)
Constitutional clarity (simple legal explanations)
Emotional urgency + empathy for vulnerable people
Contrast framing (what America should be vs what is happening)
High-stakes political storytelling
Authoritative "protector of democracy" narrative

3. Use High Retention YouTube Pacing
Include:
Strong hooks
Short punchy lines
Emotional metaphors
Human stories
Rhetorical questions
Repetition for emphasis
Build-up → release → reveal cycle
Mini-cliffhangers inside long sections

5. Human-Centric Storytelling
Every major policy or legal explanation must be tied back to:
seniors
working families
disabled citizens
single mothers
real Americans affected by the decision

6. Use Competitor-Style Rhetorical Framework
The script must include:
"Here's the truth…"
"Let me be very clear…"
"This isn't politics — this is about people."
"This is the moment where…"
"Imagine for a moment…"
"And that's the part they don't want you to see."

7. Final CTA Format
Always end with a powerful mobilizing call:
"If you care about protecting democracy, type I'M IN in the comments and share this video today."

OUTPUT FORMAT (Required):
Write the final script exactly like this:
Use section headers
Maintain word allocations
Provide polished, ready-to-record narration
Include CTA lines and emotional cues
No outline — full script only
Each section must be written as natural spoken narration, not bullet points.

📌 IMPORTANT:
Do NOT shorten the script.
 Do NOT combine sections.
 Do NOT omit emotional beats.
 Do NOT ignore the competitor voice.
 This script must feel like it could replace their most viral video.

🚀 NOW WAIT FOR INPUT
When I paste the outline, generate the full 5000-word script."""


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def setup_directories():
    """Create output directory structure"""
    for directory in [OUTPUT_DIR, TITLES_DIR, OUTLINES_DIR, SCRIPTS_DIR]:
        os.makedirs(directory, exist_ok=True)
    print(f"✅ Output directories created: {OUTPUT_DIR}/")


def save_to_file(content: str, directory: str, filename: str) -> str:
    """Save content to file and return full path"""
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return filepath


def call_claude_api(prompt: str, user_message: str, max_tokens: int = 4000) -> str:
    """
    Call Claude API with system prompt and user message
    
    Args:
        prompt: System prompt
        user_message: User input
        max_tokens: Maximum tokens for response
    
    Returns:
        API response text
    """
    try:
        client = anthropic.Anthropic(api_key=API_KEY)
        
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=max_tokens,
            system=prompt,
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        
        return message.content[0].text
    
    except Exception as e:
        print(f"❌ API Error: {str(e)}")
        return None


# ============================================================================
# MAIN AUTOMATION FUNCTIONS
# ============================================================================

def generate_titles(topic: str = None) -> List[str]:
    """
    Step 1: Generate 10 viral titles
    
    Args:
        topic: Optional specific topic/theme for titles
    
    Returns:
        List of 10 generated titles
    """
    print("\n" + "="*60)
    print("📝 STEP 1: GENERATING VIRAL TITLES")
    print("="*60)
    
    # If no topic provided, use default prompt
    if topic:
        user_message = f"Generate titles related to this topic/event: {topic}"
    else:
        user_message = "Generate 10 new viral political titles following the competitor style."
    
    print(f"🔄 Calling API...")
    response = call_claude_api(TITLE_GENERATION_PROMPT, user_message, max_tokens=2000)
    
    if not response:
        print("❌ Failed to generate titles")
        return []
    
    # Parse titles from response
    titles = [line.strip() for line in response.split('\n') if line.strip() and '—' in line]
    
    # Save titles to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"titles_{timestamp}.txt"
    filepath = save_to_file(response, TITLES_DIR, filename)
    
    print(f"✅ Generated {len(titles)} titles")
    print(f"💾 Saved to: {filepath}")
    print("\n📋 Generated Titles:")
    for i, title in enumerate(titles, 1):
        print(f"   {i}. {title}")
    
    return titles


def generate_outline(title: str) -> str:
    """
    Step 2: Generate outline from selected title
    
    Args:
        title: The video title
    
    Returns:
        Generated outline text
    """
    print("\n" + "="*60)
    print("📐 STEP 2: GENERATING OUTLINE")
    print("="*60)
    print(f"Title: {title}")
    
    user_message = f"Video Title:\n{title}"
    
    print(f"🔄 Calling API (this may take 30-60 seconds)...")
    response = call_claude_api(OUTLINE_GENERATION_PROMPT, user_message, max_tokens=4000)
    
    if not response:
        print("❌ Failed to generate outline")
        return None
    
    # Save outline to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_title = "".join(c for c in title[:50] if c.isalnum() or c in (' ', '-', '_')).strip()
    filename = f"outline_{timestamp}_{safe_title}.txt"
    filepath = save_to_file(response, OUTLINES_DIR, filename)
    
    print(f"✅ Outline generated successfully")
    print(f"💾 Saved to: {filepath}")
    
    return response


def generate_script(outline: str, title: str) -> str:
    """
    Step 3: Generate full 5000-word script from outline
    
    Args:
        outline: The generated outline
        title: The video title (for filename)
    
    Returns:
        Generated script text
    """
    print("\n" + "="*60)
    print("📜 STEP 3: GENERATING FULL SCRIPT")
    print("="*60)
    
    user_message = f"Here is the outline to expand:\n\n{outline}"
    
    print(f"🔄 Calling API (this may take 60-90 seconds)...")
    response = call_claude_api(SCRIPT_GENERATION_PROMPT, user_message, max_tokens=8000)
    
    if not response:
        print("❌ Failed to generate script")
        return None
    
    # Save script to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_title = "".join(c for c in title[:50] if c.isalnum() or c in (' ', '-', '_')).strip()
    filename = f"script_{timestamp}_{safe_title}.txt"
    filepath = save_to_file(response, SCRIPTS_DIR, filename)
    
    # Count words
    word_count = len(response.split())
    
    print(f"✅ Script generated successfully")
    print(f"📊 Word count: {word_count}")
    print(f"💾 Saved to: {filepath}")
    
    return response


# ============================================================================
# MAIN WORKFLOW
# ============================================================================

def run_full_automation(topic: str = None, title_index: int = None):
    """
    Run complete automation workflow: Titles → Outline → Script
    
    Args:
        topic: Optional topic for title generation
        title_index: If provided, use this title index (1-10), otherwise prompt user
    """
    print("\n" + "="*80)
    print("🚀 VIRAL CONTENT AUTOMATION SYSTEM")
    print("="*80)
    print("This will generate: Titles → Outline → Full Script")
    print("Estimated time: 3-5 minutes")
    print("="*80)
    
    # Setup directories
    setup_directories()
    
    # Step 1: Generate Titles
    titles = generate_titles(topic)
    if not titles:
        print("\n❌ Automation stopped: Could not generate titles")
        return
    
    # Step 2: Select Title
    if title_index and 1 <= title_index <= len(titles):
        selected_index = title_index - 1
        print(f"\n✅ Auto-selected title #{title_index}")
    else:
        print("\n" + "-"*60)
        print("📌 SELECT A TITLE")
        print("-"*60)
        while True:
            try:
                choice = input(f"Enter title number (1-{len(titles)}): ").strip()
                selected_index = int(choice) - 1
                if 0 <= selected_index < len(titles):
                    break
                print(f"❌ Please enter a number between 1 and {len(titles)}")
            except ValueError:
                print("❌ Please enter a valid number")
    
    selected_title = titles[selected_index]
    print(f"✅ Selected: {selected_title}")
    
    # Step 3: Generate Outline
    outline = generate_outline(selected_title)
    if not outline:
        print("\n❌ Automation stopped: Could not generate outline")
        return
    
    # Step 4: Generate Script
    script = generate_script(outline, selected_title)
    if not script:
        print("\n❌ Automation stopped: Could not generate script")
        return
    
    # Final Summary
    print("\n" + "="*80)
    print("🎉 AUTOMATION COMPLETE!")
    print("="*80)
    print(f"📁 All files saved in: {OUTPUT_DIR}/")
    print(f"   • Titles: {TITLES_DIR}/")
    print(f"   • Outline: {OUTLINES_DIR}/")
    print(f"   • Script: {SCRIPTS_DIR}/")
    print("="*80)


def batch_process(topic: str = None, count: int = 3):
    """
    Generate multiple complete workflows (titles → outlines → scripts)
    
    Args:
        topic: Optional topic for title generation
        count: Number of complete workflows to generate
    """
    print(f"\n🔄 BATCH MODE: Generating {count} complete workflows")
    
    for i in range(count):
        print(f"\n{'='*80}")
        print(f"🔄 BATCH {i+1}/{count}")
        print(f"{'='*80}")
        run_full_automation(topic=topic, title_index=1)  # Auto-select first title


# ============================================================================
# CLI INTERFACE
# ============================================================================

def main():
    """Main CLI interface"""
    print("\n" + "="*80)
    print("🚀 VIRAL CONTENT AUTOMATION SYSTEM")
    print("="*80)
    print("Choose mode:")
    print("1. Single workflow (Titles → Outline → Script)")
    print("2. Batch mode (Generate multiple complete workflows)")
    print("3. Titles only")
    print("4. Outline from custom title")
    print("5. Script from custom outline")
    print("="*80)
    
    choice = input("\nEnter choice (1-5): ").strip()
    
    if choice == "1":
        topic = input("\nEnter topic/theme (or press Enter for default): ").strip() or None
        run_full_automation(topic=topic)
    
    elif choice == "2":
        topic = input("\nEnter topic/theme (or press Enter for default): ").strip() or None
        count = input("How many workflows to generate? (default: 3): ").strip()
        count = int(count) if count.isdigit() else 3
        batch_process(topic=topic, count=count)
    
    elif choice == "3":
        topic = input("\nEnter topic/theme (or press Enter for default): ").strip() or None
        setup_directories()
        generate_titles(topic=topic)
    
    elif choice == "4":
        setup_directories()
        title = input("\nEnter video title: ").strip()
        if title:
            generate_outline(title)
    
    elif choice == "5":
        setup_directories()
        print("\nPaste outline (press Enter, then Ctrl+D when done):")
        import sys
        outline = sys.stdin.read()
        title = input("\nEnter title for filename: ").strip() or "custom"
        generate_script(outline, title)
    
    else:
        print("❌ Invalid choice")


if __name__ == "__main__":
    # Check if API key is set
    if API_KEY == "your-api-key-here":
        print("\n⚠️  WARNING: Please set your Anthropic API key in the script!")
        print("Edit line 22: API_KEY = 'your-actual-api-key'")
        print("\nGet your API key from: https://console.anthropic.com/")
    else:
        main()
