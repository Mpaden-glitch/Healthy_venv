input1 = input("Please input the first file to compare: ")
input2 = input("Please input the second file to compare: ")

with open(input1, 'r') as file1:
    with open(input2, 'r') as file2:
        diff = set(file1).difference(file2)

diff.discard('\n')

input3 = input("Please input the output compared value: ")

with open(input3, 'w') as file_out:
    for line in diff:
        file_out.write(line)