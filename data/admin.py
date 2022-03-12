from django.contrib import admin
from .models import ToDoList



# Register your models here.


class ToDoListAdminModel(admin.ModelAdmin):

    list_display=("baslik","eklenme_tarihi","status")
    
    class Meta:
        model=ToDoList


admin.site.register(ToDoList,ToDoListAdminModel)
