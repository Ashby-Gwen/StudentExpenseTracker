# forms.py
from django import forms
from .models import Expense, Budget

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'description']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['monthly_budget']