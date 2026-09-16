import unittest
from src.utils import *

class Problem0_9Test(unittest.TestCase):
    # 클래스 초기화 시 호출
    @classmethod
    def setUpClass(cls):
        return super().setUpClass()

    # 클래스 소멸 시 호출
    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()

    # 테스트 실행 시 호출
    def setUp(self):
        return super().setUp()

    # 테스트 종료 시 호출
    def tearDown(self):
        return super().tearDown()

    '''
    0번 문제 테스트

    설명: 입력한 n에 대해 수동으로 계산한 값과 함수의 결과 값이 같은지 테스트

    # TODO
    n=0 → 범위 안에 홀수가 없으므로 결과는 0
n=1 → 홀수 리스트가 [1]뿐인 최소 케이스, 결과는 1
짝수 n vs 그 바로 아래 홀수 n → n=6과 n=5가 같은 결과(35)를 내는지 (경계 로직 n+1 확인용)
큰 n에서 공식과 대조 → 직접 리스트를 돌리지 않고, 홀수 제곱합의 폐쇄형 공식 k(2k-1)(2k+1)/3 (k=홀수 개수)으로 나온 값과 함수 결과가 일치하는지 — 로직 자체가 맞는지 별도 검증
음수 n → range(1, n+1, 2)가 빈 리스트가 되어 0을 반환하는데, 이게 의도된 동작인지 문서화 겸 테스트로 고정해두면 좋음
    '''
    def test_problem_0(self):
        odd_list_1 = [1,3,5,7,9]
        odd_list_2 = [1,3,5,7,9,11,13,15,17,19]

        self.assertEqual(
            sum([i ** 2 for i in odd_list_1]),
            sum_odd_sqaures(9),
                )
        self.assertEqual(
                    sum([i ** 2 for i in odd_list_1]),
                    sum_odd_sqaures(10),
                )
        self.assertEqual(
            sum([i ** 2 for i in odd_list_2]),
            sum_odd_sqaures(19),
                )
        self.assertEqual(
                    sum([i ** 2 for i in odd_list_2]),
                    sum_odd_sqaures(20),
                )


if __name__ == "__main__":
    unittest.main()