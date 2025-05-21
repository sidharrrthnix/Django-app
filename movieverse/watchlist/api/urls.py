from django.urls import path
from watchlist.api.views import WatchListView, WatchListDetails, StreamPlatformList, StreamPlatformDetails



urlpatterns = [
    path('list/', WatchListView.as_view(), name='watchlist_list'),
    path('<int:pk>', WatchListDetails.as_view(), name='watchlist_details'),
    path('stream/', StreamPlatformList.as_view(), name='stream_list'),
    path('stream/<int:pk>', StreamPlatformDetails.as_view(), name='streamplatform_details')
]
