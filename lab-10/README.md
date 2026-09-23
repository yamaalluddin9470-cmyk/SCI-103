SCI-103 Physics I - Lab 7 Report
Reflection and Interference of Waves
1. Achievement
ในการทดลองนี้ ได้ศึกษาการสะท้อนและการแทรกสอดของคลื่นบนเส้นเชือก โดยใช้ VPython ในการสร้างแบบจำลองเพื่อสังเกตพฤติกรรมของคลื่นให้ชัดเจนมากขึ้น

ได้เรียนรู้เกี่ยวกับ Incident Wave ซึ่งเป็นคลื่นที่เคลื่อนที่เข้าหาขอบเขต และ Reflected Wave ซึ่งเป็นคลื่นที่สะท้อนกลับเมื่อคลื่นเคลื่อนที่ถึง Fixed Boundary

นอกจากนี้ ยังได้ศึกษาหลักการ Superposition ซึ่งอธิบายว่า เมื่อคลื่นสองคลื่นมาซ้อนทับกัน การกระจัดรวมสามารถหาได้จากผลรวมของการกระจัดของคลื่นทั้งสอง ทำให้เกิด Constructive Interference และ Destructive Interference

การทดลองนี้ช่วยให้เข้าใจเรื่องการสะท้อน การแทรกสอด และการเกิด Standing Wave ได้มากขึ้น รวมทั้งได้ฝึกใช้ VPython ในการจำลองปรากฏการณ์ทางฟิสิกส์

2. GlowScript URL
URL:https://www.glowscript.org/#/user/yamaalluddin9470/folder/SIC103-104/program/lab7

3. Results
ในการจำลองกำหนดค่าต่าง ๆ ดังนี้

Amplitude A = 1.0 m

ความยาวของเส้นเชือก L = 20.0 m

Frequency f = 1.0 Hz

Wavelength λ = 10.0 m

จำนวนจุด N = 200 จุด

3.1 การคำนวณ Wave Number
สามารถคำนวณ Wave Number ได้จาก

k = 2π / λ

แทนค่า

λ = 10.0 m

k = 2π / 10

ดังนั้น

k = 0.628 rad/m

3.2 การคำนวณ Angular Frequency
สามารถคำนวณ Angular Frequency ได้จาก

ω = 2πf

แทนค่า

f = 1.0 Hz

ω = 2π(1.0)

ดังนั้น

ω = 6.283 rad/s

3.3 การคำนวณ Wave Speed
สามารถคำนวณ Wave Speed ได้จาก

v = fλ

แทนค่า

v = (1.0)(10.0)

ดังนั้น

v = 10.0 m/s

3.4 สมการของคลื่น
สมการ Incident Wave คือ

yi(x,t) = A sin(kx - ωt)

สมการ Reflected Wave คือ

yr(x,t) = -A sin(kx + ωt)

เครื่องหมายลบในสมการ Reflected Wave แสดงถึงการกลับเฟสของคลื่นเมื่อเกิดการสะท้อนที่ Fixed Boundary

จากหลักการ Superposition การกระจัดรวมสามารถคำนวณได้จาก

y(x,t) = yi(x,t) + yr(x,t)

เมื่อนำ Incident Wave และ Reflected Wave มารวมกัน จะทำให้เกิด Interference

3.5 ผลจาก Simulation
จากการรันโปรแกรม VPython สามารถสังเกตเห็นเส้นคลื่นสีน้ำเงินอยู่ระหว่างขอบเขตสีแดงสองด้าน โดยเส้นคลื่นมีลักษณะเป็นคลื่นไซน์ ประกอบด้วยสันคลื่นและท้องคลื่นต่อเนื่องตลอดเส้นเชือก

รูปของคลื่นจะเปลี่ยนไปตามเวลา เนื่องจากโปรแกรมเป็น Animation ดังนั้น Screenshot จะแสดงพฤติกรรมของคลื่นเพียงช่วงเวลาหนึ่งเท่านั้น

Reflection and Interference of Waves

รูปที่ 1 ผลการจำลอง Reflection and Interference of Waves ด้วย VPython

4. Discussion
เมื่อคลื่นเคลื่อนที่ไปตามเส้นเชือกและเดินทางถึง Fixed Boundary คลื่นจะเกิดการสะท้อนกลับ โดย Reflected Wave จะมีการกลับเฟสเมื่อเทียบกับ Incident Wave

เมื่อ Incident Wave และ Reflected Wave เคลื่อนที่ผ่านบริเวณเดียวกัน จะเกิดการซ้อนทับกันตามหลัก Superposition โดยการกระจัดรวมสามารถเขียนได้เป็น

y = yi + yr

ถ้าคลื่นทั้งสองซ้อนทับกันในลักษณะที่เสริมกัน จะเกิด Constructive Interference ทำให้การกระจัดรวมเพิ่มขึ้น

แต่ถ้าคลื่นทั้งสองซ้อนทับกันในลักษณะที่หักล้างกัน จะเกิด Destructive Interference ทำให้การกระจัดรวมลดลง หรืออาจมีค่าเป็นศูนย์

