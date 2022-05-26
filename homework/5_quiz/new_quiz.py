import sqlite3
from time import sleep
from random import shuffle, choice

connection = sqlite3.Connection(database = 'database')
cursor = connection.cursor()

def create_db():

    que = [(1, 'Кого из перечисленных называют санитаром леса?', 1),
      (2, 'Какая страна самая большая?', 1),
      (3, 'Кого называют «царь зверей»?', 1),
      (4, 'Сколько лапок у паука?', 1),
      (5, 'Где правили фараоны?', 1),
      (6, 'Земля имеет сферическую форму и вращается вокруг Солнца по ...', 2),
      (7, 'Между орбитами каких планет расположен Сатурн?', 2),
      (8, 'Какие 2 океана соединяет Берингов пролив?', 2),
      (9, 'У какого моря нет ни одного берега?', 2),
      (10, 'Какая наука изучает строение клетки?', 2),
      (11, 'Кому принадлежат эти слова: «Кто с мечом на русскую землю придет, от меча и погибнет»', 3),
      (12, 'Какое животное обладает самым громким голосом?', 3),
      (13, 'Чем угощала Золушка своих сестер на балу? ', 3),
      (14, 'В каком городе родился русский писатель А.П. Чехов? ', 3),
      (15, 'Сколько месяцев в году имеют 28 дней?', 3),
      (16, 'Как называется самая известная смотровая площадка Москвы?', 3),
      (17, 'Как звали маму Македонского?', 4),
      (18, 'Имя какого писателя носит центральная библиотека Краснодара', 4),
      (19, 'Представителем какого стиля является Муха?', 4),
      (20, 'Столицей какой страны является город Катманду', 4),
      (21, 'Кто стоял во главе защитников обороны курганной высоты?', 4),
      (22, 'Пабло Пикассо написал более шестидесяти картин, посвящённых этой женщине. Она была его моделью, а после возлюбленной. Как её зовут?', 4),
      (23, 'Какие помидоры использую при приготовлении оригинальной неаполитанской пиццы?', 4),
      (24, 'Кто из архитекторов стал стал первой в истории женщиной, награждённой Притцкеровской премией?', 4),
      (25, 'Если Абоба, то...', 5),
      (26, 'Где Яна Каджая?', 5),
      (27, 'Какой лучший язык программирования?', 5)]

    anss = [(1, 'Дятла', 'Оленя', 'Белку', 'Зайца'),
        (2, 'Россия', 'Китай', 'Канада', 'США'),
        (3, 'Лев', 'Волк', 'Тигр', 'Медведь'),
        (4, '8', '7', '4', '12'),
        (5, 'Египет', 'Месопотамия', 'Финикия', 'Палестина'),
        (6, 'орбите', 'окружности', 'эклиптике', 'эллипсу'),
        (7, 'Между Юпитером и Ураном', 'Между Венерой и Юпитером', 'Между Меркурием и Марсом', 'Между Ураном и Нептуном'),
        (8, 'Тихий и Северный Ледовитый', 'Тихий и Южный', 'Индийский и Южный', 'Атлантический и Северный Ледовитый'),
        (9, 'Саргассово море', 'Ваттовое море', 'Море Лаптевых', 'Море Бофорта'),
        (10, 'Цитология', 'Гистология', 'Микробиология', 'Энтомология'),
        (11, 'Александр Невский', 'Ярослав II Всеволодович', 'Дмитрий Донской', 'Иван Грозный'),
        (12, 'Синий кит', 'Большой зайцегуб', 'Слон', 'Кашалот'),
        (13, 'Апельсины', 'Пироженые', 'Яблоки', 'Канапе'),
        (14, 'Таганрог', 'Москва', 'Курск', 'Новгород'),
        (15, 'Двенадцать', 'Один', 'Два', 'Десять'),
        (16, 'Воробьевы горы', 'Мост Богдана Хмельницкого', 'Балконы на набережных', 'Смотровая площадка РАН'),
        (17, 'Олимпиада', 'Афина', 'Климена', 'Эвриклея'),
        (18, 'Пушкин', 'Лемронтов', 'Толстой', 'Горький'),
        (19, 'Ар-нуво', 'Барокко', 'Абстракционизм', 'Арте повера'),
        (20, 'Непал', 'Бангладеш', 'Филиппины', 'Мьянма'),
        (21, 'Н.Н.Раевский', 'Д.В.Давыдов', 'К.Минин', 'М.И.Кутузов'),
        (22, 'Фернанда Оливье', 'Жанна Эбютерн', 'Хельга Тесторф', 'Эмилия Луиза Богарне'),
        (23, 'Сан-Марцано', 'Канестрино', 'Гроздевой Корбарино', 'Даттерини'),
        (24, 'Заха Хадид', 'Кадзуё Сэдзима','Элизабет Диллер', 'Аннетт Бенинг'),
        (25, 'Абиба', 'ааааааа', 'Баобаб', '6'),
        (26, 'В академе', 'На парах', 'У врача', 'На конференции'),
        (27, 'Bash', 'Python', 'C++', 'Java')]

    querys = ['drop table if exists answers;',
              'drop table if exists questions;',
              '''create table questions
                (
                    qid int primary key,
                    question text,
                    tour int
                );''',
              '''create table answers 
                            (
                                qid int references questions, 
                                current_answer text, 
                                random1 text, 
                                random2 text, 
                                random3 text
                            );'''
              ]


    [cursor.execute(querys[i]) for i in range(4)]
    for i in range(27):
        cursor.execute('insert into questions values' + str(que[i]))
        cursor.execute('insert into answers values' + str(anss[i]))

