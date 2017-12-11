class term:
    coff = 0

    sub_term = ""

    power = list()

    symbol = ""

    def __init__(self):

        self.coff = 0

        self.sub_term = " "

        self.symbol = ""

        self.power = []

    def get_coff(self):

        if self.sub_term[0] != '-':
            if ord(self.sub_term[0]) >= 65 and ord(self.sub_term[0]) <= 90 or ord(self.sub_term[0]) >= 97 and ord(
                    self.sub_term[0]) <= 122:
                self.coff = 1
                return self.coff

        if self.sub_term[0] == '-':

            for i in range(1, len(self.sub_term)):
                if ord(self.sub_term[1]) >= 65 and ord(self.sub_term[1]) <= 90 or ord(self.sub_term[1]) >= 97 and ord(
                        self.sub_term[1]) <= 122:
                    self.coff = -1
                    return self.coff
                if ord(self.sub_term[i]) >= 65 and ord(self.sub_term[i]) <= 90 or ord(self.sub_term[i]) >= 97 and ord(
                        self.sub_term[i]) <= 122:
                    break
                else:

                    self.coff *= 10

                    self.coff += ord(self.sub_term[i]) - 48

            self.coff *= -1
            return self.coff


        else:

            for i in range(len(self.sub_term)):

                if ord(self.sub_term[i]) >= 65 and ord(self.sub_term[i]) <= 90 or ord(self.sub_term[i]) >= 97 and ord(
                        self.sub_term[i]) <= 122:

                    break

                else:

                    self.coff *= 10

                    self.coff += ord(self.sub_term[i]) - 48
            return self.coff

    def get_symbol(self):

        for i in range(len(self.sub_term)):

            if ord(self.sub_term[i]) >= 65 and ord(self.sub_term[i]) <= 90 or ord(self.sub_term[i]) >= 97 and ord(
                    self.sub_term[i]) <= 122:
                self.symbol += self.sub_term[i]

        self.symbol += "1"
        self.symbol += "1"

        return self.symbol

    def get_power(self):

        pow_of_var1 = 0

        pow_of_var2 = 0

        flag1 = False

        flag2 = False

        test = False

        count = 0

        for i in range(len(self.sub_term)):

            if ord(self.sub_term[i]) >= 65 and ord(self.sub_term[i]) <= 90 or ord(self.sub_term[i]) >= 97 and ord(
                    self.sub_term[i]) <= 122:
                count += 1

            if self.sub_term[i] == '^':

                if count == 2:
                    test = True

                flag = False

                flag1 = True

                for j in range(i + 1, len(self.sub_term)):

                    if self.sub_term[j] == '^':

                        flag2 = True

                        for k in range(j + 1, len(self.sub_term)):
                            pow_of_var2 *= 10

                            pow_of_var2 += ord(self.sub_term[k]) - 48

                        flag = True

                        break

                    else:

                        if not ord(self.sub_term[j]) >= 65 and ord(self.sub_term[j]) <= 90 or not ord(
                                self.sub_term[j]) >= 97 and ord(self.sub_term[j]) <= 122:
                            pow_of_var1 *= 10

                            pow_of_var1 += ord(self.sub_term[j]) - 48

                if (flag is True):
                    break

        if (flag1 is False) and (flag2 is False):

            if count == 1:

                pow_of_var1 = 1

            elif count == 2:

                pow_of_var2 = 1

                pow_of_var1 = 1

            else:

                pow_of_var2 = 0

                pow_of_var1 = 0

        if (flag1 is True) and (flag2 is False):

            if count == 2:

                pow_of_var2 = 1

            else:

                pow_of_var2 = 0

        if (test is True):
            self.power.append(pow_of_var2)

            self.power.append(pow_of_var1)

            return self.power

        self.power.append(pow_of_var1)

        self.power.append(pow_of_var2)

        return self.power


def caller(z):
    a = term()

    a.sub_term = z

    a.coff = a.get_coff()

    a.symbol = a.get_symbol()

    a.power = a.get_power()

    result = ""

    result = ((a.coff, a.symbol[0], a.power[0], a.symbol[1], a.power[1]))

    return result


