from django.urls import path
from .views import MemoryCreate, MemoryList, MemoryDetail, MemoryUpdate, MemoryDelete

app_name='memoryhome'
urlpatterns = [
    path('', MemoryList.as_view(), name='memory_list'),
    path('create', MemoryCreate.as_view(), name='memory_create'),
    path('detail/<int:pk>', MemoryDetail.as_view(), name='memory_detail'),
    path('update/<int:pk>', MemoryUpdate.as_view(), name="memory_update"),
    path('delete/<int:pk>', MemoryDelete.as_view(), name='memory_delete')
]
