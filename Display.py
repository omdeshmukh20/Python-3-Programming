#Discription: Accept Book Name And Author From User & Display It 
#Date: 2/09/21
#Author : Om Deshmukh

class BookStore:

    NoOfBooks = 0

    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author

    def Display(self):
        return self.Name, self.Author
    
def main():

    x = (input("Enter Book Name : "))
    y = (input("Enter Book Author : "))

    obj1 = BookStore(x, y)

    Ret = obj1.Display()
    print("Book Name is {}, Author is {} ".format(x, y, Ret))
    
if __name__ == "__main__":
    main()
