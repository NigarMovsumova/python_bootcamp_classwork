import pickle


class FileUtility:

    def write_to_file(dictionary, filename='students.txt'):
        file = open(filename, "wb")
        pickle.dump(dictionary, file)
        file.close()

    def load_from_file(filename='students.txt'):
        file = open(filename, 'rb')
        loaded_dictionary = pickle.load(file)
        file.close()
        return loaded_dictionary

    def truncate_file(filename='students.txt'):
        file = open(filename, 'wb')
        file.truncate()
        file.close()


ExampleUtility.truncate_file()
