from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Documents
    path('docs/', views.doc_all, name='docs'),
    path('docs/<int:doc_id>/', views.doc, name='detail'),
    path('docs/create/', views.DocCreate.as_view(), name='doc_create'),
    path('docs/<int:pk>/update/', views.DocUpdate.as_view(), name='doc_update'),
    path('docs/<int:pk>/delete', views.DocDelete.as_view(), name='doc_delete'),
    # Signup
    path('accounts/signup/', views.signup, name='signup'),
]
