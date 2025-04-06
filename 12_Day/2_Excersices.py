import random
def generate_colors(type, n):
    if type == 'hexa':
        s = "0123456789abcdef"
        lst = []
        for i in range(n):
            res = '#'
            for j in range(6):
                res += random.choice(s)
            lst.append(res)
        print(lst)
    elif type == 'rgb':
        lst = []
        for i in range(n):
            r = random.randint(0, 256)
            b = random.randint(0, 256)
            g = random.randint(0, 256)
            lst.append(f"rgb({r},{b},{g})")
        print(lst)
    else:
        print("Enter type correctly")