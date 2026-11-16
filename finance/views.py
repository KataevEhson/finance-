from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import *







def registration(request):
    if request.method == 'POST':
        data = request.POST
        if data:
            User.objects.create_user(
                username = data['username'],
                password = data['password'],
                email = data['email'],
            )
        else:
            return redirect('registration')
        return redirect("login")
    return render(request, 'registration.html')


def login_user(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate(request, username = data['username'], password = data['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')



@login_required
def home(request):
    wallets = Wallet.objects.filter(user_id=request.user)
    return render(request, 'home.html', {'wallets': wallets})






@login_required
def create_wallet(request):
    if request.method == 'POST':
        Wallet.objects.create(user_id=request.user, balance=request.POST['balance'])
        return redirect('home')
    return render(request, 'create_wallet.html')






@login_required
def withdraw(request):
    wallets = Wallet.objects.filter(user_id=request.user)
    if request.method == 'POST':
        wallet = wallets.get(pk=request.POST['wallet'])
        wallet.balance -= int(request.POST['amount'])
        wallet.save()
        return redirect('add_history')
    return render(request, 'withdraw.html', {'wallets': wallets})



@login_required
def deposit(request):
    wallets = Wallet.objects.filter(user_id=request.user)
    if request.method == 'POST':
        wallet = wallets.get(pk=request.POST['wallet'])
        amount = int(request.POST['amount'])
        wallet.balance += amount
        wallet.save()
        return redirect('add_history')
    return render(request, 'deposit.html', {'wallets': wallets})










@login_required
def create_history(request):
    wallets = Wallet.objects.filter(user_id=request.user)
    if request.method == 'POST':
        data = request.POST
        History_tranzaction.objects.create(
            wallet_id= wallets.get(pk=data['wallet']),
            amount=data['amount'],
            type_tranzaction=data['type_tranzaction'],
            info=data['info']
        )
        return redirect('home')
    return render(request, 'add_history.html', {'wallets': wallets})










@login_required
def history(request):
    histories = History_tranzaction.objects.filter(wallet_id__user_id = request.user)
    return render(request, 'history.html', {'histories': histories})


@login_required
def delete_history(request, pk):
    if request.method == 'POST':
        history = History_tranzaction.objects.get(pk=pk)
        history.delete()
        return redirect('show_authors')


    return redirect('show_authors')

