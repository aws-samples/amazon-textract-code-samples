import boto3
import json
from trp import Document
from tabulate import tabulate

#create a Textract Client
textract = boto3.client('textract')
#Document
documentName = image_filename

response = None
with open(image_filename, 'rb') as document:
    imageBytes = bytearray(document.read())

# Call Textract AnalyzeDocument by passing a document from local disk
response = textract.analyze_document(
    Document={'Bytes': imageBytes},
    FeatureTypes=["FORMS",'SIGNATURES']
)

#print detected text
d = []
for item in response["Blocks"]:
    if item["BlockType"] == "SIGNATURE":
        d.append([item["Id"],item["Geometry"]])

print(tabulate(d, headers=["Id", "Geometry"],tablefmt="grid", maxcolwidths= [None,100]))


doc = Document(response)
d = []

for page in doc.pages:
    # Search fields by key
    print("\nSearch Fields:")
    key = "Signature"
    fields = page.form.searchFieldsByKey(key)
    for field in fields:
        d.append([field.key, field.value])        

print(tabulate(d, headers=["Key", "Value"]))
