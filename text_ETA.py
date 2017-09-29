#
# Author: Ali Abbasinasab
# Inspired by S. Bobba
# text_ETA.py scipt: 
#   Gets the driving time between 2 locations from google maps
#   Notification is displayed on the mac with the link to go the maps
#   Sends iMessage to a mobile number.

# Required packages: pync, googlemaps, sendMessage.applescript file

# Update below parameters with your own
GOOGLEMAPS_API_KEY = ''
TARGET_PHONE_NUMBER = ''
FROM_ADDRESS = '1 Infinite Loop, Cupertino, CA 95014' #my current location
TO_ADDRESS = '20807 Stevens Creek Blvd, Cupertino, CA 95014' #place to meet
GOOGLE_MAPS_LINK = 'https://www.google.com/maps/dir/1+Infinite+Loop,+Cupertino,+CA+95014/Peeti\'s+Coffee,+Stevens+Creek+Blvd,+Cupertino,+CA/@37.3273339,-122.0386235,16z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x808fb5b6c454b237:0x8c2e9bd251b5e9ef!2m2!1d-122.0302058!2d37.3315103!1m5!1m1!1s0x808fb5ad5465805d:0x3627cf6d3d90819d!2m2!1d-122.038265!2d37.323205'

from datetime import datetime
import googlemaps
import json
gmaps = googlemaps.Client(key=GOOGLEMAPS_API_KEY)


# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions(FROM_ADDRESS,TO_ADDRESS,
                                             mode="driving",
                                                                                  departure_time=now)

time_to_home =  directions_result[0]['legs'][0]['duration_in_traffic']['text']

# Display notification on your mac with a link to google maps with prepopulated TO and FROM fields. 
from pync import Notifier
import os

Notifier.notify(time_to_home,title='Traffic Update', open=GOOGLE_MAPS_LINK)
Notifier.remove(os.getpid())

Notifier.list(os.getpid())

# Send a text message
from subprocess import call
call(["osascript","sendText.applescript",TARGET_PHONE_NUMBER,
        "Hello, current time from Infinite Loop to Peet's Coffee is: "+time_to_home])

