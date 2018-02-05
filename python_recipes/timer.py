""" 
Section:
    time

Author:
    Simon Ward-Jones

Description:
    Timer class with start and stop and display methods

Tags:
    time, class
"""
import time

class Timer:
    def __init__(self):
        self.start = time.time()
        self.end = time.time()
        self._is_running = False

    def start_timer(self):
        """restarts the time
        """
        self.start = time.time()
        self._is_running = True


    def reset(self):
        """reset the time
        """
        self.end = self.start = time.time()

    def stop(self):
        """stop the current time
        """
        if self._is_running:
            self.end = time.time()
        else:
            print("Can't Stop until you start")

    def get_time(self):
        '''
        Returns the time elapsed (Stops the counter).

        Returns:
            TYPE: string
        '''
        self.stop()
        return self.end - self.start

    def get_elapsed(self):
        '''
        Returns the time elapsed (Does not stop the counter).

        Returns:
            TYPE: string
        '''
        return time.time() - self.start

    def get_time_hhmmss(self,duration):
        """Returns the duration in HH:mm:ss (Does not reset the counter).
        
        Returns:
            TYPE: Description
        """
        m, s = divmod(duration, 60) 
        h, m = divmod(m, 60)
        return f'{int(h):0>2}:{int(m):0>2}:{s:05.4f}'