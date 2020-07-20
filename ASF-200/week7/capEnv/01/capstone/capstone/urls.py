from django.contrib import admin
from django.urls import path
from traveler import views
from django.contrib.auth.views import LoginView, LogoutView
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='homepage'),
    path('accounts/profile/', views.IndexView.as_view(), name='homepage'),
    path('<int:pk>/', views.DetailView.as_view(), name='details'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]


# [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^$', view.IndexView.as_view(), name="homepage"),
#     url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail')
#  ]
