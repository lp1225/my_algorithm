# 词频统计


def get_word():
    with open('english.txt', 'r') as f:
        all_text = f.readlines()
    all_strings = ''.join(all_text)
    words = all_strings.split(' ')
    # print(words)
    # 构造键值对的形式，统计
    counter = {}
    for word in words:
        if word not in counter.keys():
            counter[word] = 1
        else:
            counter[word] += 1
    counter = sorted(counter, key=counter.get, reverse=True)[0:10]
    return counter


result = get_word()
print(result)