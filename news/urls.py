from django.urls import path
from .views import NewsList, FullNews, NewsCreate, NewsDelete, NewsUpdate

from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>', FullNews.as_view(), name='news_details'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/update/login/', LoginView.as_view(template_name='flatpages/login.html'), name='login')

]