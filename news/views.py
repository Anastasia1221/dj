from pyexpat.errors import messages
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, LogoutView, LoginView


from .models import Post
from .filters import NewsFilter
from .forms import PostCreate

# Create your views here.


class NewsList(ListView):

    model = Post

    ordering = '-created_at'

    template_name = 'flatpages/news.html'

    context_object_name = 'News'

    paginate_by = 3

    def get_queryset(self):
      # Получаем обычный запрос
      queryset = super().get_queryset()
      # Используем наш класс фильтрации.
      # self.request.GET содержит объект QueryDict, который мы рассматривали
      # в этом юните ранее.
      # Сохраняем нашу фильтрацию в объекте класса,
      # чтобы потом добавить в контекст и использовать в шаблоне.
      self.filterset = NewsFilter(self.request.GET, queryset)
      # Возвращаем из функции отфильтрованный список товаров
      return self.filterset.qs

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      # Добавляем в контекст объект фильтрации.
      context['filterset'] = self.filterset
      return context


class FullNews(DetailView):

    model = Post

    template_name = 'flatpages/fullNew.html'

    context_object_name = 'fullNew'


class NewsCreate(CreateView):
   
   form_class = PostCreate

   model = Post

   template_name = 'flatpages/create.html'


class NewsDelete(DeleteView):

      model = Post

      template_name ='flatpages/delete.html'

      success_url = reverse_lazy('news_list')


class NewsUpdate(LoginRequiredMixin, UpdateView):
    
    model = Post

    form_class = PostCreate

    template_name = 'flatpages/create.html'
  

class PassChange(PasswordChangeView):
    
    template_name = 'flatpages/change_password.html'




class Logout(LogoutView):
    
    template_name = 'flatpages/logout.html'



class LogIn(LoginView):
    
    template_name = 'flatpages/login.html'

