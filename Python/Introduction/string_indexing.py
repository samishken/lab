# name = "Jaylen"
# print(name[1]) # a
# print(name[-1]) # n
# print(name[3]) # l
#
# text = "Random string with a lot of characters"
# print(text[-1]) # s
# print(text[-2]) # r
#
# # range
# fruit = "Pineapple"
# print(fruit[:4]) # Pine
# print(fruit[4:]) # apple
# print(fruit[1:3]) # in

# modify string
message = "A kong string with a silly typo"
### message[2] = "l"  # "kong to long" can be modified like this
new_message = message[0:2] + "l" + message[3:]
print(new_message)

# replace old domain
def replace_domain(email, old_domain, new_domain):
    # Make the email and old_domain lowercase for case-insensitive comparison
    if "@" + old_domain.lower() in email.lower():
        index = email.lower().index("@" + old_domain.lower())
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

test_emails = [
    "user@example.com",  # Regular case
    "user@EXAMPLE.com",  # Case-insensitive match
]
old_domain = "example.com"
new_domain = "newdomain.com"

for email in test_emails:
    print(f"Original: {email} -> Updated: {replace_domain(email, old_domain, new_domain)}")



