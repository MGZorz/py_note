from matplotlib import pyplot as plt

# 构造数据
info = [10, 11, 10, 9, 3, 6, 8, 5, 7, 8, 12, 11]
# 构造每条数据显示所在的x坐标
x = range(0, 12)
# 填充数据到图表
plt.plot(x, info)
# 显示图表
plt.show()
