#Script to make systemVerilog modules quickly for ece337 and 437 lab


name = input("Enter module name: ")
filename = name + ".sv"
f = open(filename, "w")
f.write("module " + name + "(")
f.write("\n\tinput logic clk,")
f.write("\n\tinput logic n_rst")
print("Added clock and n_rst")
user = input("input? (n for done): ")
bits = ""
while(user != "n"):
    if(user[-1] == "]"):
        idx = user.find("[")
        print(idx)
        bits = user[idx:]
        user = user[0:idx]
    else:
        bits = ""
    f.write(",\n\tinput logic " + bits + " " + user)
    user = input("name? (n for done): ")
    
        
    
user = input("output? (n for done): ")
while(user != "n"):
    if(user[-1] == "]"):
        idx = user.find("[")
        print(idx)
        bits = user[idx:]
        user = user[0:idx]
    else:
        bits = ""
    f.write(",\n\toutput logic " + bits + " " + user)
    user = input("output? (n for done): ")
    
f.write("\n);\n\nendmodule")
f.close
