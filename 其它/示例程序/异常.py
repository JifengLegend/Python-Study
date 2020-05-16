if 1:
    try:
        with open('data.txt')as f:
            for each in f:
                print(each)
    except OSError as reason:
        print('出错啦' + str(reason))
