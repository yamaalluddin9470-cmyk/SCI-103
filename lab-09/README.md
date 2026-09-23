SCI-103 Physics I - Lab 06 Report
Traveling Wave on a String
 
1. Achievement
ในการทดลองนี้ ได้ศึกษา Traveling Wave บนเส้นเชือกโดยใช้ VPython ในการสร้าง Simulation เพื่อดูการเคลื่อนที่ของคลื่นตามเวลา

ได้เรียนรู้เกี่ยวกับ Amplitude, Wavelength, Frequency, Wave Number, Angular Frequency และ Wave Speed รวมถึงความสัมพันธ์ของค่าต่าง ๆ ที่มีผลต่อการเคลื่อนที่ของคลื่น 

การทดลองนี้ช่วยให้เข้าใจสมการของ Traveling Wave มากขึ้น เพราะสามารถเห็นการเคลื่อนที่ของคลื่นจาก Simulation ได้โดยตรง

2. GlowScript URL
https://www.glowscript.org/#/user/yamaalluddin9470/folder/SIC103-104/program/LAB6

3. Results
ค่าที่ใช้ใน Simulation ตามโจทย์ของอาจารย์คือ

Amplitude A = 1.0 m

Wavelength λ = 4.0 m

Frequency f = 1.0 Hz

String Length L = 20.0 m

จำนวนจุด N = 200 จุด

Time Step dt = 0.02 s 

3.1 สมการ Traveling Wave
สมการที่ใช้ในการจำลองคือ

y(x,t) = A sin(kx - ωt)

สมการนี้แสดงถึงคลื่นไซน์ที่เคลื่อนที่ไปในทิศ +x โดยรูปร่างของคลื่นยังคงเดิมขณะเคลื่อนที่ 

3.2 การคำนวณ Wave Number
Wave Number สามารถหาได้จาก

k = 2π / λ

เมื่อ

λ = 4.0 m

แทนค่า

k = 2π / 4

ดังนั้น

k = 1.57 rad/m

3.3 การคำนวณ Angular Frequency
Angular Frequency สามารถหาได้จาก

ω = 2πf

เมื่อ

f = 1.0 Hz

แทนค่า

ω = 2π(1.0)

ดังนั้น

ω = 6.28 rad/s

3.4 การคำนวณ Wave Speed
Wave Speed สามารถหาได้จาก

v = ω / k

แทนค่า

v = 6.28 / 1.57

ดังนั้น

v = 4.0 m/s

สามารถตรวจสอบได้จากอีกสมการคือ

v = fλ

v = (1.0)(4.0)

ดังนั้น

v = 4.0 m/s

ค่าทั้งสองวิธีให้ผลเท่ากัน ซึ่งสอดคล้องกับความสัมพันธ์ของ Wave Speed, Frequency และ Wavelength]

3.5 การคำนวณ Period
Period สามารถหาได้จาก

T = 1 / f

เมื่อ

f = 1.0 Hz

ดังนั้น

T = 1 / 1.0

T = 1.0 s

แสดงว่าคลื่นใช้เวลา 1.0 วินาทีในการเคลื่อนที่ครบหนึ่งรอบ

3.6 ผลจาก Simulation
จาก Screenshot ของ Simulation เห็นข้อความ "Traveling Wave on a String" และมีเส้นคลื่นสีน้ำเงินลักษณะเป็นคลื่นไซน์

คลื่นมีสันคลื่นและท้องคลื่นเกิดขึ้นต่อเนื่องบนเส้นเชือก และเมื่อรัน Animation รูปแบบของคลื่นจะเคลื่อนที่ไปตามแนวแกน x

จากค่าที่กำหนด Wavelength เท่ากับ 4.0 m และ String Length เท่ากับ 20.0 m จึงสามารถมีช่วงความยาวคลื่นได้ประมาณ

L / λ = 20 / 4

L / λ = 5

ดังนั้น บนเส้นเชือกความยาว 20 m จะมีประมาณ 5 Wavelength ซึ่งสอดคล้องกับจำนวนรอบคลื่นที่เห็นใน Screenshot

รูปที่ 1 ผลการจำลอง Traveling Wave on a String ด้วย VPython

Traveling Wave on a String

4. Discussion
จากการทดลองพบว่า Traveling Wave สามารถเคลื่อนที่ไปตามเส้นเชือกได้โดยรูปแบบของคลื่นยังคงลักษณะเป็นคลื่นไซน์ โดยการเคลื่อนที่ถูกกำหนดด้วยสมการ

y(x,t) = A sin(kx - ωt)

เครื่องหมายลบระหว่าง kx และ ωt แสดงว่าคลื่นเคลื่อนที่ไปในทิศ +x

Amplitude เป็นค่าที่กำหนดขนาดการกระจัดสูงสุดของคลื่น ถ้าเพิ่ม Amplitude คลื่นจะมีสันคลื่นและท้องคลื่นสูงขึ้น แต่ไม่ได้ทำให้ Wavelength เปลี่ยน

Wavelength เป็นระยะของคลื่นหนึ่งรอบ ถ้าเพิ่ม Wavelength ระยะห่างระหว่างสันคลื่นแต่ละจุดก็จะเพิ่มขึ้น

Frequency แสดงจำนวนรอบของคลื่นต่อหนึ่งวินาที หากเพิ่ม Frequency คลื่นจะเคลื่อนที่ผ่านจุดหนึ่งถี่ขึ้น

จากค่าที่ใช้ในการทดลองคือ Frequency 1.0 Hz และ Wavelength 4.0 m สามารถคำนวณ Wave Speed ได้เท่ากับ 4.0 m/s

จาก Simulation ทำให้เห็นพฤติกรรมของ Traveling Wave ได้ชัดเจนกว่าการดูจากสมการเพียงอย่างเดียว เพราะสามารถสังเกตการเปลี่ยนแปลงของคลื่นตามเวลาได้จาก Animation

5. Conclusion
จากการทดลองนี้ ได้ศึกษา Traveling Wave บนเส้นเชือกโดยใช้ VPython ในการสร้าง Simulation และศึกษาความสัมพันธ์ระหว่าง Amplitude, Frequency, Wavelength และ Wave Speed

จากค่าที่กำหนดให้ Amplitude เท่ากับ 1.0 m, Wavelength เท่ากับ 4.0 m และ Frequency เท่ากับ 1.0 Hz สามารถคำนวณ Wave Number ได้ประมาณ 1.57 rad/m และ Angular Frequency ได้ประมาณ 6.28 rad/s

Wave Speed ที่คำนวณได้มีค่าเท่ากับ 4.0 m/s และ Period เท่ากับ 1.0 s

จาก Screenshot เห็นรูปแบบของคลื่นไซน์ประมาณ 5 Wavelength บนเส้นเชือก ซึ่งสอดคล้องกับ String Length 20.0 m และ Wavelength 4.0 m
