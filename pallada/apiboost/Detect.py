import asyncio
import io
import glob
import os
import sys
import time
import uuid

import PIL
import requests
from urllib.parse import urlparse
from io import BytesIO
# To install this module, run:
# python -m pip install Pillow
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person

from array import array
import os
from PIL import Image
import sys
import time

# </snippet_imports>

'''
Face Quickstart
Examples include:
- Detect Faces: detects faces in an image.
- Find Similar: finds a similar face in an image using ID from Detect Faces.
- Verify: compares two images to check if they are the same person or not.
- Person Group: creates a person group and uses it to identify faces in other images.
- Large Person Group: similar to person group, but with different API calls to handle scale.
- Face List: creates a list of single-faced images, then gets data from list.
- Large Face List: creates a large list for single-faced images, trains it, then gets data.
Prerequisites:
- Python 3+
- Install Face SDK: pip install azure-cognitiveservices-vision-face
- In your root folder, add all images downloaded from here:
https://github.com/Azure-examples/cognitive-services-..
How to run:
- Run from command line or an IDE
- If the Person Group or Large Person Group (or Face List / Large Face List) examples get
interrupted after creation, be sure to delete your created person group (lists) from the API,
as you cannot create a new one with the same name. Use 'Person group - List' to check them all,
and 'Person Group - Delete' to remove one. The examples have a delete function in them, but at the end.
Person Group API: https://westus.dev.cognitive.microsoft.com/docs/servi..
Face List API: https://westus.dev.cognitive.microsoft.com/docs/servi..
References:
- Documentation: https://docs.microsoft.com/en-us/azure/cognitive-serv..
- SDK: https://docs.microsoft.com/en-us/python/api/azure-cog..
- All Face APIs: https://docs.microsoft.com/en-us/azure/cognitive-serv..
'''

# <snippet_subvars>
# This key will serve all examples in this document.
KEY = "097a60c217bf42f1b8a0104aee08e337"

# This endpoint will be used in all examples in this quickstart.
ENDPOINT = "https://alexdiploma.cognitiveservices.azure.com/"
# </snippet_subvars>

# <snippet_persongroupvars>
# Used in the Person Group Operations and Delete Person Group examples.
# You can call list_person_groups to print a list of preexisting PersonGroups.
# SOURCE_PERSON_GROUP_ID should be all lowercase and alphanumeric. For example, 'mygroupname' (dashes are OK).
PERSON_GROUP_ID = str(uuid.uuid4()) # assign a random ID (or name it anything)

# Used for the Delete Person Group example.
TARGET_PERSON_GROUP_ID = str(uuid.uuid4()) # assign a random ID (or name it anything)
# </snippet_persongroupvars>

'''
Authenticate
All examples use the same client.
'''
# <snippet_auth>
# Create an authenticated FaceClient.
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
# </snippet_auth>
# '''
# END - Authenticate
# '''
#
# '''
# Detect faces
# Detect faces in two images (get ID), draw rectangle around a third image.
# '''
# print('-----------------------------')
# print()
# print('DETECT FACES')
# print()

def faceRec(img):
    faces = face_client.face.detect_with_stream(img)
    if not faces:
        raise Exception('No face detected from image {}'.format(img))
    image_ID = faces[0].face_id
    # print('Detected face ID from', img, ':')
    for face in faces: print(face.face_id)
    # print()
    return image_ID

# image = open('../media/X6hyCvXRq7M_sMpPL4N.jpg', 'r+b')
# image2 = open('../media/simples/sasja1.jpg', 'r+b')

# faceRec(image)

def Verify(ID1, ID2):
    VerifyFaceToFaceRequest = face_client.face.verify_face_to_face(ID1, ID2)
    is_identical = getattr(VerifyFaceToFaceRequest, 'is_identical')
    confidence = getattr(VerifyFaceToFaceRequest, 'confidence')
    if is_identical == False and confidence < 0.5:
        return 0
    else:
        return VerifyFaceToFaceRequest
#
# x =Verify(faceRec(image), faceRec(image2))
# print (x)