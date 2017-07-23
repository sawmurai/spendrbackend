# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class Person(models.Model):
    """
    Represents an entity that can spend money or be spent money for
    """
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    username = models.CharField(max_length = 100, default = "anonymous")

    def __str__(self):
        return self.username


class BudgetGroup(models.Model):
    """
    Represents the relation between a group of Persons and Expenses
    """
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length = 100, default = "")
    member = models.ManyToManyField(Person)

    def __str__(self):
        return self.name


class Expense(models.Model):
    """
    Represents a single expense
    """
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    spent_by = models.ForeignKey(Person, on_delete = models.CASCADE, related_name = "spent_by")
    spent_for = models.ForeignKey(Person, on_delete = models.CASCADE, related_name = "spent_for", null = True,
                                  blank = True)
    budget_group = models.ForeignKey(BudgetGroup, on_delete = models.CASCADE, related_name = "budget_group")
    amount_spent = models.DecimalField(default = 0.0, decimal_places = 2, max_digits = 8)
    spent_for_purpose = models.CharField(max_length = 100)
    spent_at = models.DateTimeField('date published')

    def __str__(self):
        return '%s, %.2f for %s' % (self.spent_by, self.amount_spent, self.spent_for_purpose)

    def clean(self):
        if self.spent_by is None:
            raise ValidationError(_('validation.error.expense.spent_by.required'))

        if self.amount_spent <= 0:
            raise ValidationError(_('validation.error.expense.amount_spent.invalid'))

