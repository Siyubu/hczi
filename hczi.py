s = [[3,2],	[4,3],	[2,3],	[3,4]]
p = 30
def airplane_seating(seats,passangers):
    count = 1
    for i in range(len(seats)):
        minrows = seats[i][1]
        mincolums = seats[i][0]
        while count <= passangers:
            for j in range(minrows):
                #Aisle seats	
                for k in range(mincolums):
                    if (i == 0 and k == mincolums-1) or (i == len(seats)-1 and k == 0) :
                        print(f"slot [{i}][{j}][{k}] = {count}")
                        count += 1
                for m in range(0,mincolums, mincolums-1):
                    if len(seats)-1 > i > 0 :
                        print(f"slot [{i}][{j}][{m}] = {count}")
                        count += 1
                # Window Seats
                for k in range(mincolums):
                    if (i == 0 and k == 0)or (i == len(seats)-1 and k == mincolums-1) :
                        print(f"slot [{i}][{j}][{k}] = Wind")
                 # Middle Seats
                for m in range(mincolums):
                    if m > 0 and m<mincolums-1:
                      print(f"slot [{i}][{j}][{m}] = Mid")

            print(" ")


airplane_seating(s,p)