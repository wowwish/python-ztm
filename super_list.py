class SuperList(list):
    def __len__(self):
        return 1000

super_list = SuperList()
print(len(super_list))
super_list.append(5)
print(super_list[0])
print("issubclass(SuperList, list) : ", issubclass(SuperList, list))
# REMEMBER, 'object' IS THE SUPERCLASS OF EVERY OBJECT IN PYTHON. EVERY CLASS IS A SUBCLASS OF 'object'
print("issubclass(list, object) : ", issubclass(list, object))