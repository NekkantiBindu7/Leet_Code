class Solution:
    def compress(self, chars: List[str]) -> int:
        l = r = 0
        while l < len(chars) and r < len(chars):
            # assign the new letter to l
            chars[l] = chars[r]
            count = 0
            # start counting number of letter
            while r < len(chars) and chars[r] == chars[l]:
                count += 1
                r += 1
            if count > 1:
                cnt_len = len(str(count))
                # assign the count result to chars
                chars[l+1:l+1+cnt_len] = str(count)
                l += cnt_len
            l += 1
        return l