การซ้อนทับระหว่าง Incident Wave และ Reflected Wave สามารถทำให้เกิด Standing Wave ซึ่งประกอบด้วย Node และ Antinode

Node คือตำแหน่งที่การกระจัดของคลื่นเป็นศูนย์ ส่วน Antinode คือตำแหน่งที่มีการกระจัดสูงสุด

4.1 ระยะห่างระหว่าง Node
กำหนดให้

λ = 10.0 m

ระยะห่างระหว่าง Node ที่อยู่ติดกันคือ

λ / 2

แทนค่า

10.0 / 2 = 5.0 m

ดังนั้น

ระยะห่างระหว่าง Node = 5.0 m

4.2 ระยะห่างระหว่าง Node และ Antinode
ระยะห่างระหว่าง Node กับ Antinode ที่อยู่ใกล้ที่สุดคือ

λ / 4

แทนค่า

10.0 / 4 = 2.5 m

ดังนั้น

ระยะห่างระหว่าง Node และ Antinode = 2.5 m

4.3 การคำนวณ Period
สามารถคำนวณ Period ได้จาก

T = 1 / f

เมื่อ

f = 1.0 Hz

แทนค่า

T = 1 / 1.0

ดังนั้น

T = 1.0 s

แสดงว่าคลื่นใช้เวลา 1.0 วินาทีในการสั่นครบ 1 รอบ

4.4 ผลของการเปลี่ยน Parameter
จากการทดลอง ถ้าเพิ่ม Amplitude ขนาดการกระจัดของคลื่นจะเพิ่มขึ้น ทำให้คลื่นมีขนาดใหญ่ขึ้น

ถ้าเปลี่ยน Wavelength ระยะห่างระหว่าง Node และ Antinode ก็จะเปลี่ยนตามไปด้วย

ส่วนการเปลี่ยน Frequency จะส่งผลต่อความเร็วในการสั่นของคลื่น หาก Frequency สูงขึ้น คลื่นก็จะสั่นเร็วขึ้น

ข้อจำกัดของ Simulation นี้คือเป็นการจำลองเส้นเชือกในอุดมคติ จึงไม่ได้รวมปัจจัยบางอย่างที่เกิดขึ้นในระบบจริง เช่น Damping และการสูญเสียพลังงาน

นอกจากนี้ Screenshot เป็นเพียงภาพในช่วงเวลาหนึ่งของ Animation ดังนั้นการสังเกต Reflection และ Interference จะเห็นได้ชัดเจนกว่าจากการรัน Simulation ต่อเนื่อง

5. Conclusion
จากการทดลองนี้ ได้ศึกษาการสะท้อนและการแทรกสอดของคลื่นโดยใช้ VPython ในการจำลองการเคลื่อนที่ของคลื่นบนเส้นเชือก โดยนำ Incident Wave และ Reflected Wave มาซ้อนทับกันตามหลัก Superposition

ค่าที่ใช้ในการทดลองคือ

Amplitude = 1.0 m

Frequency = 1.0 Hz

Wavelength = 10.0 m

จากค่าที่กำหนด สามารถคำนวณ Wave Number ได้

k = 0.628 rad/m

Angular Frequency ได้

ω = 6.283 rad/s

และ Wave Speed ได้

v = 10.0 m/s

นอกจากนี้ เมื่อ Wavelength เท่ากับ 10.0 m สามารถคำนวณระยะห่างระหว่าง Node ที่อยู่ติดกันได้ 5.0 m และระยะห่างระหว่าง Node กับ Antinode ที่อยู่ใกล้ที่สุดได้ 2.5 m

โดยรวมแล้ว การทดลองนี้ช่วยให้เข้าใจเรื่อง Reflection, Interference, Superposition, Node, Antinode และ Standing Wave ได้ชัดเจนมากขึ้น รวมทั้งได้ฝึกใช้ VPython ในการจำลองคลื่น

Post-Lab Questions
 
1. What happens to the phase of a wave when it reflects from a fixed boundary?
เมื่อคลื่นสะท้อนจาก Fixed Boundary คลื่นจะกลับเฟส 180 องศา

2. How do constructive and destructive interference differ?
Constructive Interference คือคลื่นเสริมกัน ทำให้คลื่นรวมมีขนาดมากขึ้น ส่วน Destructive Interference คือคลื่นหักล้างกัน ทำให้คลื่นรวมมีขนาดลดลง

 
3. If the boundary were free (not fixed), how would the reflected wave change?
ถ้าเป็น Free Boundary คลื่นจะสะท้อนกลับโดยไม่เกิดการกลับเฟส

4. How many nodes and antinodes would be present if L = 20 m and λ = 10 m?
มี Node 5 จุด และ Antinode 4 จุด

5. How does interference explain resonance in musical instruments?
คลื่นที่สะท้อนกลับมาจะเกิด Interference กันจนเกิด Standing Wave และเมื่อความถี่ตรงกับความถี่ธรรมชาติ จะเกิด Resonance ทำให้เสียงดังและชัดขึ้น


