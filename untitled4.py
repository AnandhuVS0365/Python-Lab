# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VIs895exL-Nn7anpTmYSrjK_qOY1_a1k

rahul
"""

"Count the number of characters (characters frequency) in a string" 
string=input("enter a string")
ch_count={str:string.count(str)for str in set(string)}
print(ch_count)
" Add 'ing' at end of a given string . if already ends with 'ing' then add 'ly"
string=input("enter a string")
if string.endswith('ing'):
  print(string+'ly')
else:
  print(string+'ing')
"Accept a list of words and return length of longest word "
word_list=[]
limit=int(input("enter size of list"))
print('enter words')
for i in range(limit):
  word_list.append(input())
print(max(len(i) for i in word_list))
" construct following pattern using nexted for loop"
size=int (input("enter size "))
for i in range(size*2):
    if i<=size:
        for j in range(i):
            print("*",end=" ")
        print("\n")
    else:
        for j in range(size*2-i):
            print("*",end=" ")
        print("\n")
"generate all factors of a number"
number=int(input('enter a number'))
factors=[i for i in range(1,number+1) if number%i==0]
print("factors of {} are {}".format(number,factors))
"write lambda function to find area of square,rectangle and triangle"
ch=int(input("1   find area of square\n\
              2   find are of rectangle \n\
              3   find area of triangle \n"))

if ch==1:
  x=int(input("enter the length of one side of a square"))
  square=lambda x:x*x
  print("Area of square is ",square(x))
if ch==2:
  x=int(input("enter the length of rectangle"))
  y=int(input("enter the breadth of rectangel"))
  rectangle=lambda x,y:x*y
  print("Area of rectanble is ",rectangle(x,y))
if ch==3:
  x=int(input("enter the height of triangle"))
  y=int(input("enter the breadth of triangle"))
  triangle=lambda x,y:0.5*x*y
  print("Area of trinagle is ", triangle(x,y))

