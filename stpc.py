#!/usr/bin/python3

import json
import os
import re

# where our data lives
datadir = os.fsencode("ratethatpc")

# find the score for a given line, ignore the scale (e.g. /10) as this is consistent
def getScore(line):
    # matchy matchy
    m = re.search(r':?\s?[0-9][0-9]?\.?[0-9]*', line)
    # if we find something, trim any remaining chars at the front and return
    if m:
        score = m.group(0)
        score = score.strip(' ')
        score = score.strip(':')
        return score
    # nothing found? return none
    else:
        return None

def main():
    # iterate over files in data directory
    for file in os.listdir(datadir):
        filename = os.fsdecode(file)

        # empty dict for ratings
        rating = {'price': None,
                'size': None,
                'batter': None,
                'core': None,
                'freshness': None,
                'overall': None
                }
        
        # todo: empty dict for location

        # check file is json
        # note: only checks files this millenium 
        if filename.startswith("2") and filename.endswith(".json"):
            # open file and load json data from file
            with open(os.path.join(datadir, file)) as f:
                data = json.load(f)
                # check json contrains a location
                if data['node']['location'] != None:
                    # todo: store location
                    
                    # assume all items have a caption
                    caption = data['node']['edge_media_to_caption']['edges'][0]['node']['text']
                    
                    # check caption contains an overall ranking (lazy)
                    if caption.find('Overall') >= 0:
                        
                        # captions are multiline, iterate over each line in caption
                        for l in caption.splitlines():

                            # poor mans switch statement, check for various rating categories
                            # include value in rating dict
                            if l.startswith("Price:") or l.startswith("Value:"):
                                rating['price'] = getScore(l)
                            elif l.startswith("Size:"):
                                rating['size'] = getScore(l)
                            elif l.startswith("Batter:"):
                                rating['batter'] = getScore(l)
                            elif l.startswith("Potato Core:") or l.startswith("Potato core:"):
                                rating['core'] = getScore(l)
                            elif l.startswith("Freshness"):
                                rating['freshness'] = getScore(l)
                            elif l.startswith("Overall"):
                                rating['overall'] = getScore(l)

                    # todo: check if overall != None
                    # todo: combine rating and location data to single json object

                    # todo: push json object to mega json file

    # todo: when done with all files, output mega json/geojson file, ready for tableau

if __name__ == "__main__":
    main()
