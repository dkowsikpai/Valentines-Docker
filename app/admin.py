from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(RegisteredMembers)
class RegisteredMemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender_', 'age', 'native_place', 'blocked', 'ktu_reg_no', 'pair', 'pair_id']
    search_fields = ['id', 'name', 'native_place', 'ktu_reg_no']

    def gender_(self, obj):
        if obj.gender:
            return "Male"
        else: 
            return "Female"

    def pair(self, obj):
        if obj.pair_unique_id:
            e = RegisteredMembers.objects.get(unique_id=obj.pair_unique_id)
            return str(e.name + " " + e.remarks)
        else:
            return "No Pair"

    def pair_id(self, obj):
        if obj.pair_unique_id:
            e = RegisteredMembers.objects.get(unique_id=obj.pair_unique_id)
            return str(e.id)
        else:
            return "-"


@admin.register(Interests)
class RegisteredMemberAdmin(admin.ModelAdmin):
    list_display = ['interets', 'category']
