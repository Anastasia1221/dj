import django_filters
from django import forms
from .models import Post


class NewsFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(
        lookup_expr='icontains', 
        field_name='title', 
        label="Заголовок"
    )

    # # type = django_filters.CharFilter(lookup_expr='icontains', field_name='type')
    type = django_filters.ChoiceFilter(
        choices=(
            ("article", "Article"),
            ("news", "News")
        ), 
        field_name='type',
        label="Тип новости"
    )

    created_at = django_filters.DateFilter(
        lookup_expr='gte', 
        field_name='created_at', 
        widget=forms.SelectDateWidget,
        label="Дата от"
    )

    class Meta:
        model = Post
        fields = ['title', 'type', 'created_at']