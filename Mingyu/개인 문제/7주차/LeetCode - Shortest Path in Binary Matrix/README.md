# 🧩 Shortest Path in Binary Matrix

## 📌 문제 정보

| 항목 | 내용 |
| --- | --- |
| 플랫폼 | NeetCode |
| 문제 번호 | 1091 |
| 난이도 | Medium |
| 분류 | Array, Breadth-First Search, Matrix |
| 언어 | Java |
| 제출 일자 | 2026년 05월 14일 10:44:18 |
| 문제 링크 | [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) |
| 원본 경로 | `Data Structures & Algorithms/shortest-path-in-binary-matrix/submission-0.java` |

## 📝 문제 설명

- You are given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1. A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that: All the visited cells of the path are 0…
- 주요 제약: 1 <= grid.length == grid[i].length <= 100 / grid[i][j] is 0 or 1.
- 핵심 분류: Array, Breadth-First Search, Matrix
- 문제 원문 전체는 저장하지 않고, 링크와 요약 정보만 보관합니다.

## 📥 입력

```text
grid = [
 [0,1,0],
 [1,0,0],
 [1,1,0]
]
```

## 📤 출력

```text
3
```

## 💡 핵심 아이디어

- 배열을 한 번 이상 순회하면서 필요한 상태를 누적한다.
- BFS로 같은 거리의 상태를 차례대로 확장한다.
- 행과 열의 경계 조건, 방문 처리, 방향 이동을 함께 관리한다.

## 🧮 정답 계산식

정답은 조건을 만족하는 노드/칸/컴포넌트를 탐색하며 누적합니다.

## 🔍 구현 흐름

1. 입력으로 주어진 값과 예외 케이스를 먼저 정리한다.
2. 큐를 사용해 가까운 상태부터 방문하고, 방문 여부를 함께 관리한다.
3. 정답 조건을 만족하면 결과를 갱신하거나 즉시 반환한다.
4. 모든 입력을 처리한 뒤 최종 결과를 반환한다.

## ⚠️ 주의할 점

- 제약 조건: 1 <= grid.length == grid[i].length <= 100 / grid[i][j] is 0 or 1.
- 방문 처리 시점이 늦으면 중복 방문이나 무한 탐색이 생길 수 있다.

## 📁 제출 코드

- 풀이 파일: [solution.java](./solution.java)
- 수집 위치: `Data Structures & Algorithms/shortest-path-in-binary-matrix/submission-0.java`

## ⏱️ 복잡도 분석

- 시간 복잡도: 직접 분석 필요
- 공간 복잡도: 직접 분석 필요

## ✅ 한 줄 요약

Shortest Path in Binary Matrix은 Array, Breadth-First Search 관점에서 핵심 조건을 빠르게 판별하는 문제입니다.
