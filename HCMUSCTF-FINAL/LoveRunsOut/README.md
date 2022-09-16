Challenges File: https://drive.google.com/file/d/1hjj4KVyb948J_YLuNU04psTdIFnh88Rr/view?usp=sharing

Challenges cho một file Windows Memory, yêu cầu tìm **Pid-Name_of_process-Port-Excute_time-IP_and_Port_attacker**

Với dạng memory, ta sử dụng tool volatility 2.6 để phân tích

Check qua thông tin của File Memory 

![image](https://user-images.githubusercontent.com/80806913/173400841-b9259815-3553-4645-803f-2967fad0fb33.png)

Check qua các tiến trình:

![image](https://user-images.githubusercontent.com/80806913/173401162-aae28c84-0abb-4f53-9526-16042c25b845.png)

Để ý ta thấy **nc.exe** là tiến trình đáng nghi trong các tiến trình. PID = 1124

Ta sử dụng plugin connscan để kiểm tra các thông tin liên quan đến PID = 1124. 

![image](https://user-images.githubusercontent.com/80806913/173401460-992aee98-fc64-4d88-ae65-bf45e18ebb6f.png)

Remote address cho ta biết IP và port của Attacker: **1.226.182.38_59495**

Tiếp tục sử dụng plugin Sockets để kiểm tra thông tin kết nối:

![image](https://user-images.githubusercontent.com/80806913/173401790-8077048a-78fe-459c-847f-3ae810c9fd1c.png)

Ở dòng đầu tiên, PID = 1124, ta biết được **port = 80, Excute Time = 2012-11-02 09:06:48**

Từ các thông tin trên ta có flag của challenge:
**HCMUS-CTF{1124_nc.exe_80_Fri-Nov-02-09:06:48-2012_1.226.182.38_59495}**

//Ez game and this is the only Forensics chall i could solve :) 
