'''
total amount of tiles laid 2005
black tiles were laid around white ones as 1-tile width perimeter
how many white tiles are there?
'''

def count_w_tiles(total, perim_w = 1):
    if type(total) not in [float, int] or total < 9:
        print('wrong input')
        return
    
    print(f'total tiles: {total}')
    rows = perim_w * 2                      #perimeter left and right
    found = 0                               #counter for answers
    whole = lambda b: b.is_integer() and b > 0  #whole tiles
    col_f = lambda: (total - rows * (perim_w * 2)) / rows   #num of colomns

    while col_f() > perim_w * 2:            #really want that := operatior in python 3.8
        rows += 1                           #starting with perimeter tiles +1 white
        length_x = rows * 2                 #top and bottom black rows 
        col = col_f()
        
        whites = col * (rows - perim_w * 2) #number of rows - black perimeter
        blacks = col * (perim_w *2) + length_x  #perimeter + top+bottom
        if (whole(whites) and whole(blacks) and whole(col)):
            found += 1
            print(f'Option: {found}\n\twhite tiles: {int(whites)} \
                  \n\tblack tiles: {int(blacks)} \n\trows: {rows} \
                  \n\tcolumns: {int(col)+perim_w*2}\n')
    if not found:
        print(f'can\'t lay {total} tiles in given way')

count_w_tiles(2005)
