from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', 'false')
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from random import randint

number_correct_answers=0
number_question=1
right_answer_sound = SoundLoader.load('right_answer.mp3')
wrong_answer_sound = SoundLoader.load('wrong_answer.mp3')

question_list = [['https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Flag_of_Australia.svg/1920px-Flag_of_Australia.svg.png', 'Великобритания', 'Австралия', 'Новая Зеландия', 'Индия', 2],
              ['https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Flag_of_Brazil.svg/1280px-Flag_of_Brazil.svg.png', 'Бразилия', 'Аргентина', 'Ямайка', 'Португалия', 1],
              ['https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Flag_of_the_United_Kingdom_%283-5%29.svg/1920px-Flag_of_the_United_Kingdom_%283-5%29.svg.png', 'Великобритания', 'Австралия', 'Новая Зеландия', 'Индия', 1],
              ['https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/1920px-Flag_of_Germany.svg.png', 'Австрия', 'Люксембург', 'Швейцария', 'Германия', 4],
              ['https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Flag_of_Georgia.svg/1920px-Flag_of_Georgia.svg.png', 'Азербайджан', 'Таждикистан', 'Грузия', 'Абхазия', 3],
              ['https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Flag_of_Ireland.svg/1920px-Flag_of_Ireland.svg.png', 'Ирландия', 'Исландия', 'Дания', 'Норвегия', 1],
              ['https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Flag_of_Indonesia.svg/1920px-Flag_of_Indonesia.svg.png', 'Польша', 'Венгрия', 'Болгария', 'Индонезия',4],
              ['https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Flag_of_Luxembourg.svg/1920px-Flag_of_Luxembourg.svg.png', 'Нидерланды', 'Бельгия', 'Люксембург', 'Австрия', 3],
              ['https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Flag_of_Norway.svg/1280px-Flag_of_Norway.svg.png', 'Финляндия', 'Швейция', 'Норвегия', 'Дания', 3],
              ['https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Flag_of_Poland.svg/1920px-Flag_of_Poland.svg.png', 'Польша', 'Венгрия', 'Болгария', 'Индонезия',1],
              ['https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Russia.svg/1920px-Flag_of_Russia.svg.png', 'Словакия', 'Сербия', 'Словения', 'Россия', 4],
              ['https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Flag_of_Romania.svg/1920px-Flag_of_Romania.svg.png', 'Андорра', 'Румыния', 'Эфиопия', 'Уганда', 2],
              ['https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Flag_of_Serbia.svg/1280px-Flag_of_Serbia.svg.png', 'Словакия', 'Сербия', 'Словения', 'Россия', 2],
              ['https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Flag_of_Slovakia.svg/1280px-Flag_of_Slovakia.svg.png', 'Словакия', 'Сербия', 'Словения', 'Россия', 1],
              ['https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Flag_of_Slovenia.svg/1920px-Flag_of_Slovenia.svg.png', 'Словакия', 'Сербия', 'Словения', 'Россия', 3]]

class MainWidget(BoxLayout):
    def new_question(self):
        if(len(question_list)>0):
            question = question_list[randint(0,len(question_list)-1)]
            self.ids['img_question'].source = question[0]
            self.ids['btn_answer1'].text = question[1]
            self.ids['btn_answer2'].text = question[2]
            self.ids['btn_answer3'].text = question[3]
            self.ids['btn_answer4'].text = question[4]
        else:
            text = ''
            with open('result.txt', 'a+', encoding="utf-8-sig") as conn:
                conn.write('\n Результат: ' + str(number_correct_answers) + ' из 15')
            with open('result.txt', 'r', encoding="utf-8-sig") as conn:
                text = conn.read()
            self.ids['lbl_question'].text = text
            self.remove_widget(self.ids['img_question'])
            self.remove_widget(self.ids['layout_btns'])

    def btn_pressed(self, number_button):
        question:list
        for i in question_list:
            if(i[0] == self.ids['img_question'].source):
                question = i
                break
        global number_correct_answers
        global number_question
        if(number_button == question[5]):
            right_answer_sound.play()
            number_correct_answers += 1
        else:
            wrong_answer_sound.play()
        with open('result.txt','a',encoding="utf-8-sig") as conn:
            conn.write('        '+str(number_question)+'       '+question[number_button]+'      '+question[question[5]]+'\n')
        number_question+=1
        question_list.remove(question)
        self.new_question()     

class MainApp(App):
    def build(self):
        app = MainWidget()
        with open('result.txt','w',encoding="utf-8-sig") as conn:
            conn.write('Вопрос      Ваш ответ      Правильный ответ\n')
        app.new_question()
        return app

if __name__ == '__main__':
    MainApp().run()