from rest_framework import serializers

from core.models import Journey, DayEntry, EntryImage


class JourneySerializer(serializers.ModelSerializer):
    # TODO: Actually, this shouldn't be objects.all queryset but only for the given journey, hmm...
    day_entries = serializers.PrimaryKeyRelatedField(many=True, queryset=DayEntry.objects.all())

    class Meta:
        model = Journey
        fields = ('name', 'start_date', 'end_date', 'day_entries')


class DayEntrySerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)

    class Meta:
        model = DayEntry
        fields = ('title', 'date', 'text', 'images')


class EntryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryImage
