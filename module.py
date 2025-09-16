import csv

class DataFrame:
    def __init__(self, data, columns):
        self.data = data
        self.columns = columns

    
    def show(self):
        print("\t".join(self.columns))
        for row in self.data:
            print("\t".join(str(x) for x in row))

     
    def __getitem__(self, key):
        try:
            if isinstance(key, int):   
                return dict(zip(self.columns, self.data[key]))
            elif isinstance(key, str):   
                if key not in self.columns:
                    raise KeyError(f"Column '{key}' not found!")
                col_index = self.columns.index(key)
                return Column([row[col_index] for row in self.data], key, self)
            else:
                raise TypeError("Invalid key type. Use int for rows or str for columns.")
        except Exception as e:
            print("Error:", e)

     
    def set_column(self, col_name, values):
        try:
            if len(values) != len(self.data):
                raise ValueError("Column length does not match data length!")
            if col_name in self.columns:
                col_index = self.columns.index(col_name)
                for i in range(len(self.data)):
                    self.data[i][col_index] = values[i]
            else:
                self.columns.append(col_name)
                for i in range(len(self.data)):
                    self.data[i].append(values[i])
        except Exception as e:
            print("Error:", e)


    def set_cell(self, row, col, value):
        try:
            col_index = self.columns.index(col)
            self.data[row][col_index] = value
        except Exception as e:
            print("Error:", e)

    
    def save_to_file(self, filename):
        try:
            with open(filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(self.columns)
                writer.writerows(self.data)
            print(f"Data saved to {filename}")
        except Exception as e:
            print("Error:", e)


class Column:
    def __init__(self, values, name, df):
        self.values = values
        self.name = name
        self.df = df

    def sum(self):
        try:
            return sum(float(v) for v in self.values)
        except Exception:
            print(f"Cannot sum non-numeric column '{self.name}'")

    def max(self):
        try:
            return max(float(v) for v in self.values)
        except Exception:
            print(f"Cannot find max of non-numeric column '{self.name}'")

    def min(self):
        try:
            return min(float(v) for v in self.values)
        except Exception:
            print(f"Cannot find min of non-numeric column '{self.name}'")


 
def readfile(filename):
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            columns = next(reader)
            data = [row for row in reader]
        return DataFrame(data, columns)
    except Exception as e:
        print("Error:", e)
