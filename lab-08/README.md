SCI-103 Physics I - Lab 05 Report
Simple Harmonic Motion using VPython
 
1. Achievement
ในการทดลองนี้ ได้ศึกษา Simple Harmonic Motion หรือ SHM ของระบบมวลและสปริง โดยใช้ VPython ในการสร้าง Simulation เพื่อสังเกตการเปลี่ยนแปลงของ Displacement, Velocity และ Energy ตามเวลา

ได้เรียนรู้การใช้ Hooke's Law เพื่อหาแรงและ Acceleration ของมวล รวมถึงการใช้ Euler-Cromer ในการคำนวณการเคลื่อนที่ของมวลในแต่ละช่วงเวลา

นอกจากนี้ยังได้ศึกษาการเปลี่ยนแปลงระหว่าง Kinetic Energy และ Potential Energy และสังเกตว่า Total Energy ของระบบมีค่าเกือบคงที่ตลอดการเคลื่อนที่ ซึ่งเป็นลักษณะของ SHM แบบอุดมคติ 

2. GlowScript URL
https://www.glowscript.org/#/user/yamaalluddin9470/folder/SIC103-104/program/lab6

3. Results
ค่าที่ใช้ในการ Simulation คือ

Mass m = 0.5 kg

Spring Constant k = 20.0 N/m

Initial Displacement x0 = -0.3 m

Initial Velocity v0 = 0 m/s

Time Step dt = 0.001 s

Simulation Time = 10 s

3.1 การคำนวณ Angular Frequency
Angular Frequency สามารถหาได้จาก

ω = sqrt(k / m)

แทนค่า

ω = sqrt(20 / 0.5)

ω = sqrt(40)

ดังนั้น

ω = 6.32 rad/s

3.2 การคำนวณ Period
Period สามารถหาได้จาก

T = 2π / ω

แทนค่า

T = 2π / 6.32

ดังนั้น

T = 0.99 s

แสดงว่ามวลใช้เวลาประมาณ 0.99 วินาทีในการสั่นครบหนึ่งรอบ

3.3 การคำนวณ Acceleration เริ่มต้น
Acceleration ของระบบหาได้จาก

a = -(k / m)x

แทนค่า

a = -(20 / 0.5)(-0.3)

ดังนั้น

a = 12.0 m/s²

Acceleration มีทิศเข้าหาตำแหน่งสมดุล

3.4 การคำนวณ Maximum Velocity
Maximum Velocity ของ SHM หาได้จาก

vmax = Aω

โดย Amplitude A = 0.3 m

แทนค่า

vmax = (0.3)(6.32)

ดังนั้น

vmax = 1.90 m/s

ค่าที่ได้สอดคล้องกับกราฟ Velocity ใน Simulation ซึ่งมีค่าสูงสุดประมาณ 1.9 m/s

3.5 การคำนวณ Total Energy
เมื่อเริ่มต้น Velocity เท่ากับ 0 พลังงานของระบบจะอยู่ในรูป Potential Energy

Total Energy สามารถหาได้จาก

E = 1/2 kA²

แทนค่า

E = 1/2 (20)(0.3)²

E = 0.90 J

ดังนั้น

Total Energy = 0.90 J

ค่าที่คำนวณได้สอดคล้องกับเส้น Total Energy สีดำในกราฟ ซึ่งอยู่ใกล้ 0.9 J ตลอดการ Simulation

3.6 ผลจาก Simulation
จาก Simulation สามารถเห็นมวลสีแดงต่ออยู่กับสปริงในแนวดิ่ง และมวลเกิดการสั่นขึ้นลงตามเวลา

กราฟ Displacement และ Velocity แสดงการเปลี่ยนแปลงแบบเป็นคาบ โดย Displacement สีน้ำเงินมีค่าประมาณ -0.3 ถึง 0.3 m ส่วน Velocity สีแดงมีค่าประมาณ -1.9 ถึง 1.9 m/s

จากกราฟจะเห็นว่า Displacement และ Velocity ไม่ได้มีค่าสูงสุดพร้อมกัน เมื่อ Displacement มีค่ามากที่สุด Velocity จะมีค่าใกล้ 0 และเมื่อมวลเคลื่อนที่ผ่านตำแหน่งสมดุล Velocity จะมีขนาดสูงสุด

