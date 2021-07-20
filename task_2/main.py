# coding: utf-8

def count_letter(words, leter):
    count = 0
    for word in words:
        if leter in word:
            count += 1
    return count

if __name__ == '__main__':
    words = ['python', 'c++', 'c', 'scala', 'java']
    print(count_letter(words, 'c'))
