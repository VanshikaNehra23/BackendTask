from django.contrib import admin
from .models import User,Events,Waiting,UserRegistration

admin.site.register(User)
admin.site.register(Events,EventAdmin)
admin.site.register(Waiting,WaitingAdmin)
admin.site.register(UserRegistration,RegistrationAdmin)