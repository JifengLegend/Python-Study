def SaveFile(boy, girl, count):
    file_name_boy = 'boy_' + str(count) + '.txt'
    file_name_girl = 'girl_' + str(count) + '.txt'
    boy_file = open(file_name_boy, 'w')
    girl_file = open(file_name_girl, 'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()

def SplitFile(file_name):
    f = open(file_name)

    boy = []
    girl = []
    count = 1
    for each_line in f:
        if each_line[:6] != '======':
            (role, line_spoken) = each_line.split(':', 1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            SaveFile(boy, girl, count)
            boy = []
            girl = []
            count += 1
    SaveFile(boy, girl, count)
    f.close()


SplitFile('record.txt')
pirnt('函数已经正常运行')
