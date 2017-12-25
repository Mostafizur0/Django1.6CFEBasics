from django.contrib import admin
#from django.contrib.staticfiles

# Register your models here.
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model = SignUp

admin.site.register(SignUp, SignUpAdmin)
