
def is_palindrome(input_str: str) -> bool:
    for i in range(int(len(input_str) / 2)):
        if input_str[i] != input_str[- i - 1]:
            return False
    return True


def count_palindromes_per_give_string_length(input_str: str, str_len: int) -> int:
    return sum([1 for word in input_str[:str_len].split("\n") if is_palindrome(word)])


def count_palindromes_per_give_string_length_in_file(file_path: str, str_len: int) -> int:
    my_file = open(file_path, 'r')
    cnt = count_palindromes_per_give_string_length(my_file.read(), 99)
    my_file.close()
    return cnt

