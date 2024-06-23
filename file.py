def count_words_in_file(filename):
    word_count = {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()  # Tách các từ trong dòng
                for word in words:
                    word = word.lower()  # Chuyển đổi từ thành chữ thường
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    
    return word_count
