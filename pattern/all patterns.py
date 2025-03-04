"""""
Pattern 
1. Solid Square Pattern
Create a solid square of asterisks.
""""

n = 5
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()

"""""
Output:

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
2. Hollow Square Pattern
Design a square frame using asterisks.
"""

n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

"""""
Output:

* * * * *
*       *
*       *
*       *
* * * * *
3. Increasing Triangle Pattern
Generate a right-aligned triangle using asterisks.
"""

n = 5
for i in range(1, n+1):
    for j in range(i):
        print('*', end=' ')
    print()

"""""
Output:

*
* *
* * *
* * * *
* * * * *
4. Decreasing Triangle Pattern
Create a right-aligned triangle with asterisks in reverse order.
"""

n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()

"""""
Output:

* * * * *
* * * *
* * *
* *
*
5. Right-angled Triangle Pattern (Left)
Construct a left-aligned triangle.
"""

n = 5
for i in range(n):
    print('* ' * (i+1))

"""""
Output:

*
* *
* * *
* * * *
* * * * *
6. Downward Triangle Mirror Pattern
Build a mirrored triangle descending from right to left.
"""


n = 5
for i in range(n):
    print('  ' * i + '* ' * (n-i))

"""""
Output:

* * * * *
  * * * *
    * * *
      * *
        *
7. Pyramid Pattern
Create a centered pyramid.
"""

n = 5
for i in range(n):
    print(' ' * (n-i-1) + '* ' * (i+1))

"""""
Output:

    *
   * *
  * * *
 * * * *
* * * * *
8. Inverted Pyramid Pattern
Design an inverted pyramid.
"""


n = 5
for i in range(n):
    print(' ' * i + '* ' * (n-i))

"""""
Output:

* * * * *
 * * * *
  * * *
   * *
    *
Here are the remaining 22 pattern exercises with their Python code and respective outputs. These exercises cover a variety of pattern styles, progressing in complexity and helping further reinforce your understanding of nested loops in Python.

9. Diamond Pattern
Create a diamond shape with asterisks.
"""

n = 5
for i in range(n):
    print(' ' * (n-i-1) + '* ' * (i+1))
for i in range(n-1):
    print(' ' * (i+1) + '* ' * (n-i-1))

"""""
Output:

    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
10. X Pattern
Form an ‘X’ shape using asterisks.
"""


n = 5
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

"""""
Output:

*       *
  *   *
    *
  *   *
*       *
11. Hourglass Pattern
Create an hourglass pattern using asterisks.

"""


n = 5
for i in range(n, 0, -1):
    print(' ' * (n-i) + '* ' * i)
for i in range(2, n+1):
    print(' ' * (n-i) + '* ' * i)

"""
Output:

* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *
12. Right Arrow Pattern
Construct a right arrow with asterisks.
"""

n = 5
for i in range(n):
    if i < n // 2:
        print('* ' * (i+1))
    else:
        print('* ' * (n-i))
"""""
Output:

*
* *
* * *
* *
*
13. Left Arrow Pattern
Create a left arrow pattern.
"""

