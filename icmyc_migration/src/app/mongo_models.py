from mongoengine.fields import (
    StringField, IntField, BooleanField,DateTimeField,
    DictField, ListField, ObjectIdField
)
from src.app import mongo
import datetime


class Channel(mongo.Document):
    title = StringField(max_lenght=100, required=True)
    slug = StringField(max_lenght=150, required=True)
    platform = StringField(default="Swachhata", choices=['Swachhata', 'ICMYC'])
    app_name = StringField(required=True)
    type = StringField(required=True)
    archived = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField()

    meta = {
        'collection': 'channels'
    }

    def __str__(self):
        return self.title

class Role(mongo.Document):
    name = StringField(required=True, max_length=50)
    guard_name = StringField(max_length=50, default="api")
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(null=True)
    profile_ids = ListField(ObjectIdField())

    meta = {
        "collection": 'roles'
    }

    def __str__(self):
        return self.name

    @staticmethod
    def input_roles():
        return [
            'Super Admin',
            'Admin',
            'Moderator',
            'Citizen',
            'State Admin',
            'District Admin',
            'ULB Admin',
            'Civic Agency Admin',
            'Civic Agency User',
            'Engineer',
            'Escalations Engineer',
            'MP',
            'MLA',
            'Corporator',
            'SQS admin',
            'Nodal Officer',
            'MOUH',
            'Event Admin',
            'Event Moderator',
        ]

class Profile(mongo.Document):
    username = StringField(null=True)
    user_id = IntField(unique=True)
    email = StringField()
    password = StringField()
    full_name = StringField(required=False, max_length=255)
    mobile_number = StringField()
    otp = StringField()
    otp_sent_at = DateTimeField()
    mobile_number_verified = BooleanField()
    mobile_number_verified_at = DateTimeField()
    email_activation_token = StringField()
    email_activation_token_sent_at = DateTimeField()
    email_verified = BooleanField()
    email_verified_at = DateTimeField()
    mac_address = StringField()
    last_login_at = DateTimeField(null=True)
    last_login_ip = StringField()
    last_login_user_agent = StringField()
    last_login_channel = StringField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
    otp_source = StringField()
    icmyc_user_id = IntField()
    sign_up_with = StringField(default='mobile_number')
    settings = DictField(default={"email_notifications_preferred": True, 
    "sms_notifications_preferred": True, 
    "push_notifications_preferred": True})
    sign_up_ip_address = StringField(null=True)
    sign_up_user_agent = StringField(null=True)
    has_at_least_one_social_account = BooleanField(default=False)
    social_accounts = ListField()
    channels = ListField()
    avatar = StringField(null=True)
    city_id = IntField()
    ward_id = IntField()

    meta = {'collection': 'profiles'}

    def __str__(self):
        return self.full_name
