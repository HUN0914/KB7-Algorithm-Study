# 🧩 Two Sum

## 📌 문제 정보

| 항목 | 내용 |
| --- | --- |
| 플랫폼 | NeetCode |
| 문제 번호 | 1 |
| 난이도 | Easy |
| 분류 | Array, Hash Table |
| 언어 | Java |
| 제출 일자 | 2026년 05월 12일 11:12:14 |
| 문제 링크 | [Two Sum](https://leetcode.com/problems/two-sum/) |
| 원본 경로 | `Data Structures & Algorithms/two-integer-sum/submission-1.java` |

## 📝 문제 설명

- Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j. You may assume that every input has exactly one pair of indices i and j that satisfy the condition. Return the answer with the smaller index first.
- 주요 제약: 2 <= nums.length <= 1000 / -10,000,000 <= nums[i] <= 10,000,000
- 핵심 분류: Array, Hash Table
- 문제 원문 전체는 저장하지 않고, 링크와 요약 정보만 보관합니다.

## 📥 입력

```text
nums = [3,4,5,6], target = 7
```

## 📤 출력

```text
[0,1]
```

## 💡 핵심 아이디어

- 배열을 한 번 이상 순회하면서 필요한 상태를 누적한다.
- 해시 기반 조회로 이미 본 값이나 필요한 보완 값을 빠르게 찾는다.

## 🧮 정답 계산식

요구 조건 `nums[i] + nums[j] == target`을 만족하는 값을 계산합니다.

## 🔍 구현 흐름

1. 입력으로 주어진 값과 예외 케이스를 먼저 정리한다.
2. 빠른 조회가 필요한 값을 해시맵 또는 해시셋에 저장한다.
3. 정답 조건을 만족하면 결과를 갱신하거나 즉시 반환한다.
4. 모든 입력을 처리한 뒤 최종 결과를 반환한다.

## ⚠️ 주의할 점

- 제약 조건: 2 <= nums.length <= 1000 / -10,000,000 <= nums[i] <= 10,000,000 / -10,000,000 <= target <= 10,000,000
- 같은 값을 여러 번 사용할 수 있는지, 인덱스 중복이 허용되는지 확인한다.

## 📁 제출 코드

- 풀이 파일: [solution.java](./solution.java)
- 수집 위치: `Data Structures & Algorithms/two-integer-sum/submission-1.java`

## ⏱️ 복잡도 분석

- 시간 복잡도: O(n)
- 공간 복잡도: O(n)

## ✅ 한 줄 요약

Two Sum은 Array, Hash Table 관점에서 핵심 조건을 빠르게 판별하는 문제입니다. 목표 시간 복잡도는 O(n)입니다.
