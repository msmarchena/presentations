# Getting Started with Python 🐍

**PyLadies Brussels Beginner Workshop**

---

## Workshop Details

- **Date:** June 12, 2025 | 6:00 PM
- **Duration:** 2 hours
- **Location:** Interface3, Brussels
- **Instructor:** Marlene Marchena
- **Language:** English/French
- **Level:** Complete beginner friendly

---

## Slide 1: Welcome to PyLadies Brussels! 💜

### Bienvenue / Welcome! 🎉

We're thrilled you're here to start your Python journey with us!

**Today's Goal:** Set up your Python development environment like a pro

**What You Need:**

- Your laptop 💻
- Curiosity and enthusiasm ✨
- No prior experience required!

---

## Slide 2: What We'll Master Today 🎯

By the end of this workshop, you'll be able to:

1. **Install Python & VS Code** - Your coding toolkit
2. **Create virtual environments** - Keep your projects organized
3. **Use pip for package management** - Add superpowers to your code
4. **Work with requirements.txt** - Share your setup with others
5. **Follow Python best practices** - Code like a professional
6. **Write and run your first Python script** - Make something happen!

**Bonus:** You'll leave with a complete project template! 🚀

---

## Slide 3: Meet Your Instructor & PyLadies Team 👩‍💻

### Marlene Marchena

- **Data Scientist** with expertise in Python & R
- **Educator** passionate about making coding accessible
- **Mission:** Prove that learning Python doesn't have to be intimidating!

### PyLadies Brussels Mission

**Empowering women and gender minorities in Python & tech**

🔗 **Stay Connected:**

- Discord community for ongoing support
- GitHub for resources and code examples
- Monthly meetups and workshops

---

## Slide 4: Icebreaker Time! ❄️✨

**Let's get to know each other:**

Share with the group:

1. **Your name** 
2. **One thing you hope to learn today**
3. **Fun fact:** What's your favorite way to learn something new?

*No pressure - we're all here to learn together!* 😊

---

## Slide 5: Setting Up Your Python Environment 🛠️

### Step 1: Install Python

1. Visit **python.org** → Downloads
2. Choose **Python 3.11+** (latest stable version)
3. ✅ **Important:** Check "Add Python to PATH" during installation

### Step 2: Install VS Code

1. Download from **code.visualstudio.com**
2. Install the **Python extension** (by Microsoft)
3. Install **Code Runner extension** (optional but helpful)

### Step 3: Verify Installation

Open Terminal/Command Prompt and run:

```bash
python --version
# Should show: Python 3.11.x or higher
```

**Having issues?** Raise your hand - we're here to help! 🙋‍♀️

---

## Slide 6: Why Virtual Environments Matter 🏠

### The Problem Without Virtual Environments:

- Different projects need different package versions
- Global installations create conflicts
- Your system gets messy over time
- "It works on my machine" syndrome

### The Solution: Virtual Environments

**Think of it like this:** Each project gets its own private workspace

**Benefits:**

- ✅ No version conflicts
- ✅ Clean, reproducible setups
- ✅ Easy to share with others
- ✅ Professional best practice

---

## Slide 7: Creating Your First Virtual Environment 🌱

### Create a Project Folder

```bash
mkdir my-python-project
cd my-python-project
```

### Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv
```

### Activate Your Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

**Success indicator:** Your terminal prompt will show `(venv)`

### When You're Done Working

```bash
deactivate
```

---

## Slide 8: Package Management with pip 📦

### Installing Packages

```bash
# Install a single package
pip install requests

# Install multiple packages
pip install requests beautifulsoup4 pandas
```

### Managing Dependencies

```bash
# Save current packages to requirements.txt
pip freeze > requirements.txt

# Install from requirements.txt (on another machine/environment)
pip install -r requirements.txt

# Upgrade a package
pip install --upgrade requests
```

### Checking What's Installed

```bash
pip list
pip show requests  # Detailed info about specific package
```

---

## Slide 9: Hands-On: Your First Python Script! 🎉

Let's create a simple web API client:

**Create `main.py`:**

```python
import requests
import json

