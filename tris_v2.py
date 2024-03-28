import random

game_board = {i: ' ' for i in range(1, 10)}
separator = "-" * 17

win_conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                  [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


def print_board(board):
    print(f''' {board[1]}  |  {board[2]}  |  {board[3]}
---------------\n {board[4]}  |  {board[5]}  |  {board[6]}
---------------\n {board[7]}  |  {board[8]}  |  {board[9]}''')


def is_input_correct(user_input):
    if (not user_input.isnumeric()
            or int(user_input) not in game_board
            or game_board[int(user_input)] != ' '):
        return False
    return True


def has_player_won() -> bool:
    for value in win_conditions:
        if (game_board[value[0]] != ' ' and
                all(game_board[pos] == game_board[value[0]] for pos in value)):
            print(f'{game_board[value[0]]} HA VINTO!')
            return True
    return False


def main():
    print_board(game_board)
    turno = random.choice(['X', 'O'])

    for numero_turni in range(9):
        scelta = input(f'Turno di {turno}. Quale spazio vuoi? ')
        while not is_input_correct(scelta):
            scelta = input('Inserisci un numero da 1 a 9 corrispondente ad una casella libera: ')

        game_board[int(scelta)] = turno  # aggiungere la mossa del giocatore
        print_board(game_board)

        if has_player_won():
            return
        turno = 'O' if turno == 'X' else 'X'  # cambio turno

    print('PAREGGIO!')
    return


main()
