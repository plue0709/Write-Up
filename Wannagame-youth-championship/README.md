# Wanna.W^n

# Challenge: King of Stegano

Đề cho 2 file: **Chall.png và CrackMe.zip**

Như mọi bài stegano file Chall.png sẽ không mở được, mở bằng Hxd ta được: 

![image](https://user-images.githubusercontent.com/80806913/170880708-deecac91-8e6a-441d-a881-e2016d5731d0.png)

Tham khảo: https://commons.wikimedia.org/wiki/File:Hex_editor_with_text_aliasing.png để biết thêm về mã hex của file png 

Có vẻ file thiếu signature của một file png: **89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52**.Ban đầu mình bị stuck khá lâu vì mình thay dòng đầu tiên bằng signature chứ không ghi thêm vào file, nên check bằng **pngcheck** cũng bị lỗi, sau thì mình mới thêm signature đó vào file thay vì ghi đè lên file. Nó như thế này: 

![image](https://user-images.githubusercontent.com/80806913/170881294-88ee03bb-98d6-4742-bac4-1ee33adc12bc.png)

Check cuối file thì cũng thiếu signature cuối file: **00 00 00 00 49 45 4E 44 AE 42 60 82**. Bổ sung vào thì ta được một file ảnh hoàn chỉnh

Sử dụng công cụ pngcheck: https://github.com/sherlly/PCRT để kiểm tra file png có bị lỗi không.

![image](https://user-images.githubusercontent.com/80806913/170885297-0df6415a-b28c-44ea-8862-df4976104232.png)

Mở ảnh xem có gì:

![image](https://user-images.githubusercontent.com/80806913/170885358-93a6d5b4-17d0-420d-a709-86935d1d408f.png)

exiftool hay binwalk thì dĩ nhiên sẽ chẳng có gì, bỏ lên: https://aperisolve.fr/ cũng không phát hiên thêm gì

Sử dụng appa: https://github.com/csisl/appa công cụ tìm data ẩn trong một tấm png và được kết quả **W1-Y0u-4r3** có vẻ là 1 phần của flag

![image](https://user-images.githubusercontent.com/80806913/170885926-7d65a299-d154-46b0-b166-9bc01c91d9d5.png)

Có vẻ đến lúc đụng vào file **CrackMe.zip**

mở file ra thì thấy file chứa 1 file Chall.png và một folder chưa flag.txt
![image](https://user-images.githubusercontent.com/80806913/170885998-d07734c1-ac3b-499e-b6d9-726b2da930c4.png)

Chắc chắn zip2john sẽ vô dụng. Sau một lúc xem hint và tìm thì mình phát hiện hai file Chall.png trong file zip và file ảnh là như nhau.
Có một tool có thể mở được file zip khi có được một file trong đó là **pkcrack: https://github.com/keyunluo/pkcrack**. 
Mình sẽ lấy tấm ảnh đã phục hồi tạo thành file zip trên linux (vì làm trên windows không được) rồi dùng pkcrack ghi dữ liệu vào một file zip mới (ở đây là cracked.zip) mở ra và xem

![image](https://user-images.githubusercontent.com/80806913/170886397-b580b558-5c6c-40db-9b4b-f62a6593eda2.png)

![image](https://user-images.githubusercontent.com/80806913/170886207-25c23920-30ba-4f12-90bc-aa086c3c09ea.png)

![image](https://user-images.githubusercontent.com/80806913/170886263-b2fd8289-0118-461f-8f74-74b20bfcc35f.png)

Tìm được phần còn lại của flag: **-K1ng-0f-F0r3ns1cs**

flag: **W1{Y0u-4r3-K1ng-0f-F0r3ns1cs}**
