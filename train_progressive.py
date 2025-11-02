# สร้างไฟล์ train_progressive.py

import asyncio
from core.self_trainer import SelfTrainer

async def main():
    trainer = SelfTrainer()
    
    print("🎓 Progressive Training")
    print("=" * 60)
    
    # Phase 1: Easy (2 ชม.)
    print("\n📚 Phase 1: Easy (2 hours)")
    await trainer.train(2)
    
    # Phase 2: Medium (4 ชม.)
    print("\n📚 Phase 2: Medium (4 hours)")
    await trainer.train(4)
    
    # Phase 3: Hard (6 ชม.)
    print("\n📚 Phase 3: Hard (6 hours)")
    await trainer.train(6)
    
    # Phase 4: Expert (12 ชม.)
    print("\n📚 Phase 4: Expert (12 hours)")
    await trainer.train(12)
    
    print("\n" + "="*60)
    print("🎉 เสร็จ 24 ชั่วโมง!")
    print("="*60)

asyncio.run(main())