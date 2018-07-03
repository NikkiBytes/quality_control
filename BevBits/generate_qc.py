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
                filename=word+'.pdf'
                out=os.path.join(dpath, sub, 'pdfs', filename) #output pdf filename
                
                cairosvg.svg2pdf(url=img, write_to=out) #convert svg 
                
    
    #iterate through currently made images and write details to file
    pdfs = glob.glob(os.path.join(dpath, sub, 'pdfs', '*pdf'))
    
    for pdf in pdfs:
       
        name = pdf.split('/')
        for word in name:  
            if '.pdf' in word:
                filename = word.split('.')[0]
                
        new_dest = os.path.join('derivatives', sub, 'pdfs', filename+"_01.pdf")
    
    
        packet = io.BytesIO()

        c = canvas.Canvas(packet)
        c.drawString(10,100, "FILENAME: %s"%filename)  
        c.save()

        pdf3 = os.path.join('derivatives', sub, 'pdfs', 'complete_pdfs',filename+".pdf")

        packet.seek(0)
        pdf2 = PdfFileReader(packet)
        
        existing_pdf = PdfFileReader(open(pdf, 'rb'))
        output = PdfFileWriter()
        
        page = existing_pdf.getPage(0)
        page.mergePage(pdf2.getPage(0))
        output.addPage(page)
        
        outputStream = open(pdf3, "wb")
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