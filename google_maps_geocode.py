import googlemaps
from datetime import datetime

from nio.block.base import Block
from nio.signal.base import Signal
from nio.properties import Property, StringProperty, VersionProperty

class GoogleMapsGeocode(Block):

    version = VersionProperty('0.1.0')
    api_key = Property(title='API Key', default='[[GOOGLE_MAPS_API_KEY]]')
    address = Property(title="Street Address", default="")

    def process_signals(self, signals):
        lng=0.0
        lat=0.0

        for signal in signals:

            gmaps = googlemaps.Client(key=self.api_key())
            geocode_result = gmaps.geocode(str(self.address(signal)))
            lng = geocode_result[0].get('geometry')['location'].get('lng')
            lat = geocode_result[0].get('geometry')['location'].get('lat')

        self.notify_signals(Signal({"lng": lng, "lat": lat}))
