
class Trains():
   def readCityTrainfile(self,inputfile):
       self.file=inputfile
       f= open(self.file,"r")
       lines=f.readlines()
       f.close()
       res=[]
       for line in lines:
           line=line.split("/")
           list=[]
           for l in line:
               l=l.replace("\n",'')
               l=l.replace(" ",'')
               list.append(l)
           res.append(list)
       return res

## Complexity for readCityTrainfile is O(n^2)

   def showAll(self):
       lines=self.readCityTrainfile("inputPS4.txt")  
       T_no=[]
       T_names=[]
       All_dup_names=[]
       for line in lines: 
           T_no.append(line[0])
           for i in range(1,len(line)):
               All_dup_names.append(line[i])
               if line[i] not in T_names:
                   T_names.append(line[i])
       f=open("outputPS4.txt","a")
       f.write(".........Function showAll........\n")
       f.write("Total no. of freight trains: "+str(len(T_no))+"\n")
       f.write("Total no. of cities: "+str(len(T_names))+"\n")
       f.write("List of freight trains:\n")
       print(".........Function showAll........")
       print("Total no. of freight trains: ",len(T_no))
       print("Total no. of cities: ",len(T_names))
       print("List of freight trains:")
       for i in T_no:
           print(i)
           f.write(i+"\n")
       print("List of cities:")
       for i in T_names:
           print(i)
           f.write(i+"\n")
       f.close()
       return All_dup_names

## Complexity for showAll is O(n^2)


   def getDuplicatesWithCount(self,listOfElems):
        dictOfElems = dict()
        for elem in listOfElems:
            if elem in dictOfElems:
                dictOfElems[elem] += 1
            else:
                dictOfElems[elem] = 1

        dictOfElems = { key:value for key, value in dictOfElems.items() if value > 1}
        return dictOfElems
    
## Complexity for getDuplicatesWithCount is = O(n)


   def displayTransportHub(self):
       lines=self.readCityTrainfile("inputPS4.txt")
       f=open("outputPS4.txt","a")
       list_cities=[]
       for line in lines:
           for l in range(1,len(line)):
               list_cities.append(line[l])

       elements = self.getDuplicatesWithCount(list_cities)
       max_key=max(elements, key=elements.get)
       all_values=elements.values()
       max_value=max(all_values)
       f.write("\n.......Function displayTransportHub.......")
       f.write("\nMain transport hub: "+max_key)
       f.write("\nNumber of trains visited: "+str(max_value))
       f.write("\nList of Freight trains:")
       print(".......Function displayTransportHub.......")
       print("\nMain transport hub: ",max_key)
       print("\nNumber of trains visited: ",max_value)
       print("\nList of Freight trains:")
       for line in lines:
           for i in range(len(line)):
               if max_key==line[i]:
                   print("\n"+line[0])
                   f.write("\n"+line[0])
       f.close()

## Complexity for displayTransportHub is O(n^2)


   def get_promts(self,file):
       f=open(file,"r")
       lines=f.readlines()
       f.close
       list=[]
       for line in lines:
           line=line.split(':')
           arr=[]
           for l in line:
               l=l.replace("\n",'')
               arr.append(l.replace(" ",''))
           list.append(arr)
           print(list)
       return list

## Complexity for get_promts is O(n^2)

   def get_data(self,key):
       lines=self.get_promts("promptsPS4.txt")
       get=[]
       for line in lines:
           if(line[0]==key and key=="searchTrain"):
               get.append(line[1])
           elif(key=="searchCities" and line[0]==key):
               for i in range(1,len(line)):
                   get.append(line[i])
           elif(key=="ServiceAvailability" and line[0]==key):
               for i in range(1,len(line)):
                   get.append(line[i])
       return get

