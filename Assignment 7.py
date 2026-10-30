import re

# Regular expression pattern for matching email addresses
EMAIL_PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'

# Sample text containing email addresses
text = """
Contact us at support@example.com or sales123@gmail.com.
You can also reach admin.office@college.edu.
This is not an email: user@com
"""

# Find all email addresses
emails = re.findall(EMAIL_PATTERN, text)

# Display the results
print("Email addresses found:")
for email in emails:
    print(email)