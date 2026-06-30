# 🐍 PyLadies Brussels Workshop
## From Flask to FastAPI: Building Modern APIs

APIs are everywhere — but building them can feel repetitive and error-prone.

In this workshop, we'll revisit the same API you already understand, and rebuild it using FastAPI, a modern Python framework.

---

## 🎯 What We'll Explore

- How FastAPI simplifies API development
- What changes compared to Flask (and why)
- Automatic validation with Pydantic
- Why type hints matter in real APIs
- How modern APIs are built in production

---

## 🧠 Reminder: What is an API?

> **"An API is a program that answers requests with data."**

Nothing changes here. Same idea:

- Client sends a request
- Server processes it
- Server returns JSON

---

## 🔄 CRUD Still Applies

FastAPI doesn't change what we do — only how we do it.

| Action | HTTP Verb | Example |
|--------|-----------|---------|
| **C**reate | POST | Add a quote |
| **R**ead | GET | Get quotes |
| **U**pdate | PUT | Edit a quote |
| **D**elete | DELETE | Remove a quote |

> **"FastAPI improves implementation, not the concept."**

---

## 🖥️ Our Quote API (Same as Before!)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/quotes` | Get all quotes |
| GET | `/api/quotes/random` | Get a random quote |
| GET | `/api/quotes/{id}` | Get one quote |
| POST | `/api/quotes` | Create a quote |
| PUT | `/api/quotes/{id}` | Update a quote |
| DELETE | `/api/quotes/{id}` | Delete a quote |

---

## 🔧 Where the Differences Live

All six "Key Differences" below happen on the **server side** — inside `quotes_fastapi.py`.

The **client side** doesn't change at all. Whether you're calling the API from the browser, from `requests` in Python, or from `/docs`, you talk to it exactly the same way you did with Flask.

> **"A better backend doesn't change how clients talk to it."**

---

## ⚡ Key Difference #1: No `jsonify()` (Server)

**Flask**
```python
return jsonify(quotes)
```

**FastAPI**
```python
return quotes
```

👉 FastAPI automatically converts Python → JSON

> **"Less boilerplate, same result."**

---

## ⚡ Key Difference #2: No `request.json` (Server)

**Flask**
```python
@app.route("/api/quotes", methods=["POST"])
def add_quote():
    data = request.json
    new_quote = {
        "id": len(quotes) + 1,
        "text": data["text"],
        "author": data.get("author", "Unknow")
    }
    quotes.append(new_quote)
    return jsonify(new_quote), 201
```

What's happening here: `request.json` reads whatever JSON the client sent and hands it to you as a plain dictionary. From that point on, **you** are responsible for everything — checking that `"text"` exists, deciding what to do if it doesn't, deciding what `author` defaults to. Flask doesn't know or care what a "quote" is supposed to look like.

**FastAPI**
```python
@app.post("/api/quotes", status_code=201)
def add_quote(quote: QuoteIn):           # ① the body is already parsed and validated
    new_quote = {
        "id": len(quotes) + 1,
        "text": quote.text,              # ② access fields as attributes, not dict keys
        "author": quote.author,
    }
    quotes.append(new_quote)
    return new_quote
```

Here, `quote: QuoteIn` in the function signature tells FastAPI: *"this endpoint expects a request body shaped like a `QuoteIn`."* FastAPI then does, automatically, before your function even runs:

1. Reads the JSON body (same job as `request.json`)
2. Checks it against the `QuoteIn` model — is `text` present? Is it a string? Is it at least 1 character?
3. If anything is wrong, it stops and sends back a `422` error — your function never even runs
4. If everything is valid, it builds a `QuoteIn` object and passes it to you as `quote`

So `quote.text` isn't reading a dictionary key — it's accessing an attribute on an object that FastAPI has already validated for you.

> **"In Flask, `request.json` is a fact: 'here's whatever data they sent.' In FastAPI, `quote: QuoteIn` is a contract: 'this is the only shape of data this endpoint accepts.'"**

> **"The function signature becomes your API contract."**

---

## ⚡ Key Difference #3: Validation (Game Changer) (Server)

```python
class QuoteIn(BaseModel):
    text: str = Field(min_length=1)
    author: Optional[str] = "Unknown"
```

👉 FastAPI automatically:
- validates input
- rejects bad requests
- returns clear error messages

**Wait — where's `id`?**

Notice `QuoteIn` only has `text` and `author`. No `id`.

That's intentional. `id` isn't something the *client* sends — it's something the *server* decides:

