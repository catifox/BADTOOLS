from PyQt5.QtWidgets import QApplication, QMainWindow
from qt_material import apply_stylesheet
import mainui
import sys

bd = ['嗷', '呜', '啊', '~'] #默认的[兽语]

def chooseSkin():
    if ui.skin.checkState() == True:
        apply_stylesheet(app, theme='dark_blue.xml')
    else:
        apply_stylesheet(app, theme='light_blue.xml')
#这些是核心实现
def str2hex(text: str):
    ret = ""
    for x in text:
        charHexStr = hex(ord(x))[2:]
        if len(charHexStr) == 3:
            charHexStr = "0" + charHexStr
        elif len(charHexStr) == 2:
            charHexStr = "00" + charHexStr
        ret += charHexStr
    return ret


def hex2str(text: str):
    ret = ""
    for i in range(0, len(text), 4):
        unicodeHexStr = text[i:i + 4]
        charStr = chr(int(unicodeHexStr, 16))
        ret += charStr
    return ret


def toBeast(rawStr):
    global bd
    tfArray = list(str2hex(rawStr))
    beast = ""
    n = 0
    for x in tfArray:
        k = int(x, 16) + n % 16
        if k >= 16:
            k -= 16
        beast += bd[int(k / 4)] + bd[k % 4]
        n += 1
    return bd[3] + bd[1] +bd[0] +beast + bd[2]
    #return "~呜嗷" + beast + "啊"


def fromBeast(decoratedBeastStr):
    global bd
    beastStr = decoratedBeastStr[3:-1]
    beastCharArr = list(beastStr)
    unicodeHexStr = ""
    try:
        for i in range(0, len(beastCharArr), 2):
            pos1 = bd.index(beastCharArr[i])
            pos2 = bd.index(beastCharArr[i + 1])
            k = ((pos1 * 4) + pos2) - (int(i / 2) % 16)
            if k < 0:
                k += 16
            unicodeHexStr += hex(k)[2:]
        return hex2str(unicodeHexStr)
    except ValueError:
        return '密文无法解密'

#密码栏的可用性(四个不同样的字符)
#按下[确认兽语]按钮后执行
def keyWordRight():
    global bd
    global keyWord
    keyWord = str(ui.keyLineEdit.text()) #获取密码栏的文本
    if len(list(keyWord)) != 4:
        bd = ['嗷', '呜', '啊', '~']
        print('字符数量错误 :-( ,使用默认[兽语]')
    elif len(set(list(keyWord))) != len(list(keyWord)):
        bd = ['嗷', '呜', '啊', '~']
        print('有重复的字符 :-[ ,使用默认[兽语]')
    else:
        bd = list(keyWord)
        print('字符是被允许使用的')

def doIt(): #判断[加密]或[解密]
    global mainText
    mainText = str(ui.mainPlainTextEdit.toPlainText()) #获取文本栏文本
    if ui.encryptRadioButton.isChecked(): #当[加密]按钮被选中
        ui.mainPlainTextEdit.setPlainText(toBeast(mainText))
        print('已完成加密,结果返回至文本框中')
    elif ui.decryptRadioButton.isChecked(): #当[解密]按钮被按下后
        ui.mainPlainTextEdit.setPlainText(fromBeast(mainText))
        print('已完成解密,结果返回至文本框中')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = mainui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    apply_stylesheet(app, theme='light_blue.xml')
    MainWindow.show()


    ui.encryptRadioButton.setChecked(True) #默认选择[加密]
    ui.keyLineEdit.setText('嗷呜啊~') #密码栏的默认值
    ui.mainPlainTextEdit.setPlainText('问天地好在。') #文本栏的默认值

    ui.getKeyPushButton.clicked.connect(lambda:keyWordRight()) #当[确认兽语]按钮被按下后
    ui.roarPushButton.clicked.connect(lambda:doIt()) #当[ROAR!]按钮被按下后
    ui.pushButton.clicked.connect(lambda:chooseSkin()) #当[确认兽语]按钮被按下后
    ui.actionExit.triggered.connect(sys.exit)
    sys.exit(app.exec_())



'''
这里是镜中er
终于把gui写完了
十分疲惫
却也学习了些新的用法
就当是练手了罢
若是今后有空
还可将此程式剪为视频
但这一切恐怕也得咕了
21.8.22
'''