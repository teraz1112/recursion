# 最大値の探索
def maxInArray(arr):
    # 最初の要素に最大値を設定します。
    maxValue = arr[0]
    # arrの中で最大値を探索します。
    for value in arr[1:]:
        if value > maxValue: maxValue = value
    return maxValue
