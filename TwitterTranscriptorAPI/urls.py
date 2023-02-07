from django.urls import path, include
urlpatterns = [
    path('transcript/', include("TTLogic.urls"))
]
