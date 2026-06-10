# 🧩 Find if Path Exists in Graph

## 📌 문제 정보

| 항목 | 내용 |
| --- | --- |
| 플랫폼 | LeetCode |
| 문제 번호 | 1971 |
| 난이도 | Easy |
| 분류 | Depth-First Search, Breadth-First Search, Union-Find, Graph Theory |
| 언어 | Java |
| 제출 일자 | 2026년 06월 08일 16:23:28 |
| 문제 링크 | [Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/) |
| 원본 경로 | `Only in LeetCode/1971-find-if-path-exists-in-graph/1971-find-if-path-exists-in-graph.java` |
<!-- AI_ANALYSIS: version=v1 model=gemini-3.1-flash-lite hash=6305148071ba6c94 -->

## 📝 문제 설명

There is a **bi-directional** graph with `n` vertices, where each vertex is labeled from `0` to `n - 1` (**inclusive**). The edges in the graph are represented as a 2D integer array `edges`, where each `edges[i] = [ui, vi]` denotes a bi-directional edge between vertex `ui` and vertex `vi`. Every vertex pair is connected by **at most one** edge, and no vertex has an edge to itself.

You want to determine if there is a **valid path** that exists from vertex `source` to vertex `destination`.

Given `edges` and the integers `n`, `source`, and `destination`, return `true`*if there is a **valid path** from*`source`*to*`destination`*, or*`false`*otherwise**.*

**Example 1:**

```text
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 &rarr; 1 &rarr; 2
- 0 &rarr; 2
```

**Example 2:**

```text
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
```

**Constraints:**

- `1 <= n <= 2 * 105`

- `0 <= edges.length <= 2 * 105`

- `edges[i].length == 2`

- `0 <= ui, vi <= n - 1`

- `ui != vi`

- `0 <= source, destination <= n - 1`

- There are no duplicate edges.

- There are no self edges.

## 📥 입력

```text
n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
```

## 📤 출력

```text
true
```

설명: There are two paths from vertex 0 to vertex 2:
- 0 &rarr; 1 &rarr; 2
- 0 &rarr; 2

## 💡 핵심 아이디어

- 그래프의 연결성을 확인하기 위해 유니온 파인드(Union-Find) 자료구조를 활용한다.
- 모든 간선을 순회하며 각 정점들을 하나의 집합으로 병합한다.
- 최종적으로 출발 정점과 도착 정점의 루트 노드가 동일한지 확인하여 경로 존재 여부를 판별한다.

## 🧮 정답 계산식

find(source) == find(destination) 연산 결과가 참이면 경로가 존재한다.

## 🔍 구현 흐름

1. 정점의 개수 n을 기반으로 Union-Find 객체를 초기화한다.
2. 주어진 edges 배열을 순회하며 각 간선의 두 정점을 union 연산으로 연결한다.
3. 경로 압축(Path Compression) 기법을 사용하여 find 연산의 효율을 높인다.
4. 랭크 기반 병합(Union by Rank)을 통해 트리의 높이를 최소화한다.
5. source와 destination의 루트 노드를 비교하여 결과를 반환한다.

## ⚠️ 주의할 점

- 정점의 개수가 최대 20만 개에 달하므로 find 연산 시 경로 압축을 반드시 적용해야 시간 초과를 방지할 수 있다.

## 📁 제출 코드

- 풀이 파일: [solution.java](./solution.java)
- 수집 위치: `Only in LeetCode/1971-find-if-path-exists-in-graph/1971-find-if-path-exists-in-graph.java`

## ⏱️ 복잡도 분석

- 시간 복잡도: O(E * α(N))
- 공간 복잡도: O(N)

## ✅ 한 줄 요약

유니온 파인드 알고리즘을 사용하여 그래프 내 두 정점이 같은 연결 요소에 속하는지 판별하는 문제이다.
