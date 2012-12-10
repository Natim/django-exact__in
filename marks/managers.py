from djqmixin import Manager, QMixin
from django.db.models import Q

# Mixins to manage a AND'ed filter on tag_list
class MarkQMixin(QMixin):
    def exact_in(self, tags):
        queryset = self.all()
        for tag in tags:
            queryset = queryset.filter(tag__name__exact=tag)
        return queryset

MarkManager = Manager.include(MarkQMixin)
