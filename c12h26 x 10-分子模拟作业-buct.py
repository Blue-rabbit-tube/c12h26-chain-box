'''
    *Version 1.1
        #优化了38个碳原子排列的bug
        #优化了原子相互碰撞的问题
    *思路：原子 ->链形态 ->盒子(链)摆放      后相对于前都可以看成是一个质点而抽象
    *简陋demo
    *Powered by Jzx
'''


#原子定义
class my_atom:
    '''
        radius:原子半径
        x y z 原子的坐标
    '''
    radius=0
    x=0
    y=0
    z=0
    def __init__(self,x,y,z,radius):
        self.x=x
        self.y=y
        self.z=z
        self.radius=radius

    def change_absolutely_position(self,x,y,z):      #更换相对偏移坐标为绝对坐标
        self.x +=x
        self.y +=y
        self.z +=z


#高分子链定义    确定一个链的结构 选取一个点 其它点作相对偏移
class CH_define_c12h26:

    min=0
    max=0
    link_c12h26=[]                                               #对象数组实例化   38个原子

    V_max_x=0                                                    #估算链占用多大的盒子空间才能装下   第三步防止链溢出盒子
    V_max_y=0
    V_max_z=0

    X_list=[]
    Y_list=[]
    Z_list=[]

    def __init__(self,mins,maxs,space_x,space_y,space_z):             
        '''
        确定一个链起始位置   
        mins：原子半径(即最小间隔) 
        maxs:原子间距(即最大间隔)
        space_x y z 链空间大小
        '''
        import random                                                                                 #放置随机数
        import math                                                                                   #引入数学库
        self.min=mins
        self.max=maxs
        
        
        self.link_c12h26=[my_atom(0,0,0,mins) for i in range(38)]

        self.start_tem=0                                          #存放碳原子对应的队列的起始位置
        
        
        atom_list_count=0

        for i in range(1,13):                                                                        #第一个C原子固定为（0，0，0）
            
            self.start_tem=atom_list_count
            # print(i,atom_list_count)
                
            while(1):
                x=random.randint(0,maxs)                                                                  #放置随机数     生成碳原子
                y=random.randint(0,maxs)
                z=random.randint(0,maxs)
                #暴力搜索可能的原子链位置点
                if(math.sqrt(pow(x-self.link_c12h26[self.start_tem].x,2)+pow(y-self.link_c12h26[self.start_tem].y,2)+pow(z-self.link_c12h26[self.start_tem].z,2))<maxs and \
                    math.sqrt(pow(x-self.link_c12h26[self.start_tem].x,2)+pow(y-self.link_c12h26[self.start_tem].y,2)+pow(z-self.link_c12h26[self.start_tem].z,2))>mins):
                    break
                
            x+=self.link_c12h26[atom_list_count].x
            y+=self.link_c12h26[atom_list_count].y
            z+=self.link_c12h26[atom_list_count].z
                
            atom_list_count+=1
            
            while(1):  
                x=random.randint(0,maxs)                                                                  #放置随机数     生成氢原子
                y=random.randint(0,maxs)
                z=random.randint(0,maxs)
                #暴力搜索可能的原子链位置点
                if(math.sqrt(pow(x-self.link_c12h26[self.start_tem].x,2)+pow(y-self.link_c12h26[self.start_tem].y,2)+pow(z-self.link_c12h26[self.start_tem].z,2))<maxs/5 and \
                    math.sqrt(pow(x-self.link_c12h26[self.start_tem].x,2)+pow(y-self.link_c12h26[self.start_tem].y,2)+pow(z-self.link_c12h26[self.start_tem].z,2))>mins/5):
                    break
                
            x+=self.link_c12h26[atom_list_count].x
            y+=self.link_c12h26[atom_list_count].y
            z+=self.link_c12h26[atom_list_count].z
                
            atom_list_count+=1
                
            while(1):    
                x=random.randint(0,maxs)                                                                  #放置随机数     生成氢原子
                y=random.randint(0,maxs)
                z=random.randint(0,maxs)
                #暴力搜索可能的原子链位置点
                if(math.sqrt(pow(x-self.link_c12h26[self.start_tem].x,2)+pow(y-self.link_c12h26[self.start_tem].y,2)+pow(z-self.link_c12h26[self.start_tem].z,2))<maxs/5 and \
                    math.sqrt(pow(x-self.link_c12h26[self.start_tem].x,2)+pow(y-self.link_c12h26[self.start_tem].y,2)+pow(z-self.link_c12h26[self.start_tem].z,2))>mins/5):
                    break
                
            x+=self.link_c12h26[atom_list_count].x
            y+=self.link_c12h26[atom_list_count].y
            z+=self.link_c12h26[atom_list_count].z
                
            atom_list_count+=1
                
                
            if i==1 or i==12:                                         #第一个和最后一个多一个氢原子
                while(1):
                    x=random.randint(0,maxs)                                                                  #放置随机数     生成氢原子
                    y=random.randint(0,maxs)
                    z=random.randint(0,maxs)
                #暴力搜索可能的原子链位置点
                    if(math.sqrt(pow(x-self.link_c12h26[self.start_tem].x,2)+pow(y-self.link_c12h26[self.start_tem].y,2)+pow(z-self.link_c12h26[self.start_tem].z,2))<maxs/5 and \
                        math.sqrt(pow(x-self.link_c12h26[self.start_tem].x,2)+pow(y-self.link_c12h26[self.start_tem].y,2)+pow(z-self.link_c12h26[self.start_tem].z,2))>mins/5):
                        break
                
                x+=self.link_c12h26[atom_list_count].x
                y+=self.link_c12h26[atom_list_count].y
                z+=self.link_c12h26[atom_list_count].z
                atom_list_count+=1
                
                

            #加到数组里面 看一下这分子链盒子的体积XYZ有多大
            self.X_list.append(x)
            self.Y_list.append(y)
            self.Z_list.append(z)

        self.V_max_x=max(self.X_list)
        self.V_max_y=max(self.Y_list)
        self.V_max_z=max(self.Z_list)

            #原子重叠的情况不想写了 就这样叭   忽略碳氢原子半径的差异(不想写了)(把c和h的atom继承一下原子的特性然后分开写就行)

