"""
Long Training Script
ฝึก AI ระยะยาว
"""

import asyncio
from core.self_trainer import SelfTrainer

async def main():
    trainer = SelfTrainer()
    
    print("="*60)
    print("🎓 LONG TRAINING MODE")
    print("="*60)
    print()
    
    # รับ input
    hours = float(input("ฝึกกี่ชั่วโมง? (เช่น 0.1, 1, 24): "))
    
    print()
    print("⚠️  สิ่งที่ต้องรู้:")
    print(f"   - จะฝึก {hours} ชั่วโมง")
    print("   - คอมต้องเปิดตลอด")
    print("   - ไม่ต้องปิดหน้าจอก็ได้")
    print("   - กด Ctrl+C เพื่อหยุดก่อนเวลา")
    print()
    
    confirm = input("พร้อม? (y/n): ").strip().lower()
    
    if confirm == 'y':
        print("\n🚀 เริ่มฝึก!\n")
        stats = await trainer.train(duration_hours=hours)
        print("\n🎉 เสร็จแล้ว!")
    else:
        print("\n❌ ยกเลิก")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  หยุดโดยผู้ใช้ (Ctrl+C)")
        print("💾 ความคืบหน้าที่บันทึกไว้ยังอยู่")