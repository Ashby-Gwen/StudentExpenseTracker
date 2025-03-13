# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Expense, Budget
from .forms import ExpenseForm, BudgetForm

@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    budget, _ = Budget.objects.get_or_create(user=request.user)
    total_expenses = sum(exp.amount for exp in expenses)
    remaining_budget = budget.monthly_budget - total_expenses
    return render(request, 'dashboard.html', {
        'expenses': expenses,
        'budget': budget,
        'remaining_budget': remaining_budget
    })

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

@login_required
def set_budget(request):
    budget, _ = Budget.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BudgetForm(instance=budget)
    return render(request, 'set_budget.html', {'form': form})