def todo():
    tasks=[]
    
    print("\n TO DO LIST")
    print("\n----------------------")
    print("\n1.Add tasks")
    print("\n2.Remove tasks")
    print("\n3.Show tasks")
    print("\n4.Exit")
    
    while True:
        
        choice = int(input("Enter the choice:"))
        
        if choice == 1:
            n = int(input("Enter then no of tasks need to be done:"))
            
            for i in range (0,n):
                task = input("Enter task {}: ".format(i+1))
                tasks.append(task)
                
        elif choice == 2:
            r = int(input("Enter the task no needed to be removed:"))
            
            del tasks[r]
                
        elif choice == 3:
            print(tasks)
            
        elif choice == 4:
            break
            
todo()           
        
        
            
            
            