from watchlist.models import WatchList,StreamPlatform
from rest_framework.response import Response
from watchlist.api.serializers import WatchListSerializer,StreamPlatformSerializer
from rest_framework.views import APIView
from rest_framework import status



class StreamPlatformList(APIView):
  def get(self,request):
    streamplatforms = StreamPlatform.objects.all()
    serializer = StreamPlatformSerializer(streamplatforms, many=True,context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self,request):
    serializer = StreamPlatformSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StreamPlatformDetails(APIView):
  def get(self,request,pk):
    try:
      streamplatform = StreamPlatform.objects.get(pk=pk)
    except StreamPlatform.DoesNotExist:
      return Response({'error': 'StreamPlatform not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = StreamPlatformSerializer(streamplatform)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def put(self,request,pk):
    streamplatform = StreamPlatform.objects.get(pk=pk)
    serializer = StreamPlatformSerializer(streamplatform, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self,request,pk):
    streamplatform = StreamPlatform.objects.get(pk=pk)
    streamplatform.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListView(APIView):
  def get(self,request):
    watchlists = WatchList.objects.all()
    serializer = WatchListSerializer(watchlists, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self,request):
    serializer = WatchListSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchListDetails(APIView):
  def get(self,request,pk):
    try:
      watchlist = WatchList.objects.get(pk=pk)
    except WatchList.DoesNotExist:
      return Response({'error': 'WatchList not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = WatchListSerializer(watchlist)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def put(self, request, pk):
    watchlist = WatchList.objects.get(pk=pk)
    serializer = WatchListSerializer(watchlist, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    watchlist = WatchList.objects.get(pk=pk)
    watchlist.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
