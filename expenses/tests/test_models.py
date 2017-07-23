# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from expenses.models import Expense, Person, BudgetGroup
from django.core.exceptions import ValidationError


class ExpensesTestCase(TestCase):
    def test_can_add_expense_from_person_to_group(self):
        """
        A person can spent money for a budget group
        """
        spent_by = Person(username = "Person 1")
        budget_group = BudgetGroup()

        expense = Expense(spent_by = spent_by, budget_group = budget_group, amount_spent = 100)

        self.assertIsNotNone(expense)

    def test_can_add_expense_from_person_for_person(self):
        """
        A person can spent money for another person
        """
        spent_by = Person(username = "Person 1")
        spent_for = Person(username = "Person 2")
        budget_group = BudgetGroup()

        expense = Expense(spent_by = spent_by, spent_for = spent_for, budget_group = budget_group, amount_spent = 100)

        self.assertIsNotNone(expense)

    def test_can_not_spend_without_spent_by(self):
        """
        A spent_by is always required
        """
        spent_for = Person(username = "Person 2")
        budget_group = BudgetGroup()

        expense = Expense(spent_for = spent_for, budget_group = budget_group, amount_spent = 100)

        self.assertRaises(Person.DoesNotExist, expense.clean)

    def test_can_not_spend_negative_amount(self):
        """
        Creating a negative expense is not possible
        """
        spent_by = Person(username = "Person 1")
        spent_for = Person(username = "Person 2")
        budget_group = BudgetGroup()

        expense = Expense(spent_by = spent_by, spent_for = spent_for, budget_group = budget_group, amount_spent = -100)

        self.assertRaises(ValidationError, expense.clean)

    def test_can_not_spend_zero_amount(self):
        """
        Creating a negative expense is not possible
        """
        spent_by = Person(username = "Person 1")
        spent_for = Person(username = "Person 2")
        budget_group = BudgetGroup()

        expense = Expense(spent_by = spent_by, spent_for = spent_for, budget_group = budget_group, amount_spent = 0)

        self.assertRaises(ValidationError, expense.clean)


class PersonTestCase(TestCase):
    def test_new_person_is_anonymous_by_default(self):
        """
        Make sure there is always a default username "anonymous" set
        """
        person = Person()
        self.assertEqual("anonymous", person.username)


class BudgetGroupTestCase(TestCase):
    def test_budget_group_to_string(self):
        """
        The string representation of a budget group equals its name
        """
        budget_group = BudgetGroup(name = "Funky group")

        self.assertEqual("Funky group", budget_group.name)
