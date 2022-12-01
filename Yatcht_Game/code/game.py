from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

import calcFunctions
from keypad import upperScoreList, lowerScoreList, functionMap, tool_tip

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

class Yatcht(QWidget):
    def __init__(self):
        super().__init__()
        self.d_list = ['0', '0', '0', '0', '0']
        self.turn_ = 13
        self.rturn_ = 2
        self.cyatcht = 0
        self.ybonus = 0
        self.initUI()
    
    def initUI(self):
        
        title_ = QLabel('''Yatcht Game !''')
        font_ = title_.font()
        font_.setPointSize(20)
        title_.setFont(font_)
        
        rule = QPushButton('설명')
        
        rule_ = '''
게임룰 :
1. Roll을 눌러 주사위 5개를 던진다.
    
2. 체크박스를 체크한 주사위를 다시
   던진다. (횟수 2번)
                            
3. 왼쪽 족보에 주사위 숫자를
   기록한다.
   (조건에 안맞을시 0점)
                        
4. 족보를 다 채우면 게임이 끝난다.
   (Regame으로 다시 시작가능)
   
5. Bonus : 위 점수가 63점을 넘을시 35점 추가.
   Yatcht Bonus : Yatcht가 또 나올경우 100점 추가.
'''
        rule.setToolTip(rule_)
        # text 박스들과 그 리스트
        self.aces_l = QLineEdit(self)
        self.twos_l = QLineEdit(self)
        self.threes_l = QLineEdit(self)
        self.fours_l = QLineEdit(self)
        self.Fives_l = QLineEdit(self)
        self.Sixes_l = QLineEdit(self)
        self.Bonus_l = QLineEdit(self)
        
        self.Choice_l = QLineEdit(self)
        self.tcard_l = QLineEdit(self)
        self.fcard_l = QLineEdit(self)
        self.f_house_l = QLineEdit(self)
        self.s_s_l = QLineEdit(self)
        self.l_s_l = QLineEdit(self)
        self.yatcht_l = QLineEdit(self)
        self.yatchtBonus_l = QLineEdit(self)
        self.score_l = QLineEdit(self)
        
        self.lineEditList = [
            self.aces_l, self.twos_l, self.threes_l, self.fours_l, 
            self.Fives_l, self.Sixes_l, self.Bonus_l, self.Choice_l,
            self.tcard_l, self.fcard_l, self.f_house_l, self.s_s_l,
            self.l_s_l, self.yatcht_l, self.yatchtBonus_l, self.score_l
        ]
        
        self.d0_img = QPixmap('D0.png')
        self.d1_img = QPixmap('D1.png')
        self.d2_img = QPixmap('D2.png')
        self.d3_img = QPixmap('D3.png')
        self.d4_img = QPixmap('D4.png')
        self.d5_img = QPixmap('D5.png')
        self.d6_img = QPixmap('D6.png')
        
        self.dice_img = {
            "": self.d0_img,
            '1': self.d1_img, '2': self.d2_img, '3': self.d3_img,
            '4': self.d4_img, '5': self.d5_img, '6': self.d6_img
        }
        
        for dice in self.dice_img.values():
            dice.scaledToHeight(50)
            
        # 레이아웃들
        score_grid = QGridLayout()
        title_grid = QGridLayout()
        dice_grid = QGridLayout()
        main_grid = QGridLayout()
        
        # 점수판 윗부분
        r = 0
        for btnText in upperScoreList:
            button = Button(btnText, self.buttonClicked)
            button.setToolTip(tool_tip[r])
            self.lineEditList[r].setReadOnly(True)
            barrier = QLabel('｜')
            score_grid.addWidget(button, r, 0)
            score_grid.addWidget(self.lineEditList[r], r, 1)
            score_grid.addWidget(barrier, r, 2)
            r += 1
        
        # Bonus 점수판
        self.Bonus = QLabel('Bonus :')
        self.lineEditList[r].setReadOnly(True)
        barrier = QLabel('｜')
        score_grid.addWidget(self.Bonus, r, 0)
        score_grid.addWidget(self.lineEditList[r], r, 1)
        score_grid.addWidget(barrier, r, 2)
        r += 1
        
        # 점수판 아랫부분
        for btnText in lowerScoreList:
            button = Button(btnText, self.buttonClicked)
            button.setToolTip(tool_tip[r-1])
            self.lineEditList[r].setReadOnly(True)
            barrier = QLabel('｜')
            score_grid.addWidget(button, r, 0)
            score_grid.addWidget(self.lineEditList[r], r, 1)
            score_grid.addWidget(barrier, r, 2)
            r += 1
        
        # 야찌 보너스 점수판
        self.yatchtBonus = QLabel('Yatcht Bonus :')
        self.lineEditList[r].setReadOnly(True)
        barrier = QLabel('｜')
        score_grid.addWidget(self.yatchtBonus, r, 0)
        score_grid.addWidget(self.lineEditList[r], r, 1)
        score_grid.addWidget(barrier, r, 2)
        r += 1

        # 최종 점수판
        self.score = QLabel('score :')
        self.lineEditList[r].setReadOnly(True)
        barrier = QLabel('｜')
        score_grid.addWidget(self.score, r, 0)
        score_grid.addWidget(self.lineEditList[r], r, 1)
        score_grid.addWidget(barrier, r, 2)
        r += 1
        
        #score 기록판
        self.save_q = QLabel('Score List')
        self.saver = QTextEdit()
        # s = calcFunctions.save(0)
        # self.saver.setText('')
        # for i in range(len(s)):
        #         self.saver.append(f"{i+1}위 : {s[i][1]}점\t {s[i][0]}에 기록")
        self.saver.setReadOnly(True)
        
        # regame 버튼
        self.regame = QPushButton('Regame')
        barrier = QLabel('｜')
        score_grid.addWidget(self.regame, r, 0, 1, 2)
        score_grid.addWidget(barrier, r, 2)
            
        roll = Button('Roll !', self.buttonClicked)
        reroll = Button('ReRoll !', self.buttonClicked)
        
        roll_c_m = QLabel('count :')
        self.roll_c = QLineEdit('13')
        reroll_c_m = QLabel('count :')
        self.reroll_c = QLineEdit('2')
        
        # 주사위
        self.dice_1 = QLabel(self)
        self.dice_2 = QLabel(self)
        self.dice_3 = QLabel(self)
        self.dice_4 = QLabel(self)
        self.dice_5 = QLabel(self)
        self.dice_list = [self.dice_1, self.dice_2, self.dice_3, self.dice_4, self.dice_5]
        
        # 체크박스
        self.dice_1_c = QCheckBox('1', self)
        self.dice_2_c = QCheckBox('2', self)
        self.dice_3_c = QCheckBox('3', self)
        self.dice_4_c = QCheckBox('4', self)
        self.dice_5_c = QCheckBox('5', self)
        self.check_list = [self.dice_1_c, self.dice_2_c, self.dice_3_c, self.dice_4_c, self.dice_5_c]
        
        # 메세지 박스
        self.msg = QLineEdit(self)
        self.msg.setReadOnly(True)
        self.msgq = QLabel('msg :')
        
        title_grid.addWidget(title_, 0, 0)
        title_grid.addWidget(rule, 0, 1)

        for i in range(5):
            dice_grid.addWidget(self.dice_list[i], 0, i)
            dice_grid.addWidget(self.check_list[i], 1, i)
            self.dice_list[i].setPixmap(self.dice_img[self.dice_list[i].text()])
        
        hbox = QHBoxLayout()
        hbox.addWidget(roll)
        hbox.addWidget(reroll)
        
        hbox2 = QHBoxLayout()
        hbox2.addWidget(roll_c_m)
        hbox2.addWidget(self.roll_c)
        hbox2.addWidget(reroll_c_m)
        hbox2.addWidget(self.reroll_c)
        
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.msgq)
        hbox3.addWidget(self.msg)
        
        vbox = QVBoxLayout()
        vbox.addLayout(title_grid)
        vbox.addStretch(1)
        vbox.addWidget(self.save_q)
        vbox.addWidget(self.saver)
        vbox.addLayout(dice_grid)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        
        
        main_grid.addLayout(score_grid, 0, 0)
        main_grid.addLayout(vbox, 0, 1)
        
        self.setLayout(main_grid)
        
        # 버튼 기능
        self.regame.clicked.connect(self.buttonClicked)
        
        # text박스 튜플
        self.lineEditMap = {
        'Aces': self.aces_l, 'Twos': self.twos_l, 'Threes': self.threes_l, 
        'Fours': self.fours_l, 'Fives': self.Fives_l, 'Sixes': self.Sixes_l, 
        'Choice': self.Choice_l, '3card': self.tcard_l, '4card': self.fcard_l, 
        'Full house': self.f_house_l, 'S.Straight': self.s_s_l, 'L.Straight': self.l_s_l, 
        'Yatcht': self.yatcht_l, 
        }
    
    def buttonClicked(self):
        
        button = self.sender()
        key = button.text()
        
        if key == 'Roll !':
            if self.turn_ != 0 and self.d_list[0] == '0':
                dice_list = calcFunctions.roll()
                self.d_list = dice_list
                for i in range(5):
                    self.dice_list[i].setText(dice_list[i])
                    self.dice_list[i].setPixmap(self.dice_img[self.dice_list[i].text()])
                self.turn_ -= 1
                self.roll_c.setText(str(self.turn_))
                
            elif self.turn_ == 0:
                self.msg.setText('모든 턴을 사용하였습니다 !')
                
            else:
                self.msg.setText('기록을 해주세요 !')
            return 0
                
        elif key == 'ReRoll !':
            if self.dice_1_c.isChecked() == False and self.dice_2_c.isChecked() == False and \
                self.dice_3_c.isChecked() == False and self.dice_4_c.isChecked() == False and self.dice_5_c.isChecked() == False:
                self.msg.setText('다시 굴릴 주사위를 체크해주세요 !')
                
            elif self.rturn_ != 0:
                dice_list = calcFunctions.reroll(self.check_list, self.d_list)
                self.d_list = dice_list
                for i in range(5):
                    self.dice_list[i].setText(dice_list[i])
                    self.dice_list[i].setPixmap(self.dice_img[self.dice_list[i].text()])
                self.rturn_ -= 1
                self.reroll_c.setText(str(self.rturn_))
                
            elif self.rturn_ == 0:
                self.msg.setText('Reroll 횟수 초과 ! 기록을 해주세요 !')
        
            return 0
                
        elif key in functionMap.keys():
            if self.lineEditMap[key].text() == '' and self.d_list[0] != '0':
                v = functionMap[key](self.d_list)
                self.lineEditMap[key].setText(v)
                self.rturn_ = 2
                
                if calcFunctions.upsum(self.aces_l.text(), self.twos_l.text(), self.threes_l.text(), \
                    self.fours_l.text(), self.Fives_l.text(), self.Sixes_l.text()) >= 63:
                    
                    self.Bonus_l.setText('35')
                    
                if len(set(self.d_list)) == 1:
                    self.cyatcht += 1
                    if self.cyatcht > 1:
                        self.ybonus += 100
                        self.yatchtBonus_l.setText(str(self.ybonus))
                        
                for i in range(5):
                    self.dice_list[i].setText('')
                    self.dice_list[i].setPixmap(self.dice_img[self.dice_list[i].text()])
                    self.d_list[i] = '0'
                    self.check_list[i].setChecked(False)
                    
                sc = calcFunctions.score(self.aces_l.text(), self.twos_l.text(), self.threes_l.text(),  \
                    self.fours_l.text(), self.Fives_l.text(), self.Sixes_l.text(), self.Choice_l.text(),\
                    self.tcard_l.text(), self.fcard_l.text(), self.f_house_l.text(), self.s_s_l.text(), \
                    self.l_s_l.text(), self.yatcht_l.text(), self.Bonus_l.text(), self.yatchtBonus_l.text())
                
                self.score_l.setText(sc)
                self.reroll_c.setText('2')
                
            else:
                self.msg.setText('기록을 할 수 없습니다 !')
                return 0
            
        elif key == 'Regame':
            self.turn_ = 13
            self.rturn_ = 2
            self.cyatcht = 0
            self.ybonus = 0
            self.d_list = ['0', '0', '0', '0', '0']
            for label in self.lineEditList:
                label.setText('')             
            for dice in self.dice_list:
                dice.setText('')
            for i in range(5):
                self.dice_list[i].setPixmap(self.dice_img[self.dice_list[i].text()])
            self.roll_c.setText(str(self.turn_))
            self.reroll_c.setText(str(self.rturn_))
            self.msg.setText('게임을 초기화하셨습니다 !')
            return 0
            
        if self.turn_ == 0:
            s = calcFunctions.save(self.score_l.text())
            self.saver.setText('')
            for i in range(len(s)):
                self.saver.append(f"{i+1}위 : {s[i][1]}점\t {s[i][0]}에 기록")
            self.msg.setText('게임이 종료되었습니다 !')
            self.rturn_ = 0
            self.reroll_c.setText(str(self.rturn_))
            return 0
        self.msg.setText('')
            
if __name__ == '__main__':
    import sys
    from datetime import datetime
    app = QApplication(sys.argv)
    game = Yatcht()
    game.resize(500, 700)
    game.move(700,150)
    game.setWindowTitle('Yatcht_Game')
    game.show()
    sys.exit(app.exec_())