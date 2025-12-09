def count_substring(string, sub_string):
    sub = len(sub_string) 
    counts = 0
    for i in range(len(string)):
        if string[i:i + sub] == sub_string:
            counts += 1

    return counts

