# 🚀 Viral Content Automation System

**Automatically generate viral YouTube content: Titles → Outlines → Full Scripts**

Complete automation system jo political YouTube content generate karta hai competitor analysis ke basis par.

---

## ✨ Features

### 🎯 **3-Step Automation Pipeline**
1. **Title Generation** - 10 viral, FOMO-driven political titles
2. **Outline Generation** - 5000-word structured outline (8-10 sections)
3. **Script Generation** - Complete 5000-word polished script

### 🔥 **Key Capabilities**
- ✅ Competitor style matching
- ✅ Emotional trigger optimization
- ✅ High-retention pacing
- ✅ Moral authority tone
- ✅ Constitutional clarity
- ✅ Human-centric storytelling
- ✅ Built-in CTAs

---

## 📋 Requirements

### **Python Version**
- Python 3.7 ya higher

### **Dependencies**
```bash
pip install anthropic
```

### **API Key**
Anthropic API key chahiye (Claude AI)
- Get it from: https://console.anthropic.com/
- Free tier available

---

## 🛠️ Installation

### **Step 1: Download Files**
```bash
# Download the script
# viral_content_automation.py

# Install dependencies
pip install anthropic
```

### **Step 2: Add API Key**
Script file open karein aur line 22 par apni API key add karein:

```python
API_KEY = "your-actual-api-key-here"  # ⚠️ REPLACE THIS
```

### **Step 3: Run**
```bash
python viral_content_automation.py
```

---

## 🎮 Usage Modes

Script run karne par aapko 5 options milenge:

### **Mode 1: Single Workflow (Recommended)**
```
Complete automation: Titles → Outline → Script
- 10 titles generate hote hain
- Aap ek select karte hain
- Outline aur script automatically ban jati hai
```

### **Mode 2: Batch Mode**
```
Multiple complete workflows ek saath
- Perfect for bulk content creation
- Time-saving for multiple videos
```

### **Mode 3: Titles Only**
```
Sirf viral titles generate karein
- Fast generation
- Manual outline/script ke liye
```

### **Mode 4: Outline from Custom Title**
```
Apni title se outline banayein
- Custom titles ke liye
- Manual script writing ke liye
```

### **Mode 5: Script from Custom Outline**
```
Apne outline se script banayein
- Maximum control
- Custom outlines ke liye
```

---

## 📁 Output Structure

Sab kuch organized folders mein save hota hai:

```
viral_content_output/
├── 1_titles/
│   └── titles_20241117_143022.txt
├── 2_outlines/
│   └── outline_20241117_143145_Most_People_Dont_Realise.txt
└── 3_scripts/
    └── script_20241117_143310_Most_People_Dont_Realise.txt
```

---

## 💡 Example Workflow

### **Complete Automation (Mode 1)**

```bash
$ python viral_content_automation.py

Choose mode:
1. Single workflow (Titles → Outline → Script)
> 1

Enter topic/theme (or press Enter for default): Trump tariffs

📝 STEP 1: GENERATING VIRAL TITLES
✅ Generated 10 titles
💾 Saved to: viral_content_output/1_titles/titles_20241117_143022.txt

📋 Generated Titles:
   1. Most People Don't Realise What Trump Just Did With China Tariffs — Kamala Harris
   2. You Won't Believe What Supreme Court Ruled on Trump's Trade War — Kamala Harris
   ...

📌 SELECT A TITLE
Enter title number (1-10): 1

📐 STEP 2: GENERATING OUTLINE
✅ Outline generated successfully
💾 Saved to: viral_content_output/2_outlines/outline_20241117_143145.txt

📜 STEP 3: GENERATING FULL SCRIPT
✅ Script generated successfully
📊 Word count: 5147
💾 Saved to: viral_content_output/3_scripts/script_20241117_143310.txt

🎉 AUTOMATION COMPLETE!
```

---

## ⏱️ Time Estimates

| Step | Time |
|------|------|
| Title Generation | 15-30 seconds |
| Outline Generation | 30-60 seconds |
| Script Generation | 60-90 seconds |
| **Total** | **3-5 minutes** |

---

## 🎯 Target Audience

Script is specifically designed for:
- **Political commentary channels**
- **U.S. political content creators**
- **Left-leaning/moderate audience**
- **Age: 25-54**
- **Motivated by rule-of-law & social justice**

---

## 🔧 Customization

### **Change Prompts**
Script mein teen prompts hain (lines 24-200):
- `TITLE_GENERATION_PROMPT`
- `OUTLINE_GENERATION_PROMPT`
- `SCRIPT_GENERATION_PROMPT`

In prompts ko modify karke aap style change kar sakte hain.

### **Change Output Length**
Outline aur script prompts mein word count modify kar sakte hain:
```python
# Default: 5000 words
# Change karne ke liye prompts edit karein
```

### **Change Model**
API call mein model change kar sakte hain:
```python
# Line 156
model="claude-3-5-sonnet-20241022"  # Current
# Change to:
model="claude-3-opus-20240229"  # More powerful
```

---

## 📊 Cost Estimate

**Anthropic Claude API Pricing (as of Nov 2024):**

| Model | Input | Output |
|-------|-------|--------|
| Claude 3.5 Sonnet | $3 per 1M tokens | $15 per 1M tokens |

**Per Workflow Cost:**
- Title Generation: ~$0.01
- Outline Generation: ~$0.03
- Script Generation: ~$0.10
- **Total: ~$0.14 per complete workflow**

---

## 🐛 Troubleshooting

### **Error: API Key Invalid**
```
Solution: Check API key on line 22
Make sure no extra spaces or quotes
```

### **Error: Module 'anthropic' not found**
```bash
Solution: Install dependency
pip install anthropic
```

### **Error: Rate limit exceeded**
```
Solution: Wait 60 seconds
Or upgrade API tier
```

### **Script stops unexpectedly**
```
Solution: Check internet connection
Ensure API key has credits
Check API status: status.anthropic.com
```

---

## 📝 Best Practices

### **1. Topic Selection**
```
✅ Good: "Trump tariffs Supreme Court ruling"
✅ Good: "Congressional healthcare vote"
❌ Bad: "Politics" (too broad)
```

### **2. Title Selection**
```
- Choose titles with strongest emotional triggers
- Pick titles relevant to current news
- Select titles with clear contrast framing
```

### **3. Review Output**
```
Always review:
- Title accuracy
- Outline structure
- Script flow and CTAs
- Word count (should be ~5000)
```

### **4. Batch Processing**
```
For bulk content:
- Use Mode 2 (Batch)
- Generate 3-5 workflows at once
- Review and select best outputs
```

---

## 🔒 Security Notes

### **API Key Safety**
- ⚠️ Never share your API key
- ⚠️ Don't commit API key to Git
- ⚠️ Use environment variables in production

### **Use .env File (Recommended)**
```bash
# Create .env file
echo "ANTHROPIC_API_KEY=your-key-here" > .env

# Update script to read from .env
# (requires python-dotenv package)
```

---

## 🚀 Advanced Usage

### **Python Integration**

```python
from viral_content_automation import generate_titles, generate_outline, generate_script

# Generate titles
titles = generate_titles(topic="Healthcare reform")

# Generate outline
outline = generate_outline(titles[0])

# Generate script
script = generate_script(outline, titles[0])

print(f"Script word count: {len(script.split())}")
```

### **Batch Processing via Python**

```python
from viral_content_automation import batch_process

# Generate 5 complete workflows
batch_process(topic="Supreme Court decisions", count=5)
```

---

## 📚 Documentation

### **Prompt Engineering**
Har prompt carefully designed hai based on:
- Competitor analysis
- Psychological triggers
- YouTube retention patterns
- Political commentary best practices

### **Output Quality**
Scripts include:
- Strong hooks (8-12 seconds)
- Emotional metaphors
- Human stories
- Legal explanations
- Contrast framing
- Mobilizing CTAs

---

## 🤝 Support

### **Issues?**
- Check API key aur internet connection
- Review error messages carefully
- Ensure Python 3.7+ installed
- Verify dependencies installed

### **Questions?**
- Review this README thoroughly
- Check example outputs
- Test with default settings first

---

## 📄 License

This automation system is provided as-is for content creation purposes.

---

## 🎉 Ready to Start?

```bash
# 1. Install dependency
pip install anthropic

# 2. Add API key to script (line 22)
# 3. Run
python viral_content_automation.py

# 4. Select Mode 1 for complete automation
```

---

**Happy Content Creating! 🚀**
