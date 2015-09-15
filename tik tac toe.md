import random
class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """
    def __init__( self, width, height ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]

        # we do not need to return inside a constructor!
        

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        temp=True
        no=0
        H = self.height
        W = self.width
        s = ''   # the string to return
        for row in range(H):
            s += '|'   
            for col in range(W):
                s += self.data[row][col]+'|'
            s+=str(row)
            s += '\n'
        s+=' '
        for i in range(2*W):
            if temp:
                s+=str(no)
                temp=False
                no+=1
            else :
                s+=' '
                temp=True
        #s += (2*W+1) * '-'    # bottom of the board
        # and the numbers underneath here
        
        return s       # the board is complete, return it

    def addMove(self, col, ox):
        if col in range(self.width):
            for x in range(self.height):
                if self.data[x][col]==' ':
                    self.data[x][col]=ox
                    return

    def allowsMove(self,row,col):
        if col in range(self.width) and row in range(self.height):
            if self.data[row][col]==' ':
                return True
        return False

    def winsFor(self, ox):
        for i in range(self.height):
            for j in range(self.width-2):
                if self.data[i][j]==ox and self.data[i][j+1]==ox and self.data[i][j+2]==ox :
                    return True 
        for i in range(self.height-2):
            for j in range(self.width):
                if self.data[i][j]==ox and self.data[i+1][j]==ox and self.data[i+2][j]==ox :
                    return True
        for i in range(self.height-2):
            for j in range(self.width-2):
                if self.data[i][j]==ox and self.data[i+1][j+1]==ox and self.data[i+2][j+2]==ox :
                    return True
        j=self.width-1
        for i in range(self.height-2):
            while j>1:
                if self.data[i][j]==ox and self.data[i+1][j-1]==ox and self.data[i+2][j-2]==ox:
                    return True
                j-=1
        return False

    def checkwin(self,ox):
        a=[]
        for i in range(self.height):
            for j in range(self.width-2):
                if self.data[i][j]==ox and self.data[i][j+1]==ox and self.data[i][j+2]==' ' :
                    a+=[i]
                    a+=[j+2]
                    return a
                elif self.data[i][j]==ox and self.data[i][j+1]==' ' and self.data[i][j+2]==ox :
                    a+=[i]
                    a+=[j+1]
                    return a
                elif self.data[i][j]==' ' and self.data[i][j+1]==ox and self.data[i][j+2]==ox :
                    a+=[i]
                    a+=[j]
                    return a
        for i in range(self.height-2):
            for j in range(self.width):
                if self.data[i][j]==ox and self.data[i+1][j]==ox and self.data[i+2][j]==' ':
                    a+=[i+2]
                    a+=[j]
                    return a
                elif self.data[i][j]==ox and self.data[i+1][j]==' ' and self.data[i+2][j]==ox :
                    a+=[i+1]
                    a+=[j]
                    return a
                elif self.data[i][j]==' ' and self.data[i+1][j]==ox and self.data[i+2][j]==ox :
                    a+=[i]
                    a+=[j]
                    return a
        for i in range(self.height-2):
            for j in range(self.width-2):
                if self.data[i][j]==ox and self.data[i+1][j+1]==ox and self.data[i+2][j+2]==' ' :
                    a+=[i+2]
                    a+=[j+2]
                    return a
                elif self.data[i][j]==ox and self.data[i+1][j+1]==' ' and self.data[i+2][j+2]==ox :
                    a+=[i+1]
                    a+=[j+1]
                    return a
                elif self.data[i][j]==' ' and self.data[i+1][j+1]==ox and self.data[i+2][j+2]==ox :
                    a+=[i]
                    a+=[j]
                    return a
        j=self.width-1
        for i in range(self.height-2):
            while j>1:
                if self.data[i][j]==ox and self.data[i+1][j-1]==ox and self.data[i+2][j-2]==' ':
                    a+=[i+2]
                    a+=[j-2]
                    return a
                elif self.data[i][j]==ox and self.data[i+1][j-1]==' ' and self.data[i+2][j-2]==ox:
                    a+=[i+1]
                    a+=[j-1]
                    return a
                elif self.data[i][j]==' ' and self.data[i+1][j-1]==ox and self.data[i+2][j-2]==ox:
                    a+=[i]
                    a+=[j]
                    return a
                j-=1
        return a
    def hostGame(self):
        test=[]
        test1=[]
        row=-1
        col=-1
        number=0
        temp=1
        print 'Row and Colom are zero indexing base'
        user_char=raw_input('choose your symbol X or O :')
        com_char=""
        if user_char == "X":
            com_char="O"
        else :
            com_char="X"
        while True:
            temp=1
            print self
            if number%2 == 0:
                loop=True
                print "Enter choice :"
                row=int(input("row is : "))
                col=int(input("col is : "))
                while loop:
                    if self.allowsMove(row,col):
                        self.data[row][col]=user_char
                        loop = False
                    else :
                        print 'Invalid choice, try again'
                        row=input("row is : ")
                        col=input("col is : ")
            else :
                loop=True
                h=range(self.height)
                w=range(self.width)
                test=self.checkwin(com_char)
                if test:
                    self.data[test[0]][test[1]]=com_char
                    temp=0
                elif temp:
                    test1=self.checkwin(user_char)
                    if test1:
                        self.data[test1[0]][test1[1]]=com_char
                    else :
                        row=random.choice(h)
                        col=random.choice(w)
                        while loop:
                            if self.allowsMove(row,col):
                                self.data[row][col]=com_char
                                loop = False
                            else :
                                row=random.choice(h)
                                col=random.choice(w)
            number+=1
            if self.winsFor(user_char):
                print 'Congratulations! You won the match'
                print self
                break
            elif self.winsFor(com_char):
                print 'Ohh! You loss the match'
                print self
                break
            elif number == self.width*self.height:
                print 'Match is tie'
                print self
                break


print 'Welcome to Tik Take Toe Game !'
print
print "enter size of board like 3 and 3,4 and 4"
#r=int(input('height is :'))
#c=int(input('width is :'))
b=Board(3,3)
b.hostGame()
