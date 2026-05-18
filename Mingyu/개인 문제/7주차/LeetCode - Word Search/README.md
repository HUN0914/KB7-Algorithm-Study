# 🧩 Word Search

## 📌 문제 정보

| 항목 | 내용 |
| --- | --- |
| 플랫폼 | NeetCode |
| 문제 번호 | 79 |
| 난이도 | Medium |
| 분류 | Array, String, Backtracking, Depth-First Search, Matrix |
| 언어 | Java |
| 제출 일자 | 2026년 05월 18일 13:51:45 |
| 문제 링크 | [Word Search](https://leetcode.com/problems/word-search/) |
| 원본 경로 | `Data Structures & Algorithms/search-for-word/submission-0.java` |
<!-- AI_ANALYSIS: version=v1 model=gemini-3.1-flash-lite hash=23f8f34b136c651f -->

## 📝 문제 설명

Given a 2-D grid of characters `board` and a string `word`, return `true` if the word is present in the grid, otherwise return `false`.

For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

**Example 1:**

```text
Input:
board = [
 ["A","B","C","D"],
 ["S","A","A","T"],
 ["A","C","A","E"]
],
word = "CAT"

Output: true
```

**Example 2:**

```text
Input:
board = [
 ["A","B","C","D"],
 ["S","A","A","T"],
 ["A","C","A","E"]
],
word = "BAT"

Output: false
```

**Constraints:**

- `1 <= board.length, board[i].length <= 5`

- `1 <= word.length <= 10`

- `board` and `word` consists of only lowercase and uppercase English letters.

## 📥 입력

```text
board = [
 ["A","B","C","D"],
 ["S","A","A","T"],
 ["A","C","A","E"]
],
word = "CAT"
```

## 📤 출력

```text
true
```

## 💡 핵심 아이디어

- 격자의 모든 셀을 시작점으로 하여 단어를 찾을 수 있는지 확인하는 완전 탐색 기반의 DFS를 수행합니다.
- 방문한 셀은 다시 사용하지 않도록 임시 문자로 변경하여 중복 사용을 방지합니다.
- 재귀 호출이 종료된 후에는 변경했던 셀을 원래 값으로 복구하는 백트래킹을 적용합니다.

## 🧮 정답 계산식

현재 셀의 문자가 단어의 현재 인덱스 문자와 일치하고, 상하좌우 인접한 셀로 이동하며 단어의 끝까지 도달할 수 있는지 판별합니다.

## 🔍 구현 흐름

1. 격자의 모든 좌표를 순회하며 단어의 첫 글자와 일치하는 시작점을 찾습니다.
2. DFS 함수를 호출하여 현재 위치에서 단어의 다음 글자를 탐색합니다.
3. 현재 셀을 방문 처리하고 상하좌우 4방향으로 재귀 탐색을 진행합니다.
4. 단어의 모든 글자를 찾으면 true를 반환하고, 탐색 실패 시 방문 처리를 해제하여 백트래킹합니다.

## ⚠️ 주의할 점

- 재귀 호출 시 방문했던 셀을 다시 방문하지 않도록 상태를 변경하고, 탐색이 끝난 후 반드시 원래 값으로 복구해야 합니다.
- 격자의 경계 조건을 정확히 체크하여 배열 인덱스 초과 오류를 방지해야 합니다.

## 📁 제출 코드

- 풀이 파일: [solution.java](./solution.java)
- 수집 위치: `Data Structures & Algorithms/search-for-word/submission-0.java`

## ⏱️ 복잡도 분석

- 시간 복잡도: O(N * 3^L), 여기서 N은 격자의 셀 개수, L은 단어의 길이입니다.
- 공간 복잡도: O(L), 재귀 호출 스택의 깊이는 단어의 길이와 비례합니다.

## ✅ 한 줄 요약

격자 내에서 DFS와 백트래킹을 활용하여 특정 단어를 구성하는 경로가 존재하는지 탐색하는 문제입니다.
