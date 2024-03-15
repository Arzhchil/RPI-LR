class Row:
    _id_counter = 0

    def __init__(self, collection, value):
        self.id = Row._id_counter
        Row._id_counter += 1
        self.collection = collection
        self.value = value

class Table:
    def __init__(self, rowsNum):
        self.rows = []
        self.rowsNum = rowsNum

    def addrow(self, row):
        for existing_row in self.rows:
            if existing_row.id == row.id:
                raise ValueError(f"Строка с ID {row.id} уже существует.")
        self.rows.append(row)

    def setRow(self, row):
        found = False
        for i, existing_row in enumerate(self.rows):
            if existing_row.id == row.id:
                self.rows[i] = row
                found = True
                break
        if not found:
            raise ValueError(f"Нет строки с ID {row.id}")

    def getRow(self, rowId):
        for row in self.rows:
            if row.id == rowId:
                return row
        raise ValueError(f"Нет строки с ID {rowId}")

    def display(self):
        print("id", "x1", "x2", "f(x1,x2)", sep="\t")
        for row in self.rows:
            print(row.id, *row.collection, row.value, sep="\t")

class LogicFunction:
    def __init__(self, variableNum, table):
        self.variableNum = variableNum
        self.table = table

    def getExpression(self):
        terms = []
        for row in self.table.rows:
            if row.value == 1:
                terms.append(''.join(str(x) for x in row.collection))
        if len(terms) == 0:
            return '0'
        if len(terms) == 2**self.variableNum:
            return '1'
        minimized_form = " ИЛИ ".join([" И ".join(["НЕ x"+str(idx) if bit=='0' else "x"+str(idx) for idx, bit in enumerate(term, 1)]) for term in terms])
        return minimized_form

    def getTable(self):
        return self.table

    def printTable(self):
        self.table.display()

table = Table(5)
row1 = Row([0, 0], 0)
row2 = Row([0, 1], 1)
table.addrow(row1)
table.addrow(row2)
logic_func = LogicFunction(2, table)
logic_func.printTable()
print(logic_func.getExpression())
