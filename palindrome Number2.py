class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif 0 <= x < 10:
            return True
        
        else:   
            num_digits = 0
            tmp = x
            while tmp >= 10:
                tmp = tmp / 10
                num_digits+=1
            num_digits = num_digits+1
            
            if num_digits == 2:
                temp1digit = x % 10
                temp2digit = x//10
                
                if temp1digit != temp2digit:
                    return False
                return True
            half = num_digits//2
            if num_digits%2 == 1:
                temp3 = x
                fsum = x//10**(half+1)
                rsum = 0
                for n in range(0,half):
                    m = half-n-1
                    temp2 = temp3%10
                    temp3 = temp3//10
                    
                    rsum = rsum + temp2*(10**m)
                
            
            else:
                temp3 = x
                fsum = x//10**half
                rsum = 0
                for n in range(0,half):
                    m = half-n-1
                    temp2 = temp3%10
                    temp3 = temp3//10
                    
                    rsum = rsum + temp2*(10**m)
                
            if fsum != rsum:
                    return False
            return True
            
        
        
            
       
