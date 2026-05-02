from collections import deque
d = [[-1,-1], [-1,0], [0,-1], [1,1], [1,0], [0,1], [1,-1], [-1,1]]

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        R, C = len(board), len(board[0])
        q = deque([(click[0], click[1])])

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        while q:
            x, y = q.popleft()
            
            if board[x][y] != 'E':
                continue
            
            cnt = 0
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if 0<=nx<R and 0<=ny<C:
                    if board[nx][ny] == 'M':
                        cnt += 1
                
            if cnt > 0: # 주변에 폭탄이 1개 이상 있는 경우
                board[x][y] = str(cnt)
            else: # 주변에 지뢰가 없는 경우 (재귀적으로 주변 확장)
                board[x][y] = 'B'
                for dx, dy in d:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<R and 0<=ny<C:
                        if board[nx][ny] == 'E':
                            q.append((nx, ny))
                    
        return board