import os
import sys
from indic_transliteration import sanscript
from indic_transliteration import detect
from indic_transliteration.sanscript import transliterate


def convert(txt,source,target):
    coverted=transliterate(txt,source,target)
    print("Converted ",txt," to ",coverted)


sys.stdout=open("output.txt","w", encoding="utf-8")

print(detect.detect("Raj kumar"))
print(detect.detect("राजकुमार"))
convert("Rajkumar",sanscript.ITRANS,sanscript.DEVANAGARI)
convert("Raj kumar",sanscript.ITRANS,sanscript.DEVANAGARI)
convert("Kamalnath",sanscript.ITRANS,sanscript.DEVANAGARI)
convert("Kamal nath",sanscript.ITRANS,sanscript.DEVANAGARI)
convert("kaise ho",sanscript.ITRANS,sanscript.DEVANAGARI)


convert("राजकुमार",sanscript.DEVANAGARI,sanscript.ITRANS) 
convert("राज कुमार",sanscript.DEVANAGARI,sanscript.ITRANS) 
convert("कमलनाथ",sanscript.DEVANAGARI,sanscript.ITRANS) 
convert("कमल नाथ",sanscript.DEVANAGARI,sanscript.ITRANS) 

sys.stdout.close()