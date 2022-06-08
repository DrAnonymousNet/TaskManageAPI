
def main(n, arr):
	arr = arr.split(" ")
	if len(arr) > n:
		arr = arr[:n]
	
		
	smallest = float('inf')
	for i in arr:
		for j in arr:
			if j == i:
				continue
			result = abs(int(i)-int(j))
			if result < smallest:
				smallest = result
	return smallest
	
n = int(input())
arr = input()

print(main(n, arr))
	
