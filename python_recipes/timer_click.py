"""
Section:
    click

Author:
    Simon Ward-Jones

Description:
    Count Down timer command line Tool

Tags:
    click, command line inteface
"""
import sys
import click
from timer import Timer


@click.command(help="Exit the time with ctrl + c")
@click.option('--countdown',
              type=int,
              help="Convert the timer to countdown with given seconds")
def cli(countdown=None):
    timer = Timer()
    # print(timer)
    timer.start_timer()
    clean = 0
    try:
        if countdown:
            while timer.get_elapsed() < countdown:
                if timer.get_elapsed() < 2:
                    elapsed = timer.get_time_hhmmss(
                        countdown - timer.get_elapsed())
                    print(f"And They are off!!  {elapsed}",
                          end='\r',
                          flush=True)
                elif clean == 0:
                    print("                                   ",
                          end='\r')
                    clean = 1
                else:
                    print(
                        timer.get_time_hhmmss(countdown - timer.get_elapsed()),
                        end='\r',
                        flush=True)
        else:
            while timer._is_running:
                if timer.get_elapsed() < 2:
                    elapsed = timer.get_time_hhmmss(timer.get_elapsed())
                    print(f"And They are off!! {elapsed}",
                          end='\r',
                          flush=True)
                elif clean == 0:
                    print("                                   ", end='\r')
                    clean = 1
                else:
                    print(timer.get_time_hhmmss(
                        timer.get_elapsed()), end='\r', flush=True)
    except KeyboardInterrupt:
        timer.stop()
        print("                                   ",
              end='\r')
        print(timer.get_time_hhmmss(timer.get_time()))
        sys.exit()


if __name__ == '__main__':
    cli()
