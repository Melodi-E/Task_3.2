import json
import chardet


def read_file(name):
    with open(name, 'rb') as text_file:
        data = text_file.read()
        result = chardet.detect(data)
        data = data.decode(result['encoding'])
        data = json.loads(data)
        text = ''
        for items in data['rss']['channel']['items']:
            text += ' ' + items['description']
    return text


def get_words_list(name):
    long_words_list = []
    words_list = read_file(name).split()
    for word in words_list:
        if len(word) > 6:
            long_words_list.append(word)
    return long_words_list


def get_all_words(files_list):
    all_words_list = []
    for file in files_list:
        all_words_list += get_words_list(file)
    return all_words_list


def get_top():
    files_list = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']
    all_words_dict = {}
    all_words_list = get_all_words(files_list)
    for word in all_words_list:
        if word in all_words_dict:
            all_words_dict[word] += 1
        else:
            all_words_dict[word] = 1
    top_words_count = 0
    print('10 самых часто встречающихся в новостях слов:')
    for top_word in sorted(all_words_dict.items(), key=lambda x: x[1], reverse=True):
        print(top_word[0], ':', 'встречается', top_word[1], 'раз')
        top_words_count += 1
        if top_words_count > 9:
            break


get_top()
