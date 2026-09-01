def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refill = infinite_chai()
user2 = infinite_chai()

for _ in range(5):
    print(next(refill))

for _ in range(6):
    print(next(user2))


#more examples of infinite generators
set={1, 2, 3, 4, 5}
def infinite_set():
    while True:
        for i in set:
            yield i

infinite_set_gen = infinite_set()
for _ in range(10):
    print(next(infinite_set_gen))   
    