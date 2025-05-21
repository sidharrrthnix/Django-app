from rest_framework import serializers
from watchlist.models import Movie



def description_validator(value):
  if len(value) < 10:
    raise serializers.ValidationError("Description is too short")
  return value

class MovieSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  name = serializers.CharField()
  description = serializers.CharField(validators=[description_validator])
  active = serializers.BooleanField()

  def create(self, validated_data):
    return Movie.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.description = validated_data.get('description', instance.description)
    instance.active = validated_data.get('active', instance.active)
    instance.save()
    return instance


  def validate_name(self, value):
    if len(value) < 2:
      raise serializers.ValidationError("Name is too short")
    return value

  def validate(self, data):
    if data['name'] == data['description']:
      raise serializers.ValidationError("Name and description should not be the same")
    return data
