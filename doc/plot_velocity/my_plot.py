#_*_ coding:utf8 _*_

import matplotlib.pyplot as plt
import numpy as np

 
#加载没有运动约束，观测量为pose时的本体系下的速度数据
fused = np.loadtxt('vel_fused.txt')#融合结果
gt = np.loadtxt('vel_ground_truth.txt')#参考值

#加载加入运动约束，观测量为pose+vel时的本体系下的速度数据
fused_cons = np.loadtxt('vel_fused_cons.txt')#融合结果
gt_cons = np.loadtxt('vel_ground_truth_cons.txt')#参考值

#统计本体系下y轴方向上的速度误差

print("The mean and variance of velocity error in Y direction without constraint")
print( np.mean(fused[:,2]-gt[:,2]) )
print( np.var( fused[:,2]-gt[:,2], ddof=1) )

print('\n')

print("The mean and variance of velocity error in Y direction with constraint")
print( np.mean(fused_cons[:,2]-gt_cons[:,2]) )
print( np.var( fused_cons[:,2]-gt_cons[:,2], ddof=1) )

print('\n')

print('-----------------------------------------------')

print("The mean and variance of velocity error in Z direction without constraint")
print( np.mean(fused[:,3]-gt[:,3]) )
print( np.var( fused[:,3]-gt[:,3], ddof=1) )

print('\n')

print("The mean and variance of velocity error in Z direction with constraint")
print( np.mean(fused_cons[:,3]-gt_cons[:,3]) )
print( np.var( fused_cons[:,3]-gt_cons[:,3], ddof=1) )

print('\n')

plt.figure()
plt.plot(fused[:,2]-gt[:,2], linestyle="-", label="without_cons")
plt.plot(fused_cons[:,2]-gt_cons[:,2], linestyle="--", label="with_cons")
plt.legend(loc="upper right")
plt.xlabel("time")
plt.ylabel("error")
plt.title('velocity error in Y direction')
plt.show()

plt.figure()
plt.plot(fused[:,3]-gt[:,3], linestyle="-", label="without_cons")
plt.plot(fused_cons[:,3]-gt_cons[:,3], linestyle="--", label="with_cons")
plt.legend(loc="upper right")
plt.xlabel("time")
plt.ylabel("error")
plt.title('velocity error in Z direction')
plt.show()

 
