# начало кода
# 1 импорт pygame и инсталирование через командную строку - библиотеки pygame.
# 2 вывод экрана
# 3 цвет  экрана 
# 4 размер экрана и змейки 
# 5 перемещение змейки 
# 6 перемещение  змейки до границы надпись game_over = Вы проиграли!!! Попробуй снова- у тебя получится
# 7 
# 8 появление еды змейки
# 9 Увеличение длины змейки

import pygame # библиотека pygame.
import time # библиотека time.
import random # библиотека random.


pygame.init()  # init()  для инициализации экрана в начале кода.
white = (255, 255, 255/0.5)  # цветовая схема RGB (RED, GREEN, BLUE).  0 везде  черный цвет, 255 — белый.
black = (0, 0, 0) 
red = (255, 0, 0/0.5)
blue = (0, 0, 255)   # цветовая схема RGB (RED, GREEN, BLUE) с прозрачностью
yellow =(255, 255, 51/0.3)
green = (0, 255, 0/0.3)
dis_width = 900 #  ширина
dis_height = 700 # высота

dis = pygame.display.set_mode((dis_width, dis_height))  #display.set_mode()  создания экрана (размер экрана) с переменными dis_lengh, dis_width
pygame.display.set_caption('Змейка - игра на поедание пищи!!!') # display.set_caption(), выводится заголовок на экран — 'Змейка - игра на поедание пищи!!!'.
clock = pygame.time.Clock()   # текущее время обработки из библиотеки time

pyton_block = 10 # размер блока 
pyton_speed = 8   # скорость змеи
font_style = pygame.font.SysFont(None, 30) # Конструктор Font  передает имя файла -1 переменная None по умолчанию , размер шрифта -2 перемнная
font_score = pygame.font.SysFont(None, 20) # Конструктор Font  передает имя файла -1 переменная None по умолчанию , размер шрифта -2 перемнная

def my_score(score):# первая функция вывод на экран: счета в игре
    value = font_score.render("Очки в игре : " + str(score), True, yellow) # Функция render()  объединяет шаблон со словарем и возвращает объект в виде строки
    dis.blit(value, [0,0])  # при размещении указываются координаты к родительской поверхности surface

def my_pyton(pyton_block, pyton_list): # вторая функция
    for x in pyton_list: # цикл
        pygame.draw.rect(dis, black, [x[0], x[1], pyton_block, pyton_block]) # draw.rect(), рисует прямоугольник с цветом и размером с параметрами pyton_block

def message(msg, color):  # третья функция задание игры сообщения в цвете
    mesg = font_style.render(msg, True, color) # Метод render создает поверхность на которой "написан" текст. 2 аргумент сглаживание - true/false, 3 – цвет текста. также можно и 4 аргумент цвет фона.
    dis.blit(mesg, [dis_width/6, dis_height/3]) # Метод blit() применяется к той поверхности dis основная поверхность, на которую "накладывается" другая в ее системе координат.

def my_game():   # четвертая функция игры - основная для вызова игры
    game_over = False  # завершение игры
    game_close = False  # завершение игры

    x1_change = 0 # переменная 
    y1_change = 0 # переменная

    x1 = dis_width/2 # переменная координаты появления змейки на экране
    y1 = dis_height/2 # переменная координаты появления змейки на экране

    pyton_list = []
    grow_pyton = 1

    foodx = round(random.randrange(0, dis_width - pyton_block) / 10.0) * 10.0 # пища  змейки на экране с использованием библиотеки random
    # где 10.0 блок змейки. с использованием  random.randrange() возвращает случайное целое число в диапазоне (начало и конец). Функция random.randrange() три параметра в качестве входных значений: start, stop и width.
    foody = round(random.randrange(0, dis_width - pyton_block) / 10.0) * 10.0 # round округляет значение функции

    while not game_over: # цикл while для работы до окончания игры если игра не окончена
        while game_close == True:    
            dis.fill(blue)  # fill заполняет пространство игры до окончания
            message('Игра закончена = Вы проиграли!!!', red) # выводится на экран в конце
            pygame.display.update() # внесение дополнения в игру в дальнейшем

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over == True
                        game_close == False
                    if event.key == pygame.K_c:
                        my_game()

        for event in pygame.event.get():  #  цикл for in. Устанавливает текст заголовка в верхней части экрана event.get(), проверяет true/false
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:  # класс KEYDOWN для передвижения змейки через ветвление if и elif
                if event.key == pygame.K_LEFT: # влево
                    x1_change = -pyton_block    # изменения скорости передвижения змейки
                    y1_change = 0  # изменения направления передвижения змейки (не строго по вертикали и горизонтали)
                elif event.key == pygame.K_RIGHT:  # вправо
                    x1_change = pyton_block  
                    y1_change = 0
                elif event.key == pygame.K_UP:  # вверх
                    y1_change = -pyton_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:   # вниз
                    y1_change = pyton_block
                    x1_change = 0
        if x1 >= dis_width  or x1 < 0 or y1 >= dis_height or y1 < 0:  # проверка оператора or -and -not (or если все истинны, то true)
            game_close = True
        x1 += x1_change  # координаты для перемещения изменения
        y1 += y1_change   # координаты для перемещения изменения
        dis.fill(blue)   # цвет дисплея 
    # Параметр fill позволяет заполнить пространство контейнер по горизонтали (значение X), по вертикали (значение Y)

#  в скобках переменные (переменные: dis=размер экрана, red = цвет экрана, x1=координаты расположения змейки на экране, y1=координаты расположения змейки на экране, pyton_block=10, 10 = размер точки змейки
        pygame.draw.rect(dis, green, [foodx, foody, pyton_block, pyton_block]) #pygame.draw.rect(surface, …) – прямоугольник;
        pyton_grow_body = [] # тело змеи
        pyton_grow_body.append(x1) # append() добавляет в конец списка элемент, переданный ему в качестве аргумента по координатам
        pyton_grow_body.append(y1)  #c append() добавляет в конец списка элемент.
        pyton_list.append(pyton_grow_body) 
        if len(pyton_list) > grow_pyton:  # принимает длину списка и возвращает его обратно(если len > grow)
            del pyton_list[0] # удаляет элемент из списка с индексом 0
        for x in pyton_list[:-1]:  # цикл для списка pyton_list
            if x == pyton_grow_body[0]:
                game_close = True

        my_pyton(pyton_block, pyton_list)
        my_score(grow_pyton - 1)

        pygame.display.update()  # Метод update() используется для изменения значения ключа в словаре.
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - pyton_block) / 10.0) * 10.0 # координаты появления еды
            foody = round(random.randrange(0, dis_height - pyton_block) / 10.0) * 10.0
            print('Вкусняшка')
            grow_pyton += 1 # рост змеи 
        clock.tick(pyton_speed) # clock = pygame.time.Clock() Функция может использует  максимальную частоту кадров т.е.скорость змеи

    pygame.quit() # Обновляет экран.quit() - Используется для деинициализации всех модулей
    quit()  # завершение работы интерпретатора Python.
my_game() # вызов основной функции
# конец кода
