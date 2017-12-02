def get_coff(sub_term):
    coff= 0
    for i in range(len(sub_term)):
        if ord(sub_term[i]) >= 48 and ord(sub_term[i]) <= 57:
            coff *= 10
            coff += ord(sub_term[i]) - 48
    if sub_term[0] == '-':
        coff *= - 1
s= "-5585x^5"
d = get_coff(s)
print(d)

