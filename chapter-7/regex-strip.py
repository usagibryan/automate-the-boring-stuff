import re

def regex_strip(string, chars=None):
    if chars is None:
        # If no characters are specified, remove whitespace from the beginning and end of string
        regex = r'^\s+|\s+$'
    else:
        # If characters are specified, build a regular expression that matches them
        escaped_chars = re.escape(chars)
        regex = r'^[' + escaped_chars + r']+|[' + escaped_chars + r']+$'
    # Use the regular expression to replace matches with empty strings
    return re.sub(regex, '', string)