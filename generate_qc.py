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
                
                cairosvg.svg2png(url=img, write_to=out) #convert svg 
                
    
            
    #iterate through currently made images and write details to file
    pngs = glob.glob(os.path.join(dpath, sub, 'pdfs', '*png'))
    
    for png in pngs:
       
        name = pdf.split('/')
        for word in name:  
            if '.pdf' in word:
                filename = word.split('.')[0]
                
        with open(png, 'rb') as f:
            image = f.read()
            
        with open('fileXX.doc', 'wb') as f:
            f.write(image)
            f.close
                
        packet = io.BytesIO()
        c = canvas.Canvas(packet, pagesize=letter)
        c.drawString(10,100, "Filename: %s"%filename)
        c.save()
        packet.seek(0)
        input = PdfFileReader(packet)
        
        orig_pdf = PdfFileReader(open(pdf, "rb"))
        output = PdfFileWriter()
        
        page = orig_pdf.getPage(0)
        page.mergePage(input.getPage(0))
        output.addPage(page)
        # finally, write "output" to a real file
        outputStream = open("destination.pdf", "wb")
        output.write(outputStream)
        outputStream.close()
        
def main():
    global basepath
    basepath= '/Users/nikkibytes/Documents/BevBits'
    deriv_path = os.path.join(basepath, 'derivatives')
    fmriprep_path = os.path.join(basepath, 'fmriprep')
    
    subs = glob.glob(os.path.join(deriv_path, 'sub-*'))
    for sub_path in subs:
        words = sub_path.split('/')
        for w in words:
            if 'sub-' in w:
                sub = w
        print(w)
        getPDFs(deriv_path, sub, fmriprep_path)
        #mergePDFS(sub)
main()