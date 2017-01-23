import time
import webbrowser

count=0
total_count=1

print ("Start time : "+ time.ctime())
while count<total_count:
    time.sleep(5)
    webbrowser.open_new("https://www.youtube.com/watch?v=PT2_F-1esPk")
    count+=1