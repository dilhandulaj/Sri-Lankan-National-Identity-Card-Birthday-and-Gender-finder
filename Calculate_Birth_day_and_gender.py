looping=1;
while (looping !=0):
    idCardNo = input("Please Enter Your ID Card Number : ")
    getidLength = len(idCardNo)

    if(getidLength ==9):##check the length of id card
        getOldYear = int(idCardNo[0:2])
        setoldYeartoValue = "19" + str(getOldYear)
        calLeepYearorNot = (int(getOldYear) % 4)
        if(int(idCardNo[2:5])<=366):##check the gender (Male)
            if calLeepYearorNot == 0:##check not leep
                month = ["January","February","March","April","May","June","July","August","September","Octobercto","November","December"]
                monthhavedate =[31,28,31,30,31,30,31,31,30,31,30,31]           
                
                getOldDays =int(idCardNo[2:5])-1       
                for x in range(0, 13):##counting for the array points                   
                    getOldDays=getOldDays-int(monthhavedate[x])
                    if(getOldDays <= 0):##check the subtraction value
                        out01 = getOldDays +int(monthhavedate[x])               
                        print("You Birth Day : " + setoldYeartoValue + " "+month[x]+" "+str(out01)+"\n"+"Your Gender is Male")
                        break;
            
            elif calLeepYearorNot != 0:##check not leep
                month = ["January","February","March","April","May","June","July","August","September","Octobercto","November","December"]
                monthhavedate =[31,29,31,30,31,30,31,31,30,31,30,31]            
                
                getOldDays =int(idCardNo[2:5])       
                for x in range(0, 13):                   
                    getOldDays=getOldDays-int(monthhavedate[x])
                    if(getOldDays <= 0):
                        out01 = getOldDays +int(monthhavedate[x])               
                        print("You Birth Day : " + setoldYeartoValue + " "+month[x]+" "+str(out01)+"\n"+"Your Gender is Male")
                        break;
                
                        
        elif(int(idCardNo[2:5])>=501):
            if calLeepYearorNot == 0:
                month = ["January","February","March","April","May","June","July","August","September","Octobercto","November","December"]
                monthhavedate =[31,28,31,30,31,30,31,31,30,31,30,31]           
                
                getOldDays =int(idCardNo[2:5]) 
                getOldDays = getOldDays -501      
                for x in range(0, 13):                   
                    getOldDays=getOldDays-int(monthhavedate[x])
                        
                    if(getOldDays <= 0):
                        out01 = getOldDays +int(monthhavedate[x])               
                        print("You Birth Day : " + setoldYeartoValue + " "+month[x]+" "+str(out01)+"\n"+"Your Gender is Female")
                        break;
                
            elif calLeepYearorNot != 0:
                month = ["January","February","March","April","May","June","July","August","September","Octobercto","November","December"]
                monthhavedate =[31,29,31,30,31,30,31,31,30,31,30,31]           
                
                getOldDays =int(idCardNo[2:5]) 
                getOldDays = getOldDays -500    
                for x in range(0, 13):                   
                    getOldDays=getOldDays-int(monthhavedate[x])
                    if(getOldDays <= 0):
                        out01 = getOldDays +int(monthhavedate[x])               
                        print("You Birth Day : " + setoldYeartoValue + " "+month[x]+" "+str(out01)+"\n"+"Your Gender is Female")
                        break;
            
    elif (getidLength==11):
        getNewYear = int(idCardNo[0:4])
        calLeepYearorNot = (int(getNewYear) % 4)
        if(int(idCardNo[2:5])<=366):
            if calLeepYearorNot == 0:
                month = ["January","February","March","April","May","June","July","August","September","Octobercto","November","December"]
                monthhavedate =[31,28,31,30,31,30,31,31,30,31,30,31]            
                
                getOldDays =int(idCardNo[4:7])-1     
                for x in range(0, 13):                   
                    getOldDays=getOldDays-int(monthhavedate[x])
                    if(getOldDays <= 0):
                        out01 = getOldDays +int(monthhavedate[x])               
                        print("You Birth Day : " + idCardNo[0:4] + " "+month[x]+" "+str(out01)+"\n"+"Your Gender is Male")
                        break;
            elif calLeepYearorNot != 0:
                month = ["January","February","March","April","May","June","July","August","September","Octobercto","November","December"]
                monthhavedate =[31,29,31,30,31,30,31,31,30,31,30,31]
                
                getOldDays =int(idCardNo[4:7])    
                for x in range(0, 13):                   
                    getOldDays=getOldDays-int(monthhavedate[x])
                    if(getOldDays <= 0):
                        out01 = getOldDays +int(monthhavedate[x])               
                        print("You Birth Day : " + idCardNo[0:4] + " "+month[x]+" "+str(out01)+"\n"+"Your Gender is Male")
                        break;
                        
        elif(int(idCardNo[2:5])>=501):
            if calLeepYearorNot == 0:
                month = ["January","February","March","April","May","June","July","August","September","Octobercto","November","December"]
                monthhavedate =[31,28,31,30,31,30,31,31,30,31,30,31]           
                
                getOldDays =int(idCardNo[4:7])   
                getOldDays = getOldDays -501 
                for x in range(0, 13):                   
                    getOldDays=getOldDays-int(monthhavedate[x])
                        
                    if(getOldDays <= 0):
                        out01 = getOldDays +int(monthhavedate[x])               
                        print("You Birth Day : " + idCardNo[0:4] + " "+month[x]+" "+str(out01)+"\n"+"Your Gender is Female")
                        break;
            elif calLeepYearorNot != 0:
                month = ["January","February","March","April","May","June","July","August","September","Octobercto","November","December"]
                monthhavedate =[31,29,31,30,31,30,31,31,30,31,30,31]            
                
                getOldDays =int(idCardNo[4:7])  
                getOldDays = getOldDays -500
                for x in range(0, 13):                   
                    getOldDays=getOldDays-int(monthhavedate[x])
                    if(getOldDays <= 0):
                        out01 = getOldDays +int(monthhavedate[x])               
                        print("You Birth Day : " + idCardNo[0:4] + " "+month[x]+" "+str(out01)+"\n"+"Your Gender is Female")
                        break;
    looping=1;
