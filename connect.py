name = input("Enter module name: ")
filename = name + ".sv"
f = open(filename, "r")
output = name + "   (" 
lines = f.readlines()
for line in lines:
    if line.strip():  # Check if the line is not empty
        parts = line.strip().split(" logic ")
        if len(parts) == 2:
            part2 = line.strip().split("]")
            if len(part2) == 2:
                a = part2[1].strip().split(",")[0]
                output += "." + a + "(" + a + "), "
            else:
                a = parts[1].strip().split(",")[0]
                output += "." + a + "(" + a + "), "
        elif parts[0] == ");":
            break

output = output[:-2] + ");"
f.close
print(output)