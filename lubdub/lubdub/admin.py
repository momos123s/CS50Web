from django.contrib import admin
from .models import Person, Psyche, MediaFiles, Match,Messages,Hobbies_Intreasts, VisualAnalysis, PreferenceAnalysis, Profile, Sexuality
# Register your models here.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'cellPhone', 'location', 'dateOfBirth', 'Job', 'education', 'isValidated', 'isSubscribed')
    search_fields = ('username', 'email', 'cellPhone')
    list_filter = ('education', 'isValidated', 'isSubscribed')
    ordering = ('username',)
    

# Custom admin for Psyche
@admin.register(Psyche)
class PersonalityAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personality Traits', {
            'fields': ('personalityTraits', 'religion', 'personID')
        }),
    )
    list_display = ('personID', 'personalityTraits', 'religion')

