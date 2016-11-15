# sudoku solver
import sys
sys.stdin = open('sudoku.txt', 'r')
sudokus = list()
op = ''
for line in sys.stdin:
	if "Grid" in line:
		op+='*'
	else:
		op+=line
	
temp = op.split('*')
temp = temp[1:]

for each in temp:
	each = each.split('\n')
	#each = each[:-1]
	each = [[eval(x) for x in y] for y in each]
	sudokus.append(each)


def check(sudoku, xx, yy, t):
    a = 3*(xx/3)
    b = 3*(yy/3)
    #check in the box
    for x in range(a, a+3):
        for y in range(b, b+3):
            if x!=xx and y!=yy and sudoku[x][y]==t:
                return False
    #check in the row
    for x in range(9):
        if x!=xx and sudoku[x][yy]==t:
            return False
    #check in the column
    for y in range(9):
        if y!=yy and sudoku[xx][y]==t:
            return False
    return True

def noEmpty(sudoku):
    for x in range(9):
        for y in range(9):
            if sudoku[x][y]==0:
                return False
    return True

def solve(sudoku):
    if noEmpty(sudoku):
        return [True, sudoku]
    for x in range(9):
        for y in range(9):
            if sudoku[x][y]==0:
                for t in range(1,10):
                    sudoku[x][y] = t
                    if check(sudoku, x, y, t):
                        if solve(sudoku)[0]==True:
                            return [True, sudoku]
                sudoku[x][y]=0
                return [False, sudoku]

def printsudoku(sudoku):
	for x in sudoku:
		for y in x:
			print y,
		print '\n'
	
print len(sudokus[-1])
#assert False
# solve the sudokus here
s=0
cnt = 0
for x in sudokus:
	cnt+=1
	solve(x)
	printsudoku(x)
	print "***", cnt
	s+=(eval(str(x[0][0])+str(x[0][1])+str(x[0][2])))
print s
