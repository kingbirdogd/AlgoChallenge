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

def MaxSumOfRemovedKConnerItemsFromMatrixRow(matrix, k):
    rows = len(matrix)
    if 0 == rows:
        return 0
    columns = len(matrix[0])
    if 0 == columns:
        return 0
    if k > rows * columns:
        raise Exception("Operation large than the total item of matrix")
    operate_max_sum_matrix =[]
    max_select_item_each_row = min(columns, k)
    for i in range(0, rows):
        operate_max_sum_row = []
        for j in range(0,max_select_item_each_row):
            operate_max_sum_row.append(MaxSelectedKCornerItemItemFromArray(matrix[i], j + 1))
        operate_max_sum_matrix.append(operate_max_sum_row);
    dp = [0] * (k + 1)
    for i in range(0, len(operate_max_sum_matrix)):
        for bag_weigth_reverse_idx in range(0,k):
            bag_weigth = k - bag_weigth_reverse_idx
            for weigth_idx in range(0,max_select_item_each_row):
                item_weight = weigth_idx + 1
                item_value = operate_max_sum_matrix[i][weigth_idx]
                if bag_weigth >= item_weight:
                    dp[bag_weigth] = max(dp[bag_weigth], dp[bag_weigth - item_weight] + item_value)

    return dp[k]
