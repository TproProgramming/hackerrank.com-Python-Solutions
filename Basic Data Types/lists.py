"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example





: Append  to the list, .
: Append  to the list, .
: Insert  at index , .
: Print the array.
Output:
[1, 3, 2]
Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""

if __name__ == '__main__':
    N = int(input())
    
    #Initialize list
    li =[]
    for i in range(N):
        command = str(input())
        
        #Split commands, index [0] = command, [1] is value or index, [2] is value
        command_parts = command.split()
        
        
        if command_parts[0] == 'insert':
            index = int(command_parts[1])
            value = int(command_parts[2])
            li.insert(index,value)
        
        elif command_parts[0] == 'print':
            print(li)
        
        elif command_parts[0] == 'remove':
            li.remove(int(command_parts[1]))
        
        elif command_parts[0] == 'append':
            li.append(int(command_parts[1]))
        
        elif command_parts[0] == 'sort':
            li.sort()
        
        elif command_parts[0] == 'pop':
            li.pop()
        
        elif command_parts[0] == 'reverse':
            li.reverse()
        
        #Error Handling
        else:
            print("Invalid Command")
            
            
    