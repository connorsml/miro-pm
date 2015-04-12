from django.conf.urls import patterns, include, url
from solid_i18n.urls import solid_i18n_patterns

urlpatterns = patterns('',)

urlpatterns += solid_i18n_patterns('',
    url(r'^api/', include('miro_core.urls')),
)