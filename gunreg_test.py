import os
import time

i = 10
while i <= 100000:
    f = open("query_count.txt", "w")
    f.write(f"{i}")
    f.close()
    time_arr = []
    print(f"Now dealing with databases of size {i}.")
    for j in range(11):
        os.system("python3 create_gunreg_input.py < query_count.txt")
        start_time = time.time()
        os.system("python3 test/test_sse_schemes/gunreg_model.py < input.txt")
        end_time = time.time()
        if j == 0:
            continue
        time_arr.append(end_time-start_time)
        print(f"Time {j}: {end_time-start_time}")

    print(f"Average Time: {sum(time_arr)/10}\n")
    
    i *= 10
    
    
    
    
    