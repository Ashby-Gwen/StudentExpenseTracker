# models.py
from django.db import models
from django.contrib.auth.models import User

# Expense Categories
CATEGORY_CHOICES = [
    ('Food', 'Food'),
    ('Transportation', 'Transportation'),
    ('School Supplies', 'School Supplies'),
    ('Rent', 'Rent'),
    ('Miscellaneous', 'Miscellaneous')
]

# Expense Model
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.category} - {self.amount}'

# Budget Model
class Budget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    monthly_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'Budget for {self.user.username}: {self.monthly_budget}'
