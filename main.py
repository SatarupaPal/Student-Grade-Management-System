import json
def update_grade_and_status(d):
    no_of_subjects = 0
    total = 0
    for key, val in d.items():
        if key not in ['roll', 'name', 'total', 'average', 'grade', 'status'] and isinstance(val, (int, float)):
            total += val
            no_of_subjects += 1
    d['total']=total
    if no_of_subjects > 0:
        d['average'] = total / no_of_subjects
    else:
        d['average'] = 0.0
    if(d['average']>= 85):
         d['grade']='A+'
         d['status']='PASSED' 
    elif(d['average']>=75 ):
         d['grade']='A'
         d['status']='PASSED' 
    elif(d['average']>=60 ):
         d['grade']='B'
         d['status']='PASSED'
    elif(d['average']>=50 ):
         d['grade']='C'
         d['status']='PASSED'
    elif(d['average']>=40 ):
         d['grade']='D'
         d['status']='PASSED'  
    elif(d['average']< 40):
         d['grade']='F'
         d['status']='FAILED' 
try:
    with open("student_grade_management_system.json","r") as f:
        std_grade=json.load(f)  
except FileNotFoundError:
    std_grade=[]
except json.JSONDecodeError:
    print("[ERROR] JSON file is corrupted! Starting with an empty student record list.")
    std_grade = []
