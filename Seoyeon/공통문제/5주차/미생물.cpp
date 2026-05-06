#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <utility>

using namespace std;

int N, Q;
int board[15][15];

// 상하좌우 
int dr[4] = { 1, -1, 0, 0 };
int dc[4] = { 0, 0, -1, 1 };

// 미생물 무리 정보
struct Group {
	int id;		// 미생물 번호
	int area;	// 미생물 영역(차지한 칸 수)
	vector<pair<int, int>> cells; // 이 미생물이 차지한 좌표들
};

// id번 미생물이 하나의 함수로 연결되어 있는지 확인하는 함수
bool isConnected(int id) {
	bool visited[15][15] = {};
	vector<pair<int, int>> cells;

	// 보드 전체를 보면서 id번 미생물이 있는 칸들을 모두 모은다.
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < N; c++) {
			if (board[r][c] == id) {
				cells.push_back({ r, c });
			}
		}
	}

	// 해당 미생물이 아예 없으면 연결성 체크할 필요 없음
	if (cells.empty()) return true;

	queue<pair<int, int>> q; // 다음에 방문할 칸들 저장(BFS)

	// id번 미생물의 첫번째 칸에서 bfs시작
	q.push(cells[0]);
	visited[cells[0].first][cells[0].second] = true;

	int cnt = 0; // BFS로 방문한 id번 미생물 칸 개수

	while (!q.empty()) {
		pair<int, int> cur = q.front();
		q.pop();

		int r = cur.first;
		int c = cur.second;

		cnt++;

		// 현재 칸에서 상하좌우 확인
		for (int d = 0; d < 4; d++) {
			int nr = r + dr[d];
			int nc = c + dc[d];

			// 범위 밖이면 무시
			if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;

			// 이미 방문한 칸이면 무시
			if (visited[nr][nc]) continue;

			// 같은 id의 미생물이 아니면 이동 불가
			if (board[nr][nc] != id) continue;

			// 나머지는 같은 id의 미생물!
			visited[nr][nc] = true;
			q.push({ nr, nc });
		}
	}

	// 전체 id칸 개수와 BFS로 방문한 칸 개수가 같으면 한 덩어리
	// 다르면 중간이 끊겨서 여러 덩어리로 나뉜 것
	return cnt == (int)cells.size(); // 왜 int로 굳이 다시 형변환?
									 //-> cells.size() → size_t (unsigned long long)
}

// 투입 후 쪼개진 미생물 무리를 제거하는 함수
void removeSplitGroups(){
	set<int> ids;

	// 현재 board에 존재하는 미생물 번호를 set에 모은다
	// set사용 이유: 같은 id가 여러칸에 있어도 한번만 저장하려고
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < N; c++) {
			if (board[r][c] != 0) {
				ids.insert(board[r][c]);
			}
		}
	}

	vector<int> removeIds;

	// 각 미생물이 하나의 덩어리인지 확인
	for (int id : ids) {
		if (!isConnected(id)) {
			removeIds.push_back(id);
		}
	}

	// 나뉜 미생물은 board에서 전부 삭제
	for (int id : removeIds) {
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < N; c++) {
				if (board[r][c] == id) {
					board[r][c] = 0;
				}
			}
		}
	}
}

