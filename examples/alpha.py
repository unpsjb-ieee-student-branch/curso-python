import urllib.request

url = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')

from xml.etree.ElementTree import parse

doc = parse(url)
for pt in doc.findall('.//pt'):
        print(pt.text)

# Notes:
# open this site http://ctabustracker.com/bustime/home.jsp in a browser
