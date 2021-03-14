# Goal of this program is to download jpeg images from a r/carporn and upload to a Twitter account.

from bs4 import BeautifulSoup as soup
from requests import get
import requests
import os
import praw
import time

# Creating welcome message

print('This program will run in the background and run at an interval at a set time' '\n'
      'checking for new posts on r/carporn. It will then scrape the subreddit, parse the html,''\n'
      'then write the jpeg to a folder.' '\n'
      'It will then attempt to upload to a Twitter profile')


# PRAW : Initial attempt using PRAW to find submission links resulting in .jpg


def get_links():
    r = praw.Reddit(client_id='',
                    client_secret='',
                    user_agent='twitter_carporn',
                    username='carporn_twitter_bot',
                    password='')
    print(f'Logged in as {r.user.me()}')

    sub = r.subreddit('carporn')

    hot = sub.hot(limit=5)
    print(f'Gathering image submissions..')

    img_list = []

    for sub in hot:
        if not sub.stickied:
            img_list.append(sub.url)
            print(img_list)
            p = requests.get(sub.url)
            with open(r'posts\image_' + str(sub) + '.jpg', 'wb') as h:
                h.write(p.content)


get_links()


# Write the objects from the list into separate files as they're already named.



# Alternative attempt using BeautifulSoup

# reddit_username = 'notbecausewhat'

# reddit_pass = 'rovcyx-1Goxni-byqwiq'
#
#
# login_credentials = {'user': reddit_username,
#                      'passwd': reddit_pass,
#                      'api_type': 'json'}
# headers = {'user-agent': 'twitter_carporn', }
#
# client = requests.session()
# client.headers = headers
#
# r = client.post(r'https://ssl.reddit.com/api/login', data=login_credentials)
#
# j = json.loads(r.content)
#
# print(j)

#
# def find_jpeg():
#
#     html_text = requests.get('https://old.reddit.com/r/carporn/').text
#     print(html_text)
#     reddit_soup = soup(html_text, 'lxml')
#     posts = reddit_soup.find_all('body', class_='listing-page hot-page')
#     print(posts)
#
#
# find_jpeg()
