import re
from django.core.exceptions import ValidationError


email_regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
phone_number_regex = r'^\+998\d{9}$'

def check_email_or_phone(user_input):
    if re.match(email_regex, user_input) is not None:
        return 'email'
    elif re.match(phone_number_regex, user_input) is not None:
        return 'phone'
    
    else:
        data={
            'status': False,
            'message': "Email yoki telefon raqamni to'g'ri kiriting",
        }
        raise ValidationError(data)

