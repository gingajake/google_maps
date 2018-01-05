from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..google_maps_geocode import GoogleMapsGeocode


class TestGoogleMapsGeocode(NIOBlockTestCase):

    def test_process_signals(self):
        """Signals pass through block unmodified."""
        blk = GoogleMapsGeocode()
        config = {
            'api_key': 'AIzaSyBqP8CEkZkJiOHtFtylsazbkGjavbNQeDw',
            'address': '1600 Amphitheatre Parkway, Mountain View, CA',
        }
        self.configure_block(blk, config)
        blk.start()
        blk.process_signals([Signal({
            'address': '1600 Amphitheatre Parkway, Mountain View, CA'
            })])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict(), {
               'address': '1600 Amphitheatre Parkway, Mountain View, CA',
               'latitude': 37.4224082,
               'longitude': -122.0856086
             })
