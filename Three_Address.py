import networkx as nx 
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt

prio_dict = {'-':1,'+':2,'*':3,'/':4,'^':5,'**':6}
def find_top_prio(lst):
    top_prio = 1
    count_ops = 0
    
    for ops in lst:
        if ops in prio_dict:
            count_ops += 1
            if prio_dict[ops] > 1:
                top_prio = prio_dict[ops]
    return top_prio, count_ops
def THree_Address(lst):
    ip_lst = list(map(str,lst))
    
    op_lst = []
    op_lst.append(['op','arg1','arg2','result'])

    top_prio, count_ops = find_top_prio(ip_lst)

    ip = ip_lst
    i, res = 0, 0
    while i in range(len(ip)):
        if ip[i] in prio_dict:
            op = ip[i]
            if (prio_dict[op]>=top_prio) and (ip[i+1] in prio_dict):
                res += 1
                op_lst.append([ip[i+1],ip[i+2],' ','t'+str(res)])
                ip[i+1] = 't'+str(res)
                ip.pop(i+2)
                i = 0
                top_prio, count_ops = find_top_prio(ip)
            elif prio_dict[op]>=top_prio:
                res += 1
                op_lst.append([op,ip[i-1],ip[i+1],'t'+str(res)])
                ip[i] = 't'+str(res)
                ip.pop(i-1)
                ip.pop(i)
                i = 0
                top_prio, count_ops = find_top_prio(ip)
            if len(ip) == 1:
                op_lst.append(['=',ip[i],' ','a'])
            G = nx.DiGraph()
            G.clear()
            data = op_lst
            for i in range(1,len(data)-1):
                if(data[i][1]==data[i][2]):
                   data[i][1] = "L_:" + data[i][1]
                   data[i][2] = "R_:" + data[i][2]

                G.add_node("%s" %(data[i][1]))
                G.add_node("%s" %(data[i][2]))
                G.add_node("%s" %(data[i][3]))

                G.add_edge("%s" %(data[i][3]), "%s" %(data[i][1]))
                G.add_edge("%s" %(data[i][3]), "%s" %(data[i][2]))
        
            nx.nx_agraph.write_dot(G,'test.dot')
            plt.title('draw_networkx')
            pos = graphviz_layout(G, prog='dot')
            nx.draw(G, pos, with_labels=True, arrows=False, node_size=600)

            plt.show()
            plt.clf()
            plt.cla()
        i += 1
    for i in range(len(op_lst)):
        try:
            if op_lst[1] is None:
                break
            else:    
                print(op_lst[i])
        except:
            pass