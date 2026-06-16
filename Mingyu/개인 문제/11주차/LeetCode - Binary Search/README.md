# 🧩 Binary Search

## 📌 문제 정보

| 항목 | 내용 |
| --- | --- |
| 플랫폼 | NeetCode |
| 문제 번호 | 704 |
| 난이도 | Easy |
| 분류 | Array, Binary Search |
| 언어 | Java |
| 제출 일자 | 2026년 06월 16일 11:24:54 |
| 문제 링크 | [Binary Search](https://leetcode.com/problems/binary-search/) |
| 원본 경로 | `Data Structures & Algorithms/binary-search/submission-0.java` |
<!-- AI_ANALYSIS: version=v1 model=gemini-3.1-flash-lite hash=e0952a8625c599b4 -->

## 📝 문제 설명

You are given an array of **distinct** integers `nums`, sorted in ascending order, and an integer `target`.

Implement a function to search for `target` within `nums`. If it exists, then return its index, otherwise, return `-1`.

Your solution must run in O(logn)O(log n)O(logn) time.

**Example 1:**

```text
Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
```

**Example 2:**

```text
Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1
```

**Constraints:**

- `1 <= nums.length <= 10000`.

- `-10000 < nums[i], target < 10000`

- All the integers in `nums` are **unique**.

## 📥 입력

```text
nums = [-1,0,2,4,6,8], target = 4
```

## 📤 출력

```text
3
```

## 💡 핵심 아이디어

- 정렬된 배열의 특성을 활용하여 탐색 범위를 절반씩 줄여나가는 이진 탐색 알고리즘을 사용합니다.
- 현재 탐색 범위의 중간값을 타겟과 비교하여 탐색 방향을 결정합니다.
- 범위의 시작점과 끝점을 갱신하며 타겟을 찾거나 범위가 교차할 때까지 반복합니다.

## 🧮 정답 계산식

중간값 mid = left + (right - left) / 2를 기준으로 nums[mid]가 target과 같으면 인덱스를 반환하고, 작으면 left를 mid + 1로, 크면 right를 mid - 1로 갱신합니다.

## 🔍 구현 흐름

1. 배열의 시작 인덱스 left와 끝 인덱스 right를 초기화합니다.
2. left가 right보다 작거나 같을 때까지 반복문을 수행합니다.
3. 중간 인덱스 mid를 계산하여 타겟과 비교합니다.
4. 비교 결과에 따라 탐색 범위를 왼쪽 또는 오른쪽 절반으로 좁힙니다.
5. 타겟을 찾으면 해당 인덱스를 반환하고, 반복문 종료 시까지 찾지 못하면 -1을 반환합니다.

## ⚠️ 주의할 점

- 중간값 계산 시 (left + right) / 2를 사용하면 정수 오버플로우가 발생할 수 있으므로 left + (right - left) / 2 방식을 사용해야 합니다.
- 반복문의 조건이 left < right인지 left <= right인지 명확히 구분하여 무한 루프나 인덱스 누락을 방지해야 합니다.

## 📁 제출 코드

- 풀이 파일: [solution.java](./solution.java)
- 수집 위치: `Data Structures & Algorithms/binary-search/submission-0.java`

## ⏱️ 복잡도 분석

- 시간 복잡도: O(log n)
- 공간 복잡도: O(1)

## ✅ 한 줄 요약

정렬된 배열에서 이진 탐색을 통해 타겟의 인덱스를 O(log n) 시간 복잡도로 효율적으로 찾는 알고리즘입니다.
