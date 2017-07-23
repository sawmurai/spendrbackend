# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from expenses.models import Expense, Person, BudgetGroup
from expenses.serializers import ExpenseSerializer
from datetime import datetime


class ExpensesTestCase(TestCase):
    def test_serializes_correctly(self):
        """
        Test that only specific fields are serialized
        """

        spent_by = Person(username = "Person 1")
        spent_for = Person(username = "Person 2")
        budget_group = BudgetGroup()
        spent_at = datetime(2017, 05, 17)

        expense = Expense(spent_by = spent_by, spent_for = spent_for, budget_group = budget_group, amount_spent = 100,
                          spent_at = spent_at)

        serializer = ExpenseSerializer(expense)
        self.assertEqual(
            {
                'spent_at': '2017-05-17T00:00:00',
                'spent_for': spent_for.id, 'spent_for_purpose': u'',
                'spent_by': spent_by.id, 'amount_spent': u'100.00'

            },
            serializer.data
        )

