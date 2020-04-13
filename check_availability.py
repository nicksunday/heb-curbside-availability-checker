#!/usr/local/bin/python3.7

from datetime import datetime,timedelta
import argparse
import json
import requests

parser = argparse.ArgumentParser(description='Check next available curbside pickup at nearby HEB locations.')
parser.add_argument('zipcode', metavar='ZIP', type=str, nargs='?', default="78247",
                    help='the zipcode to check for nearby availability')
parser.add_argument('--radius', dest='radius', type=int, default=15,
                    help='the radius to search for store availability')

args= parser.parse_args()

headers = {"Content-Type": "application/json;charset=UTF-8", "Accept": "application/json, text/plain, */*"}
payload = f'{{"address":"{args.zipcode}","curbsideOnly":true,"radius":{args.radius},"nextAvailableTimeslot":true,"includeMedical":false}}'

r = requests.post('https://www.heb.com/commerce-api/v1/store/locator/address', headers=headers, data=payload)

response = r.json()

try:
    stores = response['stores']
except KeyError:
    exit(f"No stores with available time slots found within {args.radius} miles of {args.zipcode}.")

counter = 0
for store in stores:
    if store["storeNextAvailableTimeslot"]["serviceAvailable"] \
    and store["storeNextAvailableTimeslot"]["nextAvailableTimeslotDate"]:
        store_name = store["store"]["name"]
        address = f'{store["store"]["address1"]}, {store["store"]["city"]}, {store["store"]["state"]} {store["store"]["postalCode"]}'
        day, time = store["storeNextAvailableTimeslot"]["nextAvailableTimeslotDate"].split("T")
        timeslot, offset = time.split("-")
        timeslot = datetime.strptime(timeslot, '%H:%M:%S')
        date = datetime.strptime(day, '%Y-%m-%d')
        print(f"""{store_name}
{address}
Earliest Time Slot:
    On {date.strftime('%a %B %d, %Y')}
    Between {timeslot.strftime('%H:%M:%S')}-{(timeslot + timedelta(minutes=30)).strftime('%H:%M:%S')}
""")
    else:
        counter += 1	

if counter == len(stores):
    print(f"No stores with available time slots found within {args.radius} miles of {args.zipcode}.")
