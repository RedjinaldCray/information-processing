import json
import numpy


class Process():
    def __init__(self):
        with open('data.json', 'r', encoding='utf-8') as info:
            self.data = json.load(info)
        super(Process, self).__init__()
        self.info_dirty_cleaning = self.data['dirty']
        self.info_duplicate = self.data['duplicate']

    def out_print_array(self, array, line):
        print(" \r")
        for i in range(line):
            print("  ", array[i])
        print("\n")

    def cleaning(self):
        print("Use table with dirty clean:\n")
        line = 3
        column = 10
        self.out_print_array(self.info_dirty_cleaning, line)
        for x in range(line):
            for y in range(column):
                if self.info_dirty_cleaning[x][y] == 0 or self.info_dirty_cleaning[x][y] == "":
                    for i in range(line):
                        for j in range(column):
                            self.info_dirty_cleaning[x][y] += self.info_dirty_cleaning[i][j]
                    self.info_dirty_cleaning[x][y] = int(self.info_dirty_cleaning[x][y] / (line * column))
        self.out_print_array(self.info_dirty_cleaning, line)

    def duplicate_changes(self):
        print("\n\nUse table with duplicate values:\n", self.info_duplicate, "\n")
        line = 15
        column = 5
        line_start = 1
        self.out_print_array(self.info_duplicate, line)
        for x in range(line):
            for y in range(column):
                for cnt in range(column):
                    if self.info_duplicate[x][y] == self.info_duplicate[x][cnt] and y != cnt:
                        for i in range(line-1):
                            for j in range(column-1):
                                self.info_duplicate[x][y] += self.info_duplicate[i][j]
                        self.info_duplicate[x][y] = int(self.info_duplicate[x][y] / (line * column))
        self.out_print_array(self.info_duplicate, line)


if __name__ == '__main__':
    start = Process()
    start.cleaning()
    start.duplicate_changes()
