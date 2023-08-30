class some_data_struct():
    def __init__(self, val):
        self.val = val
        
def some_function(input_arg : some_data_struct):
    input_arg.val *= 7
    return None

X = some_data_struct(2)
print(X.val)
some_function(X)
print(X.val)