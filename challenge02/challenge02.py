count = 0
output = ""
message = open("message_02.txt")

for c in message.read():
    match c:
        case "#":
            count += 1
        case "@":
            count -= 1
        case "*":
            count = count**2
        case "&":
            output += str(count)

open("output_02.txt", "w").write(output)

print(output)
