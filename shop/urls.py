from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "E-shop Admin Panel"
admin.site.site_title = "E-shop Admin Panel"
admin.site.index_title = "Welcome admin"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('homepage/', include('homepage.urls')),
    path('customers/', include('customers.urls')),
    path('products/', include('products.urls')),
    path('contact_us/', include('contact_us.urls')),
    path('cart/', include('cart.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
