import praw
import requests
import os

class RedditScraper():

    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(
            client_id = client_id, 
            client_secret = client_secret,
            user_agent = user_agent,
        )

    def get_images(self, sub_list, dir, limit):
        '''scrapes reddit for art image and saves them on a folder'''

        os.makedirs(f'images/{dir}') # creates dir that will contain the art images

        for sub_name in sub_list:
            sub = self.reddit.subreddit(sub_name) # creates a subreddit instance

            n=0 # n is used for naming images
            for post in sub.top(limit=limit):
                url=post.url

                if url.endswith(('png', 'jpg', 'jpeg')):
                    format=url.split('.')[-1]

                    img_data = requests.get(url).content
                    with open(f'images/{dir}/{sub_name}_{n}.{format}', 'wb') as handler:
                        handler.write(img_data) # saving images
                        n+=1 