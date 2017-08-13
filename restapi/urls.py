from django.conf.urls import include, url
from django.contrib import admin
from belema import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    # Examples:
    # url(r'^$', 'restapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
url(r'^belema-api/', views.BelemaList.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)