if Check == True:
    a = HatMenElFIle(num1, num2, Generate)
    a = display(a)
    label_result.config(text="Result is " + a)

elif Check == False:
    # prevernting The Re-Writing
    fileworking(num1, num2, Generate, res)
    a = res
    a = display(a)
    label_result.config(text="Result is " + a)
