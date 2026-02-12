from flask import Flask, jsonify, request
import random

app = Flask(__name__)

quotes = [
    {"id": 1, "text": "Talk is cheap. Show me the code.", "author": "Linus Torvalds"},
    {"id": 2, "text": "Code is like humor. When you have to explain it, it's bad.", "author": "Cory House"},
    {"id": 3, "text": "First, solve the problem. Then, write the code.", "author": "John Johnson"},
]

@app.route("/api/quotes", methods=["GET"])
def get_all_quotes():
    return jsonify(quotes)

@app.route("/api/quotes/random", methods=["GET"])
def get_random_quote():
    return jsonify(random.choice(quotes))

@app.route("/api/quotes/<int:quote_id>", methods=["GET"])
def get_quote(quote_id):
    quote = None
    for q in quotes:
        if q["id"]==quote_id:
            quote = q
            break
    return jsonify(quote), 404

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

@app.route("/api/quotes/<int:quote_id>", methods=["PUT"])
def update_quote(quote_id):
    quote = None
    for q in quotes:
        if q["id"] == quote_id:
            quote = q
            break
    
    if not quote:
        return jsonify({"error": "Quote not found"}), 404
    
    data = request.json
    quote["text"] = data.get("text", quote["text"])
    quote["author"] = data.get("author", quote["author"])
    return jsonify(quote)


@app.route("/api/quotes/<int:quote_id>", methods=["DELETE"])
def delete_quote(quote_id):
    for q in quotes:
        if q["id"] == quote_id:
            quotes.remove(q)
            break
    return jsonify({"message": "Deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)