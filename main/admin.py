from django.contrib import admin
from .models import Profile,Education,Experience,Skill,Contact,Project,Photos

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','address')

admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(Photos)