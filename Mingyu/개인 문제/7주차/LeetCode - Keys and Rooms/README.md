# 🧩 Keys and Rooms

## 📌 문제 정보

| 항목 | 내용 |
| --- | --- |
| 플랫폼 | LeetCode |
| 문제 번호 | 841 |
| 난이도 | Medium |
| 분류 | Depth-First Search, Breadth-First Search, Graph Theory |
| 언어 | Java |
| 제출 일자 | 2026년 05월 13일 15:50:27 |
| 문제 링크 | [Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/) |
| 원본 경로 | `Only in LeetCode/0841-keys-and-rooms/0841-keys-and-rooms.java` |

## 📝 문제 설명

- There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key. When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, a…
- 주요 제약: n == rooms.length / 2 <= n <= 1000
- 핵심 분류: Depth-First Search, Breadth-First Search, Graph Theory
- 문제 원문 전체는 저장하지 않고, 링크와 요약 정보만 보관합니다.

## 📥 입력

```text
rooms = [[1],[2],[3],[]]
```

## 📤 출력

```text
true
```

설명: We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.

## 💡 핵심 아이디어

- DFS로 연결된 상태를 깊게 따라가며 방문 여부를 관리한다.
- BFS로 같은 거리의 상태를 차례대로 확장한다.
- 노드와 간선의 연결 관계를 기준으로 방문 가능한 영역을 탐색한다.

## 🧮 정답 계산식

정답은 조건을 만족하는 노드/칸/컴포넌트를 탐색하며 누적합니다.

## 🔍 구현 흐름

1. 입력으로 주어진 값과 예외 케이스를 먼저 정리한다.
2. 큐를 사용해 가까운 상태부터 방문하고, 방문 여부를 함께 관리한다.
3. 정답 조건을 만족하면 결과를 갱신하거나 즉시 반환한다.
4. 모든 입력을 처리한 뒤 최종 결과를 반환한다.

## ⚠️ 주의할 점

- 제약 조건: n == rooms.length / 2 <= n <= 1000 / 0 <= rooms[i].length <= 1000
- 방문 처리 시점이 늦으면 중복 방문이나 무한 탐색이 생길 수 있다.

## 📁 제출 코드

- 풀이 파일: [solution.java](./solution.java)
- 수집 위치: `Only in LeetCode/0841-keys-and-rooms/0841-keys-and-rooms.java`

## ⏱️ 복잡도 분석

- 시간 복잡도: 직접 분석 필요
- 공간 복잡도: 직접 분석 필요

## ✅ 한 줄 요약

Keys and Rooms은 Depth-First Search, Breadth-First Search 관점에서 핵심 조건을 빠르게 판별하는 문제입니다.
