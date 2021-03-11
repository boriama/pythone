def my_func(*args):
    i = 0
    total = 0
    big_total = 0
    while args[len(args)] != "*":
        while i < len(args):
            total += args[i]
            i += 1
        big_total += total
        ''' Тут я очень сильно запутался. Можете пожалуйста подсказать
        как было бы правильно посторить данный цикл'''

