'''
Vasya likes the number 239. Therefore, he considers a number pretty if its last digit
is 22, 33 or 99.
Vasya wants to watch the numbers between L and R (both inclusive), so he asked you to
determine how many pretty numbers are in this range. Can you help him?
Input
 The first line of the input contains a single integer T denoting the number of test
cases. The description of T test cases follows.
 The first and only line of each test case contains two space-separated
integers L and R.
Output
For each test case, print a single line containing one integer — the number of pretty
numbers between L and R.
Constraints
 1≤1001≤T≤100
 1≤1051≤L≤R≤105

'''

'''pretty number identification 239 '''
def count_pretty_numbers(l,r):
    pretty_count=0
    #Iterate through the range and count pretty numbers
    for num in range(l,r+1):
        last_digit=num%10
        if last_digit==5:
            pretty_count +=1
    return pretty_count
#input the number of test cases
t = int(input())
#progress each test cases
for _ in range(t):
    #Input the range L and R fro each case
    l,r=map(int,input().split())
    #call the function to count pretty numbers in the given range
    result=count_pretty_numbers(l,r)
    #print the result for each test case
    print(result)


