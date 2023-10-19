
w = ['python', 'c++', 'c', 'scala', 'java']
l = 'c'

def count_letter(words,let):
  count = 0
  for word in words:
    for letter in word:
      if letter == let:
        count += 1
        break
  return count

print(count_letter(w,l))
