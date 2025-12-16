import re
import email.utils

N = int(input())
REX = r"[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}"
for _ in range(N):
    EMAIL = email.utils.parseaddr(input())
    if re.fullmatch(REX, EMAIL[1]):
        print(email.utils.formataddr((EMAIL[0], EMAIL[1])))
