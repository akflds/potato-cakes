#!/usr/bin/python3

import json
import os
import re

datadir = os.fsencode("ratethatpc")

def getScore(m):
    score = m.group(0).split("/")
    return score[0]


def main():
    for file in os.listdir(datadir):
        filename = os.fsdecode(file)
        
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
                                m = re.search(r'[0-9]+\.?[0-9]?/10', l)
                                if m:
                                    price = getScore(m)
                                else:
                                    price = "n/a"


if __name__ == "__main__":
    main()
