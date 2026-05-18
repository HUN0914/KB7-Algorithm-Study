# 🧩 Combinations

## 📌 문제 정보

| 항목 | 내용 |
| --- | --- |
| 플랫폼 | NeetCode |
| 문제 번호 | 77 |
| 난이도 | Medium |
| 분류 | Backtracking |
| 언어 | Java |
| 제출 일자 | 2026년 05월 18일 10:20:47 |
| 문제 링크 | [Combinations](https://leetcode.com/problems/combinations/) |
| 원본 경로 | `Data Structures & Algorithms/combinations/submission-0.java` |
<!-- AI_ANALYSIS: version=v1 model=gemini-3.1-flash-lite hash=1b94be145a9c2c48 -->

## 📝 문제 설명

You are given two integers `n` and `k`, return all possible **combinations** of `k` numbers chosen from the range `[1, n]`.

You may return the answer in **any order**.

**Example 1:**

```text
Input: n = 3, k = 2

Output: [
 [1,2],
 [1,3],
 [2,3]
]
```

**Example 2:**

```text
Input: n = 3, k = 3

Output: [[1,2,3]]
```

**Constraints:**

- `1 <= k <= n <= 20`

## 📥 입력

```text
n = 3, k = 2
```

## 📤 출력

```text
[
 [1,2],
 [1,3],
 [2,3]
]
```

## 💡 핵심 아이디어

- 백트래킹을 사용하여 1부터 n까지의 숫자 중 k개를 선택하는 모든 경우의 수를 탐색합니다.
- 현재 선택된 숫자의 개수가 k에 도달하면 결과 리스트에 추가하고 재귀를 종료합니다.
- 가지치기 기법을 적용하여 남은 숫자의 개수가 필요한 개수보다 적은 경우 탐색을 조기에 중단합니다.

## 🧮 정답 계산식

현재 선택된 숫자가 path에 담겨 있을 때, 다음 숫자는 start부터 n - (k - path.size()) + 1까지 반복하여 탐색합니다.

## 🔍 구현 흐름

1. 결과를 저장할 리스트와 현재 경로를 추적할 리스트를 준비합니다.
2. 백트래킹 함수를 호출하여 1부터 n까지의 숫자를 순차적으로 선택합니다.
3. 현재 경로의 크기가 k와 같아지면 결과 리스트에 복사본을 추가합니다.
4. 반복문에서 남은 숫자의 개수를 고려하여 불필요한 탐색 범위를 제한합니다.
5. 숫자를 추가한 후 재귀 호출을 수행하고, 다시 숫자를 제거하여 다음 경우의 수를 탐색합니다.

## ⚠️ 주의할 점

- 결과 리스트에 경로를 추가할 때 반드시 새로운 리스트 객체를 생성하여 저장해야 합니다.
- 반복문의 종료 조건을 n - need + 1로 설정하여 탐색 효율을 최적화해야 합니다.

## 📁 제출 코드

- 풀이 파일: [solution.java](./solution.java)
- 수집 위치: `Data Structures & Algorithms/combinations/submission-0.java`

## ⏱️ 복잡도 분석

- 시간 복잡도: O(k * C(n, k))
- 공간 복잡도: O(k)

## ✅ 한 줄 요약

백트래킹과 가지치기를 활용하여 n개 중 k개를 선택하는 모든 조합을 효율적으로 생성하는 문제입니다.
