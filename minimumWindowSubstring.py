def findSubString(s, t):
	hash_map = dict()
	for i in t:
		if i in hash_map:
			hash_map[i] += 1
		else:
			hash_map[i] = 1

	start, end = 0, 0

	min_window_length = len(s) + 1
	min_window_start = 0

	num_of_chars = len(t)

	while end < len(s):
		if s[end] in hash_map:
			if hash_map[s[end]] > 0:
				num_of_chars -= 1
			hash_map[s[end]] -= 1

		while num_of_chars == 0:
			if end - start + 1 < min_window_length:
				min_window_length = end - start + 1
				min_window_start = start

			if s[start] in hash_map:
				hash_map[s[start]] += 1

				if hash_map[s[start]] > 0:
					num_of_chars += 1

			start += 1
		end += 1

	if min_window_length == len(s) + 1:
		return "No Substring found"
	else:
		return s[min_window_start:min_window_start + min_window_length]

s = "ADOBECODEBANC"
t = "ABC"

print(findSubString(s, t))

