# ⚡ Quick Start Guide - 5 Minutes Setup

Sirf 5 minutes mein automation start karein!

---

## 🎯 Step-by-Step Setup

### **1️⃣ Install Python** (agar nahi hai)
```bash
# Check Python version
python --version
# Should be 3.7 or higher

# If not installed, download from:
# https://www.python.org/downloads/
```

---

### **2️⃣ Download Files**
Teen files download karein:
1. `viral_content_automation.py` (main script)
2. `requirements.txt` (dependencies)
3. `README.md` (documentation)

---

### **3️⃣ Install Dependencies**
```bash
# Terminal/Command Prompt mein run karein:
pip install -r requirements.txt

# Ya direct:
pip install anthropic
```

---

### **4️⃣ Get API Key**

1. Visit: **https://console.anthropic.com/**
2. Sign up (free tier available)
3. Go to "API Keys" section
4. Click "Create Key"
5. Copy your API key

**Free Tier:**
- $5 free credit
- ~35 complete workflows free
- Credit card optional

---

### **5️⃣ Add API Key to Script**

**Option A: Edit Script File**
```python
# Open viral_content_automation.py
# Find line 22:
API_KEY = "your-api-key-here"

# Replace with:
API_KEY = "sk-ant-api03-xxxxx..."  # Your actual key
```

**Option B: Use Environment Variable** (Advanced)
```bash
# On Mac/Linux:
export ANTHROPIC_API_KEY="sk-ant-api03-xxxxx..."

# On Windows:
set ANTHROPIC_API_KEY=sk-ant-api03-xxxxx...

# Then update script line 22:
API_KEY = os.environ.get("ANTHROPIC_API_KEY", "your-api-key-here")
```

---

### **6️⃣ Run Script**
```bash
python viral_content_automation.py
```

---

## 🎮 First Run - Complete Workflow

```bash
$ python viral_content_automation.py

🚀 VIRAL CONTENT AUTOMATION SYSTEM
================================================================================
Choose mode:
1. Single workflow (Titles → Outline → Script)
2. Batch mode (Generate multiple complete workflows)
3. Titles only
4. Outline from custom title
5. Script from custom outline
================================================================================

Enter choice (1-5): 1

Enter topic/theme (or press Enter for default): 
# Press Enter for default, ya apna topic type karein

# ⏱️ Wait 3-5 minutes...

🎉 AUTOMATION COMPLETE!
================================================================================
📁 All files saved in: viral_content_output/
   • Titles: viral_content_output/1_titles/
   • Outline: viral_content_output/2_outlines/
   • Script: viral_content_output/3_scripts/
================================================================================
```

---

## 📂 Check Output

```bash
# Go to output folder
cd viral_content_output

# Check titles
cat 1_titles/titles_*.txt

# Check outline
cat 2_outlines/outline_*.txt

# Check script
cat 3_scripts/script_*.txt
```

---

## 🎯 What You Get

### **After First Run:**

1. **10 Viral Titles** 
   - FOMO-driven
   - Emotionally charged
   - Ending with "— Kamala Harris"
   - Example: *"Most People Don't Realise What Trump Just Did..."*

2. **1 Complete Outline** (from selected title)
   - 8-10 sections
   - 5000 words allocated
   - Contrast framing
   - Transition cues
   - CTA structure

3. **1 Full Script** (5000 words)
   - Polished narration
   - Moral authority tone
   - Human stories
   - Constitutional clarity
   - Ready to record

---

## 💰 Cost Per Run

**Single Complete Workflow:**
- ~$0.14 (14 cents)
- Includes: 10 titles + 1 outline + 1 script

**With $5 Free Credit:**
- ~35 complete workflows
- ~350 titles
- ~35 outlines
- ~35 full scripts

---

## 🔄 Different Modes

### **Mode 1: Complete Automation** (Recommended)
```
Best for: First time users, full automation
Time: 3-5 minutes
Output: Titles + Outline + Script
Cost: ~$0.14
```

### **Mode 2: Batch Processing**
```
Best for: Bulk content creation
Time: 10-20 minutes (for 3-5 workflows)
Output: Multiple complete sets
Cost: ~$0.14 per workflow
```

### **Mode 3: Titles Only**
```
Best for: Quick brainstorming
Time: 30 seconds
Output: 10 titles only
Cost: ~$0.01
```

### **Mode 4: Custom Title → Outline**
```
Best for: Specific title ideas
Time: 60 seconds
Output: Outline only
Cost: ~$0.03
Input: Your custom title
```

### **Mode 5: Custom Outline → Script**
```
Best for: Maximum control
Time: 90 seconds
Output: Script only
Cost: ~$0.10
Input: Your custom outline
```

---

## ⚙️ Common Workflows

