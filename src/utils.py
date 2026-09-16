from tqdm import tqdm
from itertools import permutations, combinations
import math
from collections import defaultdict

"""
0번 문제

설명: 1부터 n 사이의 홀수를 제곱하고 전부 더한 것을 반환

입력: n (int)
출력: int
"""


def sum_odd_sqaures(n: int) -> int:
    odd_list = list(range(1, n + 1, 2))

    return sum([i**2 for i in odd_list])


"""
10번 문제

설명: 주어진 n 이하의 소수를 모두 찾는 함수
    1~n에 대해서, 1~sqrt(n)으로 나누어지지 않는 모든 수는 소수 (에라토스테네스의 체)

입력: n (int)
출력: list 
"""


def find_prime_numbers_by_n(n: int) -> list:
    sqrt_n = int(math.sqrt(n))

    prime_number_list = list(range(2, n + 1))

    for i in range(2, sqrt_n + 1):
        if i in prime_number_list:
            prime_number_list = [x for x in prime_number_list if (x % i != 0 or x == i)]

    return prime_number_list


"""
27번 문제

함수 is_prime
설명: 주어진 n이 소수인지 판별하는 함수

입력: n (int)
출력: bool

함수 find_longest_quadratic_n
설명: -999 ~ 999의 a와 -1000 ~ 1000의 b에 대해서, 가장 연속적으로 많은 소수를 출력하는 n을 갖는 a, b를 탐색
    a, b를 돌면서 n이 0일 때부터 소수가 어디까지 이어지는지를 기록, 가장 긴 n을 기록한 a, b를 반환

입력: a, b (int, int)
출력: Tuple[int, int]
"""


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def find_longest_quadratic_n(a: int, b: int) -> dict:
    assert a > 0 and b > 0
    longest_quadratic_dict = {}

    for i in range(-a, a + 1):
        for j in range(-b, b + 1):
            n = 0
            while True:
                if not is_prime((n**2) + (n * i) + j):
                    break
                n += 1
            longest_quadratic_dict[(i, j)] = n

    return longest_quadratic_dict


"""
28번 문제

함수 find_spiral_diagonals
설명: 주어진 홀수 n x n 나선에 대해, 모든 대각 성분을 더한 값을 반환
    각 n x n 나선의 대각 성분 4개의 합은 점화식 4n^2 - 6(n -1)로 나타낼 수 있기 때문에, 모든 나선에 대한 대각성분의 합을 계산

입력: 홀수 n (int)
출력: int
"""


