from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data, context = {'request': request})
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']

        token, create = Token.objects.get_or_create(user = user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

"""
    {
        "token": "b9008725060fc8efb48e08377ef3e5fa52751ab5",
        "user_id": 1,
        "email": "playeando.97@gmail.com"
    }
"""  

# Create your views here.
