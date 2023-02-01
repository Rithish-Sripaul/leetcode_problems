# BRUTE FORCE
# def palindromeSubString(s):
# 	res = 0

# 	for i in range(len(s)):
# 		for k in range(i, len(s)):
# 			string = s[i:k]
# 			left = 0
# 			right = len(string)
# 			isPalind = True
# 			while left <= right:
# 				if s[left] != s[right]:
# 					isPalind = False
# 					break
# 				left += 1
# 				right -= 1
# 			res += 1 if isPalind else 0
# 	print(res)


# palindromeSubString("abc")

# IMPROVED BRUTE FORCE

def palindromeSubString(s):
	res = 0


	for i in range(len(s)):
		l, r = i - 1, i + 1
		res += 1

		while l >= 0 or r < len(s):
			if l < 0:
				print(s[i:r])
				if s[r] == s[i]:
					res += 1
			if r >= len(s):
				print(s[l:i])
				if s[l] == s[i]:
					res += 1
			if l >= 0 and r < len(s):
				print(s[l:r])
				if s[l] == s[r]:
					res += 1
				else:
					break
			l -= 1
			r += 1
	print(res)

palindromeSubString("aaa")


