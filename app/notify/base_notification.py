import re

notifications = list()

def add_notification(message):
    notifications.append({'message': message})

def is_true(value, message):
    if value:
        notifications.append({'message': message})

def is_required(value, message):
    if not value or len(value) <= 0:
        notifications.append({'message': message})

def has_min_len(value, min, message):
    if not value or len(value) < min:
        notifications.append({'message': message})

def has_max_len(value, max, message):
    if not value or len(value) > max:
        notifications.append({'message': message})

def is_fixed_len(value, bigger, message):
    if len(value) != bigger:
        notifications.append({'message': message})

def is_email(value, message):
    reg_exp = re.compile(r"/^\w + ([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/");
    if not reg_exp.findall(value):
        notifications.append({'message': message})

def get_all_notifications():
    return notifications

def valid():
    return notifications.length == 0