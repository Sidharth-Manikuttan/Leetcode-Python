class Solution:
    def maximumLength(self, s: str) -> int:
        char_groups = {}
        for i in range(len(s)):
            for j in range(i, len(s)):
                if len(set(s[i:j+1])) == 1:
                    char = s[i]
                    substr_length = j - i + 1
                    count = 0
                    for k in range(len(s) - substr_length + 1):
                        if s[k:k+substr_length] == s[i:j+1]:
                            count += 1
                    if char not in char_groups:
                        char_groups[char] = {}
                    char_groups[char][substr_length] = max(
                        char_groups[char].get(substr_length, 0), 
                        count)

        max_length = -1
        for char, lengths in char_groups.items():
            for length, count in sorted(lengths.items(), reverse=True):
                if count >= 3:
                    max_length = max(max_length, length)
                    break
        return max_length
