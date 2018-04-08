******************* Read me  ***************************


Important: Python interpreter is slow , thus running time might perform 
slower than other languages like Java ,C, C++.
Here are few links that can explain Why?

https://stackoverflow.com/questions/8097408/why-python-is-so-slow-for-a-simple-for-loop
https://stackoverflow.com/questions/3033329/why-are-python-programs-often-slower-than-the-equivalent-program-written-in-c-or


Steps to run the code,

1) Install python 2.7 
2) put source file (project.py) in the same 
directory where input test files are present 
3) Reach the folder in command prompt/terminal where python codes 
and test input files are present.



Case 1 : When input is reading from file , command line arguments are filename and print path instruction. 


Suppose we have a file named two.txt in the same folder that 
consists of following  test case.

20 2
1 2 10 8 10 2 2
2 2 10 8 10 2 4



Now run the following commands :

>>python project.py two.txt

Output: 

98 3

>>python project.py two.txt 2

Output:

98 3
[0, 10]
[1, 9]
[2, 8]

>>python project.py two.txt 0

Output:

98 3


Case 2 : When input is reading from console , command line arguments are blank space or 
"-" and print path instruction. 


run the following commands:

>>python project.py

Input:
20 2
1 2 10 8 10 2 2
2 2 10 8 10 2 4

Output:
98 3

>>python project.py - 2

Input:
20 2
1 2 10 8 10 2 2
2 2 10 8 10 2 4

Output:
98 3
[0, 10]
[1, 9]
[2, 8]

>>python project.py - 0

Input:
20 2
1 2 10 8 10 2 2
2 2 10 8 10 2 4

Output:
98 3



For other inputs like mentioned below, program is returning desired output 
along with the path.


Input:
50080 2
1 81 4050 913 1227 405 4050
2 63 3150 416 4213 315 3150

Output:
2499750 42

Input:
55645 3
1 70 1400 937 2370 140 280
2 66 1320 575 4622 132 1320
3 49 980 726 2968 98 980

Output:
1111640 702


Input:
18682 9
1 51 5049 55 3644 504 5040
2 86 8514 26 645 851 1702
3 81 8019 31 1437 801 8010
4 50 4950 50 3732 495 4950
5 66 6534 24 2944 653 1306
6 75 7425 13 1162 742 7420
7 97 9603 74 4425 960 1920
8 45 4455 52 578 445 890
9 80 7920 57 4319 792 1584

Output:
1846708 96810