void moveToNewBoard() {
	// 1) 현재 board에서 미생물 그룹 정보 수집
	map<int, vector<pair<int, int>>> mp;
	// -> map 사용 이유 : 미생물들의 좌표는 board에서 흩어져있으므로 같은 id끼리 한번에 묶기 위해!
	// key : 미생물 id
	// value : 그 미생물이 차지한 좌표 목록


	// 현재 board를 전체 탐색하면서 미생물 id별로 좌표 모은다.
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < N; c++) {

			// 빈칸은 무시
			if (board[r][c] != 0) {
				// board[r][c]번 미생물이 (r, c) 차지
				// => 해당 id의 vector에 좌표 추가
				mp[board[r][c]].push_back({ r, c });
			}
		}
	}
	/*
	mp에는 이런 식으로 저장됨:
        mp[1] = { {0,0}, {0,1}, {1,0} }
        mp[2] = { {3,3}, {3,4} }
        mp[5] = { {2,1}, {2,2}, {2,3} }

	그런데 앞으로 정렬하려면
	id, area, cells를 하나로 묶은 Group 구조체가 편함.
	*/

	vector<Group> groups;

	// map에 저장된 미생물들을 Group 형태로 바꿔서 groups에 넣는다.
	for (auto p : mp) {
		int id = p.first;	// 미생물 번호
		vector<pair<int, int>> cells = p.second; // 해당 미생물 좌표들
		int area = (int)cells.size();	// 칸 개수

		groups.push_back({ id, area, cells });
	}

	/*
		문제 조건:
		1. 차지한 영역이 넓은 미생물 먼저 이동
		2. 넓이가 같으면 먼저 투입된 미생물 먼저 이동

		먼저 투입된 미생물 = id가 작은 미생물
		왜냐하면 실험마다 id를 1, 2, 3, ... 순서로 붙였기 때문
	*/

	sort(groups.begin(), groups.end(), [](Group& a, Group& b) {
		// 넓이가 다르면 넓은 것 먼저
		if (a.area != b.area) return a.area > b.area;

		// 넓이가 같으면 id 작은 것 먼저
		return a.id < b.id;
	});

	// 새 배양 용기
	// 처음에는 아무 미생물도 없으므로 전부 0
	int newBoard[15][15] = {};

	// 정렬된 순서대로 미생물을 하나씩 새 용기에 배치하기
	for (auto& g : groups) {
		// 좌표를 상대좌표로 바꾸기
		// (위치는 이동, 모양은 유지)
		int minR = 100;
		int minC = 100;

		// 이 미생물이 차지하는 좌표중 가장작은 r, c찾기
		for (auto cell : g.cells) {
			int r = cell.first;
			int c = cell.second;

			minR = min(minR, r);
			minC = min(minC, c);
		}

		// shape에는 상대좌표 저장
		vector<pair<int, int>> shape;

		// 상대좌표 기준으로 가장 큰 r, c
		// 이걸 알아야 배양 용기 밖으로 나가는지 확인가능
		int maxR = 0;
		int maxC = 0;

		for (auto cell : g.cells) {
			int r = cell.first;
			int c = cell.second;

			// 기존 좌표에서 최소좌표를 빼서 상대좌표로 변환
			int nr = r - minR;
			int nc = c - minC;

			shape.push_back({ nr, nc });

			maxR = max(maxR, nr);
			maxC = max(maxC, nc);
		}

		// -> 새 용기의 어느 위치에 넣을지 찾아야함.
		bool placed = false;

		/*
		문제 조건:
            가능한 위치 중 x좌표가 가장 작은 위치
            같으면 y좌표가 가장 작은 위치
		*/
		for (int sr = 0; sr + maxR < N && !placed; sr++) { // (sr, sc) -> 새 배양판의 기준좌표(start row, start column 뜻함)
			for (int sc = 0; sc + maxC < N && !placed; sc++) {
				bool ok = true;

				// 이 위치에 놓을 수 있는지 검사
				for (auto s : shape) {
					int nr = sr + s.first;
					int nc = sc + s.second;

					// 이미 다른 미생물이 있으면 겹치므로 불가능
					if (newBoard[nr][nc] != 0) {
						ok = false;
						break;
					}
				}

				// 놓을 수 있다면 실제로 배치
				if (ok) {
					for (auto s : shape) {
						int nr = sr + s.first;
						int nc = sc + s.second;

						newBoard[nr][nc] = g.id;
					}
					// 배치 완료
					placed = true;
				}
				
			}
		}
		// placed = false이면 문제 조건에 따라 미생물이 새 배양용기로 옮겨지지않고 삭제되므로
		// 따로 코드 불필요	
	}
	// 모든 미생물 이동이 끝났으므로
	// 기존 board를 newBoard로 교체함.
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < N; c++) {
			board[r][c] = newBoard[r][c];
		}
	}
}

// 현재 board상태에서 실험결과 점수를 계산하는 함수
long long getScore() {
	// 점수계산에는 각 미생물의 넓이가 필요
	// 먼저 미생물 id별 넓이 구하기
	map<int, int> area; // key : 미생물 id, value : 해당 미생물의 넓이

	// board 전체를 돌면서 미생물 별 칸 개수 센다.
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < N; c++) {
			if (board[r][c] != 0) {
				int id = board[r][c];

				// id번 미생물의 칸 수 1 증가
				area[id]++;
			}
		}
	}

	/*
	인접한 미생물 쌍 찾기
	-> 같은 두 미생물이 여러 면으로 붙어 있을 수 있음 => set사용(중복 저장 막기)
	*/

	set<pair<int, int>> pairs;

	// board 전체 탐색
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < N; c++) {
			// 빈 칸이면 볼 필요 x
			if (board[r][c] == 0) continue;

			// 현재 칸의 미생물 번호
			int curId = board[r][c];

			// 상하좌우 확인
			for (int d = 0; d < 4; d++) {
				int nr = r + dr[d];
				int nc = c + dc[d];

				// 범위 밖이면 무시
				if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;

				// 옆칸이 빈칸이면 인접한 미생물 없음
				if (board[nr][nc] == 0) continue;

				// 옆칸의 미생물번호
				int nextId = board[nr][nc];

				// 같은 미생물끼리는 점수 계산 대상 아님
				if (curId == nextId) continue;

				/*
				pair를 할때 (2, 5)와 (5, 2)는 같지만 set은 다른쌍으로 인식함.
				-> 항상 작은 번호를 앞에 두도록 정리한다.
				*/

				int a = curId;
				int b = nextId;
				if (a > b) swap(a, b);

				pairs.insert({ a, b });
			}
		}
	}

	// 이제 pairs에는 인접한 미생물 쌍만 들어있음
	long long score = 0;

	// 각 인접 쌍에 대해 넓이 곱을 점수에 더한다.
	for (auto p : pairs) {
		int a = p.first;
		int b = p.second;

		score += 1LL * area[a] * area[b];
	}

	return score;
}

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> N >> Q;

	// Q번 실험 반복
	for (int id = 1; id <= Q; id++) {
		int r1, c1, r2, c2;
		cin >> r1 >> c1 >> r2 >> c2;

		// 1) 미생물 투입
		for (int r = r1; r < r2; r++) {
			for (int c = c1; c < c2; c++) {
				board[r][c] = id;
			}
		}

		// 2) 쪼개진 기존 미생물 제거
		removeSplitGroups();

		// 3) 새 배양 용기로 이동
		moveToNewBoard();

		// 4) 점수 계산
		long long result = getScore();

		cout << result << "\n";
	}


	return 0;
}
