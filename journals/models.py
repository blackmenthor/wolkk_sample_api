import datetime
import uuid

from django.db import models

from auth_sample.models import User


class Journal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_by = models.ForeignKey(User, related_name="journal_owner", on_delete=models.CASCADE)
    title = models.TextField()
    body = models.TextField(max_length=4096, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/journal', blank=True, null=True)
    deleted = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    date = models.DateField(default=datetime.date.today)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Journal ' + self.created_by.first_name + ' ' + str(self.date)
