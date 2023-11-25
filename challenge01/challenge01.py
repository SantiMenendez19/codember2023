words = {}

message = open("message_01.txt")

for word in message.read().split(" "):
    if word.lower() not in words:
        words[word.lower()] = 1
    else:
        words[word.lower()] += 1

print(words)

output = ""

for key in words:
    output += key + str(words[key])

open("output_01.txt", "w").write(output)
