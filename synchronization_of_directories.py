import schedule
import time
import argparse
import sys
import threading
from dirsync import sync

parser = argparse.ArgumentParser(
    prog='One-way synchronization of directories',
    description='The program is doing one-way synchronization of two directories '
                'according to variables of the command string.',
    epilog='(c) Denys Matyushyn'
)
parser.add_argument('-s', '--source_dir', help='Need to point the path to the source directory (mandatory variable)')
parser.add_argument('-r', '--replicated_dir', help='Need to point the path to the replicated directory '
                                                   '(mandatory variable)')
parser.add_argument('-f', '--log_file', help='Need to point the path to Logfile (mandatory variable)')
parser.add_argument('-е', '--time', help='Need to point interval of synchronization per sec. (mandatory variable).')
args = parser.parse_args()

class Logger:
    def __init__(self, filename):
        self.console = sys.stdout
        self.file = open(filename, 'w')
    def write(self, message):
        self.console.write(message)
        self.file.write(message)
    def flush(self):
        self.console.flush()
        self.file.flush()

def sync_dir():
    sync(args.source_dir, args.replicated_dir, 'sync', purge = True, verbose = True)

schedule.every(int(args.time)).seconds.do(sync_dir)
sys.stdout = Logger(args.log_file)

def loop():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=loop, daemon=True).start()
input('Press <Enter> to exit.')
