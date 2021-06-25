import pyttsx3
import PyPDF2
book = open('object_oriented_python_tutorial.pdf', 'rb')
# download a file in audiobook folder then enter the name in line 3
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()