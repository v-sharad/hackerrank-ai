def find_dust(board):
    dust_position = [(rnum,cnum) for rnum,row in enumerate(board) for cnum,element in enumerate(row) if element=='d']
    return dust_position[0][0],dust_position[0][1]

def nextMove(posr, posc, board,dustr,dustc):
    if board[posr][posc] != 'd':
        if dustr > posr:
            print("DOWN")
            posr += 1
        elif dustr < posr:
            print("UP")
            posr -= 1
        elif dustc > posc:
            print("RIGHT")
            posc += 1
        else:
            print("LEFT")
            posc -= 1
        #print(posr, posc, board,dustr,dustc)
        #nextMove(posr, posc, board,dustr,dustc)
    else:
        print("CLEAN")
        #dustr,dustc = find_dust(board)

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    dustr,dustc = find_dust(board)
    nextMove(pos[0], pos[1], board,dustr,dustc)
