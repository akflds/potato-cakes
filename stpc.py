#!/usr/bin/python3

import json
import os
import re

datadir = os.fsencode("ratethatpc")


def getScore(line):
    m = re.search(r':?\s?[0-9][0-9]?\.?[0-9]*', line)
    if m:
        score = m.group(0)
        score = score.strip(' ')
        score = score.strip(':')
        return score
    else:
        print("issue with")
        print(line)
        return None

def main():
    for file in os.listdir(datadir):
        filename = os.fsdecode(file)

        
        rating = {'price': None,
                'size': None,
                'batter': None,
                'core': None,
                'freshness': None,
                'overall': None
                }

        # note: only checks files this millenium 
        if filename.startswith("2") and filename.endswith(".json"):
            with open(os.path.join(datadir, file)) as f:
                data = json.load(f)
                # check json contrains a location
                if data['node']['location'] != None:
                    caption = data['node']['edge_media_to_caption']['edges'][0]['node']['text']
                    
                    if caption.find('Overall') >= 0:
                        for l in caption.splitlines():
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

if __name__ == "__main__":
    main()
