import sys

def clear_terminal():
    print(chr(27) + "[2J") #Clear terminal


def print_there(x, y, text):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
    #sys.stdout.flush()


def block_color(color):
    #https://gist.gitbub.com/vratiu/9780109
    if color.upper() == 'GREEN':
        return "\033[1;32;42m"
    elif color.upper() == 'WHITE':
        return "\033[0;32;47m"
    elif color.upper() == 'RED':
        return "\033[1;32;41m"
    elif color.upper() == 'BLACK':
        return "\033[1;32;40m"


def print_block(x, y, clear_block, color=None):
    if color == None:
        color = 'white'
    block_format = "{:>1}"
    block_text = ' '
    if not clear_block:
        print_there(x, y, block_color(color) + block_format.format(''))
    else:
        print_there(x, y, block_color('black') + block_format.format(block_text))


def print_blank(x, y):
    switch_list = []
    switch_list.append([1,1,1,1,1])
    switch_list.append([1,1,1,1,1])
    switch_list.append([1,1,1,1,1])
    switch_list.append([1,1,1,1,1])
    switch_list.append([1,1,1,1,1])
    for i in range(0, 25):
        col = i/5
        row = i - (col*5)
        print_block(x+row, y+col, switch_list[row][col])


def print_arrow(x, y, direction):
    switch_list = []
    if direction == 0: # Flat
        switch_list.append([1,1,1,1,1])
        switch_list.append([1,1,1,1,1])
        switch_list.append([1,0,0,0,1])
        switch_list.append([1,1,1,1,1])
        switch_list.append([1,1,1,1,1])
    elif direction == 1: # Up
        switch_list.append([1,1,0,1,1])
        switch_list.append([1,0,1,0,1])
        switch_list.append([0,1,1,1,0])
        switch_list.append([1,1,1,1,1])
        switch_list.append([1,1,1,1,1])
    elif direction == -1: # Down
        switch_list.append([1,1,1,1,1])
        switch_list.append([1,1,1,1,1])
        switch_list.append([0,1,1,1,0])
        switch_list.append([1,0,1,0,1])
        switch_list.append([1,1,0,1,1])
    elif direction == 2: # Fast up
        switch_list.append([1,1,0,1,1])
        switch_list.append([1,0,1,0,1])
        switch_list.append([0,1,0,1,0])
        switch_list.append([1,0,1,0,1])
        switch_list.append([0,1,1,1,0])
    elif direction == -2: # Fast Down
        switch_list.append([0,1,1,1,0])
        switch_list.append([1,0,1,0,1])
        switch_list.append([0,1,0,1,0])
        switch_list.append([1,0,1,0,1])
        switch_list.append([1,1,0,1,1])
    for row in range(0, 5):
        for col in range(0, 5):
            print_block(int(x+row), int(y+col), switch_list[row][col])


def print_single_number(x, y, num, block_color=None):
    #5*5 dot matrix numbers
    switch_list = None
    switch_list = []
    if num == 1:
        switch_list.append([1,0,0,1,1])
        switch_list.append([1,1,0,1,1])
        switch_list.append([1,1,0,1,1])
        switch_list.append([1,1,0,1,1])
        switch_list.append([1,0,0,0,1])
    elif num == 2:
        switch_list.append([0,0,0,0,1])
        switch_list.append([1,1,1,1,0])
        switch_list.append([1,0,0,0,1])
        switch_list.append([0,1,1,1,1])
        switch_list.append([0,0,0,0,0])
    elif num == 3:
        switch_list.append([0,0,0,0,1])
        switch_list.append([1,1,1,1,0])
        switch_list.append([1,1,0,0,1])
        switch_list.append([1,1,1,1,0])
        switch_list.append([0,0,0,0,1])
    elif num == 4:
        switch_list.append([1,1,0,0,1])
        switch_list.append([1,0,1,0,1])
        switch_list.append([0,1,1,0,1])
        switch_list.append([0,0,0,0,0])
        switch_list.append([1,1,1,0,1])
    elif num == 5:
        switch_list.append([0,0,0,0,0])
        switch_list.append([0,1,1,1,1])
        switch_list.append([0,0,0,0,1])
        switch_list.append([1,1,1,1,0])
        switch_list.append([0,0,0,0,1])
    elif num == 6:
        switch_list.append([1,0,0,0,0])
        switch_list.append([0,1,1,1,1])
        switch_list.append([0,0,0,0,1])
        switch_list.append([0,1,1,1,0])
        switch_list.append([1,0,0,0,1])
    elif num == 7:
        switch_list.append([0,0,0,0,0])
        switch_list.append([1,1,1,1,0])
        switch_list.append([1,1,1,0,1])
        switch_list.append([1,1,0,1,1])
        switch_list.append([1,0,1,1,1])
    elif num == 8:
        switch_list.append([1,0,0,0,1])
        switch_list.append([0,1,1,1,0])
        switch_list.append([1,0,0,0,1])
        switch_list.append([0,1,1,1,0])
        switch_list.append([1,0,0,0,1])
    elif num == 9:
        switch_list.append([1,0,0,0,1])
        switch_list.append([0,1,1,1,0])
        switch_list.append([1,0,0,0,0])
        switch_list.append([1,1,1,1,0])
        switch_list.append([0,0,0,0,1])
    elif num == 0:
        switch_list.append([1,0,0,0,1])
        switch_list.append([0,1,1,0,0])
        switch_list.append([0,1,0,1,0])
        switch_list.append([0,0,1,1,0])
        switch_list.append([1,0,0,0,1])
        
    for row in range(0, 5):
        for col in range(0, 5):
            print_block(int(x+row), int(y+col), switch_list[row][col], block_color)



def print_numbers(x, y, nums, block_color=None):
    char_count = 0
    orig_color = block_color
    lead_color = 'black'
    for char in str(nums):
        if int(char) == 0:
            block_color = lead_color
        else:
            block_color = orig_color
            lead_color = orig_color

        print_single_number(x, int(y+char_count), int(char), block_color)
        char_count += 6
    print_single_number(x, int(y+char_count), 0, 'black')
    print_single_number(x, int(y+char_count)+6, 0, 'black')


def print_arrows(x, y, arrow_list):
    char_count = 0
    for arrow in arrow_list:
        print_arrow(x, int(y+char_count), arrow)
        char_count += 6
    print_single_number(x, int(y+char_count), 0, 'black')
    print_single_number(x, int(y+char_count)+6, 0, 'black')



#clear_terminal()
#print_numbers(2, 2, 1984, 'red')
