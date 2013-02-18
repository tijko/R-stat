#!/usr/bin/env python

import sys
import time
import pylab
import requests
import collections
import argparse
from simplejson import JSONDecodeError

def argset():
    parser = argparse.ArgumentParser(description='Scraping statistics from Reddit!')
    parser.add_argument('-c', '--comments', help='sum total of comments', action='store_true')
    parser.add_argument('-a', '--author', help='display author of post', action='store_true')
    parser.add_argument('-i', '--images', help='all the image links', action='store_true')
    parser.add_argument('-g', '--graph', help='bar graph of # of posts/hr', action='store_true')
    parser.add_argument('-t', '--time', help='return the time the post was made', action='store_true')
    parser.add_argument('-s', '--score', help='find the score of post', action='store_true')
    parser.add_argument('-u', '--upvotes', help='display up-votes per post', action='store_true')
    parser.add_argument('-d', '--downvotes', help='display down-votes per post', action='store_true')
    parser.add_argument('-U', '--url', help='return the web address for post', action='store_true')
    parser.add_argument('-S', '--subreddit', help='allows for specifing a sub-reddit to query', action='store_true')
    parse = parser.parse_args()
    return parse


def main(options=None):
    m = '\n'
    picnum = 0
    data = collections.defaultdict(int)
    for hour in xrange(24):
        data[str(hour)]
    if options.subreddit:
        subreddit = raw_input('Which sub-reddit do you want statistics for?: ')
        req = requests.get('http://www.reddit.com/r/%s/.json?limit=50' % subreddit)
        m = m + '%s --->' % subreddit.upper()
    else:
        req = requests.get('http://www.reddit.com/.json?limit=50')
        m = m + 'FRONT PAGE --->\n'
    try:
        posts = req.json()
    except JSONDecodeError:
        print 'No Data -- Make sure this a legitimate subreddit!'
        return
    try:
        for pst in posts['data']['children']:
            m = m + '\n%s' % pst['data']['title']
            if options.author:
                m = m + '\n    Author: %s' % pst['data']['author']
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
                out = time.asctime(time.localtime(pst['data']['created_utc']))
                out = out.split(' ')
                if len(out) > 5:
                    out = out[4][:-6]
                else:
                    out = out[3][:-6]
                if out[0] == '0':
                    out = out[1:]
                data[out] += 1
            if options.images:
                if 'jpeg' in pst['data']['url'] or 'jpg' in pst['data']['url'] or 'png' in pst['data']['url']:
                    picnum += 1
                    if options.subreddit:
                        with open('/home/haumea/Pictures/%s' % picnum + subreddit, 'wb+') as f:
                            pic = requests.get(pst['data']['url'])
                            f.write(pic.content)
                    else:
                        with open('/home/haumea/Pictures/%s' % picnum, 'wb+') as f:
                            pic = requests.get(pst['data']['url'])
                            f.write(pic.content)
            m = m + '\n-------------------------------------------'
    except TypeError or KeyError:
        print 'No Data'
        return
    if options.graph:
        fig = pylab.figure()
        ax = fig.add_subplot(1,1,1)
        y = [i for i in data.values()]
        ind = range(len(y))
        ax.bar(ind, y, align='center')
        ax.set_ylabel('Posts')
        ax.set_title('Posts / hour', fontstyle='italic')
        ax.set_xticks(ind)
        ax.set_xticklabels = (["%d O'clock" % i for i in range(24)])
        pylab.show()
    print m

if __name__ == '__main__':
    a = argset()
    main(a)
