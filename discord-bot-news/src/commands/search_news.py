import discord
from discord.ext import commands
import requests

class SearchNews(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='search_news', help='Search for specific news articles')
    async def search_news(self, ctx, query):
        try:
            # Make a request to the News API to search for news based on the query
            api_key = 'YOUR_NEWS_API_KEY'
            url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
            response = requests.get(url)
            news_data = response.json()

            # Display the search results in the Discord server
            for article in news_data['articles']:
                await ctx.send(f"**{article['title']}**\n{article['description']}\nRead more: {article['url']}")

        except Exception as e:
            await ctx.send("An error occurred while searching for news. Please try again later.")

def setup(bot):
    bot.add_cog(SearchNews(bot))