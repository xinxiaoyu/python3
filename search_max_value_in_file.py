m = []

with open('/tmp/123', 'r') as f:
	for i in f:
		i = i.strip('\n')
		m += i.split(',')

n = list(map(int, m))

print(max(n))
print(min(n))
