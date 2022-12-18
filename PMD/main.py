import sys
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QWidget
import math


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcomescreen.ui", self)
        self.viga.clicked.connect(self.vigabasepg)
        
    def vigabasepg(self):
        vigab = VigaBase()
        widget.addWidget(vigab)
        widget.setCurrentIndex(widget.currentIndex()+1)
        

class VigaBase(QDialog):
    def __init__(self):
        super(VigaBase, self).__init__()
        loadUi("vigabase.ui", self)
        self.vigac.clicked.connect(self.vigaparametros)
        
    def vigaparametros(self):
        checkbox = self.checkboxqtotal.isChecked()
        if checkbox == True:
            VigacomqTotal = VigaQtotal()
            widget.addWidget(VigacomqTotal)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            self.error.setText("Defina algum parametro!")
            
            
class VigaQtotal(QDialog):
    def __init__(self):
        super(VigaQtotal, self).__init__()
        loadUi("vigacomcargatotal.ui", self)
        widget.setFixedHeight(500)
        widget.setFixedWidth(400)
        self.bresultado.clicked.connect(self.calcularR)
        
    def calcularR(self):
        #Concreto e Aço
        concretobox = float(self.cboxconcreto.currentText())
        fcd= ((concretobox)/10)/1.4
        acobox= float(self.cboxaco.currentText())
        fyd= ((acobox*10)/10)/1.15
        
        #Outras entry
        qextraget= self.cargaextra.text()
        cvigaget= self.comprimentoviga.text()
        hget= self.hviga.text()
        bwget= self.bwviga.text()
        cget= self.cobrimento.text()
        
        if len(qextraget) == 0 or len(cvigaget) == 0 or len(hget) == 0 or len(bwget) == 0 or len(cget) == 0:
            self.error.setText("Preencha todos os campos!")
        else:
            qextra= float(qextraget)
            cviga= float(cvigaget)
            h= float(hget)
            bw= float(bwget)
            c= float(cget)
            
            #calcular
            pp = 25*((h/100)*(bw/100))
            q = qextra+pp
            mk = (q*cviga**2)/8
            md = mk*1.4*100
            d = h - c
            x = 1.25*d*(1-(math.sqrt((1-(md/(0.425*bw*(d**2)*fcd))))))
            ass = (md/((d-0.4*x)*(fyd)))
            
            #resultado
            self.resultado.setText("As = "+str(round(ass,2)))





#main
App = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(450)
widget.setFixedWidth(300)
widget.show()
try:
    sys.exit(App.exec())
except:
    print("Exiting")