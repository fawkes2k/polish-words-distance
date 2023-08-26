from unidecode import unidecode

def log(message):
    from datetime import datetime
    print('[{}] {}'.format(datetime.now(), message))

def get_keyboard_distances() -> dict[str: float]:
    keyboard_distances = {}
    with open('Data/all_keyboard_distances.txt') as file:
        for line in file.readlines():
            keys, distance = line.split()
            keyboard_distances[keys] = float(distance)
        return keyboard_distances

def get_word_list() -> list[str]:
    with open('Data/slowa.txt') as file:
        log('Parsing file "{}"…'.format(file.name))
        content = unidecode(file.read())
        return content.split('\n')

def count_distances() -> dict[str: float]:
    keyboard_distances = get_keyboard_distances()
    word_list = get_word_list()
    word_distances = {}
    log('Counting word distances…')
    for word in word_list:
        length = len(word)
        word_distance = 0
        for i in range(length - 1):
            pair = word.upper()[i:i+2]
            word_distance += 0 if pair[0] == pair[1] else keyboard_distances[pair]
        word_distances[word] = round(word_distance / length, 5)
    return word_distances

def run():
    word_distances = count_distances()
    log('Sortng word distances…')
    sorted_by_distance = dict(sorted(word_distances.items(), key=lambda x: x[1], reverse=True))
    with open('result_list.txt', 'w') as file:
        log('Writing to the file "{}"…'.format(file.name))
        for word in sorted_by_distance.items(): file.write('{} = {} mm\n'.format(*word))

if __name__ == '__main__': run()
