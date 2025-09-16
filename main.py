import module

 
df = module.readfile("emps.csv")

 
print("\n=== Original Data ===")
df.show()

 
print("\nRow 1:", df[1])

 
print("Column 'Salary':", df["Salary"].values)

 
print("Cell [1][Salary]:", df[1]["Salary"])

 
print("\n=== Modify Salary Column ===")
df.set_column("Salary", ["4000", "5000", "6000"])
df.show()

 
print("\n=== Modify Cell ===")
df.set_cell(1, "Salary", "8000")
df.show()

 
print("\n=== Add Bonus Column ===")
df.set_column("Bonus", ["100", "200", "300"])
df.show()

 
print("\nSum of Salary:", df["Salary"].sum())
print("Max of Salary:", df["Salary"].max())
print("Min of Salary:", df["Salary"].min())

 
df.save_to_file("new_emps.csv")
