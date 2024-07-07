import discord
import requests
from newspaper import Article

class NewsFetcher:
    def __init__(self, client):
        self.client = client

    async def fetch_news(self, topic):
        try:
            news_api_key = "YOUR_NEWS_API_KEY"
            url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={news_api_key}"
            response = requests.get(url)
            data = response.json()

            if data["status"] == "ok":
                articles = data["articles"]
                for article in articles:
                    article_url = article["url"]
                    article_title = article["title"]
                    article_summary = self.get_article_summary(article_url)
                    await self.client.send(article_title + "\n" + article_summary)

        except Exception as e:
            print(f"An error occurred: {e}")

    def get_article_summary(self, url):
        article = Article(url)
        article.download()
        article.parse()
        return article.text[:200] + "..."  # Return first 200 characters as summary

# Initialize the bot
client = discord.Client()
news_fetcher = NewsFetcher(client)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.content.startswith('!fetch'):
        topic = message.content.split(' ')[1]
        await news_fetcher.fetch_news(topic)

# Run the bot
client.run('YOUR_DISCORD_BOT_TOKEN')