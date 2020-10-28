import os
dosya = open("Şifreler.doc", "w")
    #buradaki "w" dosyanın yazma kipinde oluşturulduğunu gösteriyor.
    # Dosya diye bir değişken oluşturup içine şifreler.doc uzantılı bir dosya yarattık
print("355738", file=dosya)
    #file adlı parametre oluşturup dosya değişkenine atadık ki dosyaya yazsın
dosya.close
    #dosyayı kapadık ki bütün bilgiler yazılsın.
import os
os.getcwd()

#bu kodlar ise dosyanın nerede olduğunu göstermektedir.