#盒子位置定义    确定高分子链在盒子中的位置    并合理摆放
class CH_link:
    box_link=[]
    def __init__(self,space_x,space_y,space_z,num,atom_radius,atom_max_distance):                                 
        '''
            分子链最大伸展空间space_x其实就是盒子空间大小   num:分子链的数目 atom_radius原子半径 atom_distance原子最大间距
        '''
        import random
        self.box_link=[CH_define_c12h26(atom_radius,atom_max_distance,space_x,space_y,space_z) for i in range(num)]
        for i in range(0,10):                                                       #取第一条分子链的起始点为起始点 
            for s in range(0,38): 

                self.box_link[i].link_c12h26[s].change_absolutely_position(random.randint(0,space_x-self.box_link[i].V_max_x) \
                    ,random.randint(0,space_y-self.box_link[i].V_max_y),random.randint(0,space_z-self.box_link[i].V_max_z))
                #不考虑链间原子碰撞问题 如果需要的话再遍历所有原子判断就行 如果出现问题 则重新生成盒子起始坐标即可
    def output(self):
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        fig = plt.figure()
        
        
        ax=[]
        
        draw_x=[]
        draw_y=[]
        draw_z=[]
        ax.append(fig.add_subplot(4,3,1, projection='3d'))
        
        for i in range(0,10):
            draw_x=[]
            draw_y=[]
            draw_z=[]
            ax.append(fig.add_subplot(4,3,i+2, projection='3d'))

            for s in range(0,38):
                print("第"+str(i+1)+"条链 第"+str(s+1)+"个原子的坐标是：")                               #数组和自然语言转换
                print(self.box_link[i].link_c12h26[s].x,self.box_link[i].link_c12h26[s].y,self.box_link[i].link_c12h26[s].z)

                st=[0,4,7,10,13,16,19,22,25,28,31,34]
                
                if s in st:
                    draw_x.append(self.box_link[i].link_c12h26[s].x)
                    draw_y.append(self.box_link[i].link_c12h26[s].y)
                    draw_z.append(self.box_link[i].link_c12h26[s].z)
                else:
                    for sst in st:
                        if s-sst<=3:
                            ax[i+1].plot((self.box_link[i].link_c12h26[s].x,self.box_link[i].link_c12h26[sst].x),(self.box_link[i].link_c12h26[s].x,\
                                self.box_link[i].link_c12h26[sst].y),(self.box_link[i].link_c12h26[s].x,self.box_link[i].link_c12h26[sst].z),'.-',c='g')
                            break
                    
            ax[0].scatter(draw_x,draw_y,draw_z,'.-',c='r')
            ax[i+1].plot(draw_x,draw_y,draw_z,'.-',c='r')
            
        plt.show()

if __name__ == "__main__":                               #主函数入口
    '''
    分子链最大伸展空间space_x其实就是盒子空间大小   num:分子链的数目 atom_radius原子半径 atom_distance原子最大间距
    '''
    
    
    sp=CH_link(100000,100000,100000,10,1,10)            #实例化这么个奇怪的盒子
    
    
    
    print(sp.output())                                      #输出结果