# First Key:
For each Row in Matrix, while we do N removed operation(from its beginning or end), we can easy find the max sum(removed items).

For Row [4, 2, 1, 7] as example:
|4|2|1|7|
|:-:|:-:|:-:|:-:|

While N == 1, means remove 1 items from this row, the best answer is 7

While N == 2, we must remove 2 items from its beginning or end. So find the max sum(removes of 2) is same as find the min sum of subarray([4, 2, 1, 7], arr.lengh - N)
arr.lengh - N = 2. That means we must found the min sum of subarray(4, 2, 1, 7], arr.lengh - N), and the answer is 
sum(array) - sum of subarray(4, 2, 1, 7], arr.lengh - N)

whe have sub array lenth 2 is:
|4|2|
|:-:|:-:|

|2|1|
|:-:|:-:|

|1|7|
|:-:|:-:|

So subarray([2,1]) has the less sum. So the answer for  max sum(removes of 2) from [4, 2, 1, 7] 
is:
sum = 14
sum of ([2,1]) is 3
so the answer is 11.

Here is the python algo, give you a row, give you an operations count, calcualte the max removed sum:
```
def MaxSelectedKCornerItemItemFromArray(v, remove_item):
    windows_size = len(v) - remove_item
    current_windows_size = 0
    sum_all = 0
    windows_sum = 0
    min_windows_sum = 0
    for i in range(0, len(v)):
        sum_all += v[i]
        windows_sum += v[i]
        current_windows_size += 1
        if current_windows_size == windows_size:
            min_windows_sum = windows_sum
        elif current_windows_size > windows_size:
            windows_sum -= v[i - windows_size]
            if windows_sum < min_windows_sum:
                min_windows_sum = windows_sum
    return sum_all - min_windows_sum
```

And we know, for each row the max removed items should be max(total_operations, columns_size) we call this max_operations

Because if the single row operations can't more than the total_operations.

So for each rows, can get an new array, operate_max_sum_row. operate_max_sum_row[i] means the max removed sum of i + 1 items.

So for the whole matrix, we can calcualte a new matrix operate_max_sum_matrix, 
The operate_max_sum_matrix[i][j] mean : the max removed item sum of row[i], do j + 1 operations

So for the matrix 

|4|2|1|7|
|:-:|:-:|:-:|:-:|
|5|3|8|9|
|6|1|0|2|

and total operations 3,

We will have the new operate_max_sum_matrix: [[7, 11, 13], [9, 17, 22], [6, 8, 9]]

|7|11|13|
|:-:|:-:|:-:|
|9|17|22|
|6|8|9|

While we have the matrix operate_max_sum_matrix, we can go to step 2

# Second Key, solve a grouping 0-1 Knapsack problem

We know that for the operate_max_sum_matrix[i][j]
i + 1 means the operation
operate_max_sum_matrix[i][j] means the value,

if we consider the total operations is a bag weights,
So the operate_max_sum_matrix[i][j] is a items. 
The items weight is: i + 1
The items prices is: operate_max_sum_matrix[i][j]

And we knows that the items divde to rows group, in each group/rows, we can just select one items.

So this became a  grouping 0-1 Knapsack problem

Let's rewrite the operate_max_sum_matrix like that:
|weight:1, price：7|weight:2, price: 11|weight:3, price: 13|
|:-:|:-:|:-:|
|weight:1, price:9|weight:2, price: 17|weight:3, price: 22|
|weight:1, price:6|weight:2, price:8|weight:3, price: 9|

Bag Weight S: 3

so let solve this Knapsack problem in python
```
    dp = [0] * (k + 1) #k = 3
    for i in range(0, len(operate_max_sum_matrix)):
        for bag_weigth_reverse_idx in range(0,k):
            bag_weigth = k - bag_weigth_reverse_idx
            for weigth_idx in range(0,max_select_item_each_row):
                item_weight = weigth_idx + 1
                item_value = operate_max_sum_matrix[i][weigth_idx]
                if bag_weigth >= item_weight:
                    dp[bag_weigth] = max(dp[bag_weigth], dp[bag_weigth - item_weight] + item_value)
```





