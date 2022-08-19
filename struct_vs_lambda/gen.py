import sys

count = int(sys.argv[1])
kind = sys.argv[2]

assert(kind in ("lambda", "struct"))

for i in range(count):
   if kind == "lambda":
      print(f'constexpr inline auto f{i} = [](){{ return {i}; }};')
   else:
      print(f'struct f{i}_ {{ auto operator()() const {{ return {i}; }} }}; constexpr inline f{i}_ f{i};')

print(f'int main(){{')
for i in range(count):
   print(f'   f{i}();')
print(f'}}')