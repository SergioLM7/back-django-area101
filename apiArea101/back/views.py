from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.decorators import api_view

#Function to send the welcome message in the main URL
@api_view(['GET'])
def welcome(request):
    return JsonResponse({"message": "¡Bienvenido a nuestra API de los libros más veniddos en España!"})

#Function to get all books in a JSON
@api_view(['GET'])
def books_list(request):
    books = [
        {"id": 1, "titulo": "El capitán Alatriste", "autor": "Arturo Pérez-Reverte", "precio": 20.0, "imagen": "https://m.media-amazon.com/images/I/81mq+3Soh+L._AC_UF894,1000_QL80_.jpg", "url":"https://www.amazon.es/capitán-Alatriste-aventuras-CAPITAN-ALATRISTE/dp/8420483532"},
        {"id": 2, "titulo": "Maldito United", "autor": "David Peace", "precio": 19.86, "imagen": "https://m.media-amazon.com/images/I/51Io6cDUf-S._AC_UF894,1000_QL80_.jpg", "url":"https://www.amazon.es/Maldito-United-David-Peace/dp/8494403303"},
        {"id": 3, "titulo": "La sombra del viento", "autor": "Carlos Ruiz Zafón", "precio": 15.0, "imagen": "https://m.media-amazon.com/images/I/71BS32NFrsL._AC_UF894,1000_QL80_.jpg", "url":"https://www.amazon.es/Sombra-Viento-Biblioteca-Carlos-Zafón/dp/8408163434"},
        {"id": 4, "titulo": "Harry Potter y el cáliz de fuego", "autor": "JK Rowling", "precio": 19.5, "imagen": "https://m.media-amazon.com/images/I/91a2FifMS8L._AC_UF894,1000_QL80_.jpg", "url":"https://www.amazon.es/Harry-Potter-Caliz-Fuego-Rowling/dp/8478886451"},
        {"id": 5, "titulo": "El tiempo entre costuras", "autor": "María Dueñas", "precio": 25.3, "imagen": "https://m.media-amazon.com/images/I/71k3KwMlt8L._AC_UF894,1000_QL80_.jpg", "url":"https://www.amazon.es/El-tiempo-entre-costuras-Novela/dp/8484607917"},
        {"id": 6, "titulo": "La isla de la mujer dormida", "autor": "Arturo Pérez-Reverte", "precio": 22.90, "imagen": "https://m.media-amazon.com/images/I/81N3fc5id5L._AC_UF894,1000_QL80_.jpg", "url":"https://www.amazon.es/isla-Mujer-Dormida-Hispánica/dp/8410299631"},
        {"id": 7, "titulo": "El clan", "autor": "Carmen Mola", "precio": 21.90, "imagen": "https://m.media-amazon.com/images/I/71aoW-+kY+L._AC_UF894,1000_QL80_.jpg", "url":"https://www.amazon.es/Clan-Inspectora-Elena-Blanco-Planeta/dp/8408291262"},
        {"id": 8, "titulo": "El niño que perdió la guerra", "autor": "Julia Navarro", "precio": 24.90, "imagen": "https://m.media-amazon.com/images/I/81rVDjUau+L._AC_UF894,1000_QL80_.jpg", "url":"https://www.amazon.es/niño-que-perdió-guerra-Éxitos/dp/8401027977"},
        {"id": 9, "titulo": "Nexus", "autor": "Yuval Noha Harari", "precio": 23.90, "imagen": "https://m.media-amazon.com/images/I/715fA0g27aL._AC_UF894,1000_QL80_.jpg", "url":"https://www.amazon.es/Nexus-breve-historia-información-Piedra/dp/8419951021"},
        {"id": 10, "titulo": "Redes", "autor": "Eloy Moreno", "precio": 15.95, "imagen": "https://m.media-amazon.com/images/I/71qlSpgJHBL._AC_UF894,1000_QL80_.jpg", "url":"https://www.amazon.es/Redes-Invisible-2-Nube-Tinta/dp/8418050357"},
    ]
    return JsonResponse(books, safe=False, status=200)

#Test User
SIMULATED_USER = {
    "username": "userArea101",
    "password": "passwordArea101"
}

#Function to check the user who is logining and create the token
@api_view(['POST'])
def token_obtain_simulated(request):
    username = request.data.get("username")
    password = request.data.get("password")
    
    if username == SIMULATED_USER["username"] and password == SIMULATED_USER["password"]:
        user = User(username=username)
        token = AccessToken.for_user(user)
        return Response({"access": str(token)}, status=status.HTTP_200_OK)
    
    return Response({"error": "Credenciales incorrectas"}, status=status.HTTP_401_UNAUTHORIZED)