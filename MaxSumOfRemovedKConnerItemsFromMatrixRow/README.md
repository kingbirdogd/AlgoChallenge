# Problem Description 
Remove k first or last items from any row of a M x N matrix, to find out the max sum of all removed items

# Problem Details
Wrtite a function MaxSumOfRemovedKConnerItemsFromMatrixRow with 2 Paramters
Paramter1 : M X N matrix, example: [[4, 2, 1, 7], [5, 3, 8, 9], [6, 1, 0, 2]], 3 Rows 4 Column table M = 3, N = 4

|4|2|1|7|
|:-:|:-:|:-:|:-:|
|5|3|8|9|
|6|1|0|2|

Paramter2 is a non-nagitive number k, where 0 <= k <= M x N
Here is an exmaple k = 3;

What you need to do is, do k times operations.
For each operation, you need to do:

1. select any i, which 0 <= i < M, select a row in matrix which is row = matrix[i]
2. remove the first or the last item from the row you select. After removed, you can't remove this item again this time. The first or the last item for this row should be the adjacent item of the removed item
3. acculate the removed item to the sum

The Function task is to find a best removed operations scenarios to make to sum to the max

# Condition:
Matrix size: M x N < 10000

and

matrix[i][j] >= 0

and

0 <= k <= M x N

# Example
matrix = [[4, 2, 1, 7], [5, 3, 8, 9], [6, 1, 0, 2]]
|4|2|1|7|
|:-:|:-:|:-:|:-:|
|5|3|8|9|
|6|1|0|2|

and

k = 3

the initialize sum = 0

the Best scenarios to do 3 operations is：

# Operation 1: 
Remove the last item of row[1],

After this operation:
matrix = [[4, 2, 1, 7], [5, 3, 8], [6, 1, 0, 2]]
|4|2|1|7|
|:-:|:-:|:-:|:-:|
|5|3|8||
|6|1|0|2|

sum = 9

# Operation 2: 
Remove the last item of row[1],

After this operation:
matrix = [[4, 2, 1, 7], [5, 3], [6, 1, 0, 2]]
|4|2|1|7|
|:-:|:-:|:-:|:-:|
|5|3|||
|6|1|0|2|

sum = 9 + 8 = 17

# Operation 3: 
Remove the last item of row[0],

After this operation:
matrix = [[4, 2, 1], [5, 3], [6, 1, 0, 2]]
|4|2|1||
|:-:|:-:|:-:|:-:|
|5|3|||
|6|1|0|2|

sum = 17 + 7 = 24

So the max sum is 24



