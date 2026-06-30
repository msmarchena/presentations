from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import random

app = FastAPI(title="Quotes API", description="PyLadies Brussels — A2 Workshop")

# ── Data ──────────────────────────────────────────────────────────────────────

quotes = [
    {"id": 1, "text": "Talk is cheap. Show me the code.", "author": "Linus Torvalds"},
    {"id": 2, "text": "Code is like humor. When you have to explain it, it's bad.", "author": "Cory House"},
    {"id": 3, "text": "First, solve the problem. Then, write the code.", "author": "John Johnson"},
]

# ── Pydantic model ─────────────────────────────────────────────────────────────
# This replaces all the manual request.json handling from Flask.
# FastAPI reads this class and:
#   1. Validates incoming data automatically
#   2. Returns a clear 422 error if something is wrong
#   3. Generates the /docs page for free

class QuoteIn(BaseModel):
    text: str = Field(min_length=1, description="The quote text")
    author: Optional[str] = Field(default="Unknown", description="Who said it")


# ── Endpoints ─────────────────────────────────────────────────────────────────

# REVEAL 1: No jsonify() needed — FastAPI converts dicts automatically
@app.get("/api/quotes")
def get_all_quotes():
    return quotes


# REVEAL 1 (continued): quote_id: int in the signature = automatic type validation
# Try hitting /api/quotes/banana — FastAPI rejects it before your code even runs
@app.get("/api/quotes/random")
def get_random_quote():
    return random.choice(quotes)


@app.get("/api/quotes/{quote_id}")
def get_quote(quote_id: int):
    for q in quotes:
        if q["id"] == quote_id:
            return q
    # Flask bug: return jsonify(quote), 404  ← always returns 404!
    # FastAPI: HTTPException makes the intent explicit
    raise HTTPException(status_code=404, detail="Quote not found")


# REVEAL 2: QuoteIn replaces data = request.json + manual field extraction
# If text is missing or empty, FastAPI returns a 422 with a clear error message
@app.post("/api/quotes", status_code=201)
def add_quote(quote: QuoteIn):
    new_quote = {
        "id": len(quotes) + 1,
        "text": quote.text,
        "author": quote.author,
    }
    quotes.append(new_quote)
    return new_quote


@app.put("/api/quotes/{quote_id}")
def update_quote(quote_id: int, updated: QuoteIn):
    for q in quotes:
        if q["id"] == quote_id:
            q["text"] = updated.text
            q["author"] = updated.author
            return q
    raise HTTPException(status_code=404, detail="Quote not found")


@app.delete("/api/quotes/{quote_id}")
def delete_quote(quote_id: int):
    for q in quotes:
        if q["id"] == quote_id:
            quotes.remove(q)
            return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Quote not found")


# ── Run ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("quotes_fastapi:app", host="127.0.0.1", port=8000, reload=True)