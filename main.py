

max=0


class shift:

    def __init__(self,array):

        self.array=array

    def right(self):
        for i in range(0, len(self.array) - 1):
            self.array[i] = self.array[i + 1]
        self.array[len(self.array) - 1] = 0

        print(self.array)

    def left(self):

        for i in range(len(self.array) - 1, 0, -1):
            self.array[i] = self.array[i - 1]
        print(self.array)


    def sort(self):
        
        for i in self.array:
             for j in range(0,len(self.array)-1):

                 if  self.array[j]>self.array[j+1]:
                    first=self.array[j]
                    secend=self.array[j+1]
                    self.array[j]=secend
                    self.array[j+1]=first



        print(self.array)


test=shift([1,5,3,4])

test.sort()
test.right()
test.right()
test.left()


#print(tab)