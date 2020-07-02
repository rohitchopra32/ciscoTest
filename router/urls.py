from django.urls import path

from router.views import RouterView, RouterTemplate, GetToken, SearchByIpAddrRange, SearchByRouterType


urlpatterns = [
    path('', RouterTemplate.as_view(), name="router_template"),
    path('ip_addr_range', SearchByIpAddrRange.as_view(), name="router_template"),
    path('router_type', SearchByRouterType.as_view(), name="router_template"),
    path('router', RouterView.as_view(), name="router_view"),
    path('getToken', GetToken.as_view(), name="get_token"),
]