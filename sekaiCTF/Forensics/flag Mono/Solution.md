# flag Mono
**Forensics - When writing the assignment, Miku used a font called flag Mono. Despite it looking just like a regular monospaced font, it claims itself to be “stylistic” in various ways.**

**“Perhaps there’s something special about it”, Miku thought.**

[Assignment-broken.xps](https://github.com/plue0709/Write-Up/blob/main/sekaiCTF/Forensics/Broken%20Converter/Assignment-broken.xps)

Nối tiếp bài [Broken Converter](https://github.com/plue0709/Write-Up/blob/main/sekaiCTF/Forensics/Broken%20Converter/Solution.md). 

Theo [tài liệu Microsoft](https://learn.microsoft.com/en-us/typography/opentype/spec/features_pt#ssxx) về font file, một file có nhiều style set, có nhiều bộ ký tự với từng tập hợp glyph, và ở [web](https://fontdrop.info/) cũng có phân tích các style set này. 

Trước hết, khi type "**flag**" thì font flag Mono sẽ chuyển thành "**Q^<U**" từ "**Q^<U**" chuyển qua 4 style set khác ta sẽ get được flag:

![image](https://user-images.githubusercontent.com/80806913/193761924-c9da63cf-afa1-434c-bba3-099b842c2838.png)

![image](https://user-images.githubusercontent.com/80806913/193761973-e4cc2a2b-5a33-451e-9bfe-8fb9f192533b.png)

![image](https://user-images.githubusercontent.com/80806913/193762006-8d1890bd-07e5-41f6-935a-74e7bd967930.png)

![image](https://user-images.githubusercontent.com/80806913/193762040-c2252197-a01a-416d-9573-2f09a77939c7.png)

## Flag: `SEKAI{OpenTypeMagicGSUBIsTuringComplete}`
