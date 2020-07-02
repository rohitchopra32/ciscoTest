from django.urls import path

from router.views import RouterView, RouterTemplate, GetToken, SearchByIpAddrRange, SearchByRouterType, SearchByIpRange

urlpatterns = [
    path('', RouterTemplate.as_view(), name="router_template"),
    path('ip_addr_range', SearchByIpAddrRange.as_view(), name="ip_addr_range"),
    path('search_by_ip_addr_range_api', SearchByIpRange.as_view(), name="search_by_ip_addr_range_api"),
    path('router_type', SearchByRouterType.as_view(), name="router_type"),
    path('router', RouterView.as_view(), name="router_view"),
    path('getToken', GetToken.as_view(), name="get_token"),
]
