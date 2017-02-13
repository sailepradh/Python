#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# with open('/Users/salendrapradh/Documents/Python_practise/Lessons/book_chapter.txt','r',encoding='utf-8') as f:
#
#     all_lines = [] # the main container
#
#     for line in f:
#         all_lines.append(line.strip())
#
#     # Now, outside the loop, I print the total
#     total = 0
#     for line in all_lines:
#         total = total + len(line) # or total += len(line)
#
#     # Now I have the total
#     print(total)

# with open('/Users/salendrapradh/Documents/Python_practise/Lessons/book_chapter.txt','r',encoding='utf-8') as f:
#
#     all_lines =  []
#
#     for line in f:
#         all_lines.append(len(line.strip()))
#
#     results = sum (all_lines)
#     print(results)

with open('/Users/salendrapradh/Documents/Python_practise/Lessons/book_chapter.t','r',encoding='utf-8') as f:

    total =  0

    for line in f:
        total += len(line.strip() )

   print (total)