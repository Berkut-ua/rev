# -*- coding: UTF-8 -*-
import sys
from PyQt4 import QtGui, QtCore
from reversi_ui import Ui_Reversi
import urllib2
import json
import board

pieces = [". ", "\xe2\x97\x8f ", "\xe2\x97\xaf "]

class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        self.my_rev = myRev()
        
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Reversi()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.btnRegister
                               , QtCore.SIGNAL("clicked()")
                               , lambda: self.my_rev.register_email(str(self.ui.strEmail.text())))
        '''
        QtCore.QObject.connect(self.ui.btnShow
                               , QtCore.SIGNAL("clicked()")
                               , lambda: self.my_rev.render())
        '''
        QtCore.QObject.connect(self.ui.btnNewGame
                               , QtCore.SIGNAL("clicked()")
                               , lambda: self.my_rev.new_game())
        QtCore.QObject.connect(self.ui.btnMove
                               , QtCore.SIGNAL("clicked()")
                               , lambda: self.my_rev.my_move(str(self.ui.lineEdit.text())))
        '''
        QtCore.QObject.connect(self.ui.btnActiveGames
                               , QtCore.SIGNAL("clicked()")
                               , lambda: self.my_rev.active_games())
        '''
        '''
        QtCore.QObject.connect(self.ui.lstWidget
                               , QtCore.SIGNAL("itemClicked()")
                               , lambda: self.my_rev.select_game())
        '''
        self.ui.lstWidget.currentItemChanged.connect(self.my_rev.select_game)

class myRev(board.ReversiBoard):        
    def __init__(self):
        board.ReversiBoard.__init__(self)
        self.REV_PREFIX = 'http://reversi.laszlo.nu:1337'
        self.email = None
        self.key = None
    
    def _read_server(self, req=None):
        jsonData = {"error": "empty request"}
        if self.key == None:
            window.ui.textBrowser.setText("pls register")
            return jsonData
            
        if not req is None:
            resp = urllib2.urlopen(self.REV_PREFIX + req)
            dat = resp.read()
            jsonData = json.loads(dat)
        return jsonData

    def new_game(self):
        if self.key:
            jsonData = self._read_server('/newgame/%s' % self.key if self.key else '')
            self.board = jsonData['board']
            self.active_games()
        else:
            window.ui.textBrowser.setText("pls register")
    
    def active_games(self):
        jsonData = self._read_server('/listgames/%s' % self.key if self.key else '')
        if 'error' in jsonData:
            window.ui.textBrowser.setText("pls register")
        else:
            window.ui.lstWidget.clear()
            window.ui.lstWidget.addItems(jsonData)
                
    def register_email(self, strEmail=None):
        #strEmail = str(window.ui.strEmail.text())
        if strEmail is None or strEmail == '':
            return
        self.email = strEmail
        self.key = None
        req = urllib2.Request('%s/register/%s' % (self.REV_PREFIX, strEmail))
        resp = urllib2.urlopen(req)
        dat = resp.read()
        jsonDat = json.loads(dat)
        if 'key' in jsonDat:
            f = open('registered.dat', 'a')
            f.write(json.dumps({'email': strEmail, 'key': jsonDat['key']}))
            f.close()
            self.key = jsonDat['key']
            window.ui.textBrowser.setText("register new %s \n %s" % (strEmail, dat))
        else:
            f = open('registered.dat', 'r')
            for line in f:
                jsonLine = json.loads(line)
                if jsonLine['email'] == strEmail:
                    self.key = jsonLine['key']
                    window.ui.textBrowser.setText('email: %s, key: %s' % (self.email, self.key))
                    break
            if self.key is None:
                window.ui.textBrowser.setText(jsonDat["error"])
        self.active_games()
                
    def _invert(self, current):
        return 1 if current  == 2 else 2
    
    def select_game(self, cur, next_l):
        self.GameID = str(cur.text()) if(cur) else ''
        if self.GameID:
            jsonData = self._read_server('/state/%s/%s' % (self.key if self.key else '', self.GameID))
            self.board = jsonData['board']
            msg = 'Game: %s \nScore %s%s:%s%s You play %s' % (
                                        jsonData['id']
                                        , unicode(pieces[1], 'utf8'), jsonData['score'][0]
                                        , unicode(pieces[2], 'utf8'), jsonData['score'][1]
                                        , unicode(pieces[self._invert(jsonData['server_color'])], 'utf8')
                                        )
            window.ui.lblBoard.setText(msg)
            self.render()
        else:
            window.ui.textBrowser.setText("Select Game pls.")

    def my_move(self, strMoveData):
        if self.GameID and self.key and strMoveData:
            jsonData = self._read_server('/move/%s/%s/%s' % (self.key, self.GameID, strMoveData))
            try:
                self.board = jsonData['board']
                self.render()
            except:
                window.ui.textBrowser.setText(str(jsonData))
                
    def render(self):
            window.ui.textBrowser.setText(unicode(board.ReversiBoard.render(self), 'utf8'))
            
        
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
        
    sys.exit(app.exec_())
