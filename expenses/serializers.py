from rest_framework import serializers
from .models import BudgetGroup, Expense, Person


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('id', 'spent_by', 'spent_for', 'amount_spent', 'spent_for_purpose', 'spent_at')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'username')


class BudgetGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetGroup
        fields = ('id', 'name')

