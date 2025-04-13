from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QButtonGroup
from random import shuffle


class question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3





question_list = []
question_list.append(question('смысл жизни?','майнкрааааааааааааааааааааааааааааафт','да','зачем','кто я'))
question_list.append(question('выбери игру?','стендофф','гд','майнкрааааааааааааааааааааааааафт','тетрис'))
question_list.append(question('пон.Ты понял что это значит?','да','нет','я школьник поверь пж','лан'))
question_list.append(question('как ты смеешься? ',' я дед инсайд','АХАХАХАХАХАХААХАХАА','хах','ХАХХАХАХАХАХАХА'))
question_list.append(question('сзади тебя хаги ваги!','страшноооооооооооооо','кто это?','пофиг.','зачем?'))

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следущий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


def ask(q:question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_question.setText(q.question)
    Ib_Correct.setText(q.right_answer)
    show_question()


def show_correct(res):
    Ib_Result.setText(res)
    show_result()




def check_answer():
    main_win.total += 1
    if answer[0].isChecked():
        show_correct('правильно!')
        main_win.score +=1
    else:
        if answer[1].isChecked or answer[2].isChecked or answer[3].isChecked:
            show_correct('неверно!')
    print('Всего: ',str(main_win.total))
    print('Правильно:',str(main_win.score))
    print('Статистика',str(main_win.score/main_win.total *100))
        

def next_question():
    main_win.cur_question += 1
    if main_win.cur_question >= len(question_list):
        main_win.cur_question=0
    q = question_list[main_win.cur_question]
    ask(q)
    



def click_ok():
    if btn_ok.text()== 'Ответить':
        check_answer()
    else:
        next_question()







#def start_test():
    #if btn_ok.text() == 'Ответить':
        #show_result()
    #else:
        #show_question()




app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Насколько ты школьник?')
main_win.resize(400,200)
btn_ok = QPushButton('ответить')
lb_question = QLabel('выбери вариант ответа:')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('смурфы')
rbtn_3 = QRadioButton('чулымцы')
rbtn_4 = QRadioButton('алеуты')
answer = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
RadioGroup=QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox=QGroupBox('Результаты теста')
Ib_Result = QLabel('прав ты или нет?')
Ib_Correct = QLabel('ответ будет тут')
layout_res = QVBoxLayout()
layout_res.addWidget(Ib_Result,alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(Ib_Correct,alignment=Qt.AlignHCenter,stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_question, alignment = (Qt.AlignHCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)


RadioGroupBox.show()
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok,stretch = 2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1,stretch=2)
layout_card.addLayout(layout_line2,stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
q=question('Сколько стоит корова?','10 коров','10 рублей','10 копеек','1')
main_win.cur_question = -1
btn_ok.clicked.connect(click_ok)
main_win.total = 0
main_win.score = 0

next_question()
main_win.setLayout(layout_card)
main_win.show()
app.exec_()







