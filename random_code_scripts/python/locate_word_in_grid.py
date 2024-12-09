grid_matrix = [
    ["N", "K", "R", "E", "C", "S", "N", "I", "R", "U", "T", "J", "E", "A", "L", "U", "S", "R", "U"],
    ["A", "A", "E", "F", "R", "E", "C", "A", "C", "N", "I", "U", "E", "W", "V", "N", "H", "O", "J"],
    ["M", "R", "O", "M", "A", "K", "B", "R", "I", "T", "M", "O", "R", "N", "H", "F", "B", "Y", "V"],
    ["H", "E", "A", "D", "A", "L", "O", "V", "E", "L", "A", "C", "E", "I", "M", "R", "R", "S", "P"],
    ["C", "N", "N", "I", "W", "I", "R", "T", "H", "O", "O", "O", "P", "K", "R", "A", "I", "E", "H"],
    ["L", "S", "I", "J", "P", "W", "E", "N", "D", "Y", "H", "A", "L", "L", "E", "N", "N", "R", "I"],
    ["E", "P", "T", "K", "K", "K", "N", "V", "O", "K", "S", "I", "L", "A", "Y", "I", "F", "G", "L"],
    ["W", "A", "A", "S", "C", "H", "M", "A", "U", "R", "I", "S", "E", "U", "A", "V", "Z", "E", "I"],
    ["N", "R", "G", "T", "A", "W", "E", "E", "L", "T", "R", "U", "M", "S", "M", "R", "S", "Y", "P"],
    ["O", "C", "G", "R", "O", "B", "G", "E", "F", "A", "J", "E", "A", "N", "N", "E", "T", "T", "E"],
    ["D", "K", "Y", "A", "A", "N", "W", "X", "G", "A", "R", "D", "R", "L", "A", "D", "I", "M", "M"],
    ["R", "J", "H", "G", "I", "C", "O", "D", "D", "A", "Z", "S", "T", "O", "S", "L", "M", "U", "E"],
    ["O", "O", "T", "W", "O", "O", "E", "S", "O", "H", "J", "G", "I", "O", "S", "A", "Z", "H", "A"],
    ["G", "N", "O", "N", "T", "P", "I", "H", "E", "D", "S", "E", "N", "P", "I", "C", "I", "A", "G"],
    ["R", "E", "R", "E", "H", "R", "Y", "E", "O", "B", "A", "R", "B", "A", "R", "A", "R", "M", "W"],
    ["A", "S", "O", "U", "H", "N", "C", "I", "J", "P", "D", "C", "G", "K", "A", "L", "A", "M", "A"],
    ["C", "B", "D", "C", "O", "I", "U", "H", "E", "L", "P", "M", "N", "Y", "M", "M", "W", "A", "L"],
    ["E", "O", "S", "T", "R", "A", "C", "H", "E", "Y", "D", "E", "I", "C", "R", "N", "H", "D", "I"],
    ["L", "R", "P", "U", "D", "E", "N", "N", "I", "N", "G", "E", "R", "O", "O", "E", "K", "B", "P"],
    ["E", "N", "A", "W", "S", "R", "E", "N", "R", "E", "B", "M", "U", "F", "F", "Y", "L", "R", "Q"],
    ["E", "M", "V", "O", "N", "N", "E", "U", "M", "A", "N", "N", "T", "D", "A", "N", "A", "U", "A"],
]
 
 
def main():
    searched_words = []
    backup_words = []
    print("Enter all the words you want all at once or one at a time and then enter nothing to get the answer...")
    while ((word := input("Search for: ")) != ""):
        word_list = word.split()
        for w in word_list:
            searched_words.append(w.upper())
            backup_words.append(w.upper())
    else:
        searched_words = list(set(searched_words))
        backup_words = list(set(backup_words))
        # For later finding
        i = 0
        l = len(backup_words)
        while i < l:
            backup_words[i] = [backup_words[i], False]
            i += 1
        locate_and_print_words(searched_words)
        print("Thank you for playing!")


def locate_and_print_words(searched_words):
    print()
    for row_index in range(len(grid_matrix)):
        for col_index in range(len(grid_matrix[row_index])):
            for word in searched_words:
                if word[0] == grid_matrix[row_index][col_index]:
                    if (word_coord := check_grid(row_index, col_index, word)) != None:
                        #backup_words[backup_words.index(word)][1] = True
                        print_grid_with_word(word_coord)
                        searched_words.remove(word)
                        print(end="\n\n")