```python
@app.post("/api/quotes", status_code=201)
def add_quote(quote: QuoteIn):
    new_quote = {
        "id": len(quotes) + 1,   # ← server decides this
        "text": quote.text,       # ← client provides this
        "author": quote.author,   # ← client provides this
    }
```

> **"The Pydantic model describes what the client is allowed to send — not the full shape of the data."**

If `id` were in `QuoteIn`, a client could send their own `id` and overwrite an existing quote. Keeping it out of the input model is a small design choice that prevents a real bug.

---

## 🧪 Example: Bad Request

**Request:**
```json
{
  "author": "Someone"
}
```

**Response:**
```json
{
  "detail": [
    {
      "loc": ["body", "text"],
      "msg": "field required"
    }
  ]
}
```

> **"Validation is no longer your responsibility."**

---

## ⚡ Key Difference #4: Type Safety (Server)

```python
@app.get("/api/quotes/{quote_id}")
def get_quote(quote_id: int):
```

👉 If user calls:
```
/api/quotes/banana
```

FastAPI returns:
```
422 Unprocessable Entity
```

> **"Your API rejects invalid input before your code runs."**

---

## ⚡ Key Difference #5: Explicit Errors (Server)

**Flask (bug-prone)**
```python
return jsonify(quote), 404
```

**FastAPI (clear)**
```python
raise HTTPException(status_code=404, detail="Quote not found")
```

> **"Errors are part of your API design."**

---

## ⚡ Key Difference #6: Auto Documentation (Server) 🤯

Run your API and open:
```
http://127.0.0.1:8000/docs
```

👉 You get:
- interactive UI
- request testing
- schema documentation

> **"Your API documents itself."**

**What `/docs` shows right now**

Since `quotes` includes an `id`, but `QuoteIn` doesn't, `/docs` shows a slightly generic shape for responses — it infers the output from whatever the function returns.

**Bonus:** make the response shape explicit with a second model:

```python
class QuoteOut(BaseModel):
    id: int
    text: str
    author: str

@app.get("/api/quotes/{quote_id}", response_model=QuoteOut)
def get_quote(quote_id: int):
    ...
```

This shows a real production pattern: **the input shape and the output shape can be different Pydantic models.** `QuoteIn` controls what a client may send; `QuoteOut` controls what `/docs` promises the client will get back.

---

## 🗄️ Data Storage (Same as Before)

We still use:

```python
quotes = [
    {"id": 1, "text": "...", "author": "..."}
]
```

⚠️ **This is not persistent**

> **"We focus on API logic, not databases (yet)."**

---

## 🚀 Running FastAPI

### 1. Install dependencies

```bash
pip install fastapi uvicorn requests
```

### 2. Run the server

```bash
python quotes_fastapi.py
```

or:

```bash
uvicorn quotes_fastapi:app --reload
```

### 3. Open

```
API:  http://127.0.0.1:8000/api/quotes
Docs: http://127.0.0.1:8000/docs
```

---

## 🧪 Python Client (Same Idea!)

Your API still works the same way:

```python
import requests

requests.get("http://localhost:8000/api/quotes")
```

👉 Nothing changes on the client side!

> **"A better backend doesn't change how clients talk to it."**

---

## 🧪 Validation in Action

**1. Wrong type**
```python
requests.get("/api/quotes/banana")
```
👉 Returns `422`

**2. Missing field**
```python
requests.post("/api/quotes", json={"author": "Someone"})
```
👉 Returns `422`

**3. Default value**
```python
requests.post("/api/quotes", json={"text": "Hello"})
```
👉 `author = "Unknown"`

---

## 🧠 The Big Insight

> **"FastAPI shifts responsibility from the developer to the framework."**

**Flask:**
- You parse data
- You validate
- You handle errors

**FastAPI:**
- Framework handles structure
- You focus on logic

---

## ⚖️ Flask vs FastAPI

| Feature | Flask | FastAPI |
|---------|-------|---------|
| JSON handling | Manual | Automatic |
| Validation | Manual | Automatic |
| Docs | None | Built-in |
| Type safety | No | Yes |
| Boilerplate | More | Less |

---

## ✅ What We Learned

- APIs concepts stay the same (CRUD, HTTP, JSON)
- FastAPI simplifies implementation
- Validation is automatic
- Type hints make APIs safer
- Errors are explicit
- Documentation is generated for free

---

## 🚀 Where to Go Next

- Add a database (SQLite / PostgreSQL)
- Add authentication
- Build a frontend (React / JS)
- Deploy your API

---

## 💡 Final Thought

> **"FastAPI doesn't change what an API is — it changes how easy it is to build one correctly."**

---

*Created for PyLadies Brussels — 2026*