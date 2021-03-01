import PyPDF2

pdf_file = open('meetingminutes1.pdf', 'rb')

reader = PyPDF2.PdfFileReader(pdf_file)

print(reader.numPages)

page = reader.getPage(0)
print(page.extractText())
