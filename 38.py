import time
from datetime import timedelta

class QuizSystem:
    def __init__(self):
        # คลังข้อสอบ
        self.quizzes = {
            "ชีววิทยา": [
                {
                    "question": "1. ออร์แกเนลล์ใดทำหน้าที่เปรียบเสมือนโรงงานไฟฟ้าของเซลล์?",
                    "choices": ["1. ไรโบโซม", "2. ไมโทคอนเดรีย", "3. กอลจิบอดี", "4. ไลโซโซม"],
                    "answer": 2
                },
                {
                    "question": "2. เบสใดที่พบใน RNA แต่ไม่พบใน DNA?",
                    "choices": ["1. อะดีนีน (A)", "2. ไทมีน (T)", "3. ยูราซิล (U)", "4. กวานีน (G)"],
                    "answer": 3
                }
            ],
            "เคมี": [
                {
                    "question": "1. พันธะที่เกิดจากการใช้อิเล็กตรอนร่วมกันของธาตุอโลหะคือพันธะใด?",
                    "choices": ["1. พันธะไอออนิก", "2. พันธะโคเวเลนต์", "3. พันธะโลหะ", "4. พันธะไฮโดรเจน"],
                    "answer": 2
                },
                {
                    "question": "2. สารที่มีค่า pH เท่ากับ 3 มีสมบัติเป็นอย่างไร?",
                    "choices": ["1. กรด", "2. เบส", "3. กลาง", "4. เป็นเค็ม"],
                    "answer": 1
                }
            ]
        }
        
        # ประวัติการทำข้อสอบ: { 'ชื่อวิชา': [{'score': x, 'total': y, 'time_sec': z}] }
        self.history = {}

    def take_quiz(self, subject_name):
        """เริ่มทำแบบทดสอบตามชื่อวิชา"""
        if subject_name not in self.quizzes:
            print(f"❌ ไม่พบวิชา '{subject_name}' ในระบบ (วิชาที่มี: {', '.join(self.quizzes.keys())})")
            return

        questions = self.quizzes[subject_name]
        score = 0
        total = len(questions)

        print(f"\n=== เริ่มทำแบบทดสอบวิชา: {subject_name} ===")
        start_time = time.time()

        for q in questions:
            print(f"\n{q['question']}")
            for choice in q['choices']:
                print(f"  {choice}")
            
            try:
                user_ans = int(input("ตอบ (ใส่หมายเลขข้อ 1-4): "))
                if user_ans == q['answer']:
                    print("✅ ถูกต้อง!")
                    score += 1
                else:
                    print(f"❌ ผิด! เฉลยที่ถูกต้องคือข้อ {q['answer']}")
            except ValueError:
                print("❌ กรอกข้อมูลไม่ถูกต้อง ถือว่าตอบผิด")

        end_time = time.time()
        time_spent = round(end_time - start_time, 2)

        # บันทึกลงประวัติ
        if subject_name not in self.history:
            self.history[subject_name] = []
        
        self.history[subject_name].append({
            'score': score,
            'total': total,
            'time_sec': time_spent
        })

        print(f"\n🎉 ทำแบบทดสอบเสร็จสิ้น!")
        print(f"คะแนนที่ได้: {score}/{total} ({(score/total)*100:.1f}%) | เวลาที่ใช้: {time_spent} วินาที")

    def show_stats(self, subject_name):
        """ดูสถิติแยกตามชื่อวิชา"""
        if subject_name not in self.history or not self.history[subject_name]:
            print(f"\n📌 ยังไม่มีประวัติการทำแบบทดสอบวิชา '{subject_name}'")
            return

        records = self.history[subject_name]
        total_attempts = len(records)
        total_score = sum(r['score'] for r in records)
        max_possible = sum(r['total'] for r in records)
        total_time_sec = sum(r['time_sec'] for r in records)
        
        avg_percentage = (total_score / max_possible) * 100
        latest = records[-1]

        print(f"\n📊 === สถิติวิชา: {subject_name} ===")
        print(f"- จำนวนครั้งที่ทำแบบทดสอบ: {total_attempts} ครั้ง")
        print(f"- คะแนนเฉลี่ยสะสม: {avg_percentage:.2f}%")
        print(f"- เวลาที่ใช้รวมทั้งหมด: {str(timedelta(seconds=round(total_time_sec)))}")
        print(f"- ผลการสอบครั้งล่าสุด: {latest['score']}/{latest['total']} ({(latest['score']/latest['total'])*100:.1f}%)")

# --- ตัวอย่างการใช้งานระบบ ---
app = QuizSystem()

# 1. ทำแบบทดสอบวิชาชีววิทยา
app.take_quiz("ชีววิทยา")

# 2. ทำแบบทดสอบวิชาเคมี
app.take_quiz("เคมี")

# 3. ดูสถิติการสอบโดยระบุชื่อวิชา
app.show_stats("ชีววิทยา")
app.show_stats("เคมี")