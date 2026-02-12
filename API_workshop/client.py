import requests

BASE_URL = "http://localhost:5000"

# GET all quotes
print("All quotes:")
print(requests.get(f"{BASE_URL}/api/quotes").json())

# POST new quote
print("\nAdding a quote...")
new_quote = {"text": "Simplicity is the ultimate sophistication.", "author": "Leonardo de Vinci"}
print(requests.post(f"{BASE_URL}/api/quotes",json=new_quote).json())

# Updating quote 4
updated = {"author": "Leonardo Da Vinci"}
response = requests.put("http://localhost:5000/api/quotes/4", json=updated)
print(response.json())

# # GET all quotes again
# print("\nAll quotes after adding:")
# print(requests.get(f"{BASE_URL}/api/quotes").json())