"""The timeout module contains a class to facilitate raising an exception if a function call takes too long."""

import time
import signal

class timeout:
    """Can raise an exception if the search process takes too long."""
    def __init__(self, seconds=1):
        self.seconds = seconds

    def timeoutCallback(self, signum, frame):
        raise TimeoutError("Timed out after " + str(self.seconds) + " seconds")

    def __enter__(self):
        try:
            signal.signal(signal.SIGALRM, self.timeoutCallback)
            signal.alarm(self.seconds)
        except:
            pass

    def __exit__(self, type, value, traceback):
        try:
            signal.alarm(0)
        except:
            pass
