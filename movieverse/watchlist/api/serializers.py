from rest_framework import serializers
from watchlist.models import WatchList,StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):
  # len_name = serializers.SerializerMethodField()
  class Meta:
    model = WatchList
    fields="__all__"

  def get_len_name(self,object):
    length = len(object.name)
    return length


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"
        extra_kwargs = {
            'url': {'view_name': 'streamplatform_details', 'lookup_field': 'pk'}
        }
# class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
#   watchlist = WatchListSerializer(many=True, read_only=True)
#   # watchlist = serializers.StringRelatedField(many=True)
#   # watchlist = serializers.HyperlinkedRelatedField(
#   #       many=True,
#   #       read_only=True,
#   #       view_name='watchlist_details'
#   #   )
#   class Meta:
#     model = StreamPlatform
#     fields = "__all__"



# class StreamPlatformSerializer(serializers.ModelSerializer):
#   watchlist = WatchListSerializer(many=True, read_only=True)

#   class Meta:
#     model = StreamPlatform
#     fields = "__all__"
