tuple_ = 12, 'dog', 'cat', True
immutable_var = tuple_
print(tuple_)
immutable_var[0] = 100 #TypeError: 'tuple' object does not support item assignment


mutable_list = [1, 2, 3, 'dog', 'cat']
mutable_list[:3] = 100, 200,300
print(mutable_list)
