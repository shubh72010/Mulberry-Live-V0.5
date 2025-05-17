import subprocess
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").strip()
    if not user_input:
        return jsonify({"reply": "Say something, please."})

    # Call GPT4All CLI with input and get output (adjust path)
    try:
        result = subprocess.run(
            ['path/to/gpt4all', '--prompt', user_input],
            capture_output=True,
            text=True,
            timeout=15
        )
        reply = result.stdout.strip()
    except Exception as e:
        reply = f"Error: {str(e)}"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
