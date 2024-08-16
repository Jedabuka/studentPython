import re


class WordsFinder:
    file_names = []

    def __init__(self, *files):
        for file in files:
            self.file_names.append(file)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                line_list = []
                for line in file:
                    line = line.lower()
                    line = re.sub(r'[,\.\=\!\?\;\:\ - ]', ' ', line)
                    line = line.split()
                    line_list.append(line)
                    all_words.update({file_name: sum(line_list, [])})

        return all_words

    def find(self, word):
        find_word = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            if word in words:
                find_word.update({file_name: words.index(word) + 1})

        return find_word

    def count(self, word):
        count_word = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            count_word[file_name] = words.count(word)

        return count_word


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))