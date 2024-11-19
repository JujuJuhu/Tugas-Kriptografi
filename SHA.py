import subprocess

def calculate_hash(file_path, algorithm):
    command = f"certutil -hashfile \"{file_path}\" {algorithm}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return "Error: Failed to calculate hash"

file_path = "asd.png"
algorithm = "SHA256"
hash_value = calculate_hash(file_path, algorithm)
print(hash_value)