name = input("Enter module name: ")
filename = name + ".sv"
f = open(filename, "r")
output = name + "   (" 
signals = ""
lines = f.readlines()
for line in lines:
    if line.strip():  # Check if the line is not empty
        parts = line.strip().split(" logic ")
        if len(parts) == 2:
            b = "logic " + parts[1].split(",")[0] + ";\n"
            c_p = b.split(" ")
            if len(c_p) == 3:
                signals += c_p[0] + " " + c_p[1] + " tb_" + c_p[2]
            if len(c_p) == 2:
                signals += c_p[0] + " " + " tb_" + c_p[1]
            part2 = line.strip().split("]")
            if len(part2) == 2:
                a = part2[1].strip().split(",")[0]
                output += "." + a + "(tb_" + a + "), "
            else:
                a = parts[1].strip().split(",")[0]
                output += "." + a + "(tb_" + a + "), "
        elif parts[0] == ");":
            break

output = output[:-2] + ");\n"
f.close
print(output)
print(signals)