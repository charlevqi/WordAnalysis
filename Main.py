"""
输入一个文本文件，统计文档里各个单词出现的次数
"""

word_countor = []
word_list = []
word_tuple = ("", 0)
tuple_list = []

file = open("prince.txt", mode="r", encoding="utf-8")
lines = file.readlines()
file.close()


def find(str='', list=[]):
    for item_index in range(len(list)):
        if list[item_index] == str:
            return item_index
    return -1


def analysis_line(line=''):
    if line == '\n' or line == '':  # 如果这一行是空的，那就不管了
        return []
    line = line.lower()
    for index in range(len(line)):  # 读一个字符
        if line[index].isalpha():  # 如果这个字符是英文字母
            continue
        else:
            tem_list = list(line)
            tem_list[index] = " "
            line = ''.join(tem_list)
    tem_set = []
    for word in line.split(' '):
        if word != '':
            tem_set.append(word)
    return tem_set


if __name__ == '__main__':
    for line in lines:
        temp_lit = analysis_line(line)
        if temp_lit != []:
            for word in temp_lit:
                b = find(word, word_list)
                if b==-1:
                    word_list.append(word)
                    word_countor.append(1)
                else:
                    word_countor[b] = word_countor[b]+1
    for index in range(len(word_countor)):
        word_tuple=(word_list[index], word_countor[index])
        tuple_list.append(word_tuple)
    tuple_list=sorted(tuple_list, key=lambda a:a[1], reverse=True)
    # 把结果输出到显示屏上
    print(tuple_list)
    # 把结果输出到文件中
    file=open("output", mode="w+", encoding="utf-8")
    for item in tuple_list:
        file.write(str(item)+"\n")
    file.close()
