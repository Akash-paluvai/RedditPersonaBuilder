# RedditPersonaBuilder

This tool analyzes a Reddit user's posts and comments to generate a psychological user persona using GPT-4.

This CLI tool scrapes a Reddit user's recent posts and comments, then generates a detailed user persona using an LLM (DeepSeek via OpenRouter API). Each persona characteristic is cited with the original post/comment.

![PEP8](https://img.shields.io/badge/code%20style-pep8-brightgreen.svg)

## Features
- **Scrapes** up to 50 comments and 50 submissions per user
- **Analyzes** content with DeepSeek LLM through OpenRouter
- **Outputs** a `.txt` file containing the persona and citations

## Setup
1. **Clone** this repository:
   ```bash
   git clone https://github.com/yourusername/RedditPersonaBuilder.git
   cd RedditPersonaBuilder
   ```

2. **Create** a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install** dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create** a `.env` file in the project root with your keys:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key
   REDDIT_CLIENT_ID=your_reddit_client_id
   REDDIT_CLIENT_SECRET=your_reddit_client_secret
   REDDIT_USER_AGENT=YourAppName/0.1 by YourRedditUsername
   ```

## Usage
```bash
python main.py
```
- When prompted, enter the full Reddit profile URL or username (e.g., `https://www.reddit.com/user/kojied/` or `kojied`).

- The persona will be saved in `output/<username>_persona.txt`.

## Examples
```
Enter Reddit user profile URL or username: kojied
[*] Scraping content for user: kojied
Scraping comments: 100%|██████████| 50/50 [00:05<00:00,  9.34it/s]
Scraping posts:    100%|██████████| 50/50 [00:02<00:00, 18.81it/s]
[*] Retrieved 100 items. Generating persona...
Persona for 'kojied' saved to output/kojied_persona.txt
```

## Contributing
- Follow PEP-8 style
- Submit issues or pull requests

## License
MIT License
