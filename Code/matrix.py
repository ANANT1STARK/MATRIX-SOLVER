# this is matrix class 
# coded by anant stark


class Matrix:
    def __init__(self,name,row,column):
        self.name=name
        self.row = row
        self.column = column
        self.no_of_elements = self.row*self.column
        self.matrix = []
    def set_value(self,*args):
        
        try:
        
            z=0
            for i in range(0,self.row):
                self.matrix.append([])

                for item in args:
                    
                    for j in range(z,self.column+z):
                        
                        
                        self.matrix[i].append(item[j])

                    z+=self.column
                    
            
        except:
            print("insufficien value or not integer value given")
    def take_value(self):
        print("******* ENTER ELEMENTS OF MATRIX ********",end='\n\n')
        r=1
        c=1
        elements = []
        for i in range(0,self.no_of_elements):
            if c>self.column:
                r+=1
                c=1
            while 1:
                try:
                    take = int(input(f"ENTER THE ROW:{r} COLUMN:{c} : "))
                    elements.append(take)
                
                    break
                except:
                    print("may be not integer type given")
        
            
            c+=1
            
        return elements
    def print_matrix(self):
        
    
        try:
            
            for index,item in enumerate(self.matrix):
                
                for index2,element in enumerate(item):
                    
                    print(f"""{self.name}[{index+1}][{index2+1}] : {element}""",end='   ')
                print()
        except : 
            print("matrix does'nt exist")
    def __len__(self):
        return self.no_of_elements
    
    def __add__(self,second_matrix):
        if self.row == second_matrix.row and self.column==second_matrix.column :

            third_matrix = Matrix(f"{self.name}+{second_matrix.name}",self.row,self.column)
            elements_of_third_matrix = []
            for i in range(0,self.row):
                for j in range(0,self.column):
                    a = self.matrix[i][j] + second_matrix.matrix[i][j]
                    elements_of_third_matrix.append(a)
            third_matrix.set_value(elements_of_third_matrix)
            return third_matrix

    def __sub__(self,second_matrix):
        if self.row == second_matrix.row and self.column==second_matrix.column :

            third_matrix = Matrix(f"{self.name}+{second_matrix.name}",self.row,self.column)
            elements_of_third_matrix = []
            for i in range(0,self.row):
                for j in range(0,self.column):
                    a = self.matrix[i][j] - second_matrix.matrix[i][j]
                    
                    elements_of_third_matrix.append(a)
            third_matrix.set_value(elements_of_third_matrix)
            return third_matrix
    

        
        else:
            print('SUBTRACTION IS NOT POSSIBLE')
            return 0
    def __mul__(self,second_matrix):
        if type(second_matrix) is Matrix:
            if self.column == second_matrix.row:

                third_matrix = Matrix(f"{self.name}+{second_matrix.name}",self.row,second_matrix.column)
                elements_of_third_matrix = []
                
                for i in range(0,self.row):

                    for k in range(0,second_matrix.column) :
                        element = 0
                        for j in range(0,self.column):        
                            a = self.matrix[i][j] * second_matrix.matrix[j][k]
                            element += a
                        
                        elements_of_third_matrix.append(element)
                third_matrix.set_value(elements_of_third_matrix)
                return third_matrix
        elif type(second_matrix) is int:
            third_matrix = Matrix(f"{self.name}X{second_matrix}",self.row,self.column)
            elements_of_third_matrix = []
            for i in range(0,self.row):
                for j in range(0,self.column):
                    a = self.matrix[i][j] * second_matrix
                    elements_of_third_matrix.append(a)
            third_matrix.set_value(elements_of_third_matrix)
            return third_matrix

            
def createdByAnant():
    print("""
             #####################################################################
             #                                                                   @
             #                                                                   @
             #                   CREATED BY :  ANANT PAREEK                      @
             #                                                                   @
             #                                                                   @
             #                                                                   @
             #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                                                   
    
    """)

