import os
import requests
from dotenv import load_dotenv
from textblob import TextBlob

load_dotenv()

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.getenv('OPENROUTER_API_KEY')
MODEL = os.getenv("LLM_MODEL", "deepseek/deepseek-r1-0528:free")


def analyze_sentiment(content_list):
    sentiments = [TextBlob(entry).sentiment.polarity for entry in content_list]
    avg = sum(sentiments) / len(sentiments) if sentiments else 0
    if avg > 0.2:
        return "Positive"
    elif avg < -0.2:
        return "Negative"
    else:
        return "Neutral"


def generate_persona(content_list: list, top_subreddits: list, max_entries: int = 30) -> str:
    entries = content_list[:max_entries]
    joined = "\n".join(entries)
    sentiment_summary = analyze_sentiment(entries)
    subreddit_summary = ", ".join([f"r/{s[0]}" for s in top_subreddits])

    system_msg = {"role": "system", "content": "You are an expert behavioral analyst."}
    user_msg = {
        "role": "user",
        "content": (
            f"Analyze the following Reddit posts and comments. Build a detailed persona including:\n"
            f"- Interests\n- Hobbies\n- Personality traits\n- Writing style\n- Political/social views (if any)\n- Notable patterns\n\n"
            f"For each trait, cite specific content (post or comment) by its ID.\n\n"
            f"Top Subreddits: {subreddit_summary}\n"
            f"Overall Tone: {sentiment_summary}\n\n"
            f"CONTENT:\n" + joined
        )
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "https://chat.openrouter.ai/",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [system_msg, user_msg]
    }

    res = requests.post(OPENROUTER_URL, json=payload, headers=headers)
    if res.status_code != 200:
        print("ERROR:", res.status_code)
        print("RESPONSE:", res.text)
        raise RuntimeError("LLM request failed.")
    data = res.json()
    return data['choices'][0]['message']['content']