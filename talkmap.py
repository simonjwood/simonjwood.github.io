

# # Leaflet cluster map of talk locations
#
# (c) 2016-2017 R. Stuart Geiger, released under the MIT license
#
# Run this from the _talks/ directory, which contains .md files of all your talks. 
# This scrapes the location YAML field from each .md file, geolocates it with
# geopy/Nominatim, and uses the getorg library to output data, HTML,
# and Javascript for a standalone cluster map.
#
# Requires: glob, getorg, geopy
#
# How to run (after adding talks or changing a location: field)
# ---------------------------------------------------------------
# One-time setup of a small virtual environment (no conda needed):
#
#     python3 -m venv ~/.venvs/talkmap
#     ~/.venvs/talkmap/bin/pip install getorg geopy
#
# Then regenerate the map:
#
#     cd ~/git/simonjwood.github.io/_talks
#     ~/.venvs/talkmap/bin/python ../talkmap.py
#
# It takes about a minute (Nominatim allows one lookup per second) and rewrites
# talkmap/org-locations.js and talkmap/map.html; commit both. A warning at the
# start about ipywidgets/ipyleaflet is harmless (it only matters in Jupyter).
# If a location prints "None", Nominatim couldn't find it: fix the spelling in
# that talk's location: field and run again.

import glob
import hashlib
import re
import getorg
from geopy import Nominatim
from geopy.extra.rate_limiter import RateLimiter

g = glob.glob("*.md")


geocoder = Nominatim(user_agent="simonjwood-talkmap")
geocode = RateLimiter(geocoder.geocode, min_delay_seconds=1)  # Nominatim usage policy: max 1 request/s
location_dict = {}
location = ""
permalink = ""
title = ""


for file in g:
    with open(file, 'r') as f:
        lines = f.read()
        if lines.find('location: "') > 1:
            loc_start = lines.find('location: "') + 11
            lines_trim = lines[loc_start:]
            loc_end = lines_trim.find('"')
            location = lines_trim[:loc_end]
                            
           
        if location and location not in location_dict:
            location_dict[location] = geocode(location)
            print(location, "\n", location_dict[location])


m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="../talkmap", hashed_usernames=False)

# Tag the data script with a hash of its contents so browsers fetch the new
# locations after each run instead of using a cached org-locations.js.
with open("../talkmap/org-locations.js", "rb") as f:
    version = hashlib.sha1(f.read()).hexdigest()[:10]
with open("../talkmap/map.html") as f:
    html = f.read()
html = re.sub(r'src="org-locations\.js(\?v=[0-9a-f]*)?"', f'src="org-locations.js?v={version}"', html)
with open("../talkmap/map.html", "w") as f:
    f.write(html)




