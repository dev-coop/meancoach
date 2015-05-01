import django_tables2 as tables

from .models import Metric, MetricRecord


class MetricTable(tables.Table):
    update = tables.TemplateColumn(template_name="metrics/_update_row.html",
                                   sortable=False)
    delete = tables.TemplateColumn(template_name="metrics/_delete_row.html",
                                   sortable=False)

    class Meta:
        model = Metric
        attrs = {"class": "table table-striped"}
        fields = (
            'name',
            'daily',
            'monthly',
            'boolean',
        )
        sequence = (
            'update',
            'delete',
            'name',
            'daily',
            'monthly',
            'boolean',
        )
