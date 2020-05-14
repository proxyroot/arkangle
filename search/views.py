from django.views.generic.base import TemplateView
from search.models import Cluster


class HomePageView(TemplateView):

    template_name = "home.html"

    def group(self, items, size=1):
        chunks = []
        chunk = []

        for item in items:
            if len(chunk) == size:
                chunks.append(chunk)
                chunk = []
            chunk.append(item)

        if chunk:
            chunks.append(chunk)

        return chunks

    def get_context_data(self, **kwargs):
        clusters = Cluster.objects.all()
        return {"groups": self.group(clusters, 3)}
