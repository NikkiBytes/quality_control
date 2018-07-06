#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 14:58:40 2018

@author: nikkibytes

"""


from PyPDF2 import PdfFileMerger,PdfFileWriter, PdfFileReader
import os 
import cairosvg
import io
import glob
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch



def mergePDFs(sub):
    pdfs = glob.glob(os.path.join(basepath, 'figures', '*.pdf'))
    merger = PdfFileMerger()

    for pdf in pdfs: 
        merger.append(pdf)
    
    merger.write("result.pdf")

def getPDFs(dpath,sub, fpath):
    #data/fmriprep/ses-1/sub-001/fmriprep/sub-001
    svgs= glob.glob(os.path.join(fpath,sub, 'fmriprep',sub, 'figures', '*flt_bbr.svg'))
    for img in svgs:
        # get our current filename 
        name = img.split('/')
        for word in name:  
            if '.svg' in word:
                word = word.split('.')[0]
                filename=word+'.png'
                out=os.path.join(dpath, sub, 'pdfs', filename) #output pdf filename
                
                #cairosvg.svg2png(url=img, write_to=out) #convert svg 
            
            
                
            
    #iterate through currently made images and write details to file
    pngs = glob.glob(os.path.join(dpath, sub, 'pdfs', '*png'))
    for png in pngs:
        print(png)
        name = png.split('/')
        for word in name:  
            if '.png' in word:
                filename = word.split('.')[0]
                print(filename)
        
        c = canvas.Canvas("mypdf.pdf", pagesize=letter)
        c.setFont('Helvetica', 20)

        c.drawString(30, 750, "FILENAME: %s"%filename )
        
       
        
        c.drawImage(png, inch, height-2 * inch )
        c.showPage()
        c.save()
    
      
def main():
    global basepath
    basepath= '/Users/nikkibytes/Documents/quality_control/BevBits'
    deriv_path = os.path.join(basepath, 'derivatives')
    fmriprep_path = os.path.join(basepath, 'fmriprep')
    
    subs = glob.glob(os.path.join(deriv_path, 'sub-*'))
    for sub_path in subs:
        words = sub_path.split('/')
        for w in words:
            if 'sub-' in w:
                sub = w
        getPDFs(deriv_path, sub, fmriprep_path)
        #mergePDFS(sub)
main()