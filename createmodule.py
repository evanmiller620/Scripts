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
    if(len(user.split(" ")) == 2):
        idx = user.split(" ")[1]
        idx = int(idx)
        idx = idx - 1
        bits = "[" + str(idx) + ":0] "
        user = user.split(" ")[0]
    else:
        bits = ""
    f.write(",\n\tinput logic " + bits + user)
    user = input("name? (n for done): ")
    
        
    
user = input("output? (n for done): ")
while(user != "n"):
    if(len(user.split(" ")) == 2):
        idx = user.split(" ")[1]
        idx = int(idx)
        idx = idx - 1
        bits = "[" + str(idx) + ":0] "
        user = user.split(" ")[0]
    else:
        bits = ""
    f.write(",\n\toutput logic " + bits + user)
    user = input("output? (n for done): ")

f.write("\n);\n\talways_ff @(posedge clk, negedge n_rst) begin\n\t\tif(n_rst == 1'b0) begin\n\t\t\t\n\t\tend else begin\n\t\t\t\n\t\tend\n\tend\n") #registers
f.write("\n\talways_comb begin\n\t\t\n\tend\n") #comb logic
f.write("endmodule")
f.close