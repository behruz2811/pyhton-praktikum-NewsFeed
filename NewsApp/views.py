from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import TemplateView, ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

from .models import News, Category
from .forms import ContactForm


# Create your views here.
def NewsListView(request):
    news_list = News.objects.all()
    context = {
        'news_list': news_list
    }
    return render(request, 'news/news_list.html', context=context)


def NewsDetailView(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        'news': news
    }
    return render(request, 'news/news_detail.html', context)


def HomePageView(request):
    categories = Category.objects.all()
    news_list = News.objects.all().order_by('-publish_time')[:5]
    local_first = News.objects.all().filter(category__name='Mahalliy').order_by('-publish_time')[:1]
    local_news = News.objects.all().filter(category__name='Mahalliy').order_by('-publish_time')[1:4]

    context = {
        'news_list': news_list,
        'categories': categories,
        'local_first': local_first,
        'local_news': local_news
    }
    return render(request, 'news/index.html', context=context)


class HomePageView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.publish.all().order_by('-publish_time')[:5]
        context['local_news'] = News.publish.all().filter(category__name='Mahalliy').order_by('-publish_time')[:5]
        context['foreign_news'] = News.publish.all().filter(category__name='Xorij').order_by('-publish_time')[:5]
        context['sport_news'] = News.publish.all().filter(category__name='Sport').order_by('-publish_time')[:5]
        context['technology_news'] = News.publish.all().filter(category__name='Texnologiya').order_by('-publish_time')[
                                     :5]
        return context


class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse('<h3>Tashakkur</h3>')

        context = {
            'form': form
        }
        return render(request, "news/contact.html", context=context)


def Page404View(request):
    context = {

    }
    return render(request, 'news/404.html', context=context)


class LocalNewsPage(ListView):
    model = News
    context_object_name = 'local_news'
    template_name = 'news/local.html'

    def get_queryset(self):
        news = self.model.publish.all().filter(category__name="Mahalliy")
        return news


class ForeignNewsPage(ListView):
    model = News
    context_object_name = 'foreign_news'
    template_name = 'news/foreign.html'

    def get_queryset(self):
        news = self.model.publish.all().filter(category__name="Xorij")
        return news


class SportNewsPage(ListView):
    model = News
    context_object_name = 'sport_news'
    template_name = 'news/sport.html'

    def get_queryset(self):
        news = self.model.publish.all().filter(category__name="Sport")
        return news


class TechnoNewsPage(ListView):
    model = News
    context_object_name = 'techno_news'
    template_name = 'news/techno.html'

    def get_queryset(self):
        news = self.model.publish.all().filter(category__name="Texnologiya")
        return news


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'crud/news_edit.html'
    fields = ('title', 'body', 'status', 'image', 'category')
    # success_url = reverse_lazy('home_page')


class NewsDeleteView(DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy("home_page")


class NewsCreateView(CreateView):
    model = News
    template_name = "crud/news_create.html"
    fields = ('title', 'slug', 'body', 'status', 'image', 'category')
