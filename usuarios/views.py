from django.shortcuts import redirect, render
from usuarios.forms import FormLogin
from django.contrib import auth, messages


def login(request):
    form = FormLogin()

    if request.method == 'POST':
        form = FormLogin(request.POST)

        if form.is_valid():
            usuario = form['usuario'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(request, username=usuario, password=senha)

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, "Login realizado com sucesso")
                return redirect('index')
            else:
                messages.error(request, "Erro ao realizar o Login!")
                return redirect('login')
                

    return render(request, 'usuarios/login.html', {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('login')