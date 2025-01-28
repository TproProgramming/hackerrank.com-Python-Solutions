"""
Task
Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

Input Format

The first line of input contains an integer, .
The second line contains  space-separated integers.
The third line contains an integer, .
The fourth line contains  space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

Sample Input

STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}
Sample Output

5
9
11
12
"""

sizeM = int(input())
m = input().split()
sizeN = int(input())
n = input().split()

#Convert to int
m = [int(x) for x in m]
n = [int(y) for y in n]

#Convert to set
m_set = set(m)
n_set = set(n)

a = m_set ^ n_set

# Convert the set to a list and sort it in ascending order
sorted_list = sorted(a)

for i in sorted_list:
    print(i)
)

