import json


class Process:
    def __init__(self):
        with open('data.json', 'r', encoding='utf-8') as info:
            self.data = json.load(info)
        super(Process, self).__init__()
        self.info_dirty_cleaning = self.data['dirty']

    def cleaning(self):
        line = 10
        column = 3
        for x in range(column):
            for y in range(line):
                print(self.info_dirty_cleaning[x][y])


        for x in range(column):
            for y in range(line):
                if self.info_dirty_cleaning[x][y] == 0:
                    with open('data.json', 'w', encoding='utf-8') as new:
                        self.info_dirty_cleaning[x][y] = self.info_dirty_cleaning[x][y + 1]
                        new.write(json.dumps(self.info_dirty_cleaning[x][y]))


if __name__ == '__main__':
    start = Process()
    start.cleaning()
