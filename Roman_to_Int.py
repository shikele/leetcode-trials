class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        if s.count('M') != 0:
            sum += s.count('M')*1000
            
            print (s.count('M'))
            if s.count('CM') != 0:
                sum = sum-s.count('CM')*100
                
        
        if s.count('D') !=0:
            sum += s.count('D')*500
            if s.count('CD') != 0:
                sum = sum-s.count('CD')*100
        
        if s.count('C') !=0:
            real_C = s.count('C')- s.count('CM')-s.count('CD')
            sum += real_C*100
            if s.count('XC') != 0:
                sum = sum-s.count('XC')*10
                
        if s.count('L') !=0:
            sum += s.count('L')*50
            if s.count('XL') != 0:
                sum = sum-s.count('XL')*10
        
        if s.count('X') !=0:
            real_X = s.count('X')-s.count('XC')-s.count('XL')
            sum += real_X*10
            
            if s.count('IX') != 0:
                sum = sum-s.count('IX')*1
        
        if s.count('V') !=0:
            sum += s.count('V')*5
            if s.count('IV') != 0:
                sum = sum-s.count('IV')*1
        
        if s.count('I') !=0:
            real_I = s.count('I')-s.count('IX')-s.count('IV')
            sum += real_I*1
        return sum
        
