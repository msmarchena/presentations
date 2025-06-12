# Getting Started with Python 🐍

**PyLadies Brussels**

---

## Workshop Details

- **Date:** June 12, 2025
- **Level:** Complete beginner friendly

---

## PyLadies Brussels Mission  💜 🎉👩‍💻

 **Empowering women and gender minorities in Python & tech**
 
Organizer: Marlene Marchena

---

## What We'll Master Today 🎯

1. **Install Python & VS Code** - Your coding toolkit
2. **Create virtual environments** - Keep your projects organized
3. **Use pip for package management** - Add superpowers to your code
4. **Work with requirements.txt** - Share your setup with others
5. **Follow Python best practices** - Code like a professional
6. **Write and run your first Python script** - Make something happen!

---

## Icebreaker Time! ❄️✨

**Let's get to know each other:**

1. **Your name** 
2. **One thing you hope to learn today**
3. **Fun fact:** What's your favorite way to learn something new?

*No pressure - we're all here to learn together!* 😊

---

## Setting Up Your Python Environment 🛠️

### Step 1: Install Python

1. Visit https://www.python.org/ → Downloads
2. Choose **Python 3.13+** (latest stable version) <br>

✅ **Important:** Check "Add Python to PATH" during installation

### Step 2: Install VS Code

1. Download from https://code.visualstudio.com/
2. Install the **Python extension** (by Microsoft)


### Step 3: Verify Installation

Open Terminal/Command Prompt and run:

```bash
python --version
# Should show: Python 3.13.x or higher
```
---

## Why Virtual Environments Matter 🏠

### The Problem Without Virtual Environments:

- Different projects need different package versions
- Global installations create conflicts
- Your system gets messy over time
- "It works on my machine" syndrome

### The Solution: Virtual Environments

**Think of it like this:** Each project gets its own private workspace

**Benefits:**

✅ No version conflicts <br>
✅ Clean, reproducible setups <br>
✅ Easy to share with others <br>
✅ Professional best practice <br>

---

## Creating Your First Virtual Environment 🌱

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
source venv\Scripts\activate
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

## Package Management with pip (don't run the code yet) 📦

### Installing Packages

```bash
# Install a single package
pip install pyjokes

# Install multiple packages
pip install pyjokes deep-translator
```

### Managing Dependencies

```bash
# Save current packages to requirements.txt
pip freeze > requirements.txt

# Install from requirements.txt (on another machine/environment)
pip install -r requirements.txt

# Upgrade a package
pip install --upgrade pyjokes
```

### Checking What's Installed

```bash
pip list
pip show pyjokes  # Detailed info about specific package
```

---
## Hands-On: Your First Python Script! 🎉

Let's create a simple Joke Generator App 🎭

✅ Create a virtual environment (venv)<br>
✅ Install a package (pip install)<br>
✅ Use the package in a simple script<br>
✅ Save dependencies to requirements.txt<br>
✅ Share the project with others


---
## Joke Generator App 🎉

**In the terminal run:**

```bash

pip install pyjokes # Install the package in your venv
pip list   # list all packages installed
pip show pyjokes  # Detailed info 

```

**Create `joke_app.py`:**

```python
import pyjokes

# Here you have English jokes
def tell_joke():
    print("Here a funny joke for you: ")
    print(pyjokes.get_joke())

if __name__ == "__main__":
    tell_joke()

```

**Run it:**

```bash
python joke_app.py
```

---

## Joke Generator App 🎉

Let's do a French translation

** Refactor `joke_app.py`:**

```python
import pyjokes
from deep_translator import GoogleTranslator
   
# Here you have Jokes in French
    
def translate_to_french(text):
    translator = GoogleTranslator(source="en", target="fr")
    translated = translator.translate(text)
    return translated

def tell_french_joke():
    joke = pyjokes.get_joke()
    french_joke = translate_to_french(joke)
    print("Blague en français :")
    print(french_joke)
    
    
if __name__ == "__main__":
    tell_french_joke()
```

**Run it:**

```bash
python name_of_your_file.py
```

---



## Project Structure 📁

### File Organization

```
my-python-project/
├── venv/                 # Virtual environment (don't commit!)
├── my_joke_app.py        # Your source code
├── requirements.txt      # Dependencies

```

## Take aways ✅

### For Every New Project:

- [ ] Create a dedicated folder
- [ ] Set up a virtual environment
- [ ] Activate before installing packages
- [ ] Create requirements.txt

### For Clean Code:

- [ ] Use meaningful variable names
- [ ] Add comments to explain complex logic

### For Collaboration:

- [ ] Keep requirements.txt updated

---

## Amazing Resources to Continue Learning 📚

### Essential Reading

- **Real Python** - Tutorials for all levels: https://realpython.com
- **Official Python Docs** - The ultimate reference: https://docs.python.org
- **Python.org Beginner's Guide**: https://wiki.python.org/moin/BeginnersGuide

### Interactive Learning

- **Python.org Online Tutorial**: https://docs.python.org/3/tutorial/
- **Codecademy Python Course**: https://www.codecademy.com/learn/learn-python-3
- **freeCodeCamp**: https://www.freecodecamp.org/learn/scientific-computing-with-python/

---

## Join Our Amazing Community! 🌟

### PyLadies Brussels

**We're more than just workshops - we're a supportive community!**

🔗 **Stay Connected:**

- Discord community for ongoing support
- GitHub : https://github.com/pyladiesbrussels
- PyLadies Brussels: https://www.meetup.com/pyladies-brussels/Monthly

### What's Next?

- **Advanced Python workshops**
- **Data Science track**
- **Web development with Django/Flask**


**Scan the QR code to join our Discord community!** 📱

---

## Thank You! 💜

**You've taken your first confident steps into Python programming!**

Remember: Every expert was once a beginner. You're now part of an amazing community of Python developers.

**Keep coding, keep learning, and most importantly - have fun!** 🐍✨

---


*Made with 💜 by PyLadies Brussels*

**Keep coding, keep learning, and most importantly - have fun!** 🐍✨

---

