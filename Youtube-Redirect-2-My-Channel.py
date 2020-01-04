#!/usr/bin/env python3


import urllib
import json
from selenium import webdriver
import time


def look_for_new_video():
    api_key = "api aa bichij ogno."
    channel_id = "UC0rd3rYEXdSSNtgVj9O8P9Q"

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(api_key, channel_id)

    inp = urllib.urlopen(url)
    resp = json.load(inp)

    vidID = resp['items'][0]['id']['videoId']

    video_exists = False
    with open('videoid.json', 'r') as json_file:
        data = json.load(json_file)
        if data['videoId'] != vidID:

            driver = webdriver.Firefox()
            driver.get(base_video_url + vidId)
            video_exists = True

    if video_exists:
        with open('videoid.json' , 'w') as json_file:

            data = {'videoId' : vidID}
            json.dump(data , json_file)


try:
    while True:
        look_for_new_video()
        time.sleep(10)
except KeyboardInterrupt:
    print('stopping')
