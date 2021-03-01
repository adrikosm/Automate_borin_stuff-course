import traceback


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"Symbol" needs to be a string of 1 in length')
    if (width < 2) or (height < 2):
        raise Exception('"Width" and "height" need to be greater than 2 in length')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)


boxPrint('O', 4, 4)
""""
try:
    raise Exception("This is an error message")
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print("The traceback info was written in an error file")
"""
