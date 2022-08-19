Both seem to be roughly the same speed.

### Raw output g++
```
$ /bin/g++ --version
g++ (GCC) 12.1.1 20220730

$ CXX=/bin/g++ ./struct_vs_lambda/run.sh 1000 10000 100000

> lambda 1000

real    0m0.292s
user    0m0.263s
sys     0m0.032s

> lambda 10000

real    0m3.027s
user    0m2.826s
sys     0m0.201s

> lambda 100000

real    0m35.682s
user    0m33.839s
sys     0m1.820s

> struct 1000

real    0m0.271s
user    0m0.238s
sys     0m0.036s

> struct 10000

real    0m2.699s
user    0m2.536s
sys     0m0.165s

> struct 100000

real    0m31.894s
user    0m30.318s
sys     0m1.559s
```

### Raw output clang++

```
$ clang++ --version
clang version 14.0.6

$ CXX=clang++ ./struct_vs_lambda/run.sh 1000 10000 100000

> lambda 1000

real    0m0.151s
user    0m0.143s
sys     0m0.020s

> lambda 10000

real    0m1.246s
user    0m1.170s
sys     0m0.086s

> lambda 100000

real    0m18.814s
user    0m18.263s
sys     0m0.553s

> struct 1000

real    0m0.168s
user    0m0.143s
sys     0m0.036s

> struct 10000

real    0m1.333s
user    0m1.303s
sys     0m0.039s

> struct 100000

real    0m20.105s
user    0m19.500s
sys     0m0.599s
```