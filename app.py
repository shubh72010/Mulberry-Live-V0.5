from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Stupid simple replies for demo
RESPONSES = {
    "hi": ["Hey!", "Hello there!", "Hi, how's it going?"],
    "how are you": ["I'm just code, but thanks for asking.", "Chillin'. You?", "Running light and free 😎"],
    "bye": ["See ya!", "Goodbye!", "Peace out ✌️"],
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "").strip().lower()

    if not user_input:
        return jsonify({"reply": "Say something, bro."})

    for keyword in RESPONSES:
        if keyword in user_input:
            return jsonify({"reply": random.choice(RESPONSES[keyword])})

    return jsonify({"reply": "I’m not smart enough to understand that yet 💀"})

if __name__ == "__main__":
    app.run(debug=True)
