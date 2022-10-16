# RUN: python .\merge_pdfs.py .\pdf\dummy.pdf .\pdf\twopage.pdf .\pdf\tilt.pdf


import PyPDF2
import sys

inputs = sys.argv[1:] # Collect all PDF files given to the script from the command-line


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger() # Initialize a Merger object from PyPDF2
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf) # append the pages of the files to the merger object
    merger.write('pdf/super.pdf')

pdf_combiner(inputs)