def find_term(x):
    y = list()
    y = x
    for i in range(len(x)):

        if x[i] == "-" and x[i][0] != "-":
            y = x.replace('-', '+-')

    return y


def split_term(x):
    x2 = list()

    x2 = [0]

    x2 = x.split("+")

    return x2


def arragment_term(x):
    y = list()

    coff = 0

    pow1 = 0

    pow2 = 0

    var = ''

    var2 = ''

    for i in range(0, len(x)):

        coff = x[i][0]

        pow1 = x[i][2]

        pow2 = x[i][4]

        var = x[i][1]

        var2 = x[i][3]

        if ord(var) > ord(var2):

            temp1 = var

            var = var2

            var2 = temp1

            temp2 = pow1

            pow1 = pow2

            pow2 = temp2

            y.append((coff, var, pow1, var2, pow2))

        else:

            y.append(x[i])

    return y


def make_term(y):
    terms_of_equ = list()

    for i in range(len(y)):
        terms_of_equ.append((caller(y[i])))

    return terms_of_equ


def calc_multi(eq1, eq2):
    list1 = eq1
    list2 = eq2
    size1 = len(list1)
    size2 = len(list2)
    result = list()
    check = False
    for i in range(0, size1):
        for j in range(0, size2):
            if (list1[i][0] == 0 and list2[j][0] == 0):
                a = 0
                b = 0
                c = 0
                d = 0
                e = 0
            else:
                a = list1[i][0] * list2[j][0]
                if (list1[i][1] == list2[j][1]):
                    b = list1[i][1]
                elif (list1[i][1] == '1' and list2[j][1] != '1'):

                    b = list2[j][1]
                elif (list1[i][1] != '1' and list2[j][1] == '1'):
                    b = list1[i][1]

                c = list1[i][2] + list2[j][2]
                if (list1[i][3] == list2[j][3]):
                    d = list1[i][3]
                elif (list1[i][3] == '1' and list2[j][3] != '1'):
                    d = list2[j][3]
                elif (list1[i][3] != '1' and list2[j][3] == '1'):
                    d = list1[i][3]
                elif (list1[i][3] != '1' and list2[j][3] != '1' and list1[i][3] != list2[j][3]):
                    s = list1[i][1]
                    r = list2[j][3]
                    c = list1[i][4]
                    check = True
                    e = list2[j][4]
                    if (s < r):
                        b = s
                        d = r
                if (check != True):
                    e = list1[i][4] + list2[j][4]
            result.append((a, b, c, d, e))

    final_result = list()

    for i in range(0, len(result)):
        sum1 = 0
        temp = 0
        found = False
        for j in range(0, len(result)):

            if (i != j):
                if result[i][2] == result[j][2] and result[i][4] == result[j][4]:
                    sum1 += int(result[i][0]) + int(result[j][0])
                    found = True
                    result[j] = ('2', '2', '2', '2', '2')
                    temp = temp + 1
        if (found == True):
            for k in range(0, temp - 1):
                sum1 = sum1 - int(result[i][0])
            if (sum1 != '2' and result[i][1] != '2' and result[i][2] != '2' and result[i][3] != '2' and result[i][
                4] != '2'):
                if (sum1 != 0):
                    final_result.append((sum1, result[i][1], result[i][2], result[i][3], result[i][4]))
        else:
            if (result[i][0] != '2' and result[i][1] != '2' and result[i][2] != '2' and result[i][3] != '2' and
                        result[i][4] != '2'):
                if (result[i][0] != 0):
                    final_result.append((result[i][0], result[i][1], result[i][2], result[i][3], result[i][4]))

    return final_result


equ2 = "-20x^2+400+7x^10y^10"

equ2 = find_term(equ2)

equ2_after_split = split_term(equ2)

terms_equ2 = make_term(equ2_after_split)

equ2_after_arragment = arragment_term(terms_equ2)
print("first = ", equ2_after_arragment)
equ = "-y^2+0-10"

equ1 = find_term(equ)

equ_after_split = split_term(equ1)

terms_equ = make_term(equ_after_split)

equ_after_arragment = arragment_term(terms_equ)
print("second = ", equ_after_arragment)
x = calc_multi(equ_after_arragment, equ2_after_arragment)
print(x)