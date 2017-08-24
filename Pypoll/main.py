import csv
import os
#input ,output files path in dictionary
file_dictionary={"election_data_1.csv":"election_analysis_1.txt","election_data_2.csv":"election_analysis_2.txt"}
for key,value in file_dictionary.items():
    print("Input File:" + key  )
#Variable initialization
   
    voter_list=[]
    candidate_votes={}
    winner=""
    percentagevalue=0
    heighest_votes=0
    csvpath=os.path.join("../PyPoll",key)
    file_text=os.path.join("../PyPoll",value)
    with open(csvpath) as csvfile :
        reader=csv.DictReader(csvfile,delimiter=",")
        #loop through each csv file
        for row in reader:
            if row["Candidate"] in candidate_votes:
                candidate_votes[row["Candidate"]] += 1
            else:
                candidate_votes[row["Candidate"]]=1
        total_votes=sum(candidate_votes.values())
        

        print("Final Results     ")
        print("...........................")
        print("Total Votes  are  "+str(total_votes))
        print("..........................")
        
        for key ,value in candidate_votes.items():
            percentage=round((value/total_votes)*100,0)
            print(str(key)+ " : " + str(percentage)+"% (" + str(value) + ")" )
            if value > heighest_votes:  
                heighest_votes=value
                winner=key
                
        print("....................")
        print("Winner : " + winner  )
        print("....................")  

    with open(file_text, "w") as txt_file:
                txt_file.write("...........................")
                txt_file.write("\n")
                txt_file.write("Final Results    ")
                txt_file.write("\n")
                txt_file.write("...........................")
                txt_file.write("\n")
                txt_file.write("Total Votes  are  "+str(total_votes))
                txt_file.write("\n")
                txt_file.write(".............................") 
                txt_file.write("\n")
                for key ,value in candidate_votes.items():
                    percentage=round((value/total_votes)*100,0)
                    txt_file.write(str(key)+ " : " + str(percentage)+" % ( " + str(value) + ") \n" )
                txt_file.write(".............................")     
                txt_file.write("\n")
                
                txt_file.write("Winner : " + winner  )
                txt_file.write("\n")
                txt_file.write(".............................") 
