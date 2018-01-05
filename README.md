GoogleMapsGeocode
===========

This block receives an incoming signal and will send a request to the Google Maps API in order to geocode the configured address/location.  Geocoding is the process of converting addresses (like a street address) into geographic coordinates (like latitude and longitude), which you can use to place markers on a map, or position the map.

Properties
--------------
  api_key
  address    

Dependencies
----------------
[googlemaps](https://developers.google.com/maps/ "Google Maps APIs")

Commands
----------------
None

Input
-------
Any list of signals.

Output
---------
Central latitude and longitude of the configured address
