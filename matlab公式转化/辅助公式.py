import re
import matplotlib.pyplot as plt

a=r'sqrt(2*u(2)/(u(2)-1))'
#a=input('请输入公式：')

#Main Code
print(a)

ax=plt.figure()
ax.text(0.1,0.8,r"$\int_a^b f(x)\mathrm{d}x$")
ax.text(0.1,0.3,r"$\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}!$",fontsize=30)
plt.show()

        
