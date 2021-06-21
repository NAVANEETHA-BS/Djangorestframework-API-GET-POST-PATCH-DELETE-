from django.urls import path
from .views import PostList
# , PostDetail

app_name = 'blog_api'

urlpatterns = [
    # path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name='listcreate'),
    path('<int:id>/', PostList.as_view(), name='detailcreate'),
    path('create/', PostList.as_view(), name='create'),
    path('edit/<int:id>/', PostList.as_view(), name='edit'),
    path('delete/<int:id>/', PostList.as_view(), name='delete')
]