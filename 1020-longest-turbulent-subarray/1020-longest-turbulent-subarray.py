class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # alternate the signs
        sign = ""
        # the first 1 is always ok because we dont have a sign yet
        res = 1
        l, r = 0, 1

        while r < len(arr):
            # check if current is bigger
            if arr[r - 1] > arr[r] and sign != ">":
                # if the result is bigger take the result else 
                res = max(res, r - l + 1)
                r += 1
                sign = ">"
            # check if prev is bigger and not same sign
            elif arr[r - 1] < arr[r] and sign != "<":
                # if the result is bigger take the result else 
                res = max(res, r - l + 1)
                r += 1
                sign = "<"

            # if we have the same sign 2 times
            else:
                if arr[r - 1] == arr[r]:
                    r += 1
                l = r - 1
                sign = ""
        return res