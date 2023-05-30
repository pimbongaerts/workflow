#!/usr/bin/env python
"""
Change current folder to basepath of specific model or timepoint
"""
import os
import sys

BASEPATH = "/mnt/coral3d/focal_plots"

model_arg = sys.argv[1]
cols = model_arg.split('_')
if len(cols) == 4:
    target_path = '{0}/{1}_{2}/{1}_{2}_{3}/{1}_{2}_{3}_{4}/'.format(BASEPATH,
                                                                       cols[0], cols[1], cols[2], cols[3])
elif len(cols) == 3:
    target_path = '{0}/{1}_{2}/{1}_{2}_{3}/'.format(BASEPATH, cols[0], cols[1], cols[2])
elif len(cols) == 2:
    target_path = '{0}/{1}/'.format(BASEPATH, model_arg)
else:
    sys.exit('Incorrect model name')

os.chdir(target_path)