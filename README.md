# stpc
See that PC! Visualising the greatest potato cakes in Australia.

This is project for the inaugural RMIT Online hack day. It combines a love of battered potato discs, rusty python skills and a curiosity about data and visualisation to put this info on the map.

## Dependencies
To run you will need:
* python 3 

Before running you'll need to use
* [instaloader](https://instaloader.github.io)

## Setup
* download or clone the repository
* in the same folder, use instaloader to grab json files from the [ratethatpc](https://instagram.com/ratethatpc) account using this command `instaloader --no-pictures --no-compress-json --no-captions --geotags ratethatpc`
* this creates `ratethatpc/` with the appropriate info
* run `python3 stpc.py`
* this will produce `result.json` and this was uploaded to Tableau (img below)

![potato cakes visualised on Tableau](stpc.png)
