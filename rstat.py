#!/usr/bin/env python

import time
import requests
import argparse

from lib.images import img_downloader
from lib.graph import RGraph
from simplejson import JSONDecodeError

def argset():
    parser = argparse.ArgumentParser(description='Scraping statistics from Reddit!')
    group = parser.add_mutually_exclusive_group()

    parser.add_argument('-c', '--comments', help='sum total of comments', action='store_true')
    parser.add_argument('-a', '--author', help='display author of post', action='store_true')
    parser.add_argument('-i', '--images', help='all the image links', action='store_true')
    parser.add_argument('-g', '--graph', help='bar graph of # of posts/hr', action='store_true')
    parser.add_argument('-t', '--time', help='return the time the post was made', action='store_true')
    parser.add_argument('-s', '--score', help='find the score of post', action='store_true')
    parser.add_argument('-u', '--upvotes', help='display up-votes per post', action='store_true')
    parser.add_argument('-d', '--downvotes', help='display down-votes per post', action='store_true')
    parser.add_argument('-U', '--url', help='return the web address for post', action='store_true')

    group.add_argument('-r', '--recent', help='display the most recent posts to reddit', action='store_true')
    group.add_argument('-S', '--subreddit', help='allows for specifing a sub-reddit to query', action='store_true')

    parse = parser.parse_args()
    return parse


def main(options=None):
    m = '\n'
    picnum = 0
    rg = RGraph

    if options.subreddit:
        subreddit = raw_input('Which sub-reddit do you want statistics for?: ')
        req = requests.get('http://www.reddit.com/r/%s/.json?limit=50' % subreddit)
        m = m + '/r/%s/ --->\n' % subreddit
        m = m + '\n' + ('-' * 43)
    elif options.recent:
        req = requests.get('http://www.reddit.com/r/all/new/.json')
        m = m + '/r/all/new/ --->\n'
        m = m + '\n' + ('-' * 43)
    else:
        req = requests.get('http://www.reddit.com/.json?limit=50')
        m = m + '/r/all/ --->\n'
        m = m + '\n' + ('-' * 43)
    try:
        posts = req.json()
    except JSONDecodeError:
        print 'No Data -- Make sure this is a legitimate subreddit!'
        return
    try:
        for pst in posts['data']['children']:
            m = m + '\n%s' % pst['data']['title']
            if options.author:
                m = m + '\n    Author: %s' % pst['data']['author']
            if options.recent:
                m = m + '\n    Subreddit: %s' % pst['data']['subreddit']
            if options.time:
                m = m + '\n    Time Posted: %s' % time.asctime(time.localtime(pst['data']['created_utc']))
            if options.url:
                m = m + '\n    Url: %s' % pst['data']['url']
            if options.comments:
                m = m + '\n    Total Comments: %s' % pst['data']['num_comments']
            if options.score:
                m = m + '\n    Score: %s' % pst['data']['score']
            if options.upvotes:
                m = m + '\n    Upvotes %s' % pst['data']['ups']
            if options.downvotes:
                m = m + '\n    Downvotes %s' % pst['data']['downs']

            if options.graph:
                rg.compute_graph(pst)
            m = m + '\n' + ('-' * 43)
    except (TypeError, KeyError) as e:
        print 'No Data'
        return
    if options.graph:
        rg.show_graph()

    print m

if __name__ == '__main__':
    a = argset()
    main(a)
