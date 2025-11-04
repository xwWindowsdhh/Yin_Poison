import re
import json
import binascii

class YinEngine:
    def __init__(self):
        self.patterns = self.load_patterns()
    
    def load_patterns(self):
        try:
            with open('virus_db.json', 'r', encoding='utf-8') as f:
                virus_db = json.load(f)
                patterns = []
                for v in virus_db.get('viruses', []):
                    if v.get('engine') == 'yin':
                        # 普通字符串特征码
                        if 'code' in v:
                            try:
                                patterns.append(v['code'].encode('utf-8'))
                                print(f"[DEBUG] 加载字符串特征码: {v['code']}")
                            except UnicodeEncodeError:
                                print(f"[WARN] 无效的字符串特征码: {v['code']}")
                        
                        # 二进制特征码（0和1组成的字符串）
                        if 'code2' in v:
                            bin_str = v['code2'].replace(' ', '')
                            if all(c in '01' for c in bin_str) and len(bin_str) % 8 == 0:
                                try:
                                    byte_data = bytes(
                                        int(bin_str[i:i+8], 2) 
                                        for i in range(0, len(bin_str), 8)
                                    )
                                    patterns.append(byte_data)
                                    hex_str = binascii.hexlify(byte_data).decode()
                                    print(f"[DEBUG] 加载二进制特征码: {hex_str}")
                                except ValueError:
                                    print(f"[ERROR] 无效的二进制特征码: {v['code2']}")
                            else:
                                print(f"[ERROR] 无效的二进制格式: {v['code2']}")
                return patterns
        except Exception as e:
            print(f"[ERROR] 加载病毒库失败: {str(e)}")
            return []
    
    def scan_file(self, file_path):
        print(f"[DEBUG] 阴引擎扫描文件: {file_path}")
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
            
            for pattern in self.patterns:
                offset = content.find(pattern)
                if offset != -1:
                    hex_pattern = binascii.hexlify(pattern).decode()
                    print(f"[MATCH] 在偏移 {offset} 处匹配到特征码: {hex_pattern}")
                    return True
            
            print("[DEBUG] 未匹配到任何特征码")
            return False
        except Exception as e:
            print(f"[ERROR] 扫描文件失败: {str(e)}")
            return False