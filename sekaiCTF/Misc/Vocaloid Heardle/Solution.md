# Vocaloid Heardle
**MISC - Well, it’s just too usual to hide a flag in stegano, database, cipher, or server. What if we decide to sing it out instead?**

[**flag.mp3**](https://github.com/plue0709/Write-Up/blob/main/sekaiCTF/Misc/Vocaloid%20Heardle/flag.mp3)

[**vocaloid_heardle.py**](https://github.com/plue0709/Write-Up/blob/main/sekaiCTF/Misc/Vocaloid%20Heardle/vocaloid_heardle.py)

> Tiếp cận

Search tên đề bài, ta hiểu được sơ qua thử thách là trong 1 file mp3 có nhiều đoạn nhạc 2-3s thì ta cần tìm được tên bài hát. Đối với Challenge, trong file .py chương trình sẽ lấy phần từng kí tự của flag trong file flag.txt chuyển thành mã decimal ascii.Từ mã ascii, chương trình dùng mã đó làm ID và lấy trong Album music của SEKAI [json](https://sekai-world.github.io/sekai-master-db-diff/musicVocals.json) bài hát có ID đó, tải file mp3 về, cắt 3s đầu và ghép tạo thành file flag.mp3

<img width="359" alt="image" src="https://user-images.githubusercontent.com/80806913/193755359-5e64838f-03b2-4dc7-9d27-1442a274dbee.png">


> Hướng giải quyết

Tạo file flag.txt với flag chứa các kí tự trong bảng ascii: **SEKAI{!"#$%&'()+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^abcdefghijklmnopqrstuvwxyz{|}~}**

Tải tất cả bài hát về bằng code đề cho sử dùng file flag.txt ở trên, nghe file flag.mp3 và check từng file đã tải :)

Ta được đoạn: **118 48 67 97 108 111 73 100 60 51 117** sử dụng [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Decimal('Space',false)&input=MTE4IDQ4IDY3IDk3IDEwOCAxMTEgNzMgMTAwIDYwIDUxIDExNw) convert ta được flag

## Flag: `SEKAI{v0CaloId<3u}`
