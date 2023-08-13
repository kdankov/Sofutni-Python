def find_Kate(mx):
    for i in range(len(mx)):
        for j in range(len(mx[i])):
            if mx[i][j] == 'k':
                return i, j
 
 
def move_Kate(mx, directions, moves=[], count=0):
    while True:
        position = find_Kate(mx)
        if position is None:
            if not moves:
                return 'Kate cannot get out'
            else:
                return min(moves)
        else:
            r, c = position
        mx[r][c] = '$'
        for direction in directions:
            if r + directions[direction][0] < len(mx) and 0 <= c + directions[direction][1] < len(mx[r]):
                if mx[r + directions[direction][0]][c + directions[direction][1]] == ' ':
                    mx[r + directions[direction][0]][c + directions[direction][1]] = 'k'
                    move_Kate(mx, directions, moves, count + 1)
            else:
                count += 1
                moves.append(count)
 
 
maze = [list(input()) for _ in range(int(input()))]
movement = {
    'U': [-1, 0],
    'D': [1, 0],
    'R': [0, 1],
    'L': [0, -1],
}
res = move_Kate(maze, movement)
if str(res).isdigit():
    print(f'Kate got out in {res} moves')
else:
    print(res)
    