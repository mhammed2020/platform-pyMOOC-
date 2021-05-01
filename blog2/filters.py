import django_filters
from . models import Course

class CourseFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')
    title =  django_filters.CharFilter(label="By Course")
    content =  django_filters.CharFilter(label="By Content")
    class Meta:
        model = Course
        fields = ['title', 'content']