from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from pytils.translit import slugify

from blog.models import Blog


# Create your views here.


class ContactView(View):

    def get(self, request):
        return render(request, 'blog/contacts.html')


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('blog_title', 'blog_description', 'blog_image', 'is_published',)
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):    # Задание 3: выводить в список статей только те, которые имеют положительный признак публикации
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.blog_title)    # В консоли нужно установить модуль pytils
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('blog_title', 'blog_description', 'blog_image', 'is_published',)
    # success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            blog = form.save()
            blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:view', args=[self.kwargs.get('pk')])


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'blog_list.html'

    def get_queryset(self, *args, **kwargs):    # Задание 3: выводить в список статей только c положительным признаком публикации
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog

    def get(self, request, pk, **kwargs):
        blog = self.get_object()
        context = {
            'object_list': Blog.objects.filter(pk=pk),
        }
        return render(request, 'blog/blog_detail.html', context)

    def get_object(self, queryset=None):    # Задание 3: при открытии отдельной статьи увеличивать счетчик просмотров;
        objects = super().get_object(queryset)
        objects.views_count += 1
        objects.save()
        return objects


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')




