# file to handle twitter connections

import twitter
import os
import random


api = twitter.Api(consumer_key='eO5RVypGHgOMlIDHIAENn8xsN',
                  consumer_secret='I9qGC2GXKtqIhf2iKDgsel3uybTgPOqV7Bdxd0k4a3vyUkuAv5',
                  access_token_key='1353383761686142981-2Jt2vNq22vUKo2bNJV3iD3u7LUrFMJ',
                  access_token_secret='dAhBnzyzFd7XatjLnCRNXejmp79e1J95VJCfOxPZ4VYBT')




def post_image():
    # Select random image from /posts/

    image = random.choice(os.listdir(r'posts'))

    # post to timeline

    post = api.PostUpdate(status='CarPorn Photo of the Day',
                          media=str('posts') + '/' + image)

    print(post.text)


post_image()
