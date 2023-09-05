# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         if word1:
#             if word2:
#                 if len(word1) == len(word2):
#                     return ''.join([word1[i] + word2[i] for i in range(len(word1))])
#                 else:
#                    s= ''.join([word1[i] + word2[i]  for i in range(min([len(word1),len(word2)]))])
#                    if len(word1) > len(word2):
#                        s += word1[len(word2)-1:]
#                    else:
#                        s += word2[len(word1)-1:]
#                    return s
#             else: word1
#         else: return word2

# def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
#     if n == 0 :
#         return True
#     if flowerbed[0] == 0 and flowerbed[1] == 0:
#         n -= 1
#         flowerbed[0] = 1
#     if flowerbed[-1] == 0 and flowerbed[-2] == 0:
#         n -= 1
#         flowerbed[-1] = 1
#     if n <= 0:
#         return True
#     for i in range(len(flowerbed)):
#         if flowerbed[i] == 0:
#             try:
#                 if flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0:
#                     n -= 1
#                     flowerbed[i] = 1
#             except IndexError:
#                 return False
#     if n <= 0:
#         return True
#     return False
# print(canPlaceFlowers([0,0], 2))