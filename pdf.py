import PyPDF2 # Import the module used to work with pdf files

with open('pdf/dummy.pdf', 'rb') as f: # Read the file in binary mode to prevent errors
    reader = PyPDF2.PdfFileReader(f)
    print("No. of pages in dummy.pdf : ", reader.numPages)
    print("First Page as an Object : ")
    page = reader.getPage(0)
    print(page)
    page.rotateCounterClockwise(90) # Rotate the page counter-clockwise 90 degrees
    writer = PyPDF2.PdfFileWriter() # Initialize a writer object
    writer.addPage(page) # Add the tilted page object as the first page to the pdf writer
    with open('pdf/tilt.pdf', 'wb') as out_file: # Open an output filestream for the binary PDF data
        writer.write(out_file) # write the writer object with all its pages into the output file

