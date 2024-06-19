def countdown(num):
    print(num)
    if num <= 1:
        return
    countdown(num - 1)


countdown(10)
