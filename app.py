from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import openai
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize OpenAI client with API key from environment
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
@app.route("/")
def home():
    return "✅ AI ReadMe Generator is running! Send a POST to /suggest with a title."


@app.route("/suggest", methods=["POST"])
def suggest():
    try:
        data = request.get_json()
        title = data.get("title", "")
        if not title:
            return jsonify({"error": "Title is required"}), 400

        prompt = f"Write a GitHub README description for a project titled: {title}"

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        suggestion = response.choices[0].message.content.strip()
        return jsonify({"suggestion": suggestion})

    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)