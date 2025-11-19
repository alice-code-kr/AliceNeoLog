class School:
    def __init__(self,name,grade,color):
        self.name = name
        self.grade = grade
        self.color = color

        # self.school_dic =  {
        #     "name": self.name,
        #     "grade": self.grade,
        #     "color": self.color
        # }
 

    def __str__(self):
        return (f"이름: {self.name}, 학년: {self.grade}, 색깔: {self.color}")

   
    

    
  
        