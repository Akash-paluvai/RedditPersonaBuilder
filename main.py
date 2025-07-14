import os
from reddit_scraper import scrape_user_content
from persona_generator import generate_persona


def save_persona(username: str, persona: str):
    out_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(out_dir, exist_ok=True)
    txt_file = os.path.join(out_dir, f"{username}_persona.txt")
    md_file = os.path.join(out_dir, f"{username}_persona.md")
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(persona)
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(persona)
    print(f"Persona for '{username}' saved to {txt_file} and {md_file}")


def extract_username_from_url(url: str) -> str:
    parts = url.rstrip("/").split("/")
    if "user" in parts:
        idx = parts.index("user")
        return parts[idx + 1]
    return url.strip()


if __name__ == "__main__":
    input_url = input("Enter Reddit user profile URL or username: ").strip()
    username = extract_username_from_url(input_url)
    print(f"[*] Scraping content for user: {username}")
    content, top_subreddits = scrape_user_content(username)
    if not content:
        print("No content found. Exiting.")
        exit(1)
    print(f"[*] Retrieved {len(content)} items. Generating persona...")
    persona_text = generate_persona(content, top_subreddits)
    save_persona(username, persona_text)
