from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^form/$', views.form, name='form'),
    # path('profile/<slug:foo>', views.getProfile, name="profile"),
    path('scratchcard/<slug:foo>', views.scratchcard, name="scratch_card"),
    # path('pair_profile/<slug:foo>', views.pairProfile, name="pair_prof")
    url(r'^.*/$', views.home, name='jhdb'),

]


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

