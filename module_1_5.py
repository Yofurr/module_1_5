immutable_var = 33, 'песня', 21.2, True, [1, 2, 3]
print(immutable_var)
immutable_var[4][0] = 21 # можно изменить только элемент списка
print(immutable_var)

# кортеж не поддерживает обращение по элементам, поэтому элемент как таковой изменить нельзя
# Кортежи часто используются в качестве хранилищ данных, особенно когда необходимо сохранить список в неизменном виде.

mutable_list=[33, 'песня', 21.2, True, [1, 2, 3]]
mutable_list[0]=31
mutable_list[1]='song'
mutable_list[2]=22.1
mutable_list[3]=False
mutable_list[4]=[3, 2, 1]
print(mutable_list)