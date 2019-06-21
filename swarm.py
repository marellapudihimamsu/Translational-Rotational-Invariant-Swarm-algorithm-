#///////////////////////////////
#// Himamsu
#// june 2019
#//////////////////////////////
import matplotlib.pyplot as pyp
import random as rand
import networkx as nx
p=[[0  for asdf in range(3)]for adsffd in range(2) ] 
for i in range(3):
  p[0][i]=rand.randint(-100,100)
  p[1][i]=rand.randint(-100,100)
pyp.plot(p[0],p[1],'b^')
pyp.grid(color='r', linestyle='-', linewidth=0.5)
pyp.axis([-100, 100, -100, 100])
pyp.show()
stepsize=0.1
distance=100
edgelist=[(0,1),(1,2),(2,0)]
G=nx.Graph(edgelist)
for dummy in range(100): 
  for i in range(3):
    G.add_node(i, pos=(p[0][i],p[1][i]))
  nx.draw(G, nx.get_node_attributes(G, 'pos'), with_labels=True, node_size=0)
  #labels = nx.get_edge_attributes(G,'weight')
  pos=nx.get_node_attributes(G,'pos')
  #nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
  pyp.show()
  pyp.axis([-100, 100, -100, 100])
  #meet algorithm
 

  for i in range(3):
    ls=G.neighbors(i)
    err=[0]*2
    for j in ls:
      #print( G[i][j] )
      #print(j,end=" ")
      reld=(        (p[0][j]-p[0][i])**2 + (p[1][j]-p[1][i])**2         )**0.5       # calculating "relative distance "
      relx=p[0][i]-p[0][j]                                                           # xi - xj
      err[0]=err[0]+(relx*(1-((distance)/reld)))                                     # sigma ((xi - xj)(1-distance / rel distance))
      rely=p[1][i]-p[1][j]                                                           # yi - yj
      err[1]=err[1]+(rely*(1-((distance)/reld)))                                     # sgima ((yi - yj)(1-distance / rel distance))
      #print(rel0/abs(rel0),end=" ")
    #print()
    p[0][i]-=stepsize*err[0]                                                         
    p[1][i]-=stepsize*err[1]
    #print(p)
pyp.grid(color='r', linestyle='-', linewidth=0.5)
pyp.plot(p[0],p[1],'k*')    
for i in range(2):
  print(str(i)+ "->"+ str(i+1)+ " Distance ",end=": ")
  print((        (p[0][i+1]-p[0][i])**2 + (p[1][i+1]-p[1][i])**2         )**0.5)
  
print(str(2)+ "->"+ str(0)+ " Distance ",end=": ")
print((        (p[0][0]-p[0][2])**2 + (p[1][0]-p[1][2])**2         )**0.5   )   #printing the distance of final edges
