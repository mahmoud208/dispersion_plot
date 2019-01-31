# -*-coding:UTF-8-*- 
import codecs 
import nltk
#import numpy, matplotlib
from nltk.draw.dispersion import dispersion_plot
text=codecs.open('quranic.txt','r','utf-8')
text4=text.read()
text.close()
#text4=nltk.Text(text4)
text4=text4.split()
#text4=u"بسم الله الرحمن الرحيم"
dispersion_plot(text4,["LEM:{ll~ah"] )
