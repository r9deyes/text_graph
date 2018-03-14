# -*-coding:utf8-*-#
if 1 and __name__ == '__main__':
    from text_graph import TextGraph, SentenceGraph, all_pairs_in_sent

    path = 'D:/Users/DAN85_000/Desktop/py/tg/'

    def f(tg, out='D:/users/DAN85_000/Desktop/result.html'):
        fl = open(out, 'wb')
        t = '<meta charset="utf-8">Kolvo vershin: %i\nKolvo dug: %i\n' % (
        tg.number_of_nodes(), tg.number_of_edges()) + '<br>'
        word_frequency_plot(tg, out[:-5] + 'w.png')
        t += '<img src="'+out[:-5]+'w.png'+'" alt="wordFrequencyGraph">'
        kn = tg.node.keys()
        kn.sort()
        wn = tg.node_property.keys()
        t += '<table><tr><th> name </th><th> ' + ' </th><th> '.join(wn) + '</th></tr>\n<tr><td>'
        t += '---' + '</td><td>---' * (len(wn)) + '</td></tr>\n<tr><td>'
        for k in kn:
            t += k.encode('utf-8')
            for w in wn:
                t += '</td><td> %.3f' % tg.node[k][w]
            t += ' </td></tr>\n<tr><td>'
        t += '</table><br>'
        # t.replace('|','</td><td>').replace('\n','</td></tr>\n<tr><td>')+
        fl.write(t)  # print(t)
        ke = tg.edges()
        ke.sort()
        we = tg.edge_property.keys()

        pair_words_frequency_plot(tg, out[:-5] + 'pw.png')
        t = '<img src="'+out[:-5]+'pw.png'+'" alt="pairwordFrequencyGraph">'
        t += '<table><tr><th> name </th><th> ' + ' </th><th> '.join(we) + '</th></tr>\n<tr><td>'
        t += '---' + '</td><td>---' * (len(we)) + '</td></tr>\n<tr><td>'
        for k in ke:
            # t+=k[0]+'->'+k[1]
            t += k[0].encode('utf-8') + '->' + k[1].encode('utf-8')
            for w in we:
                t += '</td><td> %.3f' % tg.edge[k[0]][k[1]][w]
            t += ' </td></tr>\n<tr><td>'
        t += '</table><br>'
        # t.replace('|','</td><td>').replace('\n','</td></tr>\n<tr><td>')+
        fl.write(t)  # print(t)
        fl.close()

    def f_full_stat(tg, out='D:/users/DAN85_000/Desktop/result.html'):
        fl = open(out.replace('.html','_.html'),'wb')
        t0 = 'Property \t | Max \t| Value \t | Min \t| Value \t | Avg Value \t | Closest Avg \t| Value \n'
        for p in tg.node_property:
            mx, mn, avg = tg.node_list[p][0], tg.node_list[p][-1], float(
                sum([tg.node[s][p] for s in tg.node_list[p]])) / tg.number_of_nodes()
            ca = tg.find('node', p, avg)
            t0 += '%s | %s \t| %.2f \t | %s \t| %.2f \t | %.2f \t | %s \t| %.2f \n' % \
                  (p, mx.encode('utf-8'), tg.node[mx][p], mn.encode('utf-8'), tg.node[mn][p], avg, ca.encode('utf-8'),
                   tg.node[ca][p])
            # (p,mx,tg.node[mx][p],mn,tg.node[mn][p],avg,ca,tg.node[ca][p])

        t0 += '-\t' * 17 + '\n'
        t0 += f_edges_stat(tg)

        t0 = '<table><tr><td>' + t0.replace('|', '</td><td>').replace('\n', '</td></tr>\n<tr><td>') + '</table><br>'
        fl.write(t0)
        fl.close()

    def f_edges_stat(tg):
        t0 = 'Property \t | Max \t| Value \t | Min \t| Value \t | Avg Value \t | Closest Avg \t| Value\n'
        for p in tg.edge_property:
            mx, mn, avg = tg.edge_list[p][0], tg.edge_list[p][-1], float(
                sum([tg.edge[s[0]][s[1]][p] for s in tg.edge_list[p]])) / tg.number_of_edges()
            ca = tg.find('edge', p, avg)
            t0 += '%s | %s->%s \t| %.2f \t | %s->%s \t| %.2f \t | %.2f \t | %s->%s \t| %.2f \n' % \
                  (p, mx[0].encode('utf-8'), mx[1].encode('utf-8'), tg.edge[mx[0]][mx[1]][p], mn[0].encode('utf-8'),
                   mn[1].encode('utf-8'), tg.edge[mn[0]][mn[1]][p], avg, ca[0].encode('utf-8'), ca[1].encode('utf-8'),
                   tg.edge[ca[0]][ca[1]][p])
            # (p,mx[0],mx[1],tg.edge[mx[0]][mx[1]][p],mn[0],mn[1],tg.edge[mn[0]][mn[1]][p],avg,ca[0],ca[1],tg.edge[ca[0]][ca[1]][p])
        return t0

    #	y="D:/Users/DAN85_000/Desktop/"
    #	f=open("D:/Users/DAN85_000/Desktop/new 2.txt",'r')
    # tg=text_graph
    def convert(text):
        return 0


    def opencorporaXml_processing():
        import xml.etree.ElementTree as ET
        for i in range(1, 34):
            fl = 'D:/Users/DAN85_000/Documents/corpora/' + '%i.xml' % i
            r = ET.parse(fl).getroot()
            words = [t.attrib['text'] for pp in r.findall('paragraphs') for p in pp.findall('paragraph') for s in
                     p.findall('sentence') for tt in s.findall('tokens') for t in tt.findall('token')]
            tg = TextGraph(u' '.join(words), 0,
                           stop_words=(u'в', u'но', u'и', u'на', u'из', u'то', u'к', u'а', u'что', u'-'))
            # 'm a m a m y l a r a m u')#text)
            res = path+'result.html'
            f(tg, res[:-5] + '%i.html' % i)


            # stg=tg.get_morphem_absolut_graph()
            # f(stg,'D:/Users/DAN85_000/Desktop/resultAbs.html')


    def tolstoi_processing():
        for i in range(4, 5):
            fl = path+'corpus/tolstoi/' + str(i) + '.txt'
            tg = TextGraph(fl, 1, stop_words=(u'в', u'но', u'и', u'на', u'из', u'то', u'к', u'а', u'что', u'-', u'не', u'с', u'о'))#.get_morphem_absolut_graph()
            res = path+'result/tolstoi/S_' + str(i) + '.html'
            #f(tg, res)
            #f_full_stat(tg, res)
            text_graph_scatter_representation(tg, res)

    def tolstoi_sentences():
        for i in range(1,5):
            fl = path+'corpus/tolstoi/' + str(i) + '.txt'
            sg = SentenceGraph(fl, fromfile=1,
                                stop_words=(u'в', u'но', u'и', u'на', u'из', u'то',
                                            u'к', u'а', u'что', u'-',u'не', u'с', u'о'))

    def winHelp_processing():
        for i in range(1, 11):
            fl = path + 'corpus/' + str(i) + '.txt'
            tg = TextGraph(fl, 1, stop_words=(
            u'в', u'но', u'и', u'на', u'из', u'то', u'к', u'а', u'что', u'-',u'не', u'с', u'о')).get_morphem_absolut_graph()
            res = path + 'result/' + str(i) + '.html'
            # f(tg, res)
            #f_full_stat(tg, res)
            text_graph_scatter_representation(tg)

    def word_frequency_plot(tg, fileName):
        import matplotlib.pyplot as plt
        y = [tg.node[i]['weight'] for i in tg.node_list['weight'] if tg.node[i]['weight'] > 1]
        if len(y)==0:
            print('No inputs', fileName)
            return 0
        if (y[0] >= y[-1]):
            x = list(range(0, len(y)))
        else:
            x = list(range(len(y), 0))
        plt.plot(x, y,color='b')
        plt.title("Frequency of words in full text")
        plt.ylabel('Frequency')
        plt.xlabel('Order')
        plt.savefig(fileName, format='png')
        plt.clf()


    def pair_words_frequency_plot(tg, fileName):
        import matplotlib.pyplot as plt
        y = [tg.edge[i[0]][i[1]]['weight'] for i in tg.edge_list['weight'] if tg.edge[i[0]][i[1]]['weight'] > 1]
        if len(y)==0:
            print('No inputs', fileName)
            return 0
        if (y[0] >= y[-1]):
            x = list(range(0, len(y)))
        else:
            x = list(range(len(y), 0))
        plt.plot(x, y,color='r')
        plt.title("Frequency of word's pairs in full text")
        plt.ylabel('Frequency')
        plt.xlabel('Order')
        plt.savefig(fileName, format='png')
        plt.clf()

    def text_graph_scatter_representation(tg, fileName=None):
        # type: (TextGraph, str) -> None
        import matplotlib.pyplot as plt
        import matplotlib.transforms as mtrans
        x,y,r = [],[],[]
        for i in tg.node.keys():
            x.append(tg.node[i]['textPositionFirst'])
            y.append(tg.node[i]['textPositionLast'])
            r.append(tg.node[i]['weight']**2)
        plt.plot(x, y, 'r', lw=0.5)
        plt.scatter(x, y, r)
        plt.title('Text graph scatter on first & last positions with weight')
        plt.ylabel('Last position')
        plt.xlabel('First position')
        if (fileName):
            plt.savefig(fileName, format='png')
        else:
            plt.show()
        plt.clf()

    def sentence_graph_3dplot_representation(sg, fileName=None):
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        fig = plt.figure()
        ax = Axes3D(fig) #fig.add_subplot(111, projection = '3d')

        rp = all_pairs_in_sent(sg)
        rp.sort(cmp=lambda x, y: len(x)-len(y))
        i=0
        for r in rp:
            def _f(x, y):
                if r[x] > r[y]:
                    return -1
                elif r[x] < r[y]:
                    return 1
                else:
                    return 0
            ar = r.keys()
            ar.sort(cmp=_f)
            ar = ar[1:]
            ax.plot(tuple(range(len(ar))), [r[k] for k in ar], zs=i*0.2, zdir='-y')
            i += 1
        ax.set_xlabel('Frequency word''s pair in text')
        ax.set_ylabel('Order number of word''s pair')
        ax.set_zlabel('Order number of sentences')
        plt.show()


    def greka_example():
        f1 = path + 'corpus/1.txt'
        tg = SentenceGraph(f1, fromFile=1)#TextGraph(f1,fromFile=1)
        fl = path + 'result/3d_0.png'
        #text_graph_scatter_representation(tg, fl)
        sentence_graph_3dplot_representation(tg, fl)

    greka_example()
    #winHelp_processing()
    #tolstoi_processing()
