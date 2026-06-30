# 🐍 PyLadies Brussels Workshop
## Do You Really Know What an API Is?

APIs are everywhere — weather apps, mobile apps, online payments, dashboards — but do you really know what an API is and how it works?

In this workshop, we'll take a step back and focus on understanding APIs from first principles.

---

## 🎯 What We'll Explore

- What an API actually is (beyond the buzzword)
- How different applications communicate with each other
- What CRUD means in practice
- How the same API can be used from Python, the browser, and JavaScript

---

## 💡 Key Concepts

### What is an API?

> **"An API is not a website. It's a program that answers requests with data."**

An API (Application Programming Interface) is a way for programs to communicate with each other.

### The Restaurant Analogy

```
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│  Customer   │         │   Waiter    │         │   Kitchen   │
│  (Your App) │  ────▶  │   (API)     │  ────▶  │  (Server)   │
└─────────────┘ Request └─────────────┘ Process └─────────────┘
                              │
                              │ Response
                              ▼
                        Food arrives!
```

- **You (the app)** want food (data)
- **The waiter (API)** takes your order
- **The kitchen (server)** prepares it
- You never go into the kitchen. You don't need to know how they cook.

> **"The API defines what you're allowed to ask for, and how to ask for it. Like a menu."**

---

## 🔄 CRUD: What Are We Doing With Data?

Every time you interact with data, you're doing one of four things:

| Action | Meaning | HTTP Verb | Example |
|--------|---------|-----------|---------|
| **C**reate | Add something new | POST | Add a new quote |
| **R**ead | Get something | GET | Show me all quotes |
| **U**pdate | Change something | PUT | Fix a typo |
| **D**elete | Remove something | DELETE | Remove a quote |

> **"CRUD is about intention: what do I want to do with this data?"**

---

## 🌐 APIs in the Browser

APIs are just URLs that return data instead of web pages.

### Try these in your browser right now:

| API | URL | What it returns |
|-----|-----|-----------------|
| JSONPlaceholder | https://jsonplaceholder.typicode.com/posts/1 | A fake blog post |
| Quotable | https://api.quotable.io/random | A random quote |
| Dog API | https://dog.ceo/dog-api | A random dog image |

**Does it look like a website? No!**

It's structured data (JSON) — made for programs, not humans.

---

## 📖 JSON: The Language of APIs

JSON is just a structured way to represent data:

```json
{
  "id": 1,
  "text": "Talk is cheap. Show me the code.",
  "author": "Linus Torvalds"
}
```

> **"If you understand Python dictionaries, you already understand JSON."**

---

## 🖥️ Our Quote API

We'll work with a small Python API that manages quotes.

### Endpoints

| Method | Endpoint | Action | Description |
|--------|----------|--------|-------------|
| GET | `/api/quotes` | Read | Get all quotes |
| GET | `/api/quotes/random` | Read | Get a random quote |
| GET | `/api/quotes/<id>` | Read | Get a specific quote |
| POST | `/api/quotes` | Create | Add a new quote |
| PUT | `/api/quotes/<id>` | Update | Modify a quote |
| DELETE | `/api/quotes/<id>` | Delete | Remove a quote |

> **"The server sets the rules. The client follows them."**

---

## 🗄️ A Note About Data

In a real application, data would be stored in a database (PostgreSQL, SQLite, MongoDB, etc.).

For our simple Python example, we use a **list of dictionaries**:

```python
quotes = [
    {"id": 1, "text": "Talk is cheap. Show me the code.", "author": "Linus Torvalds"},
    {"id": 2, "text": "Code is like humor...", "author": "Cory House"},
]
```

This is enough to understand how APIs work. The API doesn't care where the data comes from — it just returns it.

⚠️ **Note:** When the server stops, the data resets. That's why real applications use databases!

---

## 🚀 Running the API in Python

### 1. Install dependencies

```bash
pip install flask requests
```

### 2. Start the server

```bash
python app.py
```

### 3. Open in browser

```
http://localhost:5000/api/quotes
```

---

## 🔑 The Big Insight

> **"An API doesn't know who is calling it."**

The API doesn't care if the client is:
- A browser
- A Python script
- JavaScript
- A mobile app

It just receives a request and sends a response.

> **"Same URL. Same data. Different clients."**

---

## 📋 JavaScript Code to Copy

Run the API server first, then open the browser console (F12) at `http://localhost:5000/api/quotes`.

### GET all quotes

```javascript
fetch("http://localhost:5000/api/quotes")
  .then(r => r.json())
  .then(data => console.log(data));
```

### GET a random quote

```javascript
fetch("http://localhost:5000/api/quotes/random")
  .then(r => r.json())
  .then(data => console.log(data));
```

### GET one quote by ID

```javascript
fetch("http://localhost:5000/api/quotes/1")
  .then(r => r.json())
  .then(data => console.log(data));
```

### POST - Create a new quote

```javascript
fetch("http://localhost:5000/api/quotes", {
  method: "POST",
  headers: {"Content-Type": "application/json"},
  body: JSON.stringify({text: "Stay hungry, stay foolish.", author: "Steve Jobs"})
})
.then(r => r.json())
.then(data => console.log(data));
```

### PUT - Update a quote

```javascript
fetch("http://localhost:5000/api/quotes/4", {
  method: "PUT",
  headers: {"Content-Type": "application/json"},
  body: JSON.stringify({author: "Leonardo da Vinci"})
})
.then(r => r.json())
.then(data => console.log(data));
```

### DELETE - Remove a quote

```javascript
fetch("http://localhost:5000/api/quotes/4", {method: "DELETE"})
  .then(r => r.json())
  .then(data => console.log(data));
```
---

## ✅ What We Learned

- An API is a way for programs to talk
- APIs expose data through URLs (endpoints)
- CRUD describes what you want to do (Create, Read, Update, Delete)
- HTTP verbs express your intention (GET, POST, PUT, DELETE)
- JSON is the common language
- The server defines the rules, the client follows them
- The API doesn't care who's calling — browser, Python, JavaScript, it's all the same

---

## 🚀 Where to Go Next

**Practice with online APIs:**
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) — Fake REST API for testing
- [Public APIs List](https://github.com/public-apis/public-apis) — Hundreds of free APIs
- [Quotable](https://quotable.io/) — Random quotes
- [Dog CEO](https://dog.ceo/dog-api/) — Random dog images

**Resources:**
- [HTTP Status Codes](https://httpstatuses.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)

---
