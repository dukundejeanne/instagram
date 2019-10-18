from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.home_images,name = 'homePage'),
    url(r'^image/(\d+)',views.image,name = 'image'),
    url(r'^users/',views.user_list,name = 'user_list'),
    url(r'^search/',  views.search_users,name='search_users'),
    url(r'^edit/profile$',  views.edit_profile,name='edit_profile'),
    url(r'^profile/(?P<username>[0-9]+)$',  views.individual_profile_page,name='individual_profile_page'),
    url(r'^myprofile/$',  views.myprofile,name='myprofile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


