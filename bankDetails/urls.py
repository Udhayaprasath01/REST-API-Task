from django.urls import path, include
from bankDetails.views import BranchViewSet, AllBanksInCityView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'branch', BranchViewSet, basename='account')
urlpatterns = router.urls

urlpatterns += [
    path('all',AllBanksInCityView.as_view())
]
