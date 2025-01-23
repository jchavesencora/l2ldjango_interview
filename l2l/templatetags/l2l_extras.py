from django import template
from datetime import datetime

register = template.Library()

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"
STRING_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"



@register.filter
def l2l_dt(date):
    if isinstance(date, datetime):
        return date.strftime(STRING_DATE_FORMAT)

    if isinstance(date, str):
        try:
            parsed_date = datetime.strptime(date, DATE_FORMAT)
            return parsed_date.strftime(STRING_DATE_FORMAT)
        except ValueError:
            return date
    return None