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

@admin.register(MediaFiles)
class MediaAdmin(admin.ModelAdmin):
    fieldset = (
        ('Media ', {
            'fields':('fileName', 'fileData', 'fileDate', 'uploader')
        }),
    )
    list_display = ('fileName', 'fileData', 'fileDate', 'uploader')

@admin.register(Messages)
class Messanges(admin.ModelAdmin):
    fieldsets = (
        ('Message', {
            'fields':('matchID','message','sender','reciever','file')
        }),
    )
    list_display = ('matchID', 'message', 'sender', 'reciever', 'file')

@admin.register(Match)
class Match(admin.ModelAdmin):
    fieldsets = (
    ('Match', {
        'fields':('person1', 'person2', 'isBlocked')
        }),
    )
    list_display = ('person1', 'person2', 'isBlocked')

@admin.register(Sexuality)
class Sexuality(admin.ModelAdmin):
    fieldsets = (
        ('sexuality', {
            'fields':('personID', 'sex','sexuality')
        }),
    )
list_display = ('personID', 'sex', 'sexaulity')

@admin.register(Hobbies_Intreasts)
class Hobbies_Intreasts(admin.ModelAdmin):
    fieldsets = (
        ('Hobbies_intreasts',{
            'fields':('personID','hobbies')
        }),
    )
    list_display = ('personID', 'hobbies')

@admin.register(VisualAnalysis)
class VisualAnalysis(admin.ModelAdmin):
    fieldsets = (
        ('VisualAnalysis', {
            'fields':('person','height', 'weight', 'race', 'bodyType')
        }),
    )
    list_display = ('person', 'height', 'weight','race', 'bodyType')
