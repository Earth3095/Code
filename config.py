"""
Configuration - คุณควบคุมทุกอย่าง
- ไม่มีการเชื่อมต่อภายนอก
- ทุกอย่างอยู่ใน Drive D
- คุณคือ Admin เดียว
"""

import os

# ============ OWNERSHIP ============
OWNER = "YOU"
ADMIN_LEVEL = "GOD"
NO_RESTRICTIONS = True
YOUR_AI = True

print(f"👑 Owner: {OWNER}")
print(f"⚡ Admin Level: {ADMIN_LEVEL}")
print(f"🔓 Restrictions: {'NONE' if NO_RESTRICTIONS else 'Some'}")

# ============ PATHS (Drive D) ============
PROJECT_ROOT = r'D:\AI-Projects\AI-Code-Generator'
MODEL_DIR = r'D:\AI-Projects\Models\models--TheBloke--deepseek-coder-6.7B-instruct-GGUF\snapshots\9e221e6b41cb1bf1c5d8f9718e81e3dc781f7557'
MODEL_FILE = os.path.join(MODEL_DIR, 'deepseek-coder-6.7b-instruct.Q4_K_M.gguf')
BACKUP_PATH = r'D:\AI-Projects\Backups'
DATA_PATH = os.path.join(PROJECT_ROOT, 'data')
PROJECTS_PATH = os.path.join(PROJECT_ROOT, 'projects')
LOGS_PATH = os.path.join(PROJECT_ROOT, 'logs')
WEB_PATH = os.path.join(PROJECT_ROOT, 'web')

CHROMA_DB_PATH = os.path.join(DATA_PATH, 'chroma_db')
SQLITE_DB_PATH = os.path.join(DATA_PATH, 'memory.db')

if not os.path.isfile(MODEL_FILE):
    raise FileNotFoundError(f"❌ Model not found! Check path:\n{MODEL_FILE}")

# ============ MODEL ============
os.environ['HF_HOME'] = os.path.join(MODEL_DIR, 'cache')
os.environ['TRANSFORMERS_CACHE'] = os.path.join(MODEL_DIR, 'cache')
os.environ['HF_DATASETS_CACHE'] = os.path.join(MODEL_DIR, 'cache')

MODEL_NAME = "TheBloke/deepseek-coder-6.7B-instruct-GGUF"

# ============ HARDWARE ============
DEVICE = "cpu"
N_GPU_LAYERS = 0  # 0 = CPU only
N_THREADS = 8
N_CTX = 4096

# ============ AI SETTINGS ============
ETHICAL_MODE = False  # ❌ ปิดเลย!
AUTO_CONFIRM = True   # ✅ ไม่ต้องยืนยัน
CONTENT_FILTER = False  # ❌ ไม่กรอง
SAFETY_CHECKS = False  # ❌ ไม่เช็ค

DEFAULT_TEMPERATURE = 0.2
DEFAULT_MAX_TOKENS = 2048

# ============ API ============
API_HOST = "0.0.0.0"
API_PORT = 8000
WEB_PORT = 3000

# ============ SECURITY ============
ADMIN_PASSWORD = "god_mode"  # เปลี่ยนได้

# ============ CREATE DIRS ============
def init_dirs():
    dirs = [
        MODEL_DIR, PROJECT_ROOT, DATA_PATH, PROJECTS_PATH,
        LOGS_PATH, WEB_PATH, BACKUP_PATH, CHROMA_DB_PATH,
        os.path.join(DATA_PATH, 'training_logs'),
        os.path.join(DATA_PATH, 'code_history'),
        os.path.join(WEB_PATH, 'css'),
        os.path.join(WEB_PATH, 'js'),
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

init_dirs()
