from django.contrib import admin
from .models import User
from .models import Sport
from .models import Base

# Register your models here.
admin.site.register(User)
admin.site.register(Sport)
admin.site.register(Base)
