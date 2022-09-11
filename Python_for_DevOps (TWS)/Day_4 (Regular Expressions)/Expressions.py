# This is Regular Expression Tutorial Basic Code.

"""

Regular Expression for extracting e-mail IDs.

"""

import re                                       # To import "Regular Expression" Library.

txt = """This text service notifies soumojitdas65@gmail.com and soumojitdas65@hotmail.com and soumojitdas65@yahoo.com"""

mails = re.findall("[a-z0-9\.\-\_]+@+[a-z0-9\.\-\_]+.+[a-z]", txt)

print(mails)