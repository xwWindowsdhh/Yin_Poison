import json
from yin_engine import YinEngine
from red_engine import RedEngine

class VirusScanner:
    def __init__(self):
        self.virus_db = self.load_virus_db()
        self.yin_engine = YinEngine()
        self.red_engine = RedEngine()
    
    def load_virus_db(self):
        try:
            with open('virus_db.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {"viruses": []}
    
    def scan_file(self, file_path, engine_enabled):
        if engine_enabled.get('Yin', False):
            if self.yin_engine.scan_file(file_path):
                virus = next((v for v in self.virus_db.get('viruses', []) 
                             if v.get('engine') == 'yin'), None)
                if virus:
                    return True, f"检测到病毒: {virus['name']}\n\n病毒介绍: {virus['introduction']}\n\n解决方案: {virus['solve']}"
        
        if engine_enabled.get('Red', False):
            if self.red_engine.scan_file(file_path):
                virus = next((v for v in self.virus_db.get('viruses', []) 
                             if v.get('engine') == 'Red'), None)
                if virus:
                    return True, f"检测到病毒: {virus['name']}\n\n病毒介绍: {virus['introduction']}\n\n解决方案: {virus['solve']}"
        
        print("[DEBUG] 未匹配到任何病毒")
        return False, "未检测到病毒"