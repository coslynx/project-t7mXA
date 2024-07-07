import discord
from discord.ext import commands
import requests
from newspaper import Article

class PostNews(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def post_news(self, ctx, topic):
        api_key = "YOUR_NEWS_API_KEY"
        url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"
        
        response = requests.get(url)
        news_data = response.json()

        for article in news_data['articles']:
            news_article = Article(article['url'])
            news_article.download()
            news_article.parse()
            news_title = news_article.title
            news_content = news_article.text
            news_url = article['url']

            embed = discord.Embed(title=news_title, description=news_content, url=news_url, color=discord.Color.blue())
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(PostNews(client))