# file to handle twitter connections

import twitter
import os
import random


api = twitter.Api(consumer_key='insert key',
                  consumer_secret='secret',
                  access_token_key='token',
                  access_token_secret='token secret')




def post_image():
    # Select random image from /posts/

    image = random.choice(os.listdir(r'posts'))

    # post to timeline

    post = api.PostUpdate(status='CarPorn Photo of the Day',
                          media=str('posts') + '/' + image)

    print(post.text)


post_image()
