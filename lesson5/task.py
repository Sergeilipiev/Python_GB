# 1 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

words = 'Напишите программу, удаляющую из текста все слова, содержащие ""абв"".'
sp = list(filter(lambda x: 'а' not in x and 'б' not in x and 'в' not in x, words.split()))
print(sp)

# 2 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def player_vs_player():
    candies_total = 100
    max_take = 28
    count = 0

    x = randint(1, 2)
    if x == 1:
        first = 'Игрок 1'
        second = 'Игрок 2'
    else:
        first = 'Игрок 2'
        second = 'Игрок 1'
    print(f'{first} ходит первым !')

    while candies_total > 0:
        if count == 0:
            step = int(input(f'\nСколько конфет возьмет {first} = '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\nМожно взять только {max_take} конфет {first}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nосталось {candies_total}')
            count = 1
        else:
            print('Конфеты закончились')

        if count == 1:
            step = int(input(f'\nСколько конфет возьмет {second} = '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\nМожно взять только {max_take} конфет {second}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nосталось {candies_total}')
            count = 0
        else:
            print('Конфеты закончились')

    if count == 1:
        print(f'{second} ПОБЕДИЛ')
    if count == 0:
        print(f'{first} ПОБЕДИЛ')


player_vs_player()


def player_vs_bot():
    candies_total = 100
    max_take = 28
    players = ['Игрок 1', 'Компьютер']
    first = randint(-1, 0)

    print(f'{players[first+1]} ходит первым !')

    while candies_total > 0:
        first += 1
        if players[first % 2] == 'Компьютер':
            print(
                f'\nХодит {players[first%2]} \nОсталось {candies_total}: ')

            if candies_total < 29:
                step = candies_total
            else:
                delenie = candies_total//28
                step = candies_total - ((delenie*max_take)+1)
                if step == -1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'\nХодит  {players[first%2]} \nОсталось {candies_total}:  '))
            while step > max_take or step > candies_total:
                step = int(input(f'\nМожно взять не больше {max_take} конфет, попробуй еще раз: '))
        candies_total = candies_total - step

    print(f'Осталось {candies_total} \nПобедил {players[first%2]}')

player_vs_bot()

# 3 Создайте программу для игры в ""Крестики-нолики"".

print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = list(range(1,10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
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


# 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode(data: str) -> str:
    seq = [data[0], 1]

    for elem in data[1:]:
        if elem != seq[-2]:
            seq += [elem, 1]
        else:
            seq[-1] += 1

    return ''.join(map(str, seq))


def deencode(data: str) -> str:
    def convert():
        return seq[:-2] + [seq[-2] * (seq[-1] or 1)]

    seq = [data[0], 0]

    for elem in data[1:]:
        if elem.isdigit():
            seq[-1] = seq[-1] * 10 + int(elem)
        else:
            seq = convert() + [elem, 0]

    return "".join(convert())

with open('1.txt') as f:
   coded = encode(f.read())
with open('2.txt', 'w') as f:
    f.write(coded)