กราฟ Energy แสดง Kinetic Energy สีส้ม Potential Energy สีเขียว และ Total Energy สีดำ

Kinetic Energy และ Potential Energy มีการเพิ่มและลดสลับกัน ส่วน Total Energy อยู่ใกล้ 0.9 J และเกือบคงที่ตลอดช่วงเวลา 10 s

รูปที่ 1 ผลการจำลอง Simple Harmonic Motion และกราฟ Displacement, Velocity และ Energy

Simple Harmonic Motion (SHM)

4. Discussion
จากการทดลองพบว่า มวลที่ติดอยู่กับสปริงจะเคลื่อนที่กลับไปกลับมารอบตำแหน่งสมดุล เมื่อมวลเคลื่อนออกจากตำแหน่งสมดุล สปริงจะสร้างแรงดึงกลับในทิศตรงข้ามกับ Displacement

Acceleration สามารถหาได้จาก

a = -(k / m)x

เครื่องหมายลบแสดงว่า Acceleration มีทิศเข้าหาตำแหน่งสมดุลเสมอ ซึ่งเป็นลักษณะสำคัญของ SHM

จากกราฟ Displacement และ Velocity พบว่าทั้งสองค่าเปลี่ยนแปลงเป็นคาบ แต่ไม่ได้มีค่าสูงสุดในเวลาเดียวกัน

เมื่อมวลอยู่ที่ตำแหน่งที่มี Displacement สูงสุด Velocity จะมีค่าใกล้ 0 เนื่องจากมวลกำลังเปลี่ยนทิศการเคลื่อนที่

เมื่อมวลเคลื่อนที่ผ่านตำแหน่งสมดุล Displacement จะมีค่าใกล้ 0 แต่ Velocity จะมีขนาดสูงสุด

จากกราฟ Energy พบว่า Kinetic Energy และ Potential Energy เปลี่ยนแปลงสลับกัน เมื่อมวลเคลื่อนที่ผ่านตำแหน่งสมดุล Kinetic Energy จะมีค่ามาก ส่วน Potential Energy จะมีค่าน้อย

เมื่อมวลอยู่ที่ตำแหน่งปลายสุดของการสั่น Potential Energy จะมีค่ามาก ส่วน Kinetic Energy จะมีค่าใกล้ 0

Total Energy อยู่ใกล้ 0.9 J ตลอดการ Simulation แสดงให้เห็นว่าพลังงานไม่ได้หายไป แต่มีการเปลี่ยนรูปไปมาระหว่าง Kinetic Energy และ Potential Energy

ผลจาก Simulation จึงสอดคล้องกับพฤติกรรมของ Simple Harmonic Motion และหลักการอนุรักษ์พลังงาน

5. Conclusion
จากการทดลองนี้ ได้ศึกษา Simple Harmonic Motion ของระบบมวลและสปริงโดยใช้ VPython และวิธี Euler-Cromer ในการคำนวณการเคลื่อนที่

จากค่า Mass เท่ากับ 0.5 kg และ Spring Constant เท่ากับ 20 N/m สามารถคำนวณ Angular Frequency ได้ประมาณ 6.32 rad/s และ Period ประมาณ 0.99 s

เมื่อ Amplitude เท่ากับ 0.3 m สามารถคำนวณ Maximum Velocity ได้ประมาณ 1.90 m/s และ Total Energy ของระบบได้ประมาณ 0.90 J

ผลจาก Simulation แสดงให้เห็นว่า Displacement และ Velocity เปลี่ยนแปลงเป็นคาบ ส่วน Kinetic Energy และ Potential Energy มีการเปลี่ยนแปลงสลับกัน โดย Total Energy มีค่าเกือบคงที่

โดยรวมแล้ว การทดลองนี้ช่วยให้เข้าใจ Simple Harmonic Motion ความสัมพันธ์ระหว่าง Displacement และ Velocity รวมถึงการเปลี่ยนแปลงของพลังงานในระบบมวลและสปริงได้ชัดเจนมากขึ้น
