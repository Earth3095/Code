import asyncio
from core.ai_agent import AIComputerAgent

async def main():
    print("👑 Owner: YOU")
    print("⚡ Admin Level: GOD")
    print("🔓 Restrictions: NONE")
    print("🚀 AI Code Generator")
    print("="*50)

    agent = AIComputerAgent()

    while True:
        try:
            task = input("\nพิมพ์คำสั่ง: ").strip()
            if not task:
                continue
            if task.lower() in ["exit", "quit"]:
                print("❌ ออกจากโปรแกรม")
                break

            print(f"\n🎯 ทำงาน: {task}")
            print("⚠️ กด Ctrl+C เพื่อหยุดฉุกเฉิน\n")

            result = await agent.execute_task(task)

            print("="*50)
            print("📊 ผลลัพธ์:")
            print("="*50)
            print(result["output"])  # ใช้ 'output' แทน 'success'
            print(f"\nLanguage: {result['language']}")
            print(f"Owner: {result['owner']}")

        except KeyboardInterrupt:
            print("\n⏹️ หยุดฉุกเฉิน!")
        except Exception as e:
            print(f"❌ เกิดข้อผิดพลาด: {e}")

if __name__ == "__main__":
    asyncio.run(main())
