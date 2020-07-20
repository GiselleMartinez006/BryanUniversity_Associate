from django.contrib import admin
from django.urls import path
from traveler import views
admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view()),
    path('<int:pk>/', views.DetailView.as_view())
]


# [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^$', view.IndexView.as_view(), name="homepage"),
#     url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail')
#  ]