def find_spiral_diagonals(n: int) -> int:
    assert n % 2 != 0

    diagonal_sum = 1

    for i in range(1, (n - 1) // 2 + 1):
        current_n = 2 * i + 1
        diagonal_sum += 4 * (current_n**2) - 6 * (current_n - 1)

    return diagonal_sum


"""
29번 문제

함수
설명:

입력:
출력:
"""


def find_distinct_powers(a: int, b: int) -> list:
    distinct_powers_set = set()
    for i in range(2, a + 1):
        for j in range(2, b + 1):
            distinct_powers_set.add(i**j)

    return distinct_powers_set


"""
30번 문제

함수
설명:

입력:
출력:
"""


def find_sum_of_nth_powers(n: int) -> list:
    sum_nth_powers_list = []

    upper_n = n
    for i in range(2, n**2):
        if len(str(i * (9**n))) < i:
            upper_n = i - 1
            break

    for i in range(2, 10**upper_n):
        if sum([int(j) ** n for j in str(i)]) == i:
            sum_nth_powers_list.append(i)

    return sum_nth_powers_list


"""
31번 문제

함수 find_coin_sums
설명: 가장 큰 코인의 경우의 수를 고정시키고, 그 나머지를 남은 코인들로 다시 찾는 재귀적 함수

입력:
출력:
"""


def find_coin_sums(n: int, coins_list: list) -> set[tuple]:
    assert len(coins_list) >= 1

    biggest_coin = coins_list[0]
    coins_combination_set = set()
    q = n // biggest_coin

    if len(coins_list) > 1:
        for i in range(q, -1, -1):
            r = n - (i * biggest_coin)
            if r == 0:
                coins_combination_set.add((biggest_coin, i))
            else:
                for comb in find_coin_sums(r, coins_list[1:]):
                    if comb:
                        coins_combination_set.add((biggest_coin, i) + comb)
        return coins_combination_set
    elif len(coins_list) == 1:
        if n - (q * biggest_coin) == 0:
            return [(biggest_coin, q)]
        else:
            return [()]


"""
32번 문제

함수
설명:

입력:
출력:
"""


def find_pandigital_products() -> list:
    num_permutations_list = list(permutations([i for i in range(1, 10)]))
    pandigital_products_set = set()

    for perm in num_permutations_list:
        slicing_indices = list(combinations(range(1, len(perm)), 2))
        for indices in slicing_indices:
            first_term = int("".join([str(i) for i in perm[: indices[0]]]))
            second_term = int("".join([str(i) for i in perm[indices[0] : indices[1]]]))
            third_term = int("".join([str(i) for i in perm[indices[1] :]]))
            if first_term * second_term == third_term:
                pandigital_products_set.add(third_term)

    return pandigital_products_set


"""
33번 문제

함수
설명:

입력:
출력:
"""


def find_digit_cancelling_fractions(n: int) -> list:
    fractions_list = []

    for i in range(10 ** (n - 1), 10**n):
        for j in range(10 ** (n - 1), 10**n):
            if (i == j) or (i > j) or (i % 10 == 0 and j % 10 == 0):
                continue

            i_digits = [l for l in str(i)]
            j_digits = [l for l in str(j)]
            i_j_common_digits = set(i_digits) & set(j_digits)

            if len(i_j_common_digits) == 1:
                i_j_common_digit = next(iter(i_j_common_digits))
                try:
                    i_ = int(str(i).replace(str(i_j_common_digit), ""))
                    j_ = int(str(j).replace(str(i_j_common_digit), ""))
                    if i_ / j_ == i / j:
                        fractions_list.append((i, j))
                except:
                    continue

    return fractions_list


"""
34번 문제

함수
설명:

입력:
출력:
"""


def find_digit_factorials() -> list:
    digit_factorials_list = []
    for i in range(3, 10**7):
        factorial_sum = 0
        for l in str(i):
            factorial_sum += math.factorial(int(l))
        if factorial_sum == i:
            digit_factorials_list.append(i)

    return digit_factorials_list


"""
35번 문제


"""


def find_circular_primes(prime_list: list) -> list:
    prime_set = set(prime_list)
    circular_primes_set = set()

    for prime in prime_set:
        n = len(str(prime))
        if prime in circular_primes_set:
            continue
        elif len(set([l for l in str(prime)])) == 1:
            circular_primes_set.add(prime)
        else:
            circular_candidates_list = [
                str(prime)[n - i :] + str(prime)[: n - i] for i in range(0, n)
            ]
            circular_candidates_check_list = [
                int(c) in prime_set for c in circular_candidates_list
            ]
            if all(circular_candidates_check_list):
                circular_primes_set.update(circular_candidates_list)

    return circular_primes_set


"""
36번 문제


"""


def check_palindrome_numbers(n: int) -> bool:
    return str(n) == str(n)[::-1]


"""
37번 문제


"""


def find_truncatable_primes() -> list:
    truncatable_primes_list = []

    i = 10
    while True:
        
        i += 1

        if not is_prime(i):
            continue

        truncated_int_set = set()
        str_i = str(i)
        for j in range(1, len(str_i)):
            truncated_int_set.add(str_i[:j])
            truncated_int_set.add(str_i[len(str_i)-j:])

        if all([is_prime(int(p)) for p in truncated_int_set]):
            truncatable_primes_list.append(i)

        if len(truncatable_primes_list) == 11:
            break

    return truncatable_primes_list

"""
38번 문제


"""


def find_9_pandigital_multiples() -> int:
    biggest_concatenated_product = ""
    for i in range(1, 10 ** 9 // 2):
        if str(i)[0] == "9":
            current_concatenated_product = ""
            current_i = 1
            while True:
                current_concatenated_product += str(i * current_i)
                if len(current_concatenated_product) == 9:
                    if {str(i) for i in range(1, 10)} == set(current_concatenated_product):
                        biggest_concatenated_product = max(biggest_concatenated_product, current_concatenated_product)
                    break
                elif len(current_concatenated_product) > 9:
                    break

                current_i += 1


    return biggest_concatenated_product

"""
39번 문제


"""


def find_max_int_right_triangles(p: int) -> set:
    right_triangles_set = set()
    for i in range(1, p-1):
        for j in range(1, p-i):
            k = p - i - j
            *r, l = sorted([i, j, k])
            if l ** 2 == r[0] ** 2 + r[1] ** 2:
                right_triangles_set.add((l, r[0], r[1]))

    return right_triangles_set


"""
40번 문제


"""


def find_champernowne_constant(n: int) -> int:
    idx = 1
    num = 1
    decimal_dict = {}
    while True:
        for i in str(num):
            decimal_dict[idx] = int(i)
            idx += 1
        num += 1

        if idx > 10 ** n:
            champernowne_constant = 1
            for i in range(n+1):
                champernowne_constant *= decimal_dict[10 ** i]
            return champernowne_constant


"""
41번 문제

설명: Pan-digital 소수의 상한이 9자리라고 가정 후 체크

"""


def find_largest_pandigital_prime() -> int:
    prime_under_9_digits_list = find_prime_numbers_by_n(1000000000)

    print(prime_under_9_digits_list)