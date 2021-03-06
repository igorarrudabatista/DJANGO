
from django.contrib import admin
from django.urls import path, include
from app.views import home, form, create, view, edit, update, delete, base, general, createvendedores, cadvendedores, vendedores, bloqueartela, sucesso, cadorcamentos, orcamentos, createorcamentos, view_orcamentos, listar_orcamentos
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

        #### VENDEDORES #######
        path('createvendedores/', createvendedores, name='createvendedores'),
        path('cadvendedores/', cadvendedores, name='cadvendedores'),
        path('vendedores/', vendedores, name='vendedores'),

        ##### ORCAMENTOS ######
        path('cadorcamentos/', cadorcamentos, name='cadorcamentos'),
        path('createorcamentos/', createorcamentos, name='createorcamentos'),
        path('orcamentos/', orcamentos, name='orcamentos'),
        path('listar_orcamentos/', listar_orcamentos, name='listar_orcamentos'),
        path('view_orcamentos/<int:pk>/', view_orcamentos, name='view_orcamentos'),

       # path('viewvendedores/', viewvendedores, name='viewvendedores'),
        
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
