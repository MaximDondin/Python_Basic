import os
class Cell:
    def __init__(self, number):
        self.number = number
        self.symbol = ' '
        self.is_occupied = False

    def occupy(self, symbol_player):
        if not self.is_occupied:
            self.symbol = symbol_player
            self.is_occupied = True
            return True
        else:
            return False

class Board:
    def __init__(self):
        self.cell = [Cell(i) for i in range(1, 10)]

    def display(self):
        print('—' * 13)
        for i in range(3):
            print('|', self.cell[0 + i * 3].symbol,
                  '|', self.cell[1 + i * 3].symbol,
                  '|', self.cell[2 + i * 3].symbol, '|')
            print('—' * 13)

    def change_cell_state(self, cell_number, symbol):
        if 1 <= cell_number <= 9:
            return self.cell[cell_number - 1].occupy(symbol)
        else:
            return False

    def check_game_over(self):
        win_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                            [1, 5, 9], [3, 5, 7], [1, 4, 7],
                            [2, 5, 8], [3, 6, 9]]
        for comb in win_combinations:
            if (self.cell[comb[0] - 1].symbol == self.cell[comb[1] - 1].symbol == self.cell[comb[2] - 1].symbol == 'X' or
                    self.cell[comb[0] - 1].symbol == self.cell[comb[1] - 1].symbol == self.cell[comb[2] - 1].symbol == 'O'):
                return True
        return False


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.win = 0

    def make_move(self):
        while True:
            numb = int(input(f'{self.name}: введите номер клетки для символа {self.symbol}: '))
            if 1 <= numb <= 9:
                return numb
            else:
                print('Некорректный ввод (номера клеток от 1 до 9). Повторите попытку\n')

class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        # self.board = Board()          #можно ли создать экземпляр доски внутри другого метода,
                                        #чтобы потом не очищать её,а создать новую?

    def run_one_move(self, player):
        numb = player.make_move()
        while True:
            if not self.board.cell[numb - 1].is_occupied:
                self.board.change_cell_state(numb, player.symbol)
                #os.system('cls' if os.name == 'nt' else 'clear') не получается очистить консоль
                self.board.display()
                break
            else:
                print('Клетка занята. Выберите другой вариант!\n')
                numb = player.make_move()
        if self.board.check_game_over():
            print('Победил игрок -', player.name)
            player.win += 1
            return True

    def run_one_game(self):
        # for i in range(1,10):             # очистка доски
        #  self.board.cell[i -1].symbol = ' '
        #  self.board.cell[i -1].is_occupied = False
        # self.board = Board()
        self.board.display()
        for z in range(9):
            result = Game.run_one_move(self, self.players[z % 2])
            if result:
                break
        else:
            print('Ничья!')
        print('Счет игроков:')
        print(self.players[0].name, '-', self.players[0].win)
        print(self.players[1].name, '-', self.players[1].win, '\n')

    def run(self):
        while True:
            print('Начать новую игру? y/n')
            print('Введите "y" если "Да" или "n" если "нет"')
            count = input().lower()
            self.board = Board()        # Создание доски
            if count == 'n':
                break
            elif count == 'y':
                Game.run_one_game(self)

p1 = Player('Иван', "X")
p2 = Player('Василий', "O")
game = Game(p1, p2)
game.run()
