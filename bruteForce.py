import zipfile 
import time 
folderpath=input("path to the file")
zipf=zipfile.ZipFile(folderpath)

if not zipf:
    print("the folder is not password protected you can successfully open it")
else :
    starttime=time.time()
    result=0
    c=0
    characters=['0','1','2','3','4','5','6','7','8','9',
                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    print("brute force started")
    
    if (result==0):
        print ("checking for 4 character password")
        for i in characters :
            for j in characters:
                for k in characters:
                    for l in characters:
                        guess=str(i)+str(j)+str(k)+str(l)
                        password=guess.encode("utf8").strip()
                        print(guess)
                        c=c+1
                        try :
                            with zipfile.ZipFile(folderpath,"r") as zf:
                                zf.extractall(pwd=password)
                                print("success, the password is" +guess)
                                endtime=time.time()
                                result=1
                                break
                        except:pass 
                    if (result==1):
                        break 
                if (result==1):
                    break
            if (result==1):
                    break
    if (result==0):
        duration=endtime-starttime
        print("sorry password not found a total of "+ str(c)+ "possible combinations tried in "+str(duration)+"seconds. Password is not of 4 characters")
        
    else :
        duration=endtime-starttime
        print("congratulations! password found after trying"+str(c) +"combinations in"+str(duration)+"seconds")

    