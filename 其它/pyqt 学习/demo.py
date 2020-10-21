import sys

from PyQt5.QtWidgets import QWidget,QTableWidget

out=sys.stdout

sys.stdout=open(r'E:\QWidget.txt' ,'w')

help( QTableWidget )

sys.stdout.close()

sys.stdout=out