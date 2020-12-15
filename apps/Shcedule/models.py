from django.db import models

from apps.Groups_faculties.models import Groups
from apps.Subject.models import Subject


class Shcedule(models.Model):
    group = models.OneToOneField(Groups, on_delete=models.CASCADE)
    pon_one = models.ForeignKey(Subject, related_name='pon1', on_delete=models.CASCADE, null=True, blank=True)
    pon_two = models.ForeignKey(Subject, related_name='pon2', on_delete=models.CASCADE, null=True, blank=True)
    vtornik_one = models.ForeignKey(Subject, related_name='vtornik1', on_delete=models.CASCADE, null=True, blank=True)
    vtornik_two = models.ForeignKey(Subject, related_name='vtornik2', on_delete=models.CASCADE, null=True, blank=True)
    sreda_one = models.ForeignKey(Subject, related_name='sreda1', on_delete=models.CASCADE, null=True, blank=True)
    sreda_two = models.ForeignKey(Subject, related_name='sreda2', on_delete=models.CASCADE, null=True, blank=True)
    chetverg_one = models.ForeignKey(Subject, related_name='chetverg1', on_delete=models.CASCADE, null=True, blank=True)
    chetverg_two = models.ForeignKey(Subject, related_name='chetverg2', on_delete=models.CASCADE, null=True, blank=True)
    patniza_one = models.ForeignKey(Subject, related_name='patniza1', on_delete=models.CASCADE, null=True, blank=True)
    patniza_two = models.ForeignKey(Subject, related_name='patniza2', on_delete=models.CASCADE, null=True, blank=True)