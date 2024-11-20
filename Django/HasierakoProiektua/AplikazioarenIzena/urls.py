from django.urls import path 
from . import views 
urlpatterns = [
    path('', views.ikasle_list, name="zerrenda-default"),
    path('Ikasle/new/', views.ikasle_new, name='aplikazioarenizena-ikasle-new'),
    path('Ikasgaiak/', views.ikasgaiak_list, name="ikasgaiak-default"),
    path('Ikasgaiak/new', views.ikasgaiak_new, name="ikasgaiak-new"),
    path('Nota/', views.nota_list, name="nota-default"),
    path('Nota/new', views.nota_new, name="nota-new"),
    path('Nota-delete/<int:nota_id>/', views.eliminar_nota, name='nota-delete'),  
    path('Nota-edit/<int:nota_id>/', views.edit_nota, name='nota-edit'),
    path('editar_nota/<int:ikasgai_kodea>/<int:ikasle_kodea>/', views.editar_nota, name='editar_nota'),  # URL para editar una nota
    ]
