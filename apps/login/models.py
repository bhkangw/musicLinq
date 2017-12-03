from __future__ import unicode_literals
import re
import bcrypt
from django.db import models
import datetime

NAME_REGEX = re.compile(r'^[a-zA-Z]\w+$')
EMAIL_REGEX = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')


class UserManager(models.Manager):
    def registation_validator(self, postData):
        response = {'status': True, 'errors': []}
        # check length of name fields
        if len(postData['first_name']) < 2:
            response['errors'].append(
                "Name field must be at least 2 characters")
        # check length of password
        if len(postData['password']) < 5:
            response['errors'].append("Password must be at least 5 characters")
        # check name fields for only letter characters
        if not re.match(NAME_REGEX, postData['first_name']):
            response['errors'].append("Name field but must be letters only")
        # check emailiness of email
        if not re.match(EMAIL_REGEX, postData['email']):
            response['errors'].append("Invalid email")
        # check uniqueness of email
        if len(User.objects.filter(email=postData['email'])) > 0:
            response['errors'].append("Email already in use")
        # check password = pwconfirm
        if postData['password'] != postData['pwconfirm']:
            response['errors'].append("Passwords do not match")

        if len(response['errors']) == 0:  # make our new user
            hashed = bcrypt.hashpw((postData['password'].encode()),
                                   bcrypt.gensalt(5))
            if len(User.objects.all()) == 0:
                new_user = self.create(
                    first_name=postData['first_name'],
                    email=postData['email'],
                    user_level=9,
                    password=hashed)
                response["user"] = new_user
            else:
                new_user = self.create(
                    first_name=postData['first_name'],
                    email=postData['email'],
                    user_level=1,
                    password=hashed)
                response["user"] = new_user
        else:
            response['status'] = False
        return response

    def login_validator(self, postData):
        response = {'status': True, 'errors': []}
        # check DB for postData['email']
        if len(self.filter(email=postData['email'])) > 0:
            # check this user's password
            user = self.filter(email=postData['email'])[0]
            if not bcrypt.checkpw(postData['password'].encode(),
                                  user.password.encode()):
                response['errors'].append(
                    "Email/password incorrect, please try again!")
                response['status'] = False
            response['user'] = user
        else:
            response['errors'].append(
                "Email/password incorrect, please try again!")
            response['status'] = False
        if len(response['errors']) == 0:
            return response
        return response


class User(models.Model):
    first_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_level = models.IntegerField()
    # favquotes = models.ForeignKey(Quote, related_name="user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.email


# from __future__ import unicode_literals
# import re
# import bcrypt
# from django.db import models

# NAME_REGEX = re.compile(r'^[a-zA-Z]\w+$')
# EMAIL_REGEX = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')

# class UserManager(models.Manager):
#     def registation_validator(self, postData, type):
#         errors = {}
#         if type == "register":
#             # check length of name fields
#             if len(postData['first_name']) < 2 or len(
#                     postData['last_name']) < 2:
#                 errors['name'] = "Name fields must be at least 2 characters"
#             # check length of password
#             if len(postData['password']) < 8:
#                 errors['password'] = "Password must be at least 8 characters"
#             # check name fields for only letter characters
#             if not re.match(NAME_REGEX,
#                             postData['first_name']) or not re.match(
#                                 NAME_REGEX, postData['last_name']):
#                 errors['namenum'] = "Name field but must be letters only"
#             # check emailiness of email
#             if not re.match(EMAIL_REGEX, postData['email']):
#                 errors['email'] = "Invalid email"
#             # check uniqueness of email
#             if len(User.objects.filter(email=postData['email'])) > 0:
#                 errors['dupemail'] = "Email already in use"
#             # check password = pwconfirm
#             if postData['password'] != postData['pwconfirm']:
#                 errors['pwconfirm'] = "Passwords do not match"
#         if type == "update":
#             # check length of name fields
#             if len(postData['first_name']) < 2 or len(
#                     postData['last_name']) < 2:
#                 errors['name'] = "Name fields must be at least 2 characters"
#             # check length of password
#             if len(postData['password']) < 8:
#                 errors['password'] = "Password must be at least 8 characters"
#             # check name fields for only letter characters
#             if not re.match(NAME_REGEX,
#                             postData['first_name']) or not re.match(
#                                 NAME_REGEX, postData['last_name']):
#                 errors['namenum'] = "Name field but must be letters only"
#             # check emailiness of email
#             if not re.match(EMAIL_REGEX, postData['email']):
#                 errors['email'] = "Invalid email"
#             # check password = pwconfirm
#             if postData['password'] != postData['pwconfirm']:
#                 errors['pwconfirm'] = "Passwords do not match"

#         if not errors:  # make our new user
#             hashed = bcrypt.hashpw((postData['password'].encode()),
#                                    bcrypt.gensalt(5))
#             if len(User.objects.all()) == 0:
#                 new_user = self.create(
#                     first_name=postData['first_name'],
#                     last_name=postData['last_name'],
#                     email=postData['email'],
#                     user_level=9,
#                     password=hashed)
#                 return new_user
#             else:
#                 new_user = self.create(
#                     first_name=postData['first_name'],
#                     last_name=postData['last_name'],
#                     email=postData['email'],
#                     user_level=1,
#                     password=hashed)
#                 return new_user
#         return errors

#     def login_validator(self, postData):
#         errors = {}
#         # check DB for postData['email']
#         if len(self.filter(email=postData['email'])) > 0:
#             # check this user's password
#             user = self.filter(email=postData['email'])[0]
#             if not bcrypt.checkpw(postData['password'].encode(),
#                                   user.password.encode()):
#                 errors['loginpw'] = "Email/password incorrect"
#         else:
#             errors['login'] = "Email/password incorrect"
#         if errors:
#             return errors
#         return user

# class User(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     user_level = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = UserManager()

#     def __str__(self):
#         return self.email