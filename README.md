GoogleMapsGeocode
=================
This block receives an incoming signal and will send a request to the Google Maps API in order to geocode the configured address/location.  Geocoding is the process of converting addresses (like a street address) into geographic coordinates (like latitude and longitude), which you can use to place markers on a map, or position the map.

Properties
----------
- **address**: Street address to be converted into geographic coordinates
- **api_key**: API Key for the Google Maps API

Inputs
------
- **default**: Any list of signals

Outputs
-------
- **default**: The input list of signals plus latitude and longitude for the configured address

Commands
--------
None

Dependencies
------------
[googlemaps](https://developers.google.com/maps/ "Google Maps APIs")

Input
-----
Any list of signals.

Output
------
Central latitude and longitude of the configured address

