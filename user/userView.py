from django.shortcuts import render, redirect
from django.views import View
from .authenticationUser import *
from django.http.response import HttpResponse
from .userRepository import *

# Create your views here.
class UserToken(View):
    def get(self, request):
        user = authenticate(username='user', password='a1b2c3')
        if user:
            return HttpResponse(generateToken(user))
        return HttpResponse('User not authenticated')
    
class UserLogin(View):
    def get(self, request):
        return render(request, 'authentificationUser.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username, password)
        if user:
            token = generateToken(user)
            request.session['token'] = token  # Armazena o token na sessão
            return redirect('Weather View')
        return HttpResponse('User not authenticated')

class UserInsert(View):
    def get(self, request):
        return render(request, 'create_user.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        user_repo = UserRepository('users')  # 'users' é o nome da coleção no MongoDB
        
        # Verifica se o username já está em uso
        filter = {'username': username}
        existing_user = user_repo.get(filter)
        if existing_user:
            return render(request, 'create_user.html', {'error_message': 'Username already exists. Please choose a different one.'})
        
        # Cria o novo usuário
        user_repo.insert({
            'username': username,
            'password': password,
            'email': email
        })
        return redirect('User Login')

class userForget(View):
    def get(self, request):
        return render(request, 'forgot_password.html')

class UserEdit(View):
    def get(self, request, user_id):
        user_repo = UserRepository('users')
        user = user_repo.get_by_id(user_id)
        if not user:
            return HttpResponse('User not found', status=404)
        
        return render(request, 'edit_user.html', {'user': user})

    def post(self, request, user_id):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        user_repo = UserRepository('users')
        user = user_repo.get_by_id(user_id)
        if not user:
            return HttpResponse('User not found', status=404)
        
        user_repo.update(user_id, {
            'username': username,
            'password': password,
            'email': email
        })
        return redirect('User Login')

class UserDelete(View):
    def get(self, request, user_id):
        user_repo = UserRepository('users')
        user = user_repo.get_by_id(user_id)
        if not user:
            return HttpResponse('User not found', status=404)
        
        user_repo.delete(user_id)
        return HttpResponse('User deleted successfully')
