def max_sliding_window(num_list, size):
    if not num_list:
        return []
    
    result = []
    window = deque()
    
    # Khởi tạo cửa sổ ban đầu
    for i in range(size):
        while window and num_list[i] >= num_list[window[-1]]:
            window.pop()
        window.append(i)
    
    # Xử lý cửa sổ trượt
    for i in range(size, len(num_list)):
        result.append(num_list[window[0]])
        
        # Loại bỏ các phần tử nằm ngoài cửa sổ
        while window and window[0] <= i - size:
            window.popleft()
        
        # Loại bỏ các phần tử nhỏ hơn num_list[i]
        while window and num_list[i] >= num_list[window[-1]]:
            window.pop()
        
        window.append(i)
    
    result.append(num_list[window[0]])  # Thêm số lớn nhất của cửa sổ cuối cùng vào kết quả
    return result

# Ví dụ minh họa
num_list = [1, 3, -1, -3, 5, 3, 6, 7]
size = 3
print(max_sliding_window(num_list, size))
