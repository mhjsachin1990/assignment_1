from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='home'),
    # >>> Student  <<<
    path('students/',views.students,name='students'),
    path('students/add_students/',views.add_students,name='add_students'),
    path('students/add_students/addrecord/',views.addrecord,name='addrecord'),
    path('students/delete/<int:id>',views.delete,name='delete'),
    path('students/update/<int:id>',views.update,name='update'),
    path('students/update/updaterecord/<int:id>',views.updaterecord,name='updaterecord'),

    # >>> Department  <<<
    path('department/',views.department,name='department'),
    path('department/add_dept/',views.add_dept,name='add_dept'),
    path('department/add_dept/add_department/',views.add_department,name='add_department'),
    path('department/delete_dept/<int:id>',views.delete_dept,name='delete_dept'),
    path('department/update_dept/<int:id>',views.update_dept,name='update_dept'),
    path('department/update_dept/update_department/<int:id>',views.update_department,name='update_department'),


]