#!/usr/bin/python -tt

import urllib
from xml.etree.ElementTree import parse

daves_latitude = 41.98062
daves_longitude = -87.668452


def find_candidate():
    candidate = []
    u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    data = u.read()
    f = open('rt22.xml', 'wb')
    f.write(data)
    f.close()
    # parse xml 
    doc = parse('rt22.xml')
    print 'candidate buses:'
    for bus in doc.findall('bus'):
        lat = float(bus.findtext('lat'))
        if lat > daves_latitude:
            direction = bus.findtext('d')
            if direction.startswith('North'):
                busid = bus.findtext('id')
                candidate.append(busid)
                print busid, lat
    print
    return candidate


def distance(lat1, lat2):
    # return distance in miles between two lats
    return 69 * abs(lat1 - lat2)


def monitor(candidate):
    u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    doc = parse(u)
    for bus in doc.findall('bus'):
        busid = bus.findtext('id')
        if busid in candidate:
            lat = float(bus.findtext('lat'))
            dis = distance(lat, daves_latitude)
            print busid, dis, 'miles'
    print '-'*10


def main():
    candidate = find_candidate()
    import time
    while True:
        monitor(candidate)
        time.sleep(60)


if __name__ == '__main__':
    main()
