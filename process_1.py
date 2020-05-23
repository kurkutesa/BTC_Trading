import os
import subprocess
from subprocess import Popen
import schedule
import time

python_bin = "/Users/sopan/miniconda3/envs/py3k/bin/python"
script_file = "/Users/sopan/Downloads/BTC_Trading/get_btc_new.py"
#script_file = "/Users/sopan/Downloads/BTC_Trading/test.py"

def job():
    subprocess.Popen([python_bin, script_file])

schedule.every(2).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

