""" You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).

Function Description

Complete the rangoli function in the editor below.

rangoli has the following parameters:

int size: the size of the rangoli
Returns

string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)
Input Format

Only one line of input containing , the size of the rangoli.

Constraints
0<size<27

Sample Input

5
Sample Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e-------- """

def print_rangoli(size):
    if size == 0:
        return
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    d = {}
    width = 4 * size - 3          # corrected width formula
    center = width // 2            # middle index of each row

    for r in range(size): #first r is widest, then less letters
        row = ['-'] * width         # list of individual dash characters
        row[center] = alphabet[r]   # place this row's "home" letter dead center
        
        # place each further-out letter symmetrically, 2 positions apart
        for step, k in enumerate(range(r + 1, size), start=1):
            row[center - 2*step] = alphabet[k]
            row[center + 2*step] = alphabet[k]
        
        d[r] = row
        d[-r] = row   # mirror row - same content, negative key for ordering

    for i in sorted(d.keys()):
        return "".join(d[i])
#O complexity is O(n^2) because we have to build n rows, each of which has up to n characters (the width of the rangoli grows linearly with size).

#another solution, harder to interpret, same O complexity but more compact and elegant
    # alpha = 'abcdefghijklmnopqrstuvwxyz'
    # width = 4 * size - 3
    # lines = []
    # for i in range(size):
    #     letters = alpha[i:size]                    # e.g. for i=1, size=3  "bc"
    #     row = "-".join(letters)                     # "b-c"
    #     mirrored = row[::-1] + row[1:]               # "c-b" + "-c" "c-b-c"
    #     lines.append(mirrored.center(width, '-'))
    # return '\n'.join(lines[:0:-1] + lines)



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)