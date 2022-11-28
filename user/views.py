from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .serializers import LoginSerializer, RegisterSerializer, UserSerializer
from .utility import create_token, generate_access_token

User = get_user_model()


# LOGIN API
@permission_classes((AllowAny,))
class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, req):
        serializer = self.get_serializer(data=req.data)
        if not serializer.is_valid():
            return Response({"error": serializer.errors, "data": None}, status=400)
        if req.data["email"] is not None or req.data['email'] != "":
            user = generics.get_object_or_404(User, email=req.data["email"])
            token = generate_access_token(user)
            if token:
                res = {
                    "token": token,
                    "user": {
                        "id": user.id,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "email": user.email,
                        "phone_no": user.phone_no,
                        "profile_picture": user.profile_picture,
                    }
                }
                return Response({"data": res, "error": None}, status=201)
            else:
                return Response({"data": None, "error": "Invalid Username/Password"}, status=400)


# REGISTER VIEW
@permission_classes((AllowAny,))
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, req):
        serializer = self.get_serializer(data=req.data)
        if not serializer.is_valid():
            return Response({"error": serializer.errors, "data": None}, status=400)
        check_user = User.objects.filter(username=req.data["email"])
        if not check_user:
            user = User.objects.create_user(
                name=req.data['name'],
                # last_name=req.data['last_name'],
                username=req.data['email'],
                email=req.data['email'],
                password=req.data['password'],
            )
            user.save()
            return Response({"data": "User Created Successfully!", "error": None}, status=201)
        else:
            return Response({"data": None, "error": "User with this email already exist."}, status=400)


class SpecificUserView(APIView):
    def get(self, req, id):
        user = get_object_or_404(User, pk=id)

        res = UserSerializer(user)
        return Response({"data": res.data, "error": None}, status=200)

    def patch(self, req, id):
        user = get_object_or_404(User, pk=id)
        serializer = UserSerializer(user, data=req.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


@permission_classes((IsAuthenticated,))
class UserView(APIView):
    def get(self, req):
        user = User.objects.all()
        response = UserSerializer(user, many=True)
        return Response({"data": response.data, "error": None}, status=200)
