# stpc
See that PC! Visualising the greatest potato cakes in Australia.

This is project for the inaugural RMIT Online hack day. It combines a love of battered potato discs, rusty Python skills and a curiosity about data and visualisation to put this info on the map.

## Dependencies
To run you will need:
* python 3 

Before running you'll need to use
* [instaloader](https://instaloader.github.io)

## Setup
* download or clone the repository
* in the same folder, use instaloader to grab json files from the [ratethatpc](https://instagram.com/ratethatpc) account using this command `instaloader --no-pictures --no-compress-json --no-captions --geotags ratethatpc`
* this creates `ratethatpc/` with the appropriate files
* run `python3 stpc.py`
* this will produce `result.json` and we uploaded this to Tableau for the visualisation (img below)

## Outcomes
After bashing at Tableau for a little bit, we got all the JSON data on a map and a ranking for each category so you can find your perfect PC.

![potato cakes visualised on Tableau](stpc.png)

## Future work
The code is pretty hacky and there are a few issues documented to resolve some of these things. 
Eventually I'd like to see this on an open map somehow, let's see what happens...
