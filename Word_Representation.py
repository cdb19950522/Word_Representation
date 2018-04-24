import argparse
import numpy as np
import operator
from itertools import izip


def calculatenorm(list):
    out=np.linalg.norm(list)
    return out
def task2(targetword, file ):
    my_list = []
    for line in file:
        target = line.split(' ')
        if target[0] == targetword:
            for i in range(1,len(target)):
                my_list.append(float(target[i]))
            break
    return my_list

def findtask1(task1, file,decide):
    
    my_list = []
    decide =0
    for line in file:
        target = line.split(' ')
        if target[0] == task1:
            print 'found it'
            decide = 1
            for i in range(1,len(target)):
                my_list.append(float(target[i]))  
            break
        
    if decide ==0:
        print 'Not found it'
    return my_list,decide    
def cos(list1, list2):
    out1=np.dot(list1,list2)
    out2= out1 /(calculatenorm(list1)*calculatenorm(list2))
    return out2
def findsimilar5(my_list, file):
    
    
    similardict = {}
    for line in file:
        temp_list=[]
        target = line.split(' ')
        for i in range(1,len(target)):
            temp_list.append(float(target[i]))
        similarity=cos(temp_list,my_list)
        similardict[target[0]]= similarity
    sorteddict = sorted(similardict.items(), key =operator.itemgetter(1),reverse=True)
    return sorteddict
    
def main():
    parser = argparse.ArgumentParser(description='CS 439 Data Science Word_Representation')
    parser.add_argument('-f', '--filename', type=str, help='file source', required=True)
    args = vars(parser.parse_args())
    file_name = args['filename']
    file = open(file_name ,"r" )
    task1 = raw_input('Enter your firstname:')
    decide = 0 
    my_list,decide=findtask1(task1,file,decide) 
    #file1.close()
    file2 = open(file_name,"r")
    ###To do##
    if decide<>0:
        newdict=findsimilar5(my_list,file2)
        print 'Here are your 5 nearest neighbours of your first name'
        print newdict[1]
        print newdict[2]
        print newdict[3]
        print newdict[4]
        print newdict[5]
    file2.close()

    ##################Task2######################
    
    task2sentence= raw_input('Enter your sentence: ')
    target = task2sentence.split(' ')
    filedelete = open(file_name,"r")
    firstline=filedelete.readline()
    speline = firstline.split(' ')
    number = len(speline)
    #print number
    filedelete.close()
    array= np.zeros(number-1)
    
    for i in target:
        file3 = open(file_name,"r")
        vector = task2(i,file3)
        for i in range(0,len(vector)):
            array[i] = array[i]+vector[i]
    for i in range(0,len(array)):
        array[i]=array[i]/len(target)     
    #print array
    file3.close()
    file4 = open(file_name,"r")
    task2dict = findsimilar5(array,file4)
    print 'Here are your 5 nearest neighbours of your sentence'
    print task2dict[1]
    print task2dict[2]
    print task2dict[3]
    print task2dict[4]
    print task2dict[5]
    file4.close()
    ################Task3################
    task3s1 = raw_input('Enter your sentence s1: ')
    task3s2 = raw_input('Enter your sentence s2: ')

    ###S1 part###
    s1 = task3s1.split(' ')
    s1array = np.zeros(number-1)
    for i in s1:
        file5 = open(file_name,"r")
        vectors1=task2(i,file5)
        for i in range(0,len(vectors1)):
            s1array[i]=s1array[i]+vectors1[i]
    for i in range(0, len(s1array)):
        s1array[i]= s1array[i]/len(s1)
    file5.close()
    ####S2 part###
    s2 = task3s2.split(' ')
    s2array = np.zeros(number-1)
    for i in s2:
        file6 = open(file_name,"r")
        vectors2=task2(i,file6)
        for i in range(0,len(vectors2)):
            s2array[i]=s2array[i]+vectors2[i]
    for i in range(0, len(s2array)):
        s2array[i]= s2array[i]/len(s2)
    file6.close()
    similaritywiths1=cos(s1array,array)
    similaritywiths2=cos(s2array,array)
   


    print 's1 similarity:',similaritywiths1
    print 's2 similarity:',similaritywiths2

        

   
    



    
    
    
if __name__ == "__main__":
    main()
