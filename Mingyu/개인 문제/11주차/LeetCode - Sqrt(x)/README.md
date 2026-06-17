# 🧩 Sqrt(x)

## 📌 문제 정보

| 항목 | 내용 |
| --- | --- |
| 플랫폼 | NeetCode |
| 문제 번호 | 69 |
| 난이도 | Easy |
| 분류 | Math, Binary Search |
| 언어 | Java |
| 제출 일자 | 2026년 06월 15일 16:59:05 |
| 문제 링크 | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) |
| 원본 경로 | `Data Structures & Algorithms/sqrtx/submission-0.java` |
<!-- AI_ANALYSIS: version=v1 model=gemini-3.1-flash-lite hash=61dc71acccc69394 -->

## 📝 문제 설명

You are given a non-negative integer `x`, return the **square root** of `x` **rounded down** to the nearest integer. The returned integer should be non-negative as well.

You **must not use** any built-in exponent function or operator.

- For example, do not use `pow(x, 0.5)` in `c++` or `x ** 0.5` in `python`.

**Example 1:**

```text
Input: x = 9

Output: 3
```

**Example 2:**

```text
Input: x = 13

Output: 3
```

**Constraints:**

- `0 <= x <= ((2^31)-1)`

## 📥 입력

```text
x = 9
```

## 📤 출력

```text
3
```

## 💡 핵심 아이디어

- 제곱근을 구하는 문제는 0부터 x 사이의 정수 범위에서 이분 탐색을 통해 해결할 수 있습니다.
- mid * mid 값이 x보다 작거나 같은 최대 정수를 찾는 것이 핵심입니다.
- 중간값 계산 시 오버플로우를 방지하기 위해 long 타입을 사용하여 제곱 연산을 수행합니다.

## 🧮 정답 계산식

mid * mid <= x를 만족하는 가장 큰 정수 mid를 찾습니다.

## 🔍 구현 흐름

1. 탐색 범위를 0부터 x까지로 설정합니다.
2. 이분 탐색을 위해 중간값 mid를 계산합니다.
3. mid의 제곱이 x보다 크면 탐색 범위를 왼쪽으로 좁힙니다.
4. mid의 제곱이 x보다 작으면 ans에 mid를 저장하고 탐색 범위를 오른쪽으로 좁힙니다.
5. mid의 제곱이 x와 같으면 즉시 mid를 반환합니다.

## ⚠️ 주의할 점

- mid * mid 연산 시 int 범위를 초과할 수 있으므로 반드시 long으로 형변환해야 합니다.
- x가 0인 경우를 고려하여 초기 범위를 설정해야 합니다.
- 이분 탐색 종료 조건인 left <= right를 정확히 구현해야 무한 루프를 방지할 수 있습니다.

## 📁 제출 코드

- 풀이 파일: [solution.java](./solution.java)
- 수집 위치: `Data Structures & Algorithms/sqrtx/submission-0.java`

## ⏱️ 복잡도 분석

- 시간 복잡도: O(log x)
- 공간 복잡도: O(1)

## ✅ 한 줄 요약

이분 탐색을 활용하여 정수 범위 내에서 제곱근의 정수 부분을 효율적으로 찾아내는 알고리즘입니다.
