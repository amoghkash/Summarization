# importing required modules
import PyPDF2


class PDF():
    def __init__(self, pdfName):
        # creating a pdf file object
        self.pdfFileObj = open(pdfName, 'rb')
        
        # creating a pdf reader object
        self.pdfReader = PyPDF2.PdfReader(self.pdfFileObj)
  
    def getText(self):
        # creating a page object
        pageObj = self.pdfReader.pages[0]
        
        # extracting text from page
        text = pageObj.extract_text()
        text = text[169:len(text)]
        return(text)
        
    def close(self):
        # closing the pdf file object
        self.pdfFileObj.close()


pdf=PDF('test.pdf')

text = pdf.getText()

print(text)