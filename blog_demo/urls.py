"""blog_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blogs import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
# router1 = DefaultRouter()


router.register('toppingviewset',views.ToppingsViewSet, basename='topping')
router.register('toppingsmodelviewset',views.ToppingsModelViewSet, basename= 'modeltopping')
router.register('readonlytoppings',views.ReadOnlyToppings, basename='readonlytoppings')
router.register('personmodelviewset',views.PersonModelViewSet, basename='personmodelviewset')
router.register('songs', views.SongDemo, basename='songmodel')
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('toppings_details/',views.toppings_details),
    #path('pizza_details/', views.pizza_details),
    # path('per_create/', views.person_create),
    # path('current_datetime/',views.current_time),
    #path('cl/', views.MyView.as_view(), name='cl'),
    path('tl/', views.ToppingsList.as_view(),name='tl'),
    path('tc/', views.ToppingsCreate.as_view(),name='tc'),
    path('tu/<int:pk>/', views.ToppingsUpdate.as_view(), name = 'tu'),
    path('tr/<int:pk>/', views.ToppingsRetrieve.as_view(), name = 'tr'),
    path('td/<int:pk>/', views.ToppingsDestroy.as_view(), name = 'td'),
    path('ctl/', views.ToppingListView.as_view(), name = 'ctl'),
    path('ctc/', views.ToppingCreateView.as_view(), name = 'ctc'),
    path('ctu/<int:pk>', views.ToppingUpdateView.as_view(), name = 'ctu'),
    path('ctr/<int:pk>', views.ToppingsRetrieveView.as_view(), name = 'ctr'),
    path('ctd/<int:pk>', views.ToppingsDeleteView.as_view(),name = 'ctd'),
    path('',include(router.urls)),
    path('',include(router.urls)),
    path('', include(router.urls)),
    path('',include(router.urls))
]


