"""
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after
each character of searchWord is typed. Suggested products should have common prefix
with searchWord. If there are more than three products with a common prefix return
the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.
"""
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        count = 0
        pre = ""
        op = []
        for i in searchWord:
            op1 = []
            pre += i

            for j in products:
                if count == 0 and j.startswith(pre):
                    count += 1
                    op1.append(j)
                elif count and j.startswith(pre):
                    count += 1
                    op1.append(j)
                elif count and (not j.startswith(pre)):
                    op.append(op1)
                    count = 0
                    break

                if count == 3:
                    op.append(op1)
                    count = 0
                    break
            else:
                op.append(op1)
                count = 0

        return op


products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"


w = Solution()
print(w.suggestedProducts(products, searchWord))
