# 💫 CelestialTracker

CelestialTracker is a simple application that allows you to get satellite passes predictions over a given point on Earth.

## 🖋️ Features
- **Automatic TLE update:** the application checks if the satellite TLE record is older than 24 hours and automaticaly downloads the updated version.
- Calculates predictions for a specific satellite contained in the TLE file
- JSON output


## ⚙️ Usage

### Examples
```sh
# Calculates ISS predictions
$ python3 main.py 41.9027835 12.4963655

Latitude: 41.9027835  Longitude: 12.4963655

Satellite: ISS (ZARYA) catalog #25544 epoch 2026-07-28 03:39:38 UTC

Event: 29/07/2026 12:47:28
+-------+---------------------+------------+----------+----------+---------------+
|  Type |      Timestamp      | Elevation° | Azimuth° | Cardinal | Distance (Km) |
+-------+---------------------+------------+----------+----------+---------------+
| START | 29/07/2026 12:47:28 |    10.0    |  195.1   |   SSW    |    1483.468   |
|  MAX  | 29/07/2026 12:50:20 |    26.9    |  135.4   |    SE    |    836.142    |
|  END  | 29/07/2026 12:53:14 |    10.0    |   75.9   |   ENE    |    1497.397   |
+-------+---------------------+------------+----------+----------+---------------+
```
```
# Shows satellites contained in the TLE file
$ python3 main.py -l
Satellites:
0       ISS (ZARYA)
1       POISK
2       CSS (TIANHE)
3       ISS (NAUKA)
4       FREGAT DEB
5       CSS (WENTIAN)
6       CSS (MENGTIAN)
7       HRC MONOBLOCK CAMERA
8       SZ-21 MODULE
9       DUPLEX
10      KNACKSAT-2
11      CORAL
12      GXIBA-1
13      UITMSAT-2
14      LEOPARD
15      HMU-SAT2
16      CREW DRAGON 12
17      PROGRESS-MS 33
18      CYGNUS NG-24
19      PROGRESS-MS 34
20      TIANZHOU-10
21      SHENZHOU-23 (SZ-23)
```

### CLI Help
```
usage: main.py [-h] [-d DATE] [-e ELEVATION] [-a HORIZON_ALTITUDE] [-l] [-s SATELLITE]
               [-j]
               [latitude] [longitude]

positional arguments:
  latitude
  longitude

options:
  -h, --help            show this help message and exit
  -d, --date DATE       The date for wich you want to get the satellite passes forecast
                        (empty for current date) (format: yyyy-mm-dd)
  -e, --elevation ELEVATION
                        Elevation (in meters) from the wgs84 reference ellipsoid
  -a, --horizon_altitude HORIZON_ALTITUDE
                        Degrees above the horizon
  -l, --list_satellites
                        Shows satellites contained in the TLE file
  -s, --satellite SATELLITE
                        Satellite index in the TLE file
  -j, --json            Prints the satellite passes forecast using JSON format
```
## 🛠️ Build
```sh

# Clone
git clone https://github.com/GiuliaTrz/CelestialTracker
cd CelestialTracker

# Install dependencies
pip3 install -r requirements.txt
```

## 🧰 External Dependencies
- https://pypi.org/project/prettytable/
- https://rhodesmill.org/skyfield/