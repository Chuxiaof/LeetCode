class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        count = []
        for email in emails:
            local, domain = [], []
            idx = 0
            for char in email:
                
                if(char == "@" or char == "+"):
                    break
                elif(char == "."):
                    continue
                else:
                    local.append(char)
                idx += 1
                    
            while(email[idx] != "@"): idx += 1
            
            for char in email[idx:]: domain.append(char)
            print(local, domain)
                
            if (local, domain) not in count: count.append((local, domain))

        return len(count)