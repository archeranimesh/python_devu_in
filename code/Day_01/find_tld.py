# WAP to count the emails of a particular TLD from a given list of emails.
my_email_list = [
    "john@gmail.com",
    "ravi@rediff.com",
    "aakash@hotmail.com",
    "deepak@gmail.com",
]

tld = "gmail.com"


def find_tld(my_email_list, tld):
    count = 0
    for x in my_email_list:
        if tld in x:
            count += 1
    return count


print(str(my_email_list).count("@" + tld))

print(find_tld(my_email_list, "@" + tld))