print("STUDENT GRADE MANAGEMENT SYSTEM")
while True:
   print("[ MAIN MENU ]")
   print("1. Add New Student Record")
   print("2. View All Student Records")
   print("3. Search Student by Roll Number")
   print("4. Update Student Grades")
   print("5. Delete Student Record")
   print("6. Exit")
   try:
        ch=int(input("Enter your choice(1-6):"))
   except ValueError:
       ch=0
   match ch:
      case 1:
            d={}
            print("---  ADD NEW STUDENT RECORD ---")
            # Roll input loop
            while True:
              try:
                roll=int(input("Enter Student Roll Number:"))  
                found= False           
                for old_student in std_grade:
                     if ( old_student["roll"]==roll):
                        found=True
                        break
                if found:
                   print("[ERROR] Student Record already exists with this Roll Number!")
                else: 
                     d['roll']=roll
                     break
                continue
              except  ValueError:
                    print("[ERROR]Invalid Roll Number! Roll number must contain digits only.")
            # Name input loop
            while True:
               name = input("Enter Student Name:").strip()
               if name == "":
                  print("[ERROR] Name cannot be empty!")
               elif name.replace(" ", "").isalpha():
                  d['name'] = name
                  break
               else:
                  print("[ERROR] Name must contain letters only!")
            # Number of subjects input loop
            while True:
               no_of_subjects=input("How many subjects do you want to add?")
               if (no_of_subjects.isdigit()) and int(no_of_subjects) > 0:
                     no_of_subjects=int(no_of_subjects)
                     break
               else:
                     print("[ERROR]Please enter a valid number of subjects!") 
            total=0
            average=0
            # Marks input loop
            for subject in range(1,no_of_subjects+1):
               while True:
                  subject_name=input(f"Enter Subject {subject} Name:").strip()
                  if subject_name == "":
                        print("[ERROR] Subject name cannot be empty!")
                  elif subject_name in d:
                        print("[ERROR] Subject already exists!")
                  elif not subject_name.replace(" ", "").isalpha():
                        print("[ERROR] Subject name must contain letters only!")
                  else:
                        break
               while True:
                  marks=input(f"Enter Marks for {subject_name} (0-100):")
                  if (marks.isdigit()):
                     marks=int(marks)
                     if(marks>=0 and marks<=100):
                        d[subject_name]=marks
                        total=total+marks
                        break
                     else:
                        print("[ERROR] Marks should be between 0 and 100!")
                  else:
                     print("[ERROR] Please enter digits only! Letters or special characters are not allowed.")
            update_grade_and_status(d)      
            std_grade.append(d)
            with open("student_grade_management_system.json","w") as f:
                json.dump(std_grade,f)
            print(f"[SUCCESS] Record for {d['name']} (Roll: {d['roll']}) added successfully!")
      case 2:
            print("--- VIEW ALL STUDENT RECORDS  ---")
           
            if not std_grade:
               print("[INFO] No student records found in the system!")
            else:
                print("Roll No | Name         | Total | Average | Grade | Status")
                for old_student in std_grade:              
                  print(f"{old_student['roll']}     | {old_student['name']} | {old_student['total']}   | {old_student['average']:.2f}%  | {old_student['grade']}    | {old_student['status']}")     
                print(f"Total Students: {len(std_grade)}")
      case 3:
         print("--- SEARCH STUDENT BY ROLL NUMBER  ---")
         if not std_grade:
               print("[INFO] No student records found in the system!Please add a student first.")
         else:
            while True:
                  search=input("Enter Roll Number to search: ")
                  if (search.isdigit()):
                     search=int(search)
                     for old_student in std_grade:
                        if old_student['roll']== search:
                           print("[ RECORD FOUND ]")
                           print(f"Roll Number : {old_student['roll']}")
                           print(f"Student Name: {old_student['name']}")
                           print("Subject Wise Marks:")
                           counter=0
                           for key,value in old_student.items():
                              if key not in['roll','name','total','average','grade','status']:
                                 print(f" - {key}: {value}/100")
                                 counter+=1
                           print(f"Total Marks    :{old_student['total']}/{counter*100}")
                           print(f"Percentage     :{old_student['average']:.2f}%")
                           print(f"Overall Grade  :{old_student['grade']}")
                           print(f"Final Result   :{old_student['status']}")
                           break
                     else:
                        print("[ERROR] No Student Record Found with this Roll Number!")
                     break
                  else:
                     print("[ERROR] Invalid Input! Please enter a valid numerical Roll Number.")           
      case 4:
         print("--- UPDATE STUDENT RECORD ---")
         if not std_grade:
            print("[INFO] No student records found in the system!Please add a student first.")
         else:
            while True:      
                  update=input("Enter Roll Number to update:")
                  if update.isdigit():
                     update=int(update)
                     found_student =None
                     for i in std_grade:
                        if i['roll']== update:
                           found_student= i
                           break
                     if found_student:
                        print(f"[ RECORD FOUND: {found_student['name']} ]")
                        updated= False
                        while not updated: 
                                 print("1. Update Student Name")
                                 print("2. Update Subject Marks")
                                 option=input("Select option (1-2):")
                                 if option.isdigit():
                                    option=int(option)
                                    if(option==1):
                                       while True:
                                         name = input("Enter Student Name to update:").strip()
                                         if name == "":
                                             print("[ERROR] Name cannot be empty!")
                                         elif name.replace(" ", "").isalpha():
                                            found_student['name'] = name
                                            print("[SUCCESS] Student name updated successfully!")
                                            updated=True
                                            break
                                         else:
                                            print("[ERROR] Name must contain letters only!")
                                    elif(option==2):
                                       sub_update=input("Enter Subject Name to update:")
                                       if sub_update in found_student:
                                          while True:
                                            marks_update=input("Enter New Marks (0-100):")
                                            if marks_update.isdigit():
                                             marks_update=int(marks_update)
                                             if(marks_update>=0 and marks_update<=100):
                                                found_student[sub_update]=marks_update
                                                update_grade_and_status(found_student)
                                                print(f"[SUCCESS] Marks updated successfully for {sub_update}!")
                                                updated=True
                                                break  
                                             else:
                                                print("[ERROR] Invalid Marks! Marks must be between 0 and 100.")
                                            else:
                                             print("[ERROR] Invalid Input! Marks should be a number, not text or string.")
                                       else:
                                          print("[ERROR] Subject not found! Please enter a valid subject name.")
                                    else:
                                       print("[ERROR] Invalid Choice! Please select option 1 or 2.")
                                 else:
                                    print("[ERROR] Invalid Input! Option must be a number (1 or 2).")
                        with open("student_grade_management_system.json","w") as f:
                                 json.dump(std_grade,f)
                     else:
                           print("[ERROR] No student record found with this Roll Number!") 
                     break      
                  else:
                        print("[ERROR] Invalid Input! Please enter a valid numerical Roll Number.")                     
      
      case 5:
         print("---  DELETE STUDENT RECORD  ---")
         if not std_grade:
            print("[INFO] No student records found in the system!Please add a student first.")
         else:
            while True:
                  delete=input("Enter Roll Number to delete: ")
                  if(delete.isdigit()):
                     delete=int(delete)
                     found_student=None
                     for i in std_grade:
                        if i['roll']==delete:
                           found_student= i
                           break
                     if found_student:
                        while True:
                           y_n=input(f"Are you sure you want to delete record for {found_student['name']} (Roll: {found_student['roll']})? (y/n):")
                           if y_n=='y':
                              std_grade.remove(found_student)
                              with open("student_grade_management_system.json","w") as f:
                                json.dump(std_grade,f)
                              print(f"[SUCCESS] Record for Roll Number {found_student['roll']} deleted successfully.")
                              break
                           elif(y_n=='n'):
                              print("[INFO] Deletion cancelled.")
                              break
                           else:
                              print("[ERROR] Invalid choice! Please enter 'y' for yes or 'n' for no.")
                     else:
                           print("[ERROR] No student record found with this Roll Number!")
                     break
                  else:
                     print("[ERROR] Invalid Input! Please enter a valid numerical Roll Number.")
            
      case 6:
         print("Thank you for using Student Grade Management System! Goodbye.")
         break
      
      case _:
         print("Invalid Choice!Please enter a number between 1 and 6")   














