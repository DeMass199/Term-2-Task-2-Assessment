
def check_if_contained_in_txt(password):
    file1 = open('words.txt', 'r')
    Lines = file1.readlines()
    found = False
    # print(Lines)
    for line in Lines:
        if line.strip() in password:
            found = True
    return found


