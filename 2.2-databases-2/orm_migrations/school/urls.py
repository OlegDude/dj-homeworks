import debug_toolbar
from django.conf import settings
from django.urls import include, path

from school.views import students_list

urlpatterns = [
    path('', students_list, name='students'),
    path('__debug__/', include(debug_toolbar.urls)),
]
