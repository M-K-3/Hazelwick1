avotes = 0
bvotes = 0
cvotes = 0
total = 0

while True:
    vote = input("Enter your vote: A, B or C:  ")
    if vote == "A":
        avotes = avotes + 1
        total = total + 1

    elif vote == "B":
        bvotes = bvotes + 1
        total = total + 1

    elif vote == "C":
        cvotes = cvotes + 1
        total = total + 1
        
    elif vote == "end":
        print("Candidate A votes:", avotes)
        print("Candidate B votes:", bvotes)
        print("Candidate C votes:", cvotes)
        print("Total votes:", total)
        break