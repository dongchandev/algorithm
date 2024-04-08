import sys
from collections import defaultdict

books = defaultdict(int)
name_list = []
n = int(input())

for _ in range(n):
    book = sys.stdin.readline().rstrip()
    books[book] += 1

max_num = max(books.values())

for book in books:
    if books[book] == max_num:
        name_list.append(book)

name_list.sort()
print(name_list[0])