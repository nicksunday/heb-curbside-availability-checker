# H-E-B Curbside Pickup Availability Checker

## Usage

```bash
check_availability.py [-h] [--radius RADIUS] [ZIP]

Check next available curbside pickup at nearby HEB locations.

positional arguments:
  ZIP              the zipcode to check for nearby availability

optional arguments:
  -h, --help       show this help message and exit
  --radius RADIUS  the radius to search for store availability
```


## Example output
```bash
./check_availability.py --radius 10 78729
Research Blvd H-E-B
12860 RESEARCH BLVD, AUSTIN, TX 78750-3222
Earliest Time Slot:
    On Tue April 14, 2020
    Between 08:00:00-08:30:00

North Hills H-E-B
10710 RESEARCH BLVD. STE 200, AUSTIN, TX 78759-5780
Earliest Time Slot:
    On Tue April 14, 2020
    Between 11:30:00-12:00:00

620 and O'Connor H-E-B
16900 N RANCH ROAD 620, ROUND ROCK, TX 78681-3922
Earliest Time Slot:
    On Tue April 14, 2020
    Between 12:00:00-12:30:00
```
