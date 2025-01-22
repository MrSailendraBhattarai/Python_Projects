
# Execution Time
import time
start=time.time()
result=sum(range(1,1000001))
end=time.time()

execution=end-start

print(f'Execution Time: {execution:.5f} seconds')