from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView

from apps.Shcedule.models import Shcedule
from apps.users.decorators import student_required


@method_decorator([login_required, student_required], name='dispatch')
class ScheduleView(ListView):
    model = Shcedule
    template_name = 'schedule.html'
    context_object_name = 'schedule'

    def get_queryset(self):
        queryset = Shcedule.objects.get(group=self.request.user.student.group)
        print(queryset, self.request.user.student.group)
        return queryset


@method_decorator([login_required, user_passes_test(lambda u: u.is_superuser)], name='dispatch')
class CreateSchedule(CreateView):
    model = Shcedule
    template_name = 'schedule_create.html'
    fields = '__all__'
    success_url = reverse_lazy('schedule')
