from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(RegisteredMembers)
class RegisteredMemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender', 'age', 'native_place', 'blocked', 'ktu_reg_no', 'pair']

    def pair(self, obj):
        if obj.pair_unique_id:
            e = RegisteredMembers.objects.get(unique_id=obj.pair_unique_id)
            return str(e.name + " " + e.remarks)
        else:
            return "No Pair"


@admin.register(Interests)
class RegisteredMemberAdmin(admin.ModelAdmin):
    list_display = ['interets', 'category']
