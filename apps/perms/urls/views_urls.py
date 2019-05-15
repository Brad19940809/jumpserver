# coding:utf-8

from django.conf.urls import url
from django.urls import path
from .. import views

app_name = 'perms'

urlpatterns = [
    # asset permission
    path('asset-permission/', views.AssetPermissionListView.as_view(), name='asset-permission-list'),
    path('asset-permission/create/', views.AssetPermissionCreateView.as_view(), name='asset-permission-create'),
    path('asset-permission/<uuid:pk>/update/', views.AssetPermissionUpdateView.as_view(), name='asset-permission-update'),
    path('asset-permission/<uuid:pk>/', views.AssetPermissionDetailView.as_view(),name='asset-permission-detail'),
    path('asset-permission/<uuid:pk>/delete/', views.AssetPermissionDeleteView.as_view(), name='asset-permission-delete'),
    path('asset-permission/<uuid:pk>/user/', views.AssetPermissionUserView.as_view(), name='asset-permission-user-list'),
    path('asset-permission/<uuid:pk>/asset/', views.AssetPermissionAssetView.as_view(), name='asset-permission-asset-list'),

    # application permission
    path('application-permission/', views.ApplicationPermissionListView.as_view(), name='application-permission-list'),
    path('application-permission/create/', views.ApplicationPermissionCreateView.as_view(), name='application-permission-create'),
    path('application-permission/<uuid:pk>/update/', views.ApplicationPermissionUpdateView.as_view(), name='application-permission-update'),
    path('application-permission/<uuid:pk>/', views.ApplicationPermissionDetailView.as_view(), name='application-permission-detail'),
    path('application-permission/<uuid:pk>/user/', views.ApplicationPermissionUserView.as_view(), name='application-permission-user-list'),
    path('application-permission/<uuid:pk>/application/', views.ApplicationPermissionApplicationView.as_view(), name='application-permission-application-list'),

]
