import os
from dotenv import load_dotenv
import praw
from tqdm import tqdm
from collections import Counter

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)


def scrape_user_content(username: str, limit: int = 50) -> tuple:
    content = []
    subreddits = []
    try:
        user = reddit.redditor(username)
        for comment in tqdm(user.comments.new(limit=limit), desc="Scraping comments"):
            body = comment.body.replace("\n", " ").strip()
            content.append(f"[COMMENT] {body} (id:{comment.id})")
            subreddits.append(str(comment.subreddit.display_name))
        for post in tqdm(user.submissions.new(limit=limit), desc="Scraping posts"):
            title = post.title.replace("\n", " ").strip()
            selftext = post.selftext.replace("\n", " ").strip()
            combined = f"{title} - {selftext}" if selftext else title
            content.append(f"[POST] {combined} (id:{post.id})")
            subreddits.append(str(post.subreddit.display_name))
    except Exception as e:
        print(f"Error scraping user '{username}': {e}")
    top_subreddits = Counter(subreddits).most_common(5)
    return content, top_subreddits
