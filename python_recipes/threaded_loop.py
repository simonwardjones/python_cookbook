import threading
from datetime import datetime
import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(threadName)s - %(message)s",
    datefmt="%m/%d/%YT%H:%M:%S.%f")


class loop():
    def __init__(self, interval, function, args=(), kwargs={}):
        self.stop_event = threading.Event()
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.interval = interval
        self.is_running = False

    def _repeat_function(self):
        next_time = time.time() + self.interval
        actual_finish = time.time()
        # Note the while repeats every second assuming
        # the function complets in under a second
        while not self.stop_event.wait(max(0, next_time - actual_finish)):
            next_time = time.time() + self.interval
            logging.info(
                f"Calling {self.function.__name__} with args "
                f"{self.args} and kwargs {self.kwargs} at time : "
                f"{datetime.utcnow().strftime('%H:%M:%S.%f')}")
            self.function(*self.args, **self.kwargs)
            actual_finish = time.time()

    def start(self):
        if not self.is_running:
            self.stop_event = threading.Event()
            t = threading.Thread(target=self._repeat_function)
            t.daemon = True
            t.start()
            self.is_running = True
            logging.info('Started loop')

    def stop(self):
        if self.is_running:
            self.stop_event.set()
            self.is_running = False
            logging.info('Stopped loop')


def example_func(name, height=3):
    logging.info(f'name {name}, height {height}')
    return 'done'


if __name__ == '__main__':
    simon_loop = loop(interval=1,
                      function=example_func,
                      args=('simon',),
                      kwargs={"height": 44}
                      )
    simon_loop.start()
    time.sleep(5)
    simon_loop.stop()
    time.sleep(5)
    simon_loop.start()
    time.sleep(5)
    simon_loop.stop()
