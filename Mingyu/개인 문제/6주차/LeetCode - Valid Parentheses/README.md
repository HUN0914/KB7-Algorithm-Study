# 🧩 Valid Parentheses

## 📌 문제 정보

| 항목 | 내용 |
| --- | --- |
| 플랫폼 | NeetCode |
| 문제 번호 | 20 |
| 난이도 | Easy |
| 분류 | String, Stack |
| 언어 | Java |
| 제출 일자 | 2026년 05월 11일 15:52:16 |
| 문제 링크 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) |
| 원본 경로 | `Data Structures & Algorithms/validate-parentheses/submission-2.java` |

## 📝 문제 설명

- You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'. The input string s is valid if and only if: Return true if s is a valid string, and false otherwise.
- 주요 제약: 1 <= s.length <= 1000
- 핵심 분류: String, Stack
- 문제 원문 전체는 저장하지 않고, 링크와 요약 정보만 보관합니다.

## 📥 입력

```text
s = "[]"
```

## 📤 출력

```text
true
```

## 💡 핵심 아이디어

- 문자 단위의 순서, 빈도, 짝 관계를 명확히 관리한다.
- 최근에 열린 상태를 스택에 저장하고 닫히는 조건과 매칭한다.

## 🧮 정답 계산식

입력에서 요구 조건을 만족하는 값을 계산해 반환합니다.

## 🔍 구현 흐름

1. 입력으로 주어진 값과 예외 케이스를 먼저 정리한다.
2. 스택에 아직 처리되지 않은 후보를 유지하며 현재 값과 비교한다.
3. 정답 조건을 만족하면 결과를 갱신하거나 즉시 반환한다.
4. 모든 입력을 처리한 뒤 최종 결과를 반환한다.

## ⚠️ 주의할 점

- 제약 조건: 1 <= s.length <= 1000
- 스택이 비어 있는 상태에서 top을 참조하지 않도록 처리한다.

## 📁 제출 코드

- 풀이 파일: [solution.java](./solution.java)
- 수집 위치: `Data Structures & Algorithms/validate-parentheses/submission-2.java`

## ⏱️ 복잡도 분석

- 시간 복잡도: O(n)
- 공간 복잡도: O(n)

## ✅ 한 줄 요약

Valid Parentheses은 String, Stack 관점에서 핵심 조건을 빠르게 판별하는 문제입니다. 목표 시간 복잡도는 O(n)입니다.
