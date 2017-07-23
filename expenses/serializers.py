from rest_framework import serializers
from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('spent_by', 'spent_for', 'amount_spent', 'spent_for_purpose', 'spent_at')
