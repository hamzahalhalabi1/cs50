
def calculator(expression):
    x, y, z = expression.split(" ")
    x = float(x)
    z = float(z)
    match y:
        case '+':
            return x+z
        case '-':
            return x-z
        case '*':
            return x*z
        case '/':
            return x/z

expression= input('Expression: ')
print(calculator(expression))
