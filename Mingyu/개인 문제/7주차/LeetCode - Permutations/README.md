# 🧩 Permutations

## 📌 문제 정보

| 항목 | 내용 |
| --- | --- |
| 플랫폼 | NeetCode |
| 문제 번호 | 46 |
| 난이도 | Medium |
| 분류 | Array, Backtracking |
| 언어 | Java |
| 제출 일자 | 2026년 05월 18일 09:41:37 |
| 문제 링크 | [Permutations](https://leetcode.com/problems/permutations/) |
| 원본 경로 | `Data Structures & Algorithms/permutations/submission-0.java` |
<!-- AI_ANALYSIS: version=v1 model=gemini-3.1-flash-lite hash=b126ba5f1fd17b9a -->

## 📝 문제 설명

Given an array `nums` of **unique** integers, return all the possible permutations. You may return the answer in **any order**.

**Example 1:**

```text
Input: nums = [1,2,3]

Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Example 2:**

```text
Input: nums = [7]

Output: [[7]]
```

**Constraints:**

- `1 <= nums.length <= 6`

- `-10 <= nums[i] <= 10`

## 📥 입력

```text
nums = [1,2,3]
```

## 📤 출력

```text
[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

## 💡 핵심 아이디어

- 백트래킹을 사용하여 배열의 모든 가능한 순열을 생성합니다.
- 현재 인덱스부터 배열 끝까지의 요소들을 순차적으로 스왑하며 재귀 호출을 수행합니다.
- 재귀 깊이가 배열의 길이와 같아지면 현재 배열 상태를 결과 리스트에 추가합니다.

## 🧮 정답 계산식

현재 인덱스 idx에서 배열 끝까지의 각 요소 i에 대해 swap(nums[idx], nums[i])를 수행하고 재귀 호출 후 다시 원상복구(backtrack)합니다.

## 🔍 구현 흐름

1. 결과를 저장할 리스트를 초기화합니다.
2. 백트래킹 함수를 호출하여 현재 인덱스부터 순열 생성을 시작합니다.
3. 재귀 종료 조건인 인덱스가 배열 길이와 같아지는 시점에 현재 배열을 복사하여 결과 리스트에 추가합니다.
4. 현재 인덱스부터 배열 끝까지 반복문을 돌며 요소를 스왑하고 다음 단계로 재귀 호출합니다.
5. 재귀 호출 이후 다시 스왑을 수행하여 배열을 이전 상태로 되돌립니다.

## ⚠️ 주의할 점

- 재귀 호출 시 배열을 복사하여 결과 리스트에 넣지 않으면 참조값이 저장되어 최종 결과가 모두 동일해질 수 있습니다.
- 스왑 후 재귀 호출이 끝나면 반드시 다시 스왑하여 배열을 원래 상태로 복구해야 합니다.

## 📁 제출 코드

- 풀이 파일: [solution.java](./solution.java)
- 수집 위치: `Data Structures & Algorithms/permutations/submission-0.java`

## ⏱️ 복잡도 분석

- 시간 복잡도: O(N * N!)
- 공간 복잡도: O(N)

## ✅ 한 줄 요약

백트래킹과 스왑 연산을 활용하여 주어진 고유 정수 배열의 모든 순열을 생성하는 문제입니다.
