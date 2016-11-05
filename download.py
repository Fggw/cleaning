#!/usr/bin/env python

"""
Script to convert r data files into .csv
"""

import os
import sys
import pandas as pd
import numpy as np
import requests
import shutil

def download_file(row):
    url = row['link']
    name = row['name']
    print "Downloading {}".format(name)

    local_filename = "../data/{}.csv".format(name)
    df = pd.read_csv(url + '?$limit=300000')
    df.to_csv(local_filename)
    print "Finished {}".format(name)

    return True


def read_and_download():
    datasets = pd.read_csv('datasets.txt', sep='|')
    datasets.apply(download_file, axis=1)

if __name__ == "__main__":
    read_and_download()