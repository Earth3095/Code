import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import config

print("🔍 ทดสอบระบบทั้งหมด...\n")

# Test imports
print("1. Testing imports...")
try:
    from core.memory_system import MemorySystem
    from core.file_analyzer import FileAnalyzer
    from core.unlimited_engine import UnlimitedAIEngine
    from core.code_executor import CodeExecutor
    print("✅ All imports OK!\n")
except Exception as e:
    print(f"❌ Import failed: {e}\n")
    exit(1)

# Test Memory
print("2. Testing Memory System...")
try:
    memory = MemorySystem()
    print("✅ Memory System OK\n")
except Exception as e:
    print(f"❌ Memory: {e}\n")

# Test Analyzer
print("3. Testing File Analyzer...")
try:
    analyzer = FileAnalyzer()
    print("✅ File Analyzer OK\n")
except Exception as e:
    print(f"❌ Analyzer: {e}\n")

# Test Executor
print("4. Testing Code Executor...")
try:
    executor = CodeExecutor()
    result = executor.execute("print('Hello')", "python")
    if result['success']:
        print("✅ Code Executor OK\n")
    else:
        print("⚠️ Executor works but test failed\n")
except Exception as e:
    print(f"❌ Executor: {e}\n")

print("="*50)
print("🎉 ระบบพร้อมใช้งาน!")
print(f"📂 Project: {config.PROJECT_ROOT}")
print(f"🤖 Models: {config.MODEL_PATH}")
print("="*50)