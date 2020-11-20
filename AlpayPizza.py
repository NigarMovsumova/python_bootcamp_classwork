import pickle


objects = []
with (open("order.txt", "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break
    print(objects)
