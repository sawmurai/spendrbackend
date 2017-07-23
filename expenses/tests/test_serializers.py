# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from expenses.models import Expense, Person, BudgetGroup
from expenses.serializers import BudgetGroupSerializer, ExpenseSerializer, PersonSerializer
from datetime import datetime


class ExpensesSerializerTestCase(TestCase):
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
                'id': str(expense.id), 'spent_at': '2017-05-17T00:00:00',
                'spent_for': spent_for.id, 'spent_for_purpose': u'',
                'spent_by': spent_by.id, 'amount_spent': u'100.00'

            },
            serializer.data
        )


class PersonSerializerTestCase(TestCase):
    def test_serializes_correctly(self):
        """
        Test that only specific fields are serialized
        """

        person = Person(username = "Person 1")
        serializer = PersonSerializer(person)
        self.assertEqual(
            {
                'id': str(person.id), 'username': person.username

            },
            serializer.data
        )


class BudgetGroupSerializerTestCase(TestCase):
    def test_serializes_correctly(self):
        """
        Test that only specific fields are serialized
        """

        budget_group = BudgetGroup(name = "Funky group")
        serializer = BudgetGroupSerializer(budget_group)
        self.assertEqual(
            {
                'id': str(budget_group.id), 'name': budget_group.name

            },
            serializer.data
        )
