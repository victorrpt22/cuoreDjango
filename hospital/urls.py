from django.conf.urls import url

from hospital import views

urlpatterns = [
    url(r'^addresses/$', views.AddressList.as_view(), name='address_list'),
    url(r'^accounts/$', views.AccountList.as_view(), name='account_list'),

    url(r'^accounts/(?P<pk>[0-9]+)$', views.AccountDetail.as_view(), name='account_detail'),
    url(r'^addresses/(?P<pk>[0-9]+)$', views.AddressDetail.as_view(), name='address_detail'),
]
