import re

print("Magic Calculator Py")
print("Type 'quit' to exit")

previews = 0
run = True


def perform_math():
    global run
    global previews
    equation = ''

    if previews == 0:
        equation = input('enter equation:')
    else:
        equation = str(input(previews))

    if equation == 'quit':
        print('Bye')
        run = False
    else:
        equation = re.sub('[a-zA-Z,.()" "]', '', equation)

        if previews == 0:
            previews = eval(equation)
        else:
            previews = eval(str(previews) + equation)


while run:
    perform_math()