import easygui
import shutil
import random

file = easygui.fileopenbox()
extension = file.split(".")[1]
no = random.getrandbits(8)
shutil.copy(file, f"E:/File Jos/Kuliah/Semester 5/Sistem Terdistribusi dan Komputer Paralel/kirimFileSocketProgramming/UDP/fileCopy{no}.{extension}")


