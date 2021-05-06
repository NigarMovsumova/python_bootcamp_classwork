# 1. 1-den 100e kimi ededler var, onlarin cemini
# tapmaq lazimdir, cemi 100den ashagi olana kimi
s = 0
for i in range(1, 100):
    if s + i > 100:
        break
    s = s + i

print(s)
