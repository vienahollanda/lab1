from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_xml
from wishlist.views import show_json
from wishlist.views import show_json_by_id
from wishlist.views import show_xml_by_id
from wishlist.views import show_form_register
from wishlist.views import show_login_user
from wishlist.views import show_logout_user
app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('register/', show_form_register, name='show_form_register'),
    path('login/', show_login_user, name='show_login_user'),
    path('logout/', show_logout_user, name='show_logout_user'),
]