n = 5
for i in range(n):
    if i <= n // 2:
        print('  ' * (n//2 - i) + '* ' * (i+1))
    else:
        print('  ' * (i - n//2) + '* ' * (n-i))
"""""
Output:

        *
      * *
    * * *
      * *
        *
14. Checkerboard Pattern
Generate a checkerboard pattern of asterisks.
"""

n = 5
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
"""""
Output:

* * * * *
 * * * * 
* * * * *
 * * * * 
* * * * *
15. Zigzag Pattern
Create a zigzag pattern using asterisks.
"""

n = 9
for i in range(3):
    for j in range(n):
        if (j % 4 == 0 and i == 0) or (j % 4 == 2 and i == 2) or (j % 4 == 1 or j % 4 == 3 and i == 1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

"""""
Output:

*     *     *
 *   * *   * 
  *     *    
16. Plus Sign Pattern
Form a plus sign (+) shape.
"""

n = 5  # n must be odd
mid = n // 2
for i in range(n):
    for j in range(n):
        if i == mid or j == mid:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
"""""
Output:

    *    
    *    
* * * * *
    *    
    *    
17. Cross Pattern
Create a cross (X) pattern using asterisks.
"""

n = 5  # n should be odd
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
"""""
Output:

*       *
  *   *
    *
  *   *
*       *
18. Vertical Lines Pattern
Generate vertical lines using asterisks.
"""


n = 5
for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            print('*', end='  ')
        else:
            print(' ', end='  ')
    print()
"""""
Output:

*   *   *
*   *   *
*   *   *
*   *   *
*   *   *
19. Staircase Pattern (Ascending)
Build an ascending staircase pattern.
"""

n = 5
for i in range(1, n+1):
    print((' ' * (n-i)) + ('# ' * i))

"""""
Output:

    #
   # #
  # # #
 # # # #
# # # # #
20. Staircase Pattern (Descending)
Create a descending staircase pattern.
"""

n = 5
for i in range(n, 0, -1):
    print((' ' * (n-i)) + ('# ' * i))
"""""
Output:

# # # # #
 # # # #
  # # #
   # #
    #
21. Alternating Pattern
Design a pattern with alternating asterisks and dashes.
"""

n = 5
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print('*', end=' ')
        else:
            print('-', end=' ')
    print()

"""""
Output:

* - * - *
- * - * -
* - * - *
- * - * -
* - * - *
22. Spiral Pattern
Create a spiral pattern inside a matrix.
"""

n = 5
a = [[' ' for x in range(n)] for y in range(n)]
x, y = 0, 0
dx, dy = 0, 1

for i in range(n**2):
    a[x][y] = '*'
    if a[(x+dx)%n][(y+dy)%n] == '*':
        dx, dy = dy, -dx
    x, y = x + dx, y + dy

for row in a:
    print(' '.join(row))

"""""
Output:

* * * * *
        *
* * *   *
*     * *
* * * * *
23. Swastika Pattern
Generate a swastika pattern (commonly used in ancient cultures).
"""

n = 7  # n must be odd
mid = n // 2
for i in range(n):
    for j in range(n):
        if (i == mid or j == mid) or (i < mid and j == 0) or (j < mid and i == 0) or (i > mid and j == n-1) or (j > mid and i == n-1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

"""""
Output:

* * * * * * *
*           *
* * *   * * *
        *    
* * *   * * *
*           *
* * * * * * *
24. Interlocking Squares Pattern
Design a pattern with two interlocking squares.
"""


n = 8  # Even number larger than 4
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1 or i == 0 or j == 0 or i == n - 1 or j == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

"""""
Output:

* * * * * * * *
* *         * *
*   *     *   *
*     * *     *
*     * *     *
*   *     *   *
* *         * *
* * * * * * * *
25. Circular Pattern
Create a circular pattern using asterisks (approximation).
"""

n = 10  # Larger for a more rounded appearance
for i in range(n):
    for j in range(n):
        if ((i-n//2)**2 + (j-n//2)**2 < (n//2)**2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

"""""
Output:

          * * * *
      * * * * * * * *
    * * * * * * * * *
  * * * * * * * * * *
* * * * * * * * * * * *
* * * * * * * * * * * *
  * * * * *

 * * * * *
    * * * * * * * * *
      * * * * * * * *
          * * * *
26. Heart Pattern
Form a heart shape using asterisks.
"""


for row in range(6):
    for col in range(7):
        if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

"""""
Output:

  * *     * *
*     * *     *
*             *
  *         *
    *     *
      *
Here are four additional pattern-building exercises using nested loops in Python, each complete with Python code and the corresponding output:

27. Left Diagonal Pattern
Create a left diagonal pattern using asterisks.
"""

n = 5
for i in range(n):
    for j in range(n):
        if i == j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

"""""
Output:

*         
  *       
    *     
      *   
        * 
28. Right Diagonal Pattern
Construct a right diagonal pattern from top right to bottom left.
"""


n = 5
for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

"""""
Output:

        * 
      *   
    *     
  *       
*         
29. Triangle with Numbers
Generate a right-aligned triangle pattern using consecutive numbers instead of asterisks.
"""

n = 5
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()

"""""
Output:

1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
30. Sandglass Pattern
Create a sandglass or hourglass pattern using asterisks.
"""

n = 5
for i in range(n, 0, -1):
    print(' ' * (n - i) + '* ' * i)
for i in range(2, n + 1):
    print(' ' * (n - i) + '* ' * i)

"""""
Output:

* * * * * 
 * * * * 
  * * * 
   * * 
    *
   * * 
  * * * 
 * * * * 
* * * * * 
"""