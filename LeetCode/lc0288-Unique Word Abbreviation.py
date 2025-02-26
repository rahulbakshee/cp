class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbr = defaultdict(set)
        
        for word in dictionary:
            key, value = self.get_abbr(word)
    
            # add it to the gloabl dict (abbr)
            self.abbr[key].add(value)
            

    def isUnique(self, word: str) -> bool:
        key, value = self.get_abbr(word)

        if key not in self.abbr:
            return True
        
        if key in self.abbr:
            if len(self.abbr[key])==1 and word in self.abbr[key]:
                return True
            else:
                return False
            

        return False           
                   
        
    def get_abbr(self, word:str)-> None:
        if len(word) <= 2:
            key = word
            
        else:
            length = len(word)-2
            key = word[0] + str(length) + word[-1] 
        
        return key, word

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
