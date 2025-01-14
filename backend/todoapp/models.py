from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

#Base Model
class BaseModel(models.Model):
    uid = models.UUIDField(default = uuid.uuid4, editable = False, primary_key = True)
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now = True)

    class Meta:
        abstract = True

# Todo Model
class Todo(BaseModel):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 400)
    is_completed = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'todos')