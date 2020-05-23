import os
import subprocess
from subprocess import Popen
import schedule
import time


# Path of Virtual Environment
python_bin = "~/miniconda3/envs/py3k/bin/python"
# Path of the Script to be executed
script_file = "~/Downloads/BTC_Trading/get_btc_new.py"

def job():
    subprocess.Popen([python_bin, script_file])

schedule.every(2).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

