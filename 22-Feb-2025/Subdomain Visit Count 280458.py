# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        address = {}
        for elem in cpdomains:
            elem = list(elem.split(" "))
            elem[0]= int(elem[0])
            curr = elem[1].split(".")
            print(curr)
            full_domain = ""

            for i in range(len(curr) - 1, -1, -1):
                full_domain = curr[i] + ("." + full_domain if full_domain else "")
                if full_domain in address:
                    address[full_domain] += elem[0]
                else:
                    address[full_domain] = elem[0]
        result = [f"{count} {domain}" for domain, count in address.items()]
        return result 

           