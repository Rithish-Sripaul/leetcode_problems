def findlongestString(s):
	curr_hash_map = dict()

	for i in s:
		if i not in curr_hash_map:
			curr_hash_map[i] = 0

	start, end = 0, 0
	max_length = -1

	while end < len(s):

		curr_hash_map[s[end]] += 1
		while curr_hash_map[s[end]] > 1:
			max_length = max(max_length, end - start)
			curr_hash_map[s[start]] -= 1
			start += 1

		end += 1

	if max_length < 0:
		return len(s)
	return max(max_length, end - start)

s = "aabd"
print(findlongestString(s))


