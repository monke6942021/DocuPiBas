import os

i = 10
while i <= 100000:
    f = open("query_count.txt", "w")
    f.write(f"{i}")
    f.close()
    print(f"Now testing with database of size {i}")
    for j in range(11):
        print(f"Trial {j}")
        os.system("python3 create_gunreg_input.py < query_count.txt")
        os.system("python3 test/test_sse_schemes/timed_gunreg_model.py < input.txt")
    print()
    i *= 10