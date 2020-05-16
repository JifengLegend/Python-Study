'''有红、黄、蓝三种颜色的求，
其中红球 3 个，黄球 3 个，绿球 6 个。
先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，
编程计算摸出球的各种颜色搭配。
'''
print('red\tyellow\tgreen')
for red in range(0, 4):  # 红球可能是0-3个
    for yellow in range(0, 4):  # 黄球可能是0-3个
        for green in range(2, 7):  # 绿球可能是2-6个
            if red + yellow + green == 8:
                # 注意，下边不是字符串拼接，因此不用“+”哦~
                print(red, '\t', yellow, '\t', green)
