from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailSet = set([])
        for email in emails:
            parsed = ""
            n = len(email)
            i = 0
            while i < n and email[i] != "@":
                if email[i] == "+":
                    while email[i] != "@":
                        i+= 1
                    i -= 1
                elif email[i] != ".":
                    parsed += email[i]
                i += 1
            parsed += email[i:]
            emailSet.add(parsed)
            print(parsed)
        return len(emailSet)