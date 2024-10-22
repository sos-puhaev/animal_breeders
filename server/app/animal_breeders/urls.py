from django.urls import include, path

urlpatterns = [
    path('api/v1/', include('animal_breeders.api.v1.urls')),
]