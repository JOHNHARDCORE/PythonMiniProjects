def binarySearch(start, end, needle, list):
  if end < start:
    return -1

  mid = (end + start) // 2
  val = list[mid]

  if val == needle:
    return mid
  
  if val < needle:
    return binarySearch(mid + 1, end, needle, list)
  else:
    return binarySearch(start, mid - 1, needle, list)    

user_list = list(map(lambda x: int(x), \
  input("Enter a comma separated list of ints (ex: 1, 2, 3, 4)\n") \
    .split(','))) \
  	.sort()

needle = int(input("Enter the number you want to search for\n"))

index = binarySearch(0, len(user_list), needle, user_list)

print(f'Found {needle} at index {index}' if index != -1 else f'{needle} not in list')