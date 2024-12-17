# views.py
from django import forms
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Sample user data (Account Number: [PIN, Balance])
USERS = {
    "123456": {"pin": "1234", "balance": 5000},
    "654321": {"pin": "5678", "balance": 3000},
}

CURRENT_USER = None


def home(request):
    if request.method == "POST":
        account_number = request.POST.get("account_number")
        pin = request.POST.get("pin")
        if account_number in USERS and USERS[account_number]["pin"] == pin:
            global CURRENT_USER
            CURRENT_USER = account_number
            return redirect("menu")
        else:
            return render(request, "home.html", {"error": "Invalid account number or PIN."})

    return render(request, "home.html")


def menu(request):
    """Display ATM menu options."""
    if not CURRENT_USER:
        return redirect("home")

    return render(request, "menu.html")


def check_balance(request):
    """Display the current balance."""
    if not CURRENT_USER:
        return redirect("home")

    balance = USERS[CURRENT_USER]["balance"]
    return render(request, "check_balance.html", {"balance": balance})


def deposit_money(request):
    """Handle deposit functionality."""
    if not CURRENT_USER:
        return redirect("home")

    if request.method == "POST":
        amount = float(request.POST.get("amount"))
        USERS[CURRENT_USER]["balance"] += amount
        return render(request, "deposit_money.html", {"success": f"${amount} deposited successfully!"})

    return render(request, "deposit_money.html")


def withdraw_money(request):
    """Handle withdraw functionality."""
    if not CURRENT_USER:
        return redirect("home")

    if request.method == "POST":
        amount = float(request.POST.get("amount"))
        if amount <= USERS[CURRENT_USER]["balance"]:
            USERS[CURRENT_USER]["balance"] -= amount
            return render(request, "withdraw_money.html", {"success": f"${amount} withdrawn successfully!"})
        else:
            return render(request, "withdraw_money.html", {"error": "Insufficient balance."})

    return render(request, "withdraw_money.html")


def change_pin(request):
    """Handle PIN change functionality."""
    if not CURRENT_USER:
        return redirect("home")

    if request.method == "POST":
        new_pin = request.POST.get("new_pin")
        USERS[CURRENT_USER]["pin"] = new_pin
        return render(request, "change_pin.html", {"success": "PIN changed successfully!"})

    return render(request, "change_pin.html")


def logout(request):
    """Logout the current user."""
    global CURRENT_USER
    CURRENT_USER = None
    return redirect("home")