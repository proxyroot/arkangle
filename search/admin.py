from django.contrib import admin

from search.models import Cluster


@admin.register(Cluster)
class ClusterAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "nodes"]
