
from django.conf.urls import url, include
from django.contrib import admin
from blog import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list, name='home'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^intro/$', views.intro, name='intro')

]
