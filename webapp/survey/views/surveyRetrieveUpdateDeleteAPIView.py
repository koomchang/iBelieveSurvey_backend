from django.utils import timezone
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from survey.models import Survey
from survey.serializers import SurveyRetrieveSerializer, SurveySerializer


class SurveyRetrieveUpdateDestoryAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Survey.objects.all()

    def get_serializer_class(self):
        if getattr(self, 'swagger_fake_view', False):
            return SurveySerializer

        instance = self.get_object()
        HIDDEN_END_SURVEY = instance.is_survey_hidden and instance.end_at < timezone.now()
        NOT_STARTED_SURVEY = instance.status == Survey.IDLE

        if HIDDEN_END_SURVEY or NOT_STARTED_SURVEY:
            return SurveySerializer
        else:
            return SurveyRetrieveSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance.status != Survey.IDLE:
            return Response({'error': '설문이 진행중이거나 종료되어서 수정할 수 없습니다.'}, status=400)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)