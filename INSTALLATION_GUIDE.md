# 🔧 Complete Installation Guide

**Detailed step-by-step installation guide for all operating systems**

---

## 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [Windows Installation](#windows-installation)
3. [macOS Installation](#macos-installation)
4. [Linux Installation](#linux-installation)
5. [Verification](#verification)
6. [Troubleshooting](#troubleshooting)

---

## System Requirements

### **Minimum Requirements:**
- **Operating System:** Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python:** Version 3.7 or higher
- **RAM:** 2GB minimum
- **Disk Space:** 100MB free space
- **Internet:** Stable connection required

### **Recommended:**
- Python 3.9 or higher
- 4GB RAM
- SSD storage

---

## Windows Installation

### **Step 1: Install Python**

#### **Check if Python is already installed:**
```cmd
python --version
```

If you see `Python 3.7.x` or higher, skip to Step 2.

#### **Install Python:**
1. Visit: https://www.python.org/downloads/
2. Download "Windows installer (64-bit)"
3. Run installer
4. ⚠️ **IMPORTANT:** Check "Add Python to PATH"
5. Click "Install Now"
6. Wait for installation
7. Click "Close"

#### **Verify installation:**
```cmd
python --version
pip --version
```

---

### **Step 2: Download Automation Files**

#### **Option A: Download as ZIP**
1. Download all files to a folder (e.g., `C:\ViralAutomation\`)
2. Extract if zipped

#### **Option B: Using Git** (if installed)
```cmd
cd C:\
git clone <repository-url> ViralAutomation
cd ViralAutomation
```

---

### **Step 3: Install Dependencies**

```cmd
cd C:\ViralAutomation
pip install -r requirements.txt
```

**If error occurs:**
```cmd
python -m pip install --upgrade pip
pip install anthropic
```

---

### **Step 4: Get API Key**

1. Visit: https://console.anthropic.com/
2. Sign up (free tier available)
3. Go to "API Keys"
4. Click "Create Key"
5. Copy the key (starts with `sk-ant-api03-...`)

---

### **Step 5: Add API Key**

#### **Method A: Edit Script File**
1. Open `viral_content_automation.py` with Notepad
2. Find line 22:
   ```python
   API_KEY = "your-api-key-here"
   ```
3. Replace with your key:
   ```python
   API_KEY = "sk-ant-api03-xxxxx..."
   ```
4. Save file (Ctrl+S)

#### **Method B: Environment Variable** (Advanced)
1. Open System Properties → Environment Variables
2. Add new User Variable:
   - Name: `ANTHROPIC_API_KEY`
   - Value: `sk-ant-api03-xxxxx...`
3. Update script line 22:
   ```python
   API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
   ```

---

### **Step 6: Run the Script**

```cmd
cd C:\ViralAutomation
python viral_content_automation.py
```

---

## macOS Installation

### **Step 1: Install Python**

#### **Check if Python is installed:**
```bash
python3 --version
```

If version is 3.7+, skip to Step 2.

#### **Install Python using Homebrew:**

**First, install Homebrew if not installed:**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Then install Python:**
```bash
brew install python3
```

#### **Verify installation:**
```bash
python3 --version
pip3 --version
```

---

### **Step 2: Download Automation Files**

```bash
# Create directory
mkdir -p ~/ViralAutomation
cd ~/ViralAutomation

# Download files here
# Or use git:
# git clone <repository-url> ~/ViralAutomation
```

---

### **Step 3: Install Dependencies**

```bash
cd ~/ViralAutomation
pip3 install -r requirements.txt
```

**If error occurs:**
```bash
python3 -m pip install --upgrade pip
pip3 install anthropic
```

---

### **Step 4: Get API Key**

1. Visit: https://console.anthropic.com/
2. Sign up (free tier available)
3. Go to "API Keys"
4. Click "Create Key"
5. Copy the key

---

### **Step 5: Add API Key**

#### **Method A: Edit Script**
```bash
nano viral_content_automation.py
# or
open -a TextEdit viral_content_automation.py
```

Find line 22 and replace with your key:
```python
API_KEY = "sk-ant-api03-xxxxx..."
```

Save (Ctrl+X, Y, Enter for nano)

#### **Method B: Environment Variable**
```bash
# Add to ~/.zshrc or ~/.bash_profile
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-xxxxx..."' >> ~/.zshrc
source ~/.zshrc
```

Update script:
```python
API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
```

---

### **Step 6: Run the Script**

```bash
cd ~/ViralAutomation
python3 viral_content_automation.py
```

---

## Linux Installation

### **Step 1: Install Python**

#### **Ubuntu/Debian:**
```bash
# Check version
python3 --version

# If not installed or old version:
sudo apt update
sudo apt install python3 python3-pip
```

#### **Fedora/RHEL:**
```bash
sudo dnf install python3 python3-pip
```

#### **Arch:**
```bash
sudo pacman -S python python-pip
```

#### **Verify:**
```bash
python3 --version
pip3 --version
```

---

### **Step 2: Download Files**

```bash
mkdir -p ~/viral_automation
cd ~/viral_automation

# Download files or use git
# git clone <repo> ~/viral_automation
```

---

### **Step 3: Install Dependencies**

```bash
cd ~/viral_automation
pip3 install -r requirements.txt --user
```

**If permission error:**
```bash
pip3 install --user anthropic
```

---

### **Step 4: Get API Key**

Same as macOS (see above)

---

### **Step 5: Add API Key**

#### **Method A: Edit Script**
```bash
nano viral_content_automation.py
# or
vim viral_content_automation.py
```

Replace line 22:
```python
API_KEY = "sk-ant-api03-xxxxx..."
```

#### **Method B: Environment Variable**
```bash
# Add to ~/.bashrc
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-xxxxx..."' >> ~/.bashrc
source ~/.bashrc
```

---

### **Step 6: Run Script**

```bash
cd ~/viral_automation
python3 viral_content_automation.py
```

---

## Verification

### **Test Installation:**

Run this verification script:

```bash
python3 -c "
import sys
print(f'Python version: {sys.version}')

try:
    import anthropic
    print('✅ anthropic module installed')
except:
    print('❌ anthropic module NOT installed')

print('\nReady to use!' if sys.version_info >= (3,7) else 'Please upgrade Python')
"
```

**Expected output:**
```
Python version: 3.x.x
✅ anthropic module installed

Ready to use!
```

---

### **Test API Key:**

```bash
python3 viral_content_automation.py
```

If API key is correct:
- No error about invalid key
- Menu appears with 5 options

If API key is wrong:
- Error message appears
- Check key on line 22

---

## Troubleshooting

### **Problem: "python: command not found"**

**Windows:**
```cmd
# Use full path:
C:\Python39\python.exe viral_content_automation.py

# Or reinstall Python with "Add to PATH" checked
```

**macOS/Linux:**
```bash
# Use python3 instead:
python3 viral_content_automation.py

# Or create alias:
echo "alias python=python3" >> ~/.bashrc
source ~/.bashrc
```

---

### **Problem: "pip: command not found"**

**Windows:**
```cmd
python -m pip install anthropic
```

**macOS/Linux:**
```bash
python3 -m pip install anthropic
# or
pip3 install anthropic
```

---

### **Problem: "Permission denied"**

**macOS/Linux:**
```bash
# Add --user flag:
pip3 install --user anthropic

# Or use sudo (not recommended):
sudo pip3 install anthropic
```

**Windows:**
```cmd
# Run Command Prompt as Administrator
# Right-click cmd.exe → "Run as administrator"
```

---

### **Problem: "anthropic module not found"**

**Solution 1: Reinstall**
```bash
pip uninstall anthropic
pip install anthropic
```

**Solution 2: Check Python paths**
```bash
# Which Python is running?
which python3

# Which pip is installing?
which pip3

# They should match!
```

**Solution 3: Use virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

pip install anthropic
```

---

### **Problem: "API key invalid"**

**Check these:**
1. Key starts with `sk-ant-api03-`
2. No extra spaces before/after
3. Wrapped in quotes: `"sk-ant-..."`
4. Line 22 in script is correct
5. Key is active on console.anthropic.com

**Regenerate key:**
1. Go to console.anthropic.com
2. Delete old key
3. Create new key
4. Update script

---

### **Problem: "Connection error"**

**Check:**
1. Internet connection
2. Firewall settings
3. Proxy settings (if applicable)
4. VPN (try disabling)

**Test connection:**
```bash
ping anthropic.com
```

---

### **Problem: "Rate limit exceeded"**

**Solutions:**
1. Wait 60 seconds
2. Check API usage on console
3. Upgrade API tier if needed
4. Reduce batch size

---

### **Problem: Script runs but no output**

**Check:**
1. Output folder: `viral_content_output/`
2. Permissions to write files
3. Disk space available
4. Wait full time (3-5 minutes)

**Debug:**
```bash
# Run with verbose output:
python3 viral_content_automation.py

# Check if folder exists:
ls -la viral_content_output/
```

---

### **Problem: "Import error: anthropic"**

**Full reinstall:**
```bash
# Remove old installation
pip3 uninstall anthropic -y

# Clear cache
pip3 cache purge

# Reinstall
pip3 install --upgrade anthropic

# Verify
python3 -c "import anthropic; print('OK')"
```

---

### **Problem: Different Python versions**

**Find all Python installations:**

**Windows:**
```cmd
where python
```

**macOS/Linux:**
```bash
which -a python3
```

**Use specific version:**
```bash
/usr/bin/python3.9 viral_content_automation.py
```

---

## Advanced Setup

### **Using Virtual Environment** (Recommended)

**Create virtual environment:**
```bash
# Create
python3 -m venv venv

# Activate
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run script
python viral_content_automation.py

# Deactivate when done
deactivate
```

**Benefits:**
- Isolated dependencies
- No conflicts with system Python
- Easy to delete/recreate

---

### **Using .env File for API Key**

**Install python-dotenv:**
```bash
pip install python-dotenv
```

**Create .env file:**
```bash
echo "ANTHROPIC_API_KEY=sk-ant-api03-xxxxx..." > .env
```

**Update script (top of file):**
```python
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("ANTHROPIC_API_KEY")
```

**Add .env to .gitignore:**
```bash
echo ".env" >> .gitignore
```

---

## Platform-Specific Notes

### **Windows Subsystem for Linux (WSL)**
Follow Linux instructions inside WSL.

### **Chromebook (Linux mode)**
Follow Linux (Debian) instructions.

### **Raspberry Pi**
```bash
sudo apt install python3 python3-pip
pip3 install anthropic
```

### **Docker** (Advanced)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "viral_content_automation.py"]
```

---

## Getting Help

### **Check First:**
1. README.md
2. QUICKSTART.md
3. This installation guide
4. Error messages

### **Common Issues:**
- Python version too old → Upgrade to 3.7+
- Missing module → `pip install anthropic`
- Wrong API key → Check console.anthropic.com
- No internet → Check connection

---

## ✅ Installation Checklist

- [ ] Python 3.7+ installed
- [ ] `python --version` works
- [ ] `pip --version` works
- [ ] Files downloaded to folder
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] API key obtained from console.anthropic.com
- [ ] API key added to script (line 22)
- [ ] Script runs without errors
- [ ] Output folder created
- [ ] Test run completed successfully

---

## 🎉 Ready!

Your installation is complete! Run the script:

```bash
python viral_content_automation.py
```

Choose Mode 1 for your first complete workflow!

---

**Need more help? Check README.md and QUICKSTART.md**
