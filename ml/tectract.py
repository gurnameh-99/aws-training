import boto3

# create client object
textract = boto3.client('textract')

# specify the document file to analyze
with open('example.pdf', 'rb') as document_file:
    document_bytes = document_file.read()

# call the analyze_document method to extract text and data from the document
response = textract.analyze_document(Document={'Bytes': document_bytes}, FeatureTypes=['TABLES', 'FORMS'])

# print the detected text and data
for block in response['Blocks']:
    if block['BlockType'] == 'LINE':
        print(block['Text'])
    elif block['BlockType'] == 'TABLE':
        for row in block['Table']['Rows']:
            row_text = []
            for cell in row['Cells']:
                row_text.append(cell['Text'])
            print('\t'.join(row_text))
    elif block['BlockType'] == 'SELECTION_ELEMENT':
        if block['SelectionStatus'] == 'SELECTED':
            print('[X] ' + block['Text'])
        else:
            print('[ ] ' + block['Text'])
