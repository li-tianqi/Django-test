from django.conf.urls import include, url

from django.contrib import admin
from Hello import views as Hello_views
from calc_test import views as calc_views


admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'Test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', calc_views.index2),
    url(r'^plus/$', calc_views.plus, name='plus'),
    url(r'^add/', calc_views.add, name='add'),
    url(r'^add2/(\d+)/(\d+)/$', calc_views.add2, name='add2'),
    url(r'^home/', Hello_views.home, name='home'),
    url(r'^change_csv/', calc_views.change_csv, name='change_csv')
]
