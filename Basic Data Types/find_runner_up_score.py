"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.


Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is . Hence, we print  as the runner-up score.
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort(reverse=True)
    
    arr_max = arr[0]
    for i in range(0,len(arr)):
        if arr[i] == arr_max:
            continue
        else:
            #Print second highest 
            print(arr[i])
            break
    