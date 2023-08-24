class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphanum = 'abcdefghijklmnopqrstuvwxyz0123456789'
        s_arr = []

        for char in s:
            # Iterate forwards over characters in string
            # O(n)
            if (char in alphanum):
                s_arr.append(char)

        for idx,char in enumerate(s_arr):
            if (s_arr[idx] != s_arr[len(s_arr)-idx-1]):
                return False
        
        return True