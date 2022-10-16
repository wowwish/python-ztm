import PyPDF2

# Read the input PDF
input_pdf = PyPDF2.PdfFileReader(open('pdf/super.pdf', 'rb'))
# Read the PDF with the watermark and get the corresponding page with the watermark template
watermark_page = PyPDF2.PdfFileReader(open('pdf/wtr.pdf', 'rb')).getPage(0)
output = PyPDF2.PdfFileWriter() # Initialize the writer object to append page data

for i in range(input_pdf.getNumPages()): # loop through each page of the input PDF
    page = input_pdf.getPage(i) # get each page of the input PDF
    page.mergePage(watermark_page) # merge the Page data with the watermark page data
    output.addPage(page) # append the merged data as a page into the output writer object

with open('pdf/watermarked_output.pdf', 'wb') as output_file: # Open an output file stream to write the binary data
    output.write(output_file) # save the binary PDF data into the output file
