policies = open("encryption_policies.txt")

invalid_keys = []

for line in policies.read().splitlines():
    policy, key = line.split(":")
    policy = policy.strip()
    key = key.strip()
    times, char = policy.split(" ")
    i, j = times.split("-")

    count = key.count(char)

    if count < int(i) or count > int(j):
        invalid_keys.append(key)

print(invalid_keys)
print(invalid_keys[12])
print(invalid_keys[41])

open("output_03.txt", "w").write(invalid_keys[41])
