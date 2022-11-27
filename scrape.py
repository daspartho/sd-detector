from reddit_scraper import RedditScraper
import os
from dotenv import load_dotenv

load_dotenv()

client_id=os.getenv('ID')
client_secret=os.getenv('SECRET')
user_agent=os.getenv('AGENT')

bot = RedditScraper(
    client_id = client_id, 
    client_secret = client_secret,
    user_agent = user_agent,
    )

sub_list = ['Art', 'ImaginaryMindscapes', 'ImaginaryMonsters', 'ImaginaryCharacters', 'DigitalArt']

bot.get_images(sub_list=sub_list, dir='human', limit=None)