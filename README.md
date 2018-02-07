# pyinstaller-tkinter-

## problem ##  
if you use tkinter as GUI ,you run pyinstall with your .py 
errorcode : counld't found .ico file

solution:
1. use binary open your icon.ico  
2. base64 encode  
3. save file in icon.py  


## ico2base ##  
```python  
import base64
open_icon = open("Mushroom.ico","rb")  # your ico img
b64str = base64.b64encode(open_icon.read())
open_icon.close()
write_data = ("img = %s" % b64str)
f = open("icon.py","w+")
f.write(write_data)
f.close()
```  

## tkinter with pyinstaller ##
```python  
root = Tk()
my_gui = GUI(root)
tmp = open("temp.ico","wb+")
tmp.write(base64.b64decode(img))
tmp.close()
root.iconbitmap("temp.ico")
os.remove("temp.ico")
root.mainloop()

```  
## console ##
```  
pyinstaller tkinter_with_pyinstaller.py -F  
```
ref http://blog.csdn.net/lion_cui/article/details/51329497  very thanks


