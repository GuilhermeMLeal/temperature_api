from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .authenticationUser import authenticate, generateToken
from .userRepository import UserRepository
import bcrypt

class UserLogin(View):
    def get(self, request):
        return render(request, 'authentificationUser.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            token = generateToken(user)
            response = redirect('Weather View')
            response.set_cookie('jwt', token)  # Armazena o token no cookie 'jwt'
            response.set_cookie('user_id', user.id)  # Armazena o ID do usuário no cookie 'user_id'
            return response
        return HttpResponse('User not authenticated')

class UserLogout(View):
    def get(self, request):
        response = redirect('Weather View')
        response.delete_cookie('jwt')
        response.delete_cookie('user_id')  # Deleta o cookie 'user_id'
        return response


class UserInsert(View):
    def get(self, request):
        return render(request, 'create_user.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')
        
        if password != confirm_password:
            return render(request, 'create_user.html', {'error_message': 'Passwords do not match.'})
        
        user_repo = UserRepository('users')
        
        filter = {'username': username}
        existing_user = user_repo.get(filter)
        if existing_user:
            return render(request, 'create_user.html', {'error_message': 'Username already exists. Please choose a different one.'})
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        # Log para depuração
        print(f"Hashed password: {hashed_password}")
        
        user_repo.insert({
            'username': username,
            'password': hashed_password,
            'email': email
        })
        return redirect('User Login')

class UserEdit(View):
    def get(self, request, user_id):
        user_repo = UserRepository('users')
        user = user_repo.getByID(user_id)
        if not user:
            return HttpResponse('User not found', status=404)
        
        return render(request, 'edit_user.html', {'user': user, 'user_id': user_id})

    def post(self, request, user_id):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        user_repo = UserRepository('users')
        user = user_repo.getByID(user_id)
        if not user:
            return HttpResponse('User not found', status=404)
        
        # Hash da senha
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        user_repo.update({
            'username': username,
            'password': hashed_password,
            'email': email
        }, user_id)
        return redirect('User Login')

class UserDelete(View):
    def get(self, request, user_id):
        user_repo = UserRepository('users')
        user = user_repo.getByID(user_id)
        if not user:
            return HttpResponse('User not found', status=404)
        
        return render(request, 'confirm_delete_user.html', {'user': user})

    def post(self, request, user_id):
        user_repo = UserRepository('users')
        user_repo.deleteByID(user_id)
        return HttpResponse('User deleted successfully')


class UserForget(View):
    def get(self, request):
        return render(request, 'forgot_password.html')
        