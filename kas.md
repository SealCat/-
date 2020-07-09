# 1.

```python
for i in range(1,10):
	for j in range(1，i+1):
        k = f'{j} * {i} = {j*i}'
        if i == j :
            print(k)
        else:
            print(k, end=' ')
```

# 2.

```python
m = "0,1,2,3,4,5,6,7,8,9, a,b,c,d,e, V,W,X,Y,Z Python作业"
dic = {"num": 0, "alpha": 0, "space": 0, "other": 0}
for i in m:
    l = ord(i)
    if l == 32:
        dic["space"] += 1
    elif 64 < l < 91 or 96 < l < 123:
        dic["alpha"] += 1
    elif 47 < l < 58:
        dic["num"] += 1
    else:
        dic["other"] += 1
print(dic)
```

# 3.

```python
import random
li = []
li.append(chr(random.randint(48,57)))
li.append(chr(random.randint(65,90)))
li.append(chr(random.randint(97,122)))
li.append(random.choice([chr(random.randint(0,9)), chr(random.randint(65,90)), chr(random.randint(97,122))]))
random.shuffle(li)
print(''.join(li))
```

# 4.

```python
def x(n):
    if n == 1:
        return 1
    else:
        return n * x(n-1)
sum = 0
for i in range(1, 11):
    v = x(i)
    sum += v
print(sum)
```

# 5.

```python
li = [4, 6, 2, 3231, 45]
li.sort()
for i in li:
	print(i)
```

