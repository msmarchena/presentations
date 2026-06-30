import requests

BASE_URL = "http://localhost:8000"

# ── GET all quotes ─────────────────────────────────────────────────────────────
print("\n--- GET all quotes ---")
response = requests.get(f"{BASE_URL}/api/quotes")
print(response.json())

# ── GET a random quote ─────────────────────────────────────────────────────────
print("\n--- GET random quote ---")
response = requests.get(f"{BASE_URL}/api/quotes/random")
print(response.json())

# ── GET one quote by ID ────────────────────────────────────────────────────────
print("\n--- GET quote by ID (id=1) ---")
response = requests.get(f"{BASE_URL}/api/quotes/1")
print(response.json())

# ── REVEAL 1: type validation ──────────────────────────────────────────────────
# In Flask, /api/quotes/banana would crash or return an ugly error.
# FastAPI rejects it automatically because quote_id: int
print("\n--- GET quote by ID (id=banana) → expect 422 ---")
response = requests.get(f"{BASE_URL}/api/quotes/banana")
print(f"Status: {response.status_code}")
print(response.json())

# ── GET quote that doesn't exist ───────────────────────────────────────────────
print("\n--- GET quote by ID (id=999) → expect 404 ---")
response = requests.get(f"{BASE_URL}/api/quotes/999")
print(f"Status: {response.status_code}")
print(response.json())

# ── POST a new quote ───────────────────────────────────────────────────────────
print("\n--- POST new quote ---")
new_quote = {"text": "Simplicity is the ultimate sophistication.", "author": "Leonardo da Vinci"}
response = requests.post(f"{BASE_URL}/api/quotes", json=new_quote)
print(f"Status: {response.status_code}")
print(response.json())

# ── REVEAL 2: Pydantic validation ─────────────────────────────────────────────
# In Flask, sending bad data would either crash or silently store garbage.
# FastAPI + Pydantic returns a clear 422 with exactly what's wrong.
print("\n--- POST with missing text → expect 422 ---")
bad_quote = {"author": "Someone"}
response = requests.post(f"{BASE_URL}/api/quotes", json=bad_quote)
print(f"Status: {response.status_code}")
print(response.json())

# ── POST with author missing (should default to "Unknown") ─────────────────────
print("\n--- POST with no author → should default to 'Unknown' ---")
no_author = {"text": "Code never lies, comments sometimes do."}
response = requests.post(f"{BASE_URL}/api/quotes", json=no_author)
print(f"Status: {response.status_code}")
print(response.json())

# ── PUT update a quote ─────────────────────────────────────────────────────────
print("\n--- PUT update quote id=4 ---")
updated = {"text": "Simplicity is the ultimate sophistication.", "author": "Leonardo Da Vinci"}
response = requests.put(f"{BASE_URL}/api/quotes/4", json=updated)
print(f"Status: {response.status_code}")
print(response.json())

# ── DELETE a quote ─────────────────────────────────────────────────────────────
print("\n--- DELETE quote id=4 ---")
response = requests.delete(f"{BASE_URL}/api/quotes/4")
print(f"Status: {response.status_code}")
print(response.json())

# ── GET all quotes again to confirm delete worked ──────────────────────────────
print("\n--- GET all quotes (after delete) ---")
response = requests.get(f"{BASE_URL}/api/quotes")
print(response.json())