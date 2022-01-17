import random

Words_list = [
    {"word": "Yemen", "question": "Arabic Country?"},
    {"word": "easy", "question": "simple think?"},
    {"word": "Frog", "question": " Animal live in the sea?"},
    {"word": "Ring", "question": "something worn by hand?"},
    {"word": "Year", "question": "12 months ?"},
    {"word": "Frog", "question": "12 months ?"},
]
Words_Chose = []
PuzzleList = [["-" for a in range(0, 6)] for b in range(0, 6)]


def printPuzzle():
    for i in range(0, 6):
        print(*PuzzleList[i])


# def printSoulation():
#     for i in range(0, 6):
#         # Words_list[index_dic]["word"].lower()
#         print(Words_Chose[i]["word"])
#         # question = Words_Chose[i]["question"]
#         # print("word : " + word + " question:" + question)
#         # print(i["word"])
#         # solation = i["word"]
#         # PuzzleList.index(solation[0])
#         # for i in range(0,6):
#         #     PuzzleList.index(solation)
#         #     print("YAH")
#     # Words_Chose[]
#     pass


index_dic = 0
word_dic = ""


def word_From_dic():
    global word_dic, index_dic
    if index_dic < len(Words_list):
        word_dic = Words_list[index_dic]["word"].lower()
        if len(word_dic) < 6:
            word_dic = word_dic + "#"
        index_dic += 1
    else:
        index_dic = 0
        word_dic = "#"


chick_pop = False
black = 0


def pop_dic():
    global index_dic
    global chick_pop

    if chick_pop:
        Words_Chose.append(str(Words_list[index_dic - 1]).lower())
        Words_list.pop(index_dic - 1)
        index_dic = 0
        chick_pop = False


def insert_list(row, clo):
    global chick_pop
    global black
    global word_dic
    if PuzzleList[row][0] == "-":
        word_From_dic()
        PuzzleList[row][clo - 1] = word_dic[clo - 1]
    # elif PuzzleList[row][0] == "#":
    #     word_From_dic()
    #     PuzzleList[row][clo] = word_dic[clo - 1]
    while PuzzleList[row][0] != word_dic[0]:
        if word_dic[0] == "#":
            break
        # elif PuzzleList[row][clo-1] == "-":
        #     word_From_dic()
        #     PuzzleList[row][clo] = word_dic[clo]
        #     break
        word_From_dic()
        chick_pop = True
    try:
        PuzzleList[row][clo] = word_dic[clo]
    except:
        word_From_dic()
        chick_pop = False
    pop_dic()


def InputPuzzle():
    global word_dic
    global index_dic
    global chick_pop
    for row in range(0, 2):
        word_From_dic()
        for clo in range(0, len(word_dic)):
            if row == 0:
                PuzzleList[row][clo] = word_dic[clo]
                chick_pop = True
            elif row == 1:
                # insert_list(row, clo)
                while PuzzleList[row - 1][0] != word_dic[0] or word_dic == "#":
                    word_From_dic()
                PuzzleList[clo][0] = word_dic[clo]
                chick_pop = True
        pop_dic()

    for row in range(1, 6):
        for clo in range(1, len(word_dic) + 1):
            insert_list(row, clo)
        pop_dic()

    # for row in range(2, 3):
    #     for clo in range(1, len(word_dic)):
    #         if row == 2:
    #             while PuzzleList[row][0] != word_dic[0]:
    #                 word_From_dic()
    #                 # print(PuzzleList[row][0] +" <>" + word_dic)
    #             PuzzleList[row][clo] = word_dic[clo]
    #     pop_dic()
    #     # print(Words_list[0])


InputPuzzle()
printPuzzle()
# print(Words_Chose)

# InputPuzzle()
# printPuzzle()
