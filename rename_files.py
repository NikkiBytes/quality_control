#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 16:54:38 2018

@author: nikkibytes
"""
import glob
import os

dirs = glob.glob('/Users/nikkibytes/Documents/BevBits/Raw/ses-2/bbx*')

for folder in dirs:
   # print(folder)
    name = folder.split('/')[7]
    sub = name.split('_')[1].split('w')[0]
    #print(sub)
    out = '/Users/nikkibytes/Documents/BevBits/Raw/ses-2/sub-%s'%sub
    print(out)
    os.rename(folder, out )