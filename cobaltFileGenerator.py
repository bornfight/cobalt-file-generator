import os, sys
from docx import Document

directoryName = "generated-test-files"
defaultPack = ['jpg', 'jpeg', 'pdf', 'png', 'docx', 'gif', 'doc']
magicNumbers = {
	"jpg" : bytearray.fromhex("FF D8 FF DB"),
	"jpeg" : bytearray.fromhex("FF D8 FF EE"),
	"pdf" : bytearray.fromhex("25 50 44 46 2d"),
	"png" : bytearray.fromhex("89 50 4E 47 0D 0A 1A 0A"),
	"docx" : bytearray.fromhex("50 4B 03 04 14 00 00 00 08 00 6F 6E 74 65 6E 74 5F 54 79"),
	"doc" : bytearray.fromhex("D0 CF 11 E0 A1 B1 1A E1"),
	"gif" : bytearray.fromhex("47 49 46 38 37 61")
}

def createFile(extension):
	global directoryName
	global magicNumbers
	fileName = directoryName + '/' + extension + 'TestFile.' + extension
	if(extension == "docx" or extension == "doc"):
		document = Document()
		document.add_heading('Test Heading', 0)
		document.add_paragraph('Test Paragraph')
		document.save(fileName)
	else:
		open(fileName, 'a').close()
		f = open(fileName, mode='w+b')
		f.write(magicNumbers[extension])
		f.close()

if os.path.exists(directoryName):
	os.system('rm -rf '+ directoryName)

os.mkdir(directoryName)

if len(sys.argv) > 1:
	for extension in sys.argv:
		if extension in magicNumbers:
			createFile(extension)
else: ## if there are no args provided generate files from defaultPack
	for extension in defaultPack:
		createFile(extension)

