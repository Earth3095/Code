"""ทดสอบความเข้าใจภาษาไทย"""
import asyncio
from core.unlimited_engine import UnlimitedAIEngine

async def test_thai():
    ai = UnlimitedAIEngine()
    
    tests = [
        # ง่าย
        "สร้างฟังก์ชันบวกเลข",
        "เขียนโค้ดพิมพ์ hello world",
        
        # กลาง
        "สร้าง calculator มีบวก ลบ คูณ หาร",
        "เขียนฟังก์ชันเช็คว่าเลขเป็น prime หรือเปล่า",
        
        # ยาก
        "สร้างระบบจัดการข้อมูลนักเรียน ประกอบด้วย class Student และ class School",
        "เขียน web scraper ดึงข้อมูลจากเว็บไซต์ แล้วเก็บลงdatabase",
    ]
    
    for i, instruction in enumerate(tests, 1):
        print(f"\n{'='*60}")
        print(f"Test {i}: {instruction}")
        print("="*60)
        
        result = await ai.generate_code(instruction)
        
        if result['success']:
            print("✅ สร้างโค้ดได้")
            print(f"Code preview:\n{result['code'][:200]}...")
        else:
            print("❌ ล้มเหลว")

asyncio.run(test_thai())