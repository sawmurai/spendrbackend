# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Expense, Person, BudgetGroup

admin.site.register(Expense)
admin.site.register(Person)
admin.site.register(BudgetGroup)