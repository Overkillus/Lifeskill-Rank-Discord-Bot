import os
from google.cloud import vision
from google.cloud.vision import types
from urllib.request import urlopen, Request
import base64
import binascii

def text_from_image_google(url):
    # enter own location of Google Cloud credentials here
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'keys/googleVisionAPIToken.json'
    client = vision.ImageAnnotatorClient()

    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(request).read()
    encoded_image = base64.b64encode(page)
    content = binascii.a2b_base64(encoded_image)

    visionImage = vision.types.Image(content=content)
    visionResponse = client.text_detection(image=visionImage)

    print(visionResponse.full_text_annotation.text)
    return visionResponse.full_text_annotation.text