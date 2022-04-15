class Solution(object):
    def myAtoi(self, s):
        sign = 1
        max_int, min_int = 2147483647, -2147483648
        result, pos = 0, 0
        ls = len(s)
        while pos < ls and s[pos] == ' ':
            pos += 1
        if pos < ls and s[pos] == '-':
            sign = -1
            pos += 1
        elif pos < ls and s[pos] == '+':
            pos += 1
        while pos < ls and ord(s[pos]) >= ord('0') and ord(s[pos]) <= ord('9'):
            num = ord(s[pos]) - ord('0')
            if result > max_int / 10 or ( result == max_int / 10 and num >= 8):
                if sign == -1:
                    return min_int
                return max_int
            result = result * 10 + num
            pos += 1
        return sign * result


if __name__ == '__main__':
    s = Solution();
    print (s.myAtoi("+-2"))