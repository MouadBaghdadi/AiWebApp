from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    provider = fields.CharField(max_length=20)
    email = fields.CharField(max_length=200, unique=True)
    avatar = fields.CharField(max_length=1000, default=None, null=True)
    username = fields.CharField(max_length=30, default=None, null=True)
    nickname = fields.CharField(max_length=30, default=None, null=True)
    verified = fields.BooleanField(default=False)
    onboarded = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    last_logged_in = fields.DatetimeField(auto_now=True)
