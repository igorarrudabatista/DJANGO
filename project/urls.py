
from django.contrib import admin
from django.urls import path, include
from app.views import home, form, create, view, edit, update, delete, base, general, createvendedores, cadvendedores, vendedores, bloqueartela, sucesso, cadorcamentos
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

from project.settings import DEBUG, MEDIA_ROOT, MEDIA_URL


urlpatterns = [
    path('admin/', admin.site.urls),
        path('', home, name='home'),
        path('form/', form, name='form'),
        path('base/', base, name='base'),
        path('general/', general, name='general'),
        path('createvendedores/', createvendedores, name='createvendedores'),
        path('cadvendedores/', cadvendedores, name='cadvendedores'),
        path('cadorcamentos/', cadorcamentos, name='cadorcamentos'),

       # path('viewvendedores/', viewvendedores, name='viewvendedores'),
        path('vendedores/', vendedores, name='vendedores'),
        path('accounts/', include('accounts.urls')),
        path('accounts/', include('django.contrib.auth.urls')),
        path('bloqueartela/', bloqueartela, name='bloqueartela'),
        path('successo', sucesso, name ='sucesso'),

        
        
        

        path('create/', create, name='create'),
        path('view/<int:pk>/', view, name='view'),
        path('edit/<int:pk>/', edit, name='edit'),
        path('update/<int:pk>/', update, name='update'),
        path('delete/<int:pk>/', delete, name='delete'),

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
