from django.urls import path, include
from api.models import CategoryResource,CourseResource
from tastypie.api import Api 



api = Api(api_name='v1')
api.register(CourseResource())
api.register(CategoryResource())

# api/v1/courses/
# api/v1/categories/

# For POST , DELETE
# Key: Authorization
# Value: ApiKey Ihor:ihor123456

urlpatterns = [
    path('', include(api.urls), name='index')
]
