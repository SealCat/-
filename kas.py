
def c():
    import random
    li = []
    li.append(chr(random.randint(48,57)))
    li.append(chr(random.randint(65,90)))
    li.append(chr(random.randint(97,122)))
    li.append(random.choice([
        chr(random.randint(48,57)),
        chr(random.randint(65,90)),
        chr(random.randint(97,122))
        ]))
    random.shuffle(li)
    print(''.join(li))

c()
