
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def receipes(request):
    queryset = Recipe.objects.filter(user=request.user)
    if request.method == "POST":
        recipe_name = request.POST.get('recipe_name')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=description,
            recipe_image=image
        )

        return redirect('/receipes/')

    queryset = Recipe.objects.all()
   
    return render(request, 'recipe.html', {'recipes': queryset})

def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == "POST":
        recipe.delete()
        return redirect('/receipes/')

    return redirect('/receipes/')


def register(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            password=password
        )

        messages.success(request, "Registration successful!")
        return redirect('login')

    return render(request, 'register.html')

def login_page(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('receipes')

        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')

    return render(request, 'login.html')

def logout_page(request):

    logout(request)

    return redirect('login')