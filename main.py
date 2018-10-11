import string
import random
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

types = ['up','down','left','right']
class app(App):
    matrix = ''
    def build(self):
        self.labels = [[] for j in range(10)]
        floatlayout = FloatLayout()
        self.gridlayout = GridLayout()
        self.gridlayout.size_hint = (1, .8)
        self.gridlayout.pos_hint = {"top": 1}
        floatlayout.add_widget(self.gridlayout)
        self.gridlayout.rows = 10
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                l = Label(text=str(self.matrix[i][j]))
                l.font_size = 15
                self.labels[i].append(l)
                self.gridlayout.add_widget(l)
        self.t = TextInput()
        self.t.size_hint = (.5,.1)
        self.t.pos_hint = {"bottom":1, 'left':1}
        btn = Button(text="commit")
        btn.size_hint = (.5, .1)
        btn.pos_hint = {"bottom":1, 'right':1}
        floatlayout.add_widget(self.t)
        floatlayout.add_widget(btn)
        btn.bind(on_press=self.btnclicked)
        return floatlayout
    def btnclicked(self, o):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.labels[i][j].color = (1,1,1,1)
                self.labels[i][j].font_size = 15
        self.seek(self.matrix, self.t.text)
    def seek(self, matrix, name, x=0, y=0):
        for i in range(x, len(matrix)):
            for j in range(y, len(matrix[0])):
                ret = self.algorithm(matrix, name, j, i)

    def algorithm(self, matrix, name, x, y, t=0):
        ok = False
        minimum, maximum = 0, 0
        step = 1
        self.showlabels = []
        if t == 0:
            minimum, maximum = y, -1
            step = -1
        elif t == 1:
            minimum, maximum = y, len(matrix)
        elif t == 2:
            minimum, maximum = x, -1
            step = -1
        elif t == 3:
            minimum, maximum = x, len(matrix[y])
        if t <= 1:
            counter = 0
            tmp = 0
            for i in range(minimum, maximum, step):
                if matrix[i][x] == name[tmp]:
                    counter += 1
                    self.showlabels.append(self.labels[i][x])
                else:
                    ok = False
                    break
                if len(name) == counter:
                    for ii in self.showlabels:
                        ii.color = (0,1,0,1)
                        ii.font_size = 25
                    self.t.text = 'Found : %s' % types[t]
                    return True
                tmp += 1
        if 2 <= t <= 3:
            counter = 0
            tmp = 0
            for i in range(minimum, maximum, step):
                if matrix[y][i] == name[tmp]:
                    counter += 1
                    self.showlabels.append(self.labels[y][i])
                else:
                    ok = False
                    break
                if len(name) == counter:
                    for ii in self.showlabels:
                        ii.color = (0,1,0,1)
                        ii.font_size = 25
                    self.t.text = 'Found : %s' % types[t]
                    return True
                tmp += 1
        self.showlabels = []
        if ok == False:
            if t == 3:
                return False
            else:
                t += 1
                self.algorithm(matrix, name, x, y, t)

def main():
    c, r = 10, 10
    matrix = [['0' for i in range(c)] for j in range(r)]
    chars = list(string.ascii_letters)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = random.choice (chars)
    a = app()
    a.matrix = matrix
    a.run()
    # name = raw_input('Enter The Something\n')
    # name = list(name)
    # seek(matrix, name)

if __name__ == '__main__':
    main()
