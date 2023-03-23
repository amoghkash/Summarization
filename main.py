from pdf_handler import PDF
from model import Model

pdf = PDF("test.pdf")

model = Model("INSERT KEY HERE")

summarization = model.summarize(pdf.getText())


print(summarization)