from prettytable import PrettyTable

x = PrettyTable()
x.add_column("City name",["saiteja","chaitanya","aakash"])
x.add_column("Area",["vijayawada","hydrabad","guntur"])
x.align = "l"
print(x)