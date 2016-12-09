import django_tables2 as tables

from .models import Query

data = [
    {"query": "apples", "parent": "camden", "active": True, "date_added": "2016-09-18 17:36:27.585893", "date_deactivated": "2016-09-18 17:36:27.585893"},
    {"query": "beers", "parent": "camden", "active": True, "date_added": "2016-09-18 17:38:59.053775", "date_deactivated": "2016-09-18 17:38:59.053775"},
    {"query": "emmys", "parent": "kappa", "active": True, "date_added": "2016-09-18 17:32:59.041354", "date_deactivated": "2016-09-18 17:32:59.041354"}
]

class QueryTable(tables.Table):
    class Meta:
        model = Query
