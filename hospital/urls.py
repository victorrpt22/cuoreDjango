from django.conf.urls import url

from hospital import views

urlpatterns = [
    url(r'^addresses/$', views.AddressList.as_view(), name='address_list'),
    url(r'^accounts/$', views.AccountList.as_view(), name='address_list'),
]
