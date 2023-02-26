import boto3

# create client object
rekognition = boto3.client('rekognition')

# specify the image file to analyze
with open('example.jpg', 'rb') as image_file:
    image_bytes = image_file.read()

# call the detect_labels method to detect objects and scenes in the image
response = rekognition.detect_labels(Image={'Bytes': image_bytes})

# print the detected labels
for label in response['Labels']:
    print(label['Name'], label['Confidence'])
