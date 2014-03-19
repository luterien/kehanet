from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework import routers

from apps.api.views import ProfileViewSet, register_user

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', ProfileViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kehanetusers.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/1.0/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # custom views
    url(r'^api/1.0/register/$', register_user),

    # homepage
    url(r'^$', TemplateView.as_view(template_name="index.html")),

)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    )


