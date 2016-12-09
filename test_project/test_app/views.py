# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django_tables2 import RequestConfig

from .models import Query
from .tables import QueryTable


def queries(request):
    table = QueryTable(Query.objects.all())
    RequestConfig(request).configure(table)

    return render(request, 'table_test.html', {'table': table})
