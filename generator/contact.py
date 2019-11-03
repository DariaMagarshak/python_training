from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys
import calendar


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:,f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o =="-n":
        n = int(a)
    elif o == "-f":
        f=a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits +""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

random_year1 = [random.choice(string.digits) for h in range(4)]
random_year2 = [random.choice(string.digits) for h in range(4)]

random_day1 = str(random.choice(list(range(1, 32))))
random_day2 = str(random.choice(list(range(1, 32))))

random_month1 = random.choice(calendar.month_name)
random_month2 = random.choice(calendar.month_name)


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", company="",
                               company_address="", home_number="", mobile_number="", work_number="", fax_number="", email="",
                               email2="", email3="", homepage="", bday="-", bmonth="-", byear="", aday="-",
                               amonth="-", ayear="", address2="", homephone="", notes="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
                               nickname=random_string("nickname", 10), company=random_string("company", 10),
                               company_address=random_string("company_address", 10), home_number=random_string("home_number", 10),
                               mobile_number=random_string("mobile_number", 10), work_number=random_string("work_number", 10), fax_number=random_string("fax_number", 10),
                               email=random_string("email", 10), email2=random_string("email2", 10), email3=random_string("email3", 10), homepage=random_string("homepage", 10),
                               bday=random_day1, bmonth=random_month1, byear=random_year1, aday=random_day2,
                               amonth=random_month1, ayear=random_year2, address2=random_string("address2", 10),
                               homephone=random_string("homephone", 10), notes=random_string("notes", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

