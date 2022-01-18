from django.contrib import admin
from django.apps import apps

from .models import ExtendUser

app = apps.get_app_config('graphql_auth')

admin.site.register(ExtendUser)

for model_name, model in app.models.items():
    admin.site.register(model)
