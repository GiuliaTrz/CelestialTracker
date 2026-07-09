import time

class CelestialTracker:
    def __init__(self):
        pass

    def getISSPredictions(self, latitude : float, longitude : float, timestamp : int = None):
        if timestamp is None:
            timestamp = int(time.time())
        
        print(f"DEBUG : Using timestamp: {timestamp}")

        
        return