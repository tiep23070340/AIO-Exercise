# hàm đếm số chữ trong một từ
def count_letters(n):
  result={}
  for letter in n:
    if letter in result:
      result[letter]+=1
    else:
      result[letter]=1
  return result
# test case
n="happiness"
print(count_letters(n))