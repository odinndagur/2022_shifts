import hashlib
 
def hashfile(file):
    BUF_SIZE = 65536
    sha256 = hashlib.sha256()
    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()
    

def compare_file_hashes(file1: str, file2: str) -> bool:
    f1_hash = hashfile(file1)
    f2_hash = hashfile(file2)
    return f1_hash is f2_hash