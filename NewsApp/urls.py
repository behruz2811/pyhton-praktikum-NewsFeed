from django.urls import path
from .views import NewsListView, NewsDetailView, HomePageView, ContactPageView, Page404View, \
    LocalNewsPage, TechnoNewsPage, SportNewsPage, ForeignNewsPage, NewsUpdateView, NewsDeleteView, NewsCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('news/<slug:news>/', NewsDetailView, name='news_detail_page'),
    path('create/', NewsCreateView.as_view(), name='news_create_page'),
    path('news/<slug>/edit/', NewsUpdateView.as_view(), name='news_edit_page'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name='news_delete_page'),
    path('local/', LocalNewsPage.as_view(), name='local_news_page'),
    path('sport/', SportNewsPage.as_view(), name='sport_news_page'),
    path('foreign/', ForeignNewsPage.as_view(), name='foreign_news_page'),
    path('techno/', TechnoNewsPage.as_view(), name='techno_news_page'),
    path('404/', Page404View, name='404_page'),
    path('news/', NewsListView, name='all_news_list'),
]
