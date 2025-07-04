
from django.urls import path
# se importa las vistas de la aplicación
from administrativo import views

urlpatterns = [
        path('', views.index, name='index'),
        path('detalle/matricula/<int:id>', views.detalle_matricula,
            name='detalle_matricula'),
        path('crear/nueva/matricula', views.crear_matricula,
            name='crear_matricula'),
        path('editar/matricula/<int:id>', views.editar_matricula,
                name='editar_matricula'),
        path('detalle/estudiante/<int:id>', views.detalle_estudiante,
            name='detalle_estudiante'),
        path('crear_modulo/', views.crear_modulo, name='crear_modulo'),
        path('crear_estudiante/', views.crear_estudiante, name='crear_estudiante'),    
        path('listar_estudiantes/', views.listar_Estudiante, name='listar_estudiantes'),    
        path('listar_modulos/', views.listar_modulo, name='listar_modulos'),    
 ]
