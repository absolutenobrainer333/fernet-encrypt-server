from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response

from cryptography.fernet import Fernet

from .utils.base64util import convertStringToBase64String


class FernetEncryption(CreateAPIView):
    def create(self, request, *args, **kwargs):
        key, data = request.data["key"], request.data["data"]
        fernetEncryptAlgorithm = Fernet(convertStringToBase64String(key))
        encryptedString = fernetEncryptAlgorithm.encrypt(str.encode(data))
        return Response(encryptedString, status=status.HTTP_200_OK)


class FernetDecryption(CreateAPIView):
    def create(self, request, *args, **kwargs):
        key, data = request.data["key"], request.data["data"]
        try:
            fernetEncryptAlgorithm = Fernet(convertStringToBase64String(key))
            decryptedString = fernetEncryptAlgorithm.decrypt(data)
            return Response(decryptedString, status=status.HTTP_200_OK)
        except:
            return Response("Incorrect key", status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
