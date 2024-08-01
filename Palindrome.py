num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")         # without converting to string and checking for palinfrome
else:
    print("Not a palindrome!")


######################################################################

class Solution(object):
    def isPalindrome(self, x):
        temp = str(x)                           # converting in string and then cehcking for palindrome
        n = temp[::-1]
        if temp == n:
            return True
        else:
            return False