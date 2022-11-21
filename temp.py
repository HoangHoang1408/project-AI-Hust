import time

total_time = 0
n_test = 10000
for i in range(n_test):
    start = time.time()
    with open("./metric/temp.csv", "a") as f:
        f.write("hello from hoang, slfjldsf")
    end = time.time()
    total_time += end - start

print(total_time / n_test)
