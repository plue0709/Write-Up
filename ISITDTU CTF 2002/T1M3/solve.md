### T1M3

![image](https://user-images.githubusercontent.com/80806913/202464987-950ac990-097f-47ea-aa14-98bb3e74b8b9.png)

Đề cung cấp 1 file pcap, sau khi đọc qua stream tcp và data của các gói tin thì biết được gói tin chứa các lệnh SQL mà hacker thực hiện để tấn cống server

Đầu tiên mình sẽ lọc để lấy data chỉ các câu lệnh SQL ra sử dụng **export packet dissections** để lọc

![image](https://user-images.githubusercontent.com/80806913/202465794-1b6cefe9-7fc0-4d38-ad0e-d07b85b5a298.png)

![image](https://user-images.githubusercontent.com/80806913/202466022-22cb43da-f90c-436e-bb9e-63b90bad49f1.png)

Ta sẽ được file như trên, lướt đọc các câu lệnh, ta thấy đến mộc đoạn các câu lệnh chứa "!=" và sau đó là 1 mã ascii của 1 ký tự. lấy mã ascii đi decode ta được flag

![image](https://user-images.githubusercontent.com/80806913/202467458-43adb2ef-c485-488b-a995-32cfde8780c7.png)

**flag: ISITDTU{W3llC0M3_T0_ISITDTU_2@22}**
