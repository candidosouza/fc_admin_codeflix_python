from django.urls import path  # pylint: disable=import-self

from django_app import container
from .api import CategoryResource

def __init_category_resource():
    return {
        'create_use_case': container.use_case_category_create_category,
        'list_use_case': container.use_case_category_list_categories,
    }


urlpatterns = [
    path('categories/', CategoryResource.as_view(
        **__init_category_resource()
    )),
]
