from django.contrib import admin

from .models import Forum, Opportunity, Tag, User, Waitlist

admin.site.register(User)
admin.site.register(Opportunity)
admin.site.register(Forum)
admin.site.register(Tag)
admin.site.register(Waitlist)
