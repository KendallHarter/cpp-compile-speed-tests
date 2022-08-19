Structs are faster but more verbose.
Lambda expressions may be better due to being more succinct.

### Raw output
```
> lambda 1000

real    0m0.470s
user    0m0.448s
sys     0m0.023s

> lambda 10000

real    0m5.072s
user    0m4.912s
sys     0m0.158s

> lambda 100000

real    0m59.227s
user    0m57.660s
sys     0m1.530s

> struct 1000

real    0m0.426s
user    0m0.409s
sys     0m0.018s

> struct 10000

real    0m4.736s
user    0m4.569s
sys     0m0.166s

> struct 100000

real    0m56.777s
user    0m55.224s
sys     0m1.503s
```