from pypdf import PdfReader
reader = PdfReader("tmp/Тестовое задание.pdf")
print(reader.pages)
print(len(reader.pages))

print(reader.pages[1].extract_text())