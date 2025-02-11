def add(title):
    with open ("books.txt", "a") as f:
        f.write(f"{title}\n")
        print(f"{title} has been added to library")
        

def read():
    with open("books.txt") as f:
       content = f.readlines()
       if not content:
           print("No books available in library")
           return
       n = input("enter the book you want to read:")
       
       for i in content:
           details = i.strip().split(" | ")
           title = details[0].lower()
           if n == title:
               print("Book is available")
               return
       print("Book is not available")
       return
   


def update():
    with open("books.txt") as f:
        content = f.readlines()
        if not content:
            print("No books to update")
            return 
        n = input("Enter the book you want to update:")
        new_books = []
        
        for i in content:
            title = i.strip().lower()
            if n == title:
                n1 = input("Enter the name you are updating to:")
                new_books.append(n1 + "\n")
            else:
                new_books.append(i)
                
                
            with open("books.txt", "w") as f:
                f.writelines(new_books)
            print("Book updated successfully")


def delete():
    with open("books.txt") as f:
        content = f.readlines()
        if not content:
            print("No book to delete")
            return
            
        n = input("Enter the book you want to delete:")
        deleted = False
        
        with open("books.txt", "w") as f:
            for i in content:
             details = i.strip().split(" | ")
             if details[0].lower() == n.lower():
                    deleted = True
             else:
                 f.write(i)
                
        if deleted:
            print("book is deleted")
        else:
            print("book is not deleted")
            
            
def menu():
    while True:
        print("LIBRARY MANAGEMENT SYSTEM")
        print("1.ADD BOOKS")
        print("2.READ BOOKS")
        print("3.UPDATE BOOKS")
        print("4.DELETE BOOKS")
        print("5.EXIT")
        
        case = int(input("Enter your choice[1,2,3,4,5]:"))
        
        if case == 1:
            add(input("Enter the books you want to add:"))
        elif case == 2:
            read()
        elif case == 3:
            update()
        elif case == 4:
            delete()
        elif case == 5:
            print("Exiting")
            break    
        else:
            print("Wrong choice! Select again!")
            
menu()
        
    
            
                
            
        

            
           

       

        

