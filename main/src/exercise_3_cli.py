import sys
import exercise_3


def count_palindromes_cli_wrapper():
    return exercise_3.count_palindromes_per_give_string_length_in_file(sys.argv[1], int(sys.argv[2]))


print(count_palindromes_cli_wrapper())


# example call
# python .\main\src\exercise_3_cli.py .\main\tests\palindrome_test.txt 99