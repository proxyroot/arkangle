from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Cluster


@registry.register_document
class ClusterDocument(Document):
    class Index:
        name = "cluster"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Cluster
        fields = ["id", "name", "nodes"]
