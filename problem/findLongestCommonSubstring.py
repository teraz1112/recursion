def findLongestCommonSubstring(string1, string2):
    m = len(string1)
    n = len(string2)

    # 共通部分文字列の長さを格納するテーブル
    table = [[0] * (n + 1) for _ in range(m + 1)]

    # 最長共通部分文字列の長さとその終端位置を記録する変数
    max_length = 0
    end_index = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > max_length:
                    max_length = table[i][j]
                    end_index = i

    # 最長共通部分文字列を取得
    longest_common_substring = string1[end_index - max_length: end_index]

    return longest_common_substring
