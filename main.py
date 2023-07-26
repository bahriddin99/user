import sys

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QVBoxLayout, QPushButton, QLabel

from PyQt5.QtCore import Qt

class Button(QPushButton):
    def __init__(self):
        super().__init__()
        self.setFixedSize(90,90)

class Label(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("background: #ff0066; color: #fff; font-size: 30px; padding: 10px; border-radius: 20px")

class ButtonReset(QPushButton):
    def __init__(self,text):
        super().__init__(text)
        self.setFixedSize(300,50)
        self.setStyleSheet('QPushButton {font-size: 30px; background: #66ff66; border-radius: 10px; padding: 10px 0px; border: 2px solid black}'
            "QPushButton::hover{background: #003300; border: 4px solid #66ff66; color: #66ff66}")



class TicTacToe(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("TicTacToe")
        self.initUI()
        self.show()
    
    def initUI(self):
        self.v_box = QVBoxLayout()
        self.g_box = QGridLayout()
        self.btns = list()

        self.label = Label('X turn')
        self.btn_reset = ButtonReset("Reset Game")

        self.turn = 'X'
    
        for i in range(3):
            temp = list()
            for j in range(3):
                temp.append(Button())
            self.btns.append(temp)

        for i in range(3):
            for j in range(3):
                self.g_box.addWidget(self.btns[i][j], i,j)
                self.btns[i][j].clicked.connect(self.press)        

        self.v_box.addLayout(self.g_box)
        self.v_box.addWidget(self.label)
        self.v_box.addWidget(self.btn_reset)

        self.setLayout(self.v_box)

        self.btn_reset.clicked.connect(self.reset)

    def press(self):
        btn = self.sender()
        btn.setEnabled(False)
        if self.turn == 'X':
            btn.setText('X')
            btn.setStyleSheet('font-size: 70px; color: blue')
            self.turn = 'O'
        else :
            btn.setText('O')
            btn.setStyleSheet('font-size: 70px; color: red')
            self.turn = 'X'

        self.label.setText(f"{self.turn} turn")
        if self.check_winner():
            self.label.setText(f"{btn.text()} Win")
            self.deActive()
            return 0

    def reset(self):
        for i in range(3):
            for j in range(3):
                self.btns[i][j].setStyleSheet("")
                self.btns[i][j].setText('')
                self.btns[i][j].setEnabled(True)
        self.turn = 'X'
        self.label.setText(f"{self.turn} turn")

    def check_winner(self):
        for i in range(3):
            if self.btns[i][0].text() == self.btns[i][1].text() and self.btns[i][0].text() == self.btns[i][2].text() and self.btns[i][0].text() != '':
                self.btns[i][0].setStyleSheet('QPushButton {font-size: 70px; color: white; background: green}')
                self.btns[i][1].setStyleSheet('QPushButton {font-size: 70px; color: white; background: green}')
                self.btns[i][2].setStyleSheet('QPushButton {font-size: 70px; color: white; background: green}')
                return True
            
        for i in range(3):
            if self.btns[0][i].text() == self.btns[1][i].text() and self.btns[0][i].text() == self.btns[2][i].text() and self.btns[0][i].text() != '':
                self.btns[0][i].setStyleSheet('QPushButton {font-size: 70px; color: white; background: green}')
                self.btns[1][i].setStyleSheet('QPushButton {font-size: 70px; color: white; background: green}')
                self.btns[2][i].setStyleSheet('QPushButton {font-size: 70px; color: white; background: green}')
                return True
            
        if self.btns[0][0].text() == self.btns[1][1].text() and self.btns[0][0].text() == self.btns[2][2].text() and self.btns[0][0].text() != '':
            self.btns[0][0].setStyleSheet('QPushButton {font-size: 70px; color: white; background: green}')
            self.btns[1][1].setStyleSheet('QPushButton {font-size: 70px; color: white; background: green}')
            self.btns[2][2].setStyleSheet('QPushButton {font-size: 70px; color: white; background: green}')
            return True

        if self.btns[0][2].text() == self.btns[1][1].text() and self.btns[0][2].text() == self.btns[2][0].text() and self.btns[1][1].text() != '':
            self.btns[2][0].setStyleSheet('QPushButton {font-size: 70px; color: white; background: green}')
            self.btns[1][1].setStyleSheet('QPushButton {font-size: 70px; color: white; background: green}')
            self.btns[0][2].setStyleSheet('QPushButton {font-size: 70px; color: white; background: green}')
            return True
        return False
    

    def deActive(self):
        for i in range(3):
            for j in range(3):
                self.btns[i][j].setEnabled(False)

        



app = QApplication([])

win = TicTacToe()

sys.exit(app.exec_())
