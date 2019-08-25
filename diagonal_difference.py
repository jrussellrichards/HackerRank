def diagonalDifference(arr):
    
    sum_right_diagonal=0
    sum_left_diagonal=0
    last_column=len(arr)-1

    for position,value in enumerate(arr):
        sum_right_diagonal+=arr[position][position]
        sum_left_diagonal+=arr[position][last_column]
        last_column-=1
    
    abs_difference=abs(sum_left_diagonal-sum_right_diagonal)
    
    return abs_difference


print(diagonalDifference(
    [[4,5,6],
    [1,2,3],
    [1,2,6]]
    )
    )