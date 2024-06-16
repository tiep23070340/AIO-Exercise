def levenshtein_distance(s, t):
    # Độ dài của hai chuỗi
    m = len(s)
    n = len(t)
    
    # Tạo một bảng 2 chiều để lưu trữ khoảng cách Levenshtein
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Khởi tạo giá trị ban đầu
    for i in range(m + 1):
        dp[i][0] = i  # Khoảng cách Levenshtein từ s[:i] đến t[:0] là i (xóa i ký tự)
    for j in range(n + 1):
        dp[0][j] = j  # Khoảng cách Levenshtein từ s[:0] đến t[:j] là j (thêm j ký tự)
    
    # Tính toán khoảng cách Levenshtein cho từng cặp con của chuỗi s và t
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s[i - 1] == t[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,         # Xóa
                           dp[i][j - 1] + 1,         # Thêm
                           dp[i - 1][j - 1] + cost)  # Thay thế hoặc không thay thế
            
    # Khoảng cách Levenshtein giữa s và t là dp[m][n]
    return dp[m][n]

# Ví dụ:
source = "yu"
target = "you"
print(f"Khoảng cách Levenshtein giữa '{source}' và '{target}' là:", levenshtein_distance(source, target))
