import pprint

from PyPDF2 import PdfFileReader, PdfFileMerger
import PyPDF2
from os import walk


if __name__ == '__main__':
    filenames = next(walk("."), (None, None, []))[2]
    infiles = []
    print("searching...")
    for name in filenames:
        #print(name[-4:])
        if(name[-4:]==".pdf"):
            print(name);
            infiles.append(name)
    print("processing...")
    for name in infiles:
        print(name)
        file_in = open(name, 'rb')
        pdf_reader = PdfFileReader(file_in)
        try:
            metadata = pdf_reader.getDocumentInfo()
            pprint.pprint(metadata)

            pdf_merger = PdfFileMerger()
            pdf_merger.append(file_in)
            pdf_merger.addMetadata({
                '/Title': name[:-4]
            })
            
            file_out = open(name, 'wb')
            pdf_merger.write(file_out)
            file_in.close()
            file_out.close()
        except PyPDF2.errors.PdfReadError:
            print("File encrypted! Skipping")
        
