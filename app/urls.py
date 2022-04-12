from django.contrib import admin
from django.urls import path
from . import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', v.input, name="home"),
    path('', v.UploadView.as_view(), name='fileupload'),
    path('tabel/', v.tabel, name="tabel"),
    path('proses/', v.input, name="proses"),
    path('chart/', v.chart, name="chart"),
    path('hapusdata/', v.hapustabel, name="hapusdata"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)