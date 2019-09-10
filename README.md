# stpc
See that PC! Visualising the greatest potato cakes in Australia.

This is my project for the inaugural [RMIT Online](https://online.rmit.edu.au/) hackathon. It combines a love of battered potato discs, rusty Python skills, a belief in visualising data and maps.

## Dependencies

To run you will need:

* python 3 
* [instaloader](https://instaloader.github.io)

## Setup

* download or clone the repository
* in the same folder, use instaloader to grab JSON files from the [ratethatpc](https://instagram.com/ratethatpc) account using this command `instaloader --no-pictures --no-compress-json --no-captions --geotags ratethatpc`
* this creates `ratethatpc/` with the appropriate files
* run `python3 stpc.py`
* this will produce `result.json` which I went on to upload into Tableau for the visualisation (see below)

## Outcomes
After bashing at Tableau for a little bit, we got all the JSON data on a map and a ranking for each category so you can find your perfect PC.

![potato cakes visualised on Tableau](stpc.png)

## Future work
The code is pretty hacky and there are a few issues documented to resolve some of these things. 

Eventually I'd like to see this on an open map somehow, let's see what happens...