def sym2place(x, y, sym='*'):
    print(f"\u001b[{x}C", end='')
    if y:
        print(f"\u001b[{y}B", end='')
    print(sym, end='\r')
    if y:
        print(f"\u001b[{y}A", end='')

def string_printer(string_, y, x=-1, delay=0.005):
    if x != -1:
        sym2place(x, y, string_)
    else:
        for_print = '{0:{1}{2}{3}}'.format(string_, ' ', '^', 210)
        [(sym2place(x, y), sleep(delay)) for x in range(1, 211)]
        [(sym2place(x, y, sym), sleep(delay)) for x, sym in zip(range(1, 211), for_print)]


def timer(string_):
    for second in [3, 2, 1]:
        if second == 3:
            sym2place(10, 30, ' ' * 190)
        else:
            for i in range(len(string_)+2):
                sym2place(100 + i, 30)
                sleep(0.010)
        for i in range(len(string_)):
            sym2place(100 + i, 30, string_[i])
            sleep(0.010)
        sym2place(100 + len(string_), 30, str(second)+' ')
        sleep(0.8)

def ramka(i):
    if i < 213:
        sym2place(i, 0)
    if i < 58:
        sym2place(0, i)
    if 1 < i < 215:
        sym2place(i-2, 2)
    if 271 > i > 212:
        sym2place(211, i - 212)
    if 270 > i > 57:
        sym2place(i-57, 57)
    if 27 < i < 239:
        sym2place(i - 27, 27)
    if 31 < i < 243:
        sym2place(i - 31, 31)

your = 'Your input:    '
def beautiful_input():
    for i in range(len(your)):
        sym2place(100+i, 35)
        sleep(0.010)
    for i in range(len(your)):
        sym2place(100+i, 35, your[i])
        sleep(0.010)
    print("\u001b[35B", end="\u001b[112C")
    result = input()
    print("\u001b[1A", end="\u001b[100C")
    print(" " * 15)
    print("\r", end="\u001b[36A")
    return result

def queryst(level):
    cursor.execute(f'select * from questions where tour = {level}')                         # question query
    question = choice(cursor.fetchall())
    cursor.execute('select * from answers where qid =' + str(question[0]))                  # answer query by question id
    answers = cursor.fetchall()
    answers = list(answers[0])[1:]
    cur_ans = answers[0]
    shuffle(answers)
    return [question[1], cur_ans] + [answers]

hello = '*' + '{0:{1}{2}{3}}'.format("Hello, it is a quiz by Borovoy Arseny and Makhotka Alla", ' ', '^', 210)
lets = '*' + '{0:{1}{2}{3}}'.format("Press y to start", ' ', '^', 210)
for i in range(271):
    ramka(i)
    if 1 < i < 212:
        string_printer("*", 1, i-1)
    if 20 < i < 231:
        string_printer(hello[i-21], 1, i-20)
    if 29 < i < 240:
        string_printer("*", 29, i - 29)
    if 49 < i < 260:
        string_printer(lets[i-50], 29, i-49)
    sleep(0.010)
#
if beautiful_input()[0].lower() == 'y':
    for i in range(220):
        if i < 5:
            sym2place(106, 54 - i)
            sym2place(106, 53 + i)
        if i < 107:
            sym2place(107 - i, 54)
            sym2place(107 + i, 54)
        if 3 < i < 110:
            sym2place(110 - i, 50)
            sym2place(101 + i, 50)
        sleep(0.010)

timer('Start after ')
create_db()
for again in range(1, 6):
    data = queryst(again)
    question = '{0:{1}{2}{3}}'.format('1) ' + data[0], ' ', '^', 212)
    vars1 = '{0:{1}{2}{3}}'.format('1) ' + data[2][0], ' ', '^', 105) + '*' + '{0:{1}{2}{3}}'.format('2) ' + data[2][1], ' ', '^', 105)
    vars2 = '{0:{1}{2}{3}}'.format('3) ' + data[2][2], ' ', '^', 105) + '*' + '{0:{1}{2}{3}}'.format('4) ' + data[2][3], ' ', '^', 105)
    for i in range(2, 211):
        string_printer("*", 30, i)
        string_printer("*", 52, i)
        string_printer("*", 56, i)
        sleep(0.004)
    for i in range(2, 212):
        string_printer(question[i], 30, i)
        string_printer(vars1[i-1], 52, i)
        string_printer(vars2[i-1], 56, i)
        sleep(0.004)
    answer = beautiful_input()
    if answer != str(data[2].index(data[1]) + 1):
        string_printer(f"Game over! Your Score {again-1}/5", 30)
        break
    if again == 5:
        timer("You won! Prize after ")
        count_ = 1
        print("\n" * 60)
        with open(file='/home/sirius/Downloads/Telegram Desktop/banner2.txt') as f:
            for line in f:
                count_ += 1
                print(line[:-2])
                if count_ > 58:
                    sleep(0.1)
