# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CurrentDevices(models.Model):
    tool_id = models.IntegerField(blank=True, null=True)
    mac_number = models.TextField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)
    place = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'current_devices'


class CurrentLocalDevices(models.Model):
    mac_number = models.TextField()

    class Meta:
        managed = False
        db_table = 'current_local_devices'


class TestModel2(models.Model):
    test_field = models.IntegerField(blank=True)
    x = models.DateTimeField(blank=True)

    class Meta:
        db_table = 'test_model2'
