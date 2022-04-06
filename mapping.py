import pygeoip

GI = pygeoip.GeoIP('GeoLiteCity.dat')

#output should be the location of the given ip; NOTE: does not work for IPV6

gi = pygeoip.GeoIP('GeoLiteCity.dat')
def printRecord(tgt):
     rec = gi.record_by_name(tgt)
     city = rec['city']
     region = rec['region_code']
     country = rec['country_name']
     long = rec['longitude']
     lat = rec['latitude']
     print('[*] Target: ' + tgt + ' Geo-located.')
     print('[+] City: ' +str(city)+', latitude: '+str(lat)+ ', longitude: '+str(long))
     return {'city':str(city),
             'latitude' : str(lat),
             'longitude' : str(long)}
tgt = '103.238.107.129'
printRecord(tgt)