### **Workflow A: Full Automation**
```bash
1. Run script
2. Choose Mode 1
3. Enter topic (optional)
4. Select title from 10 options
5. Wait 3-5 minutes
6. Get complete script
```

### **Workflow B: Bulk Content**
```bash
1. Run script
2. Choose Mode 2
3. Enter topic
4. Enter count (e.g., 5)
5. Wait 15-25 minutes
6. Get 5 complete scripts
```

### **Workflow C: Title Brainstorming**
```bash
1. Run script
2. Choose Mode 3
3. Enter topic
4. Get 10 titles instantly
5. Pick best ones for manual work
```

---

## 🐛 Troubleshooting First Run

### **Error: "anthropic module not found"**
```bash
# Solution:
pip install anthropic
# or
pip install -r requirements.txt
```

### **Error: "API key invalid"**
```bash
# Solution:
1. Check line 22 in script
2. Ensure no extra spaces
3. Use quotes: API_KEY = "sk-ant-..."
4. Verify key at console.anthropic.com
```

### **Script runs but no output**
```bash
# Solution:
1. Check internet connection
2. Wait full time (3-5 min)
3. Check viral_content_output/ folder
4. Look for error messages in terminal
```

### **API rate limit error**
```bash
# Solution:
1. Wait 60 seconds
2. Try again
3. Or upgrade API tier
```

---

## 📊 Output Examples

### **Example Title:**
```
Most People Don't Realise What Supreme Court Justice Just Did 
To Trump's Executive Order — Kamala Harris
```

### **Example Outline Section:**
```
1) Hook: The Hidden Constitutional Crisis — 180 words
Summary: Open with the moment Supreme Court Justice [Name] issued 
the emergency stay on Trump's executive order—contrast the promise 
of "restoring law and order" with the reality of constitutional chaos.
Transition: Now reveal what this ruling actually means for millions 
of Americans.
```

### **Example Script Opening:**
```
Here's the truth that most Americans missed this week.

While cable news focused on the latest Twitter drama, something 
extraordinary happened inside the Supreme Court. Something that 
will affect every family watching this video right now.

Let me be very clear: This isn't about politics. This is about 
the Constitution. This is about the promise America made to you—
and whether that promise still matters.

[Continue for 5000 words...]
```

---

## ✅ Success Checklist

After first run, check:

- [ ] Python 3.7+ installed
- [ ] Dependencies installed (`anthropic`)
- [ ] API key added to script
- [ ] Script runs without errors
- [ ] Output folder created (`viral_content_output/`)
- [ ] 10 titles generated
- [ ] Outline generated (if Mode 1)
- [ ] Script generated (if Mode 1)
- [ ] Files saved with timestamps
- [ ] Word count ~5000 (for script)

---

## 🚀 Next Steps

After successful first run:

1. **Review Output Quality**
   - Check if titles match your niche
   - Verify outline structure
   - Read script for tone/style

2. **Customize Prompts** (Optional)
   - Edit prompts in script (lines 24-200)
   - Adjust word counts
   - Change style/tone

3. **Scale Up**
   - Try batch mode (Mode 2)
   - Generate multiple variants
   - A/B test different topics

4. **Integrate with Workflow**
   - Use titles for ideation
   - Edit scripts for recording
   - Combine with video production

---

## 💡 Pro Tips

### **Tip 1: Topic Selection**
```
✅ Specific: "Trump tariffs Supreme Court ruling"
❌ Generic: "politics news"

✅ Current: "2024 immigration bill vote"
❌ Outdated: "2020 election"
```

### **Tip 2: Title Selection**
```
Choose titles with:
- Strong emotional triggers
- Current relevance
- Clear conflict/contrast
- Surprise element
```

### **Tip 3: Editing Scripts**
```
Scripts are 90% ready - just:
- Update specific facts/dates
- Add your personal stories
- Adjust CTAs for your channel
- Fine-tune transitions
```

### **Tip 4: Batch Processing**
```
Generate 5 workflows, then:
- Pick best 2-3 titles
- Merge best outline sections
- Use strongest script elements
```

---

## 📞 Need Help?

### **Check These First:**
1. README.md (full documentation)
2. Error messages in terminal
3. API key validity
4. Internet connection
5. Python version

### **Common Issues:**
- Wrong Python version → Install 3.7+
- Missing dependency → Run `pip install -r requirements.txt`
- API errors → Check key & credits
- No output → Wait full time & check folder

---

## 🎉 You're Ready!

```bash
# Start automation:
python viral_content_automation.py

# Choose Mode 1
# Enter topic (or press Enter)
# Select title
# Wait 3-5 minutes
# Get complete script!
```

**Happy Content Creating! 🚀**

---

**Time to First Output: 5 minutes**  
**Cost: $0.14 per workflow**  
**Output: Professional 5000-word script**