def get_github_info():
    """Fetch and display GitHub API information"""
    print("🚀 Fetching data from GitHub API...")
    
    try:
        response = requests.get("https://api.github.com")
        
        if response.status_code == 200:
            print(f"✅ Success! Status code: {response.status_code}")
            print(f"📊 Rate limit remaining: {response.headers.get('X-RateLimit-Remaining', 'Unknown')}")
            
            # Pretty print some API endpoints
            data = response.json()
            print("\n🔗 Available API endpoints:")
            for key, url in list(data.items())[:5]:  # Show first 5
                print(f"  • {key}: {url}")
                
        else:
            print(f"❌ Request failed with status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error occurred: {e}")

if __name__ == "__main__":
    get_github_info()
    print("\n🎉 Great job! You just made your first API call with Python!")
```

**Run it:**

```bash
python main.py
```

---

## Slide 10: Professional Project Structure 📁

### Recommended File Organization

```
my-python-project/
├── venv/                 # Virtual environment (don't commit!)
├── src/                  # Your source code
│   └── main.py
├── requirements.txt      # Dependencies
├── .gitignore           # Files to ignore in Git
├── README.md            # Project documentation
└── .env.example         # Environment variables template
```

### Essential .gitignore Content

```gitignore
# Virtual Environment
venv/
env/
.venv/

# Python Cache
__pycache__/
*.pyc
*.pyo

# Environment Variables
.env

# IDE Files
.vscode/
.idea/
```

---

## Slide 11: Best Practices Checklist ✅

### For Every New Project:

- [ ] Create a dedicated folder
- [ ] Set up a virtual environment
- [ ] Activate before installing packages
- [ ] Create requirements.txt
- [ ] Add .gitignore file
- [ ] Write a clear README.md

### For Clean Code:

- [ ] Use meaningful variable names
- [ ] Add comments to explain complex logic
- [ ] Follow PEP 8 style guidelines
- [ ] Handle errors gracefully (try/except)

### For Collaboration:

- [ ] Keep requirements.txt updated
- [ ] Document how to run your project
- [ ] Never commit your venv folder

---

## Slide 12: Amazing Resources to Continue Learning 📚

### Essential Reading

- **Real Python** - Tutorials for all levels: https://realpython.com
- **Official Python Docs** - The ultimate reference: https://docs.python.org
- **Python.org Beginner's Guide**: https://wiki.python.org/moin/BeginnersGuide

### Interactive Learning

- **Python.org Online Tutorial**: https://docs.python.org/3/tutorial/
- **Codecademy Python Course**: https://www.codecademy.com/learn/learn-python-3
- **freeCodeCamp**: https://www.freecodecamp.org/learn/scientific-computing-with-python/

### VS Code Extensions

- **Python** (Microsoft) - Essential!
- **Python Docstring Generator** - Auto-generate documentation
- **GitLens** - Enhanced Git capabilities
- **Prettier** - Code formatting

---

## Slide 13: Join Our Amazing Community! 🌟

### PyLadies Brussels

**We're more than just workshops - we're a supportive community!**

### How to Stay Connected:

- 💬 **Discord:** Get help, share projects, chat with fellow learners
- 🐙 **GitHub:** Access all our workshop materials and examples
- 📅 **Monthly Meetups:** Regular workshops and networking events
- 🌐 **Global Network:** Part of the worldwide PyLadies community

### What's Next?

- **Advanced Python workshops**
- **Data Science track**
- **Web development with Django/Flask**
- **Career development sessions**

**Scan the QR code to join our Discord community!** 📱

---

## Thank You! 💜

**You've taken your first confident steps into Python programming!**

Remember: Every expert was once a beginner. You're now part of an amazing community of Python developers.

**Keep coding, keep learning, and most importantly - have fun!** 🐍✨

---

### Contact Information

- **Instructor:** Marlene Marchena
- **PyLadies Brussels:** https://www.meetup.com/pyladies-brussels/
- **Global PyLadies:** https://pyladies.com

*Made with 💜 by PyLadies Brussels*

**Keep coding, keep learning, and most importantly - have fun!** 🐍✨

---

