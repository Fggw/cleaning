#!/usr/bin/env python

"""
Script to convert r data files into .csv
"""

import os
import sys
import rpy2.robjects as r
from rpy2.robjects import pandas2ri

pandas2ri.activate()

# find the relevant files
BASE = '../chicago/DATA/'
FILES = [f for f in os.listdir(BASE) if '.Rds' in f]

print FILES

for f in FILES:

    name, ext = f.split('.')
    
    try:
        obj = r.r['readRDS'](BASE + f)
        pyobj = pandas2ri.ri2py(obj)

        outname = "../chidata/{}.csv".format(name)

        if not os.path.isfile(outname):
            print "Writing", outname
            pyobj.to_csv(outname)

    except Exception as error:
        print f, error    

print "All done"
