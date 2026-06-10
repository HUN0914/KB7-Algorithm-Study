# 🧩 Valid Palindrome

## 📌 문제 정보

| 항목 | 내용 |
| --- | --- |
| 플랫폼 | NeetCode |
| 문제 번호 | 125 |
| 난이도 | Easy |
| 분류 | Two Pointers, String |
| 언어 | Java |
| 제출 일자 | 2026년 06월 10일 11:43:37 |
| 문제 링크 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) |
| 원본 경로 | `Data Structures & Algorithms/is-palindrome/submission-0.java` |
<!-- AI_ANALYSIS: version=v1 model=gemini-3.1-flash-lite hash=3167cb13718de982 -->

## 📝 문제 설명

Given a string `s`, return `true` if it is a **palindrome**, otherwise return `false`.

A **palindrome** is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

**Note:** Alphanumeric characters consist of letters `(A-Z, a-z)` and numbers `(0-9)`.

**Example 1:**

```text
Input: s = "Was it a car or a cat I saw?"

Output: true
```

Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

**Example 2:**

```text
Input: s = "tab a cat"

Output: false
```

Explanation: "tabacat" is not a palindrome.

**Constraints:**

- `1 <= s.length <= 1000`

- `s` is made up of only printable ASCII characters.

## 📥 입력

```text
s = "Was it a car or a cat I saw?"
```

## 📤 출력

```text
true
```

## 💡 핵심 아이디어

- 문자열의 양 끝에서 시작하는 두 개의 포인터를 사용하여 중앙으로 이동하며 비교합니다.
- 알파벳과 숫자가 아닌 문자는 무시하고 건너뛰는 로직을 적용합니다.
- 대소문자를 구분하지 않기 위해 비교 시 모든 문자를 소문자로 변환합니다.

## 🧮 정답 계산식

양쪽 포인터가 가리키는 유효한 문자가 모두 일치할 때까지 반복하며, 불일치하는 순간 false를 반환합니다.

## 🔍 구현 흐름

1. 문자열의 시작과 끝을 가리키는 두 포인터를 초기화합니다.
2. 왼쪽 포인터가 가리키는 문자가 알파벳이나 숫자가 아니면 오른쪽으로 이동합니다.
3. 오른쪽 포인터가 가리키는 문자가 알파벳이나 숫자가 아니면 왼쪽으로 이동합니다.
4. 두 포인터가 가리키는 문자를 소문자로 변환하여 비교하고 다르면 false를 반환합니다.
5. 포인터를 각각 안쪽으로 한 칸씩 이동하며 반복합니다.
6. 반복문이 종료되면 true를 반환합니다.

## ⚠️ 주의할 점

- 두 포인터가 교차하거나 만날 때까지 반복문이 안전하게 종료되도록 left < right 조건을 유지해야 합니다.
- 문자열 내에 알파벳이나 숫자가 하나도 없는 경우 빈 문자열과 동일하게 처리되어 true가 반환됨을 인지해야 합니다.

## 📁 제출 코드

- 풀이 파일: [solution.java](./solution.java)
- 수집 위치: `Data Structures & Algorithms/is-palindrome/submission-0.java`

## ⏱️ 복잡도 분석

- 시간 복잡도: O(n)
- 공간 복잡도: O(1)

## ✅ 한 줄 요약

투 포인터 기법을 활용하여 비알파벳 문자를 건너뛰며 대소문자 구분 없이 회문 여부를 판별합니다.
