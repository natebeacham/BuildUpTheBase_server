from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from django.db import models
from django.contrib import admin
from buildup import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.Index.as_view(), name="index"),

    url(r'^changelog/$', views.changelog, name="changelog"),
    url(r'^leaderboard/$', views.Leaderboard.as_view(), name="leaderboard"),

    url(r'^users/(?P<username>[a-zA-Z0-9]*)/$', views.UserDetail.as_view(), name="user-detail"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