## Complexity for get_data is O(n^2)

   def displayConnectedCities(self,train):
       lines=self.readCityTrainfile("inputPS4.txt")
       f=open("outputPS4.txt","a")
       f.write("\n........Function displayConnectedCities......")
       f.write("\nFreight train number: "+train)
       print("........Function displayConnectedCities......")
       print("\nFreight train number: "+train)
       l=[]
       for line in lines:
           if train==line[0]:
               c=0
               for i in range(1,len(line)):
                   l.append(line[i])
                   c+=1
       print("\nNumber of cities connected:",c)
       print("\nList of cities connected directly by "+train)
       f.write("\nNumber of cities connected:"+str(c))
       f.write("\nList of cities connected directly by "+train)
       for i in l:
           print("\n"+i)
           f.write("\n"+i)
       f.close()

## Complexity for displayConnectedCities is O(n^2)

   def displayDireactTrain(self,city_a,city_b):
       f=open("outputPS4.txt","a")
       f.write("\n.......Function displayDireactTrain.......")
       f.write("\nCity A: "+city_a)
       f.write("\nCity B: "+city_b)
       print(".......Function displayDireactTrain.......")
       print("City A: "+city_a)
       print("City B: "+city_b)
       lines=self.readCityTrainfile("inputPS4.txt")
       res=''
       for line in lines:
           if city_a in line:
               for i in range(len(line)):
                   # print("yes")
                   if(city_b==line[i].replace(" ",'')):
                       print("yes")
                       res=line[0]
       print("Package can be sent directly: Yes, "+res)
       f.write("\nPackage can be sent directly: Yes, "+res)
       f.close()

## Complexity for displayDireactTrain is O(n^2)

   def get_path(self,city_a,city_b):
       lines=self.readCityTrainfile("inputPS4.txt")
       list=[]
       list.append(city_a)
       for line in lines:
           if city_a in line:
               for i in range(len(line)):
                   if(city_b==line[i]):
                       list.append(line[0])
       list.append(city_b)
       print(list)

## Complexity for get_path is O(n^2)

   def findServiceAvailable(self,city_a,city_b):
       f=open("outputPS4.txt","a")
       f.write("\n.......Function findServiceAvailable.......")
       f.write("\nCity A: "+city_a)
       f.write("\nCity B: "+city_b)
       print(".......Function findServiceAvailable....")
       print("City A:",city_a)
       print("City B:",city_b)
       lines=self.readCityTrainfile("inputPS4.txt")
       list=[]
       for line in lines:
           if city_a in line:
               list.append(line)
           if city_b in line:
               list.append(line)
       print(list)
       if(len(list)!=1):
           for line in list:
               for i in range(1,len(line)):
                   for j in range(1,len(line)):
                       if line[i]!=line[j]:
                           self.get_path(line[i],line[j])

## Complexity for get_path is O(n^3)

obj=Trains()
## Below code is to test and display the output of the above functions

print("1. Method readCityTrainfile calls\n")
print("2. Method showAll calls\n")
print("3. Method displayTransportHub calls\n")
print("4. Method displayConnectedCities calls\n")
print("5. Method displayDireactTrain calls\n")
print("6. Method findServiceAvailable calls\n")
print("7. calls all Method and save output in outputPS4.txt\n")
n=int(input("Enter the value: "))

if(n==1):
   obj.readCityTrainfile("inputPS4.txt")
   print(obj)
elif(n==2):
   obj.showAll()
elif(n==3):
   obj.displayTransportHub()
elif(n==4):
   obj.displayConnectedCities(obj.get_data("searchTrain")[0])
elif(n==5):
   city=obj.get_data("searchCities")
   obj.displayDireactTrain(city[0],city[1])
elif(n==6):
   city=obj.get_data("ServiceAvailability")
   obj.findServiceAvailable(city[0],city[2])
elif(n==7):
   obj.readCityTrainfile("inputPS4.txt")
   obj.showAll()
   obj.displayTransportHub()
   obj.displayConnectedCities(obj.get_data("searchTrain")[0])
   city=obj.get_data("searchCities")
   obj.displayDireactTrain(city[0],city[1])
   city=obj.get_data("ServiceAvailability")
   obj.findServiceAvailable(city[0],city[2])