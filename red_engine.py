import hashlib
import json

class RedEngine:
    def __init__(self):
        self.virus_db = self.load_virus_db()
    
    def load_virus_db(self):
        try:
            with open('virus_db.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {"viruses": []}
    
    def calculate_hash(self, file_path):
        with open(file_path, 'rb') as f:
            return hashlib.sha1(f.read()).hexdigest()
    
    def scan_file(self, file_path):
        print(f"[DEBUG] Red引擎开始扫描文件: {file_path}")
        file_hash = self.calculate_hash(file_path)
        print(f"[DEBUG] 文件哈希值: {file_hash}")
        
        for virus in self.virus_db.get('viruses', []):
            if virus.get('engine') != 'Red':
                continue
            print(f"[DEBUG] 比对病毒库: {virus['name']} ({virus['hash']})")
            if virus['hash'] == file_hash:
                print(f"[DEBUG] 匹配到病毒: {virus['name']}")
                return True
        
        print("[DEBUG] 未匹配到任何病毒")
        return False