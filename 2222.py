import csv

questions = ['Какой жанр вас интересует?нажмите ENTER,если неважно.',
             'Вас интереснует полностью отснятое аниме?Ответьте да или нет.Нажмите ENTER,если неважно.',
             'Аниме какого года выпуска вы хотите увидеть?Напишите число или нажмите ENTER,если неважно',
             'Напишите число,рейтинг аниме которого будет выше или нажмите ENTER,если неважно',
             'Какой формат показа (TV, Web, Movie, etc)?нажмите ENTER,если неважно',
             'Какое минимальное количество голосов?нажмите ENTER,если неважно']
answers = []
for question in questions:
    print(question)
    answers.append(input())
result = []
with open('anime.csv') as file:
    reader = csv.DictReader(file, delimiter=',')
    for line in reader:
        if (answers[1] == 'да' and line['Finished'] == ('True' or 'Unknown')) or (answers[1] == '') or (
                answers[1] == 'нет' and (line['Finished'] == ('False' or 'Unknown'))):
            if line['StartYear'] > answers[2] or answers[2] == '' or line['StartYear'] == 'Unknown':
                if line['Rating Score'] > answers[3] or answers[3] == '' or line['Rating Score'] == 'Unknown':
                    if answers[4] == line['Type'] or answers[4] == '' or line['Type'] == 'Unknown':
                        if answers[5] <= line['Number Votes'] or answers[5] == '' or line['Number Votes'] == 'Unknown':
                            if answers[0] == '' or answers[0] in line['Tags']:
                                result.append(line['Name'])

with open('resultfile.txt', 'w', encoding='utf-8') as answerfile:
    for i in result:
        answerfile.write(f'{i}\n')
print('Список подходящих вам аниме в файле resultfile.txt')
