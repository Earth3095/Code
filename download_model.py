"""
Model Downloader - คุณเป็นเจ้าของ Model
ดาวน์โหลดแล้วเป็นของคุณตลอดไป
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import config
from huggingface_hub import hf_hub_download

def check_existing():
    cache_dir = os.path.join(config.MODEL_PATH, 'cache')
    if os.path.exists(cache_dir):
        for root, dirs, files in os.walk(cache_dir):
            for file in files:
                if file.endswith('.gguf'):
                    path = os.path.join(root, file)
                    size = os.path.getsize(path) / (1024**2)
                    print(f"✅ Found: {file} ({size:.0f} MB)")
                    return path
    return None

def download():
    print("="*60)
    print("🔥 DOWNLOADING YOUR AI MODEL")
    print("="*60)
    print(f"👑 Owner: {config.OWNER}")
    print(f"📂 Location: {config.MODEL_PATH}")
    print(f"📦 Size: ~4-5 GB")
    print(f"⏰ Time: 10-20 min")
    print("="*60)
    
    existing = check_existing()
    if existing:
        if input("\nModel exists. Re-download? (y/n): ").lower() != 'y':
            return existing
    
    try:
        print("\n📥 Downloading...\n")
        path = hf_hub_download(
            repo_id=config.MODEL_NAME,
            filename=config.MODEL_FILE,
            cache_dir=config.MODEL_PATH,
            resume_download=True
        )
        print(f"\n✅ DONE! Your model: {path}")
        return path
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    # Install llama-cpp-python
    print("📦 Installing llama-cpp-python...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "llama-cpp-python", "-q"])
    
    # Download
    model = download()
    
    if model:
        print("\n" + "="*60)
        print("🎉 YOUR AI IS READY!")
        print("="*60)
        print("Next: python run.py")
    else:
        print("\n❌ Failed. Try again.")