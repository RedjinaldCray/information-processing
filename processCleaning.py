import json
import random


class Process():
    def __init__(self):
        with open('data.json', 'r', encoding='utf-8') as info:
            self.data = json.load(info)
        super(Process, self).__init__()
        self.info_dirty_cleaning = self.data['dirty']
        self.info_duplicate = self.data['duplicate']
        self.abnormal_class = self.data['abnormal']['quantity_members_of_class']
        self.abnormal_group = self.data['abnormal']['quantity_members_of_students_group']

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
        print("\n\nUse table with duplicate values:\n\n")
        line = 15
        column = 5
        self.out_print_array(self.info_duplicate, line)
        for x in range(line):
            for y in range(column):
                for cnt in range(column):
                    if self.info_duplicate[x][y] == self.info_duplicate[x][cnt] and y != cnt:
                        for i in range(line - 1):
                            for j in range(column - 1):
                                self.info_duplicate[x][y] += self.info_duplicate[i][j]
                        self.info_duplicate[x][y] = int(self.info_duplicate[x][y] / (line * column))
        self.out_print_array(self.info_duplicate, line)

    def change_of_data_of_abnormal_class(self):
        print("\n\nUse table with abnormal values of quantity members of class:\n\n")
        column = 15
        print(self.abnormal_class, "\n\n")
        for y in range(column):
            if self.abnormal_class[y] < 5 or self.abnormal_class[y] > 40:
                if self.abnormal_class[y] < 5:
                    self.abnormal_class[y] = random.randint(6, 10)
                else:
                    self.abnormal_class[y] = random.randint(35, 39)
        print(self.abnormal_class, "\n\n")

    # def change_of_data_of_abnormal_group(self):
    #     print("\n\nUse table with abnormal values of quantity members of group:\n\n")
    #     line = 2
    #     column = 10
    #     d = 3
    #     p = 2
    #     self.out_print_array(self.abnormal_group, line)
    #     for x in range(line):
    #         for y in range(column):
    #             if self.abnormal_group[x][y] < 1 or self.abnormal_group[x][y] > 30:
    #                 if self.abnormal_group[x][y] < 1:
    #                     self.abnormal_group[x][y] = random.randint(2, 5)
    #                 else:
    #                     self.abnormal_group[x][y] = random.randint(25, 29)
    #     self.out_print_array(self.abnormal_group, line)

    def abnormal_data_group(self):
        line = 2
        column = 10
        d = 3
        p = 2
        count_r = 1
        self.out_print_array(self.abnormal_group, line)
        for x in range(line):
            for y in range(column-1):
                for count in range(y, column):
                    if self.abnormal_group[x][y] + p == self.abnormal_group[x][count]:
                        if count - d == y:
                            print('nice data')
                        else:
                            self.abnormal_group[x][count] = self.abnormal_group[x][y] + p
                    else:
                        self.abnormal_group[x][count] = self.abnormal_group[x][y] + p
        self.out_print_array(self.abnormal_group, line)


if __name__ == '__main__':
    start = Process()
    start.cleaning()
    start.duplicate_changes()
    start.change_of_data_of_abnormal_class()
    start.abnormal_data_group()
