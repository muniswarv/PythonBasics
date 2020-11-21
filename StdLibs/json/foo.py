#!/usr/bin/env python

"""
    Referenced from 
        https://www.youtube.com/watch?v=9Xt2e9x4xwQ

    Status:
        Not Working
"""

import urllib2
#import json
import simplejson


url = "https://www.youtube.com/results?search_query=json+tutorial+for+beginners&oq=json+&gs_l=youtube.1.0.0l10.6363.7333.0.12650.5.4.0.1.1.0.183.638.0j4.4.0...0.0...1ac.1.11.youtube.mKBgnjiljyw"

req = urllib2.Request(url)
opener = urllib2.build_opener()
f = opener.open(req)
json = simplejson.load(f)

for item in json:
    print item.get('create_at')
    print item.get('text')


