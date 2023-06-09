import os
import subprocess
import re

def get_sha2_fingerprint(file_name: os.path) -> tuple[str, str]:
    process = subprocess.Popen(['ssh-keygen', '-l', '-E', 'sha256', '-f', file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = process.communicate()
    
    match = re.match(r'^\d* [^:]*:([^ ]*)[^(]*\((.*)\)$', out)
    fingerprint: str = match.group(1)
    cipher_algo: str = match.group(2)
    return fingerprint, cipher_algo


def main():
    ssh_dir: os.path = "/etc/ssh/"
    
    for file in os.listdir(ssh_dir):
        if file.endswith(".pub"):
            fingerprint, cipher_algo = get_sha2_fingerprint(os.path.join(ssh_dir, file))
            
            print(f"{cipher_algo} : {fingerprint}")
    
    return 0

if __name__ == "__main__":
    main()