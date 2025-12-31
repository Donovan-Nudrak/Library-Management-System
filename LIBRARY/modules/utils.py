#!/usr/bin/env python3

from tqdm import tqdm
from datetime import datetime

import platform
import time
import os


def pause_clear():
    pause()
    clear()


def pause(sleep=2):
    time.sleep(sleep)


def clear():
    if platform.system() == "Linux":
        sys = "clear"
    else:
        sys = "cls"
    os.system(sys)


def loading_bar(text, times=100):
    seconds = range(times)
    for second in tqdm(seconds, desc=text, unit="LOAD"):
        time.sleep(0.1)
    print("Successful process")


def logs(log):
    file = "logs.txt"
    date = datetime.now()
    lines = (f"{log} | {date} \n")
    if file:
        with open(file, "a", encoding="utf-8") as f:
            f.write(lines)
