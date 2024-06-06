from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    path("", views.index, name="index"),
    path("products", views.product_list, name="product_list"),
    path("products/<int:product_id>", views.product_detail, name="product_detail"),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)