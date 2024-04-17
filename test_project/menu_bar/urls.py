from django.urls import path
from django.views.generic import TemplateView

app_name = 'menu_bar'

urlpatterns = [
    path("", TemplateView.as_view(template_name="menu_bar/menu_template.html")),
]
