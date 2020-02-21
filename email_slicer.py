# obtain user email address

email = input("What is your email?: ").strip()

# slice user name

user = email[:email.index("@")]

# slice domain name

domain = email[email.index("@") + 1 :]

# format message

output = "Your username is {} and your domain is {}".format(user, domain)

print(output)

# display output message
