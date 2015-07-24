from rest_framework import serializers, viewsets
from .models import Question
from .models import Choice

# Serializers define the API representation.
class ChoiceSerializer(serializers.ModelSerializer):
	# question = serializers.HyperlinkedRelatedField(view_name='choices', read_only=True)
	class Meta:
		model = Choice


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('url', 'id', 'pub_date', 'question_text', 'choices')


# ViewSets define the view behavior.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer





