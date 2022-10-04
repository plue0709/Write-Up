# Broken Converter
**Forensics - Miku has finally finished her assignment and is ready to submit – but for some reason, the school requires all assignments to be submitted as .xps files. Miku found a converter online and used the converted file for submission. The file looked good at first, but it seems as if there’s something broken in the converter. Can you help her figure out what is wrong?**

[Assignment-broken.xps](https://github.com/plue0709/Write-Up/blob/main/sekaiCTF/Forensics/Broken%20Converter/Assignment-broken.xps)

> Tiếp cận

Mở file bằng **XPS viewer** được vài đoạn text vô nghĩa

![image](https://user-images.githubusercontent.com/80806913/193757390-371ffce2-3701-4f98-bffa-619886b5ccae.png)

Nhưng khi copy các kí tự của đoạn text và paste ra thì lại nhận được các kí tự khác

![image](https://user-images.githubusercontent.com/80806913/193757622-a964267f-2dce-46cf-a78b-319ceb55d459.png)

Có vẻ do font ttf của file

> Hướng giải quyết

Cũng như các file docx hay xlxs, xps thực chất cũng là file nén, sửa đuôi file giải nén ra và tìm kiếm một lúc thì ta thấy file odttf này

![image](https://user-images.githubusercontent.com/80806913/193757912-47831591-6456-4a6c-9f82-9ad0c72be2e2.png)

Theo Google thì odttf:

![image](https://user-images.githubusercontent.com/80806913/193758044-fa0d2508-0bdb-45c5-9212-3b73c7e77cf4.png)

Trước hết cần chuyển odttf thành file ttf để xem file. Sử dụng đoạn code python dưới đây hoặc một số tool trên mạng khác để convert:

```
import os
import sys

fn_in = sys.argv[1]
fn_out = os.path.splitext(sys.argv[1])[0] + '.ttf'
print(fn_out)
# Parse
key = os.path.splitext(os.path.basename(fn_in))[0].replace('-', '')
# Convert to Int reversed
key_int = [int(key[i-2:i], 16) for i in range(32, 0, -2)]

with open(fn_in, 'rb') as fh_in, open(fn_out, 'wb') as fh_out:
	cont = fh_in.read()
	fh_out.write(bytes(b ^ key_int[i % len(key_int)] for i, b in enumerate(cont[:32])))
	fh_out.write(cont[32:])
	
```

Mở file ttf: 

![image](https://user-images.githubusercontent.com/80806913/193758714-8b989b6b-f115-45db-aa5d-2ed15d052eb8.png)

Các ký tự bị xáo trộn rất loạn. Nhưng khi sắp xếp các ký tự lại theo bảng mã Ascii ta được flag. Sử dụng [web](https://fontdrop.info/) để phân tích font.

![image](https://user-images.githubusercontent.com/80806913/193759228-4a496124-f7b7-4b9a-939a-09f8436f4679.png)


## Flag: `SEKAI{sCR4MBLeD_a5ci1-FONT+GlYPHZ,W3|!.d0n&}`
