from django.contrib import admin
from .models import Bylaw, Policy, Movie, Projectionist, Officers, Schedule

admin.site.register(Bylaw)
admin.site.register(Policy)
admin.site.register(Movie)
admin.site.register(Projectionist)
admin.site.register(Officers)
admin.site.register(Schedule)
