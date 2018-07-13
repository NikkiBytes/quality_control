#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:4:58 2018

@author: nikkibytes

 Script to remove files from func in derivatives
"""


import os
import glob
import shutil



basepath = "/projects/niblab/bids_projects/Experiments/Bevel/data"
derivpath = os.path.join(basepath, "derivatives")

subjects=glob.glob(os.path.join(derivpath, "sub-*"))


funcs = glob.glob(os.path.join(derivpath, "sub-*", "func", "*nii.gz*"))

for funcpath in funcs:
    print(funcpath)
    os.remove(funcpath)


motions = glob.glob(os.path.join(derivpath, "sub-*", "func", "motion_assessment", "*txt"))

for motodir in motions:
    print(motodir)
    os.remove(motodir)

pngs = glob.glob(os.path.join(derivpath, "sub-*", "func", "motion_assessment", "*png"))

for img in pngs:
    print(img)
    os.remove(img)

analysis = glob.glob(os.path.join(derivpath, "sub-*", "func", "Analysis", "feat1", "*feat1"))

for file in analysis:
    print(file)
    shutil.rmtree(file)