def check_grid(row_index, col_index, word):
    word_row_index = row_index
    word_col_index = col_index
    word_index = 0

    # check on line left
    while word_col_index >= 0:
        if grid_matrix[word_row_index][word_col_index] == word[word_index]:
            word_col_index -= 1
            word_index += 1
        else:
            break
        if word_index == len(word):
            return [row_index, col_index, "left", word_index]
    
    # check on line right
    word_row_index = row_index
    word_col_index = col_index
    word_index = 0
    while word_col_index < len(grid_matrix[row_index]):
        if grid_matrix[word_row_index][word_col_index] == word[word_index]:
            word_col_index += 1
            word_index += 1
        else:
            break
        if word_index == len(word):
            return [row_index, col_index, "right", word_index]

    # check on colomn up
    word_row_index = row_index
    word_col_index = col_index
    word_index = 0
    while word_row_index >= 0:
        if grid_matrix[word_row_index][word_col_index] == word[word_index]:
            word_row_index -= 1
            word_index += 1
        else:
            break
        if word_index == len(word):
            return [row_index, col_index, "up", word_index]

    # check on column down
    word_row_index = row_index
    word_col_index = col_index
    word_index = 0
    while word_row_index < len(grid_matrix):
        if grid_matrix[word_row_index][word_col_index] == word[word_index]:
            word_row_index += 1
            word_index += 1
        else:
            break
        if word_index == len(word):
            return [row_index, col_index, "down", word_index]
    
    # check diagonally up right
    word_row_index = row_index
    word_col_index = col_index
    word_index = 0
    while word_row_index >= 0 and word_col_index < len(grid_matrix[word_row_index]):
        if grid_matrix[word_row_index][word_col_index] == word[word_index]:
            word_row_index -= 1
            word_col_index += 1
            word_index += 1
        else:
            break
        if word_index == len(word):
            return [row_index, col_index, "diag_up_r", word_index]
    
    # check diagonally up left
    word_row_index = row_index
    word_col_index = col_index
    word_index = 0
    while word_row_index >= 0 and word_col_index >= 0:
        if grid_matrix[word_row_index][word_col_index] == word[word_index]:
            word_row_index -= 1
            word_col_index -= 1
            word_index += 1
        else:
            break
        if word_index == len(word):
            return [row_index, col_index, "diag_up_l", word_index]

    # check diagonally down right
    word_row_index = row_index
    word_col_index = col_index
    word_index = 0
    while word_row_index < len(grid_matrix) and word_col_index < len(grid_matrix[word_row_index]):
        if grid_matrix[word_row_index][word_col_index] == word[word_index]:
            word_row_index += 1
            word_col_index += 1
            word_index += 1
        else:
            break
        if word_index == len(word):
            return [row_index, col_index, "diag_down_r", word_index]

    # check diagonally down left
    word_row_index = row_index
    word_col_index = col_index
    word_index = 0
    while word_row_index < len(grid_matrix) and word_col_index >= 0:
        if grid_matrix[word_row_index][word_col_index] == word[word_index]:
            word_row_index += 1
            word_col_index -= 1
            word_index += 1
        else:
            break
        if word_index == len(word):
            return [row_index, col_index, "diag_down_l", word_index]


def print_grid_with_word (word_coord):
    (x, y, dir, w_length) = word_coord
    coordinates = []
    match dir:
        case "right":
            for i in range(w_length):
                coordinates.append((x, y + i))
        case "left":
            for i in range(w_length):
                coordinates.append((x, y - i))
        case "up":
            for i in range(w_length):
                coordinates.append((x - i, y))
        case "down":
            for i in range(w_length):
                coordinates.append((x + i, y))
        case "diag_up_r":
            for i in range(w_length):
                coordinates.append((x - i, y + i))
        case "diag_up_l":
            for i in range(w_length):
                coordinates.append((x - i, y - i))
        case "diag_down_r":
            for i in range(w_length):
                coordinates.append((x + i, y + i))
        case "diag_down_l":
            for i in range(w_length):
                coordinates.append((x + i, y - i))
        case _:
            ...
    for i in range(len(grid_matrix)):
        for j in range(len(grid_matrix[i])):
            if (i, j) in coordinates:
                print("\033[93m {}\033[00m".format(grid_matrix[i][j]), end="")
            else:
                print("\033[96m {}\033[00m" .format(grid_matrix[i][j]), end="")
        print()


if __name__ == "__main__":
    main()


