from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from golong import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'golong.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'rideshare.views.home', name='home'),

    url(r'^register/$', 'rideshare.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),


    url(r'^profile/$', 'rideshare.views.profile', name='profile'),
    url(r'^car_form/$', 'rideshare.views.car_form', name='car_form'),
    url(r'^route_form/$', 'rideshare.views.route_form', name='route_form'),
    url(r'^car/(?P<car_id>\w+)/edit/$', 'rideshare.views.edit_car', name='edit_car'),
    url(r'^car/(?P<car_id>\w+)/$', 'rideshare.views.view_car', name='view_car'),
    url(r'^car/(?P<car_id>\w+)/car/$', 'rideshare.views.delete_car', name='delete_car'),
    url(r'^route/(?P<route_id>\w+)/edit/$', 'rideshare.views.edit_route', name='edit_route'),
    url(r'^route/(?P<route_id>\w+)/delete/$', 'rideshare.views.delete_route', name='delete_route'),
    url(r'^route/(?P<route_id>\w+)/$', 'rideshare.views.view_route', name='view_route'),
    url(r'^traveler/(?P<traveler_id>\w+)/$', 'rideshare.views.view_traveler', name='view_traveler'),

)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)