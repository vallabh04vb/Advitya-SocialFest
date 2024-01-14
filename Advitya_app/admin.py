from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from Advitya_app.models import UserAccount
from .models import Activity,UserActivityRegistration,UserActivityRegistrationInitial
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin


# from .models import CustomUser
# # Register your models here.
# @admin.register(Socio_trivia_reg)
# class Acc (ImportExportModelAdmin):
#   pass
# @admin.register(UserActivityRegistration)
# class Acc (ImportExportModelAdmin):
#   pass
# @admin.register(Activity)
# class Acc (ImportExportModelAdmin):
#   pass
# @admin.register(Event)
# class Acc (ImportExportModelAdmin):
#   pass
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Activity, UserActivityRegistration, UserActivityRegistrationInitial

class UserActivityRegistrationInline(admin.TabularInline):
    model = UserActivityRegistration
    extra = 0  # Set to 0 to display all registrations without extra empty forms

class ActivityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [UserActivityRegistrationInline]

admin.site.register(Activity, ActivityAdmin)

class UserActivityRegistrationResource(resources.ModelResource):
    # Define a field to include the related Activity name
    activity_name = fields.Field(column_name='Activity Name')

    class Meta:
        model = UserActivityRegistration
        fields = ('id', 'user', 'email', 'name_user', 'activity', 'activity_name', 'phone_number')

    def dehydrate_activity_name(self, user_activity_registration):
        # Customize the exported value based on activity IDs
        activity_id = user_activity_registration.activity.id if user_activity_registration.activity else None
        if activity_id == 1:
            return "Samwaad"
        elif activity_id == 2:
            return "CSR"
        else:
            return ''

class UserActivityRegistrationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = UserActivityRegistrationResource

admin.site.register(UserActivityRegistration, UserActivityRegistrationAdmin)


@admin.register(UserAccount)
class Acc (ImportExportModelAdmin):
  pass
@admin.register(UserActivityRegistrationInitial)
class Acc (ImportExportModelAdmin):
  pass




# class CustomUserAdmin(UserAdmin):
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')

# admin.site.register(CustomUser, CustomUserAdmin)


