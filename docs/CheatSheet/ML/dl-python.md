 
# Deep learning in Python

## tqdm

进度条库

1.传入可迭代对象
```python
import time
from tqdm import *
for i in tqdm(range(1000)):
    time.sleep(.01)   #进度条每0.01s前进一次，总时间为1000*0.01=10s 
```

```
#  运行结果如下

100%|██████████| 1000/1000 [00:10<00:00, 93.21it/s]  
```

使用trange
```python
trange(i) 是 tqdm(range(i)) 的简单写法

from tqdm import trange

for i in trange(1000):
    time.sleep(.01)
```

```
# 运行结果如下
100%|██████████| 1000/1000 [00:10<00:00, 93.21it/s]  
————————————————
```
                            