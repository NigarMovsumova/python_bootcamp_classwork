numbers = []


def sum_numbers():
    numbers = []
    sum = 0
    numbers.append(1)
    numbers.append(4)
    sum += numbers[0] + numbers[1]
    print(sum)


global_variable = 'global'


# non local
def local():
    local_variable = 'local'
    print(local_variable)

    def non_local():
        print(global_variable)
        non_local_variable = 'non local'
        print(local_variable)
