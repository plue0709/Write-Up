# Appnote.txt
![image](https://user-images.githubusercontent.com/80806913/177124451-6342904c-9408-4195-8806-00bd4ccc1281.png)

Giải nén File tải về, nhận được thêm một File dump.zip, giải nén dump.zip được file **hello.txt**

![image](https://user-images.githubusercontent.com/80806913/177124987-5f86f3d4-dc7e-4b28-9e89-4647cd4b260f.png)

Có vẻ file txt không thể khai thác được gì, chỉ còn lại file **dump.zip**, thử strings dump.zip thì

![image](https://user-images.githubusercontent.com/80806913/177125537-6c130cfd-4866-4519-b184-5e4295346f60.png)

Mở file dump.zip bằng HxD, xem một lượt thì tìm thấy rất nhiều signature của file zip(**50 4B 03 04**), và đi kèm với đó mỗi signature là **flag** + số + một chữ cái trong bảng chữ cái như hình trên, nếu lọc ra thì sẽ nhận được 19 lần chuỗi: **abcdefghijklmnopqrstuvwxyzCTF{0137}_**

> Hình dung ban đầu hướng giải quyết

Sẽ lấy từ file dump.zip ra 18 file flag.zip và 1 trong 18 file đó sẽ chứa flag

Nhưng không sau khi thử rất nhiều lần tách ghép dựa theo cấu trúc file zip thì vẫn bị lỗi

![image](https://user-images.githubusercontent.com/80806913/177127335-62850ad5-fad0-4b4b-8ef2-7d59d7ac0cfc.png)

Tài liệu về cấu trúc file zip

![unknown](https://user-images.githubusercontent.com/80806913/177125981-5d0f51d2-56fb-4bb7-ae52-3dc774a24d20.png)

>Quay lại xem cấu trúc file dump.zip

Kiểm tra 4 bytes bắt đầu(**50 4b 03 04**) của file dump.zip nhận được 686 kết quả

Kiểm tra 4 bytes giữa (**50 4b 01 02**)của file cũng nhận được 686 kết quả

Nhưng kiểm tra 4 bytes cuối(**50 4b 05 06**) thì chỉ nhận được 21 kết quả
![image](https://user-images.githubusercontent.com/80806913/177128356-25c87d11-7bec-466f-95a4-c7e81c1b0137.png)

Có thể giải thích có 686 kết quả = 36x19 + 2, 36 là 36 ký tự  **abcdefghijklmnopqrstuvwxyzCTF{0137}_** 2 là 2 file **hello.txt** và **hi.txt**

>Ngầm suy đoán flag có 19 ký tự, mỗi ký tự lấy trong **abcdefghijklmnopqrstuvwxyzCTF{0137}_**

Ở phần **END OF CENTRAL DIRECTORY** có các bytes chứa offset bắt đầu của **central directory**

Ví dụ như **50 4B 05 06 00 00 00 00 01 00 01 00 5A E4 00 00 88 0A 00 00 A2 01** thì **0A 88** là offset bắt đầu (little endian), có 21 vị trí offset như thế, mình thử tìm với một vài offset đầu thì thấy chữ cái đi kèm với signature của file mình nói ở đầu tạo ra CTF{

![image](https://user-images.githubusercontent.com/80806913/177129513-04aecc81-6ff5-499f-ab42-e9435a5a1c95.png)
![image](https://user-images.githubusercontent.com/80806913/177129597-c51726f0-f5ad-433b-aed2-b505f6582ca7.png)
![image](https://user-images.githubusercontent.com/80806913/177129659-804fcf41-f6f1-4af4-a081-90fff880b33e.png)
![image](https://user-images.githubusercontent.com/80806913/177129708-268798f6-3fd7-4a1f-b2dd-19a482a60014.png)

Đến đây thì đã rõ cách tìm ra flag, mình lọc lấy 21 offset và tìm offset để lấy từng chữ cái của flag 

![image](https://user-images.githubusercontent.com/80806913/177130079-36888d17-6ea4-46c2-997a-e9b22c042c05.png)

**CTF{p0s7m0d3rn_z1p}**






