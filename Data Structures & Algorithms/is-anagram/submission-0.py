
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!= len(t):
            return False

        dictt1 = self.frequency_dict(s)
        dictt2 = self.frequency_dict(t)

        return dictt1 == dictt2

    


    def frequency_dict(self,string):

        dictt ={}
        for val in string:
            if val in dictt:
                dictt[val]+=1
            else:
                dictt[val]=1

        return dictt

        

    
        

        