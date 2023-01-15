# Здача №23 Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1, 10))


def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token +"? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer -1]) not in "XO"):
                board[player_answer -1] = player_token
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)

main(board)






# theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
#             '4': ' ' , '5': ' ' , '6': ' ' ,
#             '1': ' ' , '2': ' ' , '3': ' ' }

# board_keys = []

# for key in theBoard:
#     board_keys.append(key)

# def printBoard(board):
#     print(board['7'] + '|' + board['8'] + '|' + board['9'])
#     print('-+-+-')
#     print(board['4'] + '|' + board['5'] + '|' + board['6'])
#     print('-+-+-')
#     print(board['1'] + '|' + board['2'] + '|' + board['3'])

# def game():

#     turn = 'X'
#     count = 0


#     for i in range(10):
#         printBoard(theBoard)
#         print("Выш ход," + turn + ".Куда поставить знак?")

#         move = input()        

#         if theBoard[move] == ' ':
#             theBoard[move] = turn
#             count += 1
#         else:
#             print("Эта позиция уже занята.\nКуда поставить знак?")
#             continue

        
#         if count >= 5:
#             if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
#                 printBoard(theBoard)
#                 print("\nКонец игры.\n")                
#                 print(" **** " +turn + " победа. ****")                
#                 break
#             elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
#                 printBoard(theBoard)
#                 print("\nКонец игры.\n")                
#                 print(" **** " +turn + " победа. ****")
#                 break
#             elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
#                 printBoard(theBoard)
#                 print("\nКонец игры.\n")                
#                 print(" **** " +turn + " победа. ****")
#                 break
#             elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
#                 printBoard(theBoard)
#                 print("\nКонец игры.\n")                
#                 print(" **** " +turn + " победа. ****")
#                 break
#             elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
#                 printBoard(theBoard)
#                 print("\nКонец игры.\n")                
#                 print(" **** " +turn + " победа. ****")
#                 break
#             elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
#                 printBoard(theBoard)
#                 print("\nКонец игры.\n")                
#                 print(" **** " +turn + " победа. ****")
#                 break 
#             elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
#                 printBoard(theBoard)
#                 print("\nКонец игры.\n")                
#                 print(" **** " +turn + " победа. ****")
#                 break
#             elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
#                 printBoard(theBoard)
#                 print("\nКонец игры.\n")                
#                 print(" **** " +turn + " победа. ****")
#                 break 

        
#         if count == 9:
#             print("\nКонец игры.\n")                
#             print("Ничья!!")

        
#         if turn =='X':
#             turn = 'O'
#         else:
#             turn = 'X'        
    
    
#     restart = input("Хотите сыграть ещё раз?(y/n)")
#     if restart == "y" or restart == "Y":  
#         for key in board_keys:
#             theBoard[key] = " "

#         game()

# if __name__ == "__main__":
#     game()