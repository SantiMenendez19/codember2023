files = open("files_quarantine.txt")

real_files = []

for file in files.read().splitlines():
    chain, checksum = file.split("-")
    unique_chars = {}
    for char in chain:
        if char not in unique_chars:
            unique_chars[char] = 1
        else:
            unique_chars[char] += 1
    real_checksum = ""
    for key in unique_chars:
        if unique_chars[key] == 1:
            real_checksum += key
    if real_checksum == checksum:
        real_files.append(file)
    print(unique_chars, real_checksum, chain, checksum)

print(real_files[32])

open("output_04.txt", "w").write(real_files[32])