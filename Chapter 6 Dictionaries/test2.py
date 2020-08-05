def object_with_beautiful_identity():
    for i in range(10_000):
        # Change the next line
        str_id = str(id(i))
        print(str_id)
        if str_id[:-2] == '888' :
            print (i)

if __name__ == "__main__":
    object_with_beautiful_identity()