import hashlib

def calculate_sha1(file_path):
    hasher = hashlib.sha1()
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

def calculate_sha256(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

def calculate_md5(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

if __name__ == '__main__':
    file_path = input('请输入文件路径: ')
    print(f'文件的SHA1哈希值是: {calculate_sha1(file_path)}')
    print(f'文件的SHA256哈希值是: {calculate_sha256(file_path)}')
    print(f'文件的MD5哈希值是: {calculate_md5(file_path)}')
    input()