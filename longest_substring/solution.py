from collections import deque


class Solution:
    def longest_substring_len(self, s: str) -> int:
        seen_deque = deque()
        seen_set = set()
        max_len = 0

        for ch in s:
            while ch in seen_set:
                removed = seen_deque.popleft()
                seen_set.remove(removed)
            seen_deque.append(ch)
            seen_set.add(ch)
            max_len = max(max_len, len(seen_deque))

        return max_len