# print('V cnt: %i, E cnt: %i'%(len(tg.node),len(tg.edge)))
##	path=tg.shortest_way(tg.vertexes.lists['wight'][0],tg.node.lists['wight'][-1])
#	for v in tg.node.keys():
#		s=v+' - '+str(tg.node[v])
#		#for p in tg.node[v].keys():
#		#	s+='\t'+str(tg.node[v][p])
#		print(s)
#	print('==========================\n')
#	for v in tg.edge:
#		for vv in tg.edge[v]:
#			s=v+','+vv+' - '+str(tg.edge[v][vv])
#			#for p in tg.edge[v][vv]:
#			#	s+='\t'+str(tg.edge[v][vv][p])
#			print(s)
#
# To test графическое представление: слово это точка с координатами (первой позиции, последней позиции),
#									размещаем на координатной плоскости и соединеняем в соответствии с дугами.
#			Это всего лишь yet another графическое представление графа на плоскости, которое не может 
#				отражать характеристику весов и не способствует раскрытию идеи использования
#				ребер и дуг.
#
#
if 0 and __name__ == '__main__':
    from text_graph import TextGraph


    def str2nodes_n_edges():
        text = 'q w e r t y'
        nodes = ['q', 'w', 'e', 'r', 't', 'y']
        edges = [('q', 'w'), ('w', 'e'), ('e', 'r'), ('r', 't'), ('t', 'y')]
        tg = TextGraph(text)
        assert (set(tg.node.keys) == set(nodes))
        assert (set(tg.edge.keys) == set(edges))


    def str2nodes_set_n_edges():
        text = 'q w e w e r r t y'
        nodes = ['q', 'w', 'e', 'r', 't', 'y']
        edges = [('q', 'w'), ('w', 'e'), ('e', 'w'), ('w', 'e'), ('e', 'r'), ('r', 'r'), ('r', 't'), ('t', 'y')]
        tg = TextGraph(text)
        assert (set(tg.node.keys()) == set(nodes))
        assert (set(tg.edge.keys()) == set(edges))


    def tg2tree():
        ##### 1 2 3 4 5 6 7 8 9
        text = 'q w e w e r r t y'
        nodes = ['q', 'w', 'e', 'r', 't', 'y']
        edges = [('q', 'w'), ('w', 'e'), ('e', 'w'), ('w', 'e'), ('e', 'r'), ('r', 'r'), ('r', 't'), ('t', 'y')]
        firstPositions = [1, 2, 3, 6, 8, 9]  # # q->w->e->r->t->y
        lastPositions = [1, 4, 5, 7, 8, 9]  # #    /\ |  ()
        ################   3   4	 6	 7						#    +--+
        excessTreeEdges = [('e', 'w'), ('r', 'r')]  # ###################
        # 1   4									#
        tree_edges = set([('q', 'w'), ('w', 'e'), ('e', 'r'), \
                          ('r', 't'), ('t', 'y')])  # # q->w->e->r->t->y


    #														#
    def tg2tree2():
        text = 'q w e r t w y u i o p'


    def tg2tree3():
        text = 'q w e r t y w u i t o p'
