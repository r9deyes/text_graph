#-*-coding:utf8-*-#
import networkx as nx
import chardet
### TODO use chardet library for auto detecting encoding
import re
class text_words:
	t,i,ii,sp,wp,sw=None,None,None,None,None,None
	pre_word=None
	prepre_word=None
	def __init__(s,text,stop_words=[u'-'],	#ur'[a-zA-Zа-яёА-ЯЁ\-]+'
				 words_pattern=ur'([a-zA-Z]|й|ц|у|к|е|н|г|ш|щ|з|х|ъ|ф|ы|в|а|п|р|о|л|д|ж|э|я|ч|с|м|и|т|ь|б|ю|ё|Й|Ц|У|К|Е|Н|Г|Ш|Щ|З|Х|Ъ|Ф|Ы|В|А|П|Р|О|Л|Д|Ж|Э|Я|Ч|С|М|И|Т|Ь|Б|Ю|Ё|\-)+',
				 separating=u'(\.|;|\s|,)+'):
		s.t=text
		s.i=0
		s.ii=-1
		if isinstance(words_pattern, str) or isinstance(words_pattern, unicode):
			s.wp=re.compile(words_pattern)
		elif hasattr(words_pattern, 'search'):
			s.wp = words_pattern
		else:
			s.wp = re.compile(str(words_pattern))
		s.sp=re.compile(separating)
		s.sw=stop_words
		s.pre_word=None
		s.prepre_word=None
	
	def _slice(s,i1,i2,i3=1):
		res=[]
		if (i1==None): i1=0
		if (i3==None): i3=1
		for i in xrange(i1,i2,i3):
			res.append(s[i])
		return res
	
	def __getitem__(s,i):
		if (isinstance(i,slice)):
			return s._slice(i.start,i.stop,i.step)
		res=None
		_str=None
		if (i<0):
			raise(IndexError)
		if (i==s.ii):
			return s.pre_word
		if (i==s.ii-1 and s.prepre_word!=None):
			return s.prepre_word
		if (i<s.ii):
			s.i=0
			s.ii=-1
			s.pre_word=None
			s.prepre_word=None
		while (s.ii!=i):
			res=s.wp.search(s.t,s.i)
			if (res==None):
				raise(IndexError)
			_str=unicode(s.t[res.start():res.end()])
			_str=_str.lower() ############### BUMP! all results will lower \/ But why here?
			s.i=res.end()
			if (0 or _str in s.sw):
				continue
			s.ii+=1
			s.prepre_word=s.pre_word
			s.pre_word=_str
		return _str
	
	def lower(text):
		cl=u'йцукенгшщзхъфывапролджэячсмитьбюё'
		cU=u'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
		for c in range(33):
			text=text.replace(cU[c],cl[c])
		return text
	
	def __setitem__(s,i,y):
		if (i<0):
			raise(IndexError)
		if (i==s.ii):
			s.pre_word=y
		if (i==s.ii-1):
			s.prepre_word=y

class text_graph(nx.DiGraph):
	path='D:\Users\DAN85_000\Downloads\mystem-3.0-win7-32bit'
	node_list=None
	node_property=None
	edge_list=None
	edge_property=None
	
	def __init__(s,text,fromFile=0,stop_words=('-')):
		nx.DiGraph.__init__(s)
		if (fromFile):
			with open(text) as f:
				text=f.read()
		try:
			encoding=chardet.detect(text[:289]+' '+text[len(text)/2-144:len(text)/2+144]+' '+text[-289:])['encoding']
		except(TypeError):
			encoding='utf-8'
			print('Error: Encoding not detected, utf-8 selected\n')
		if (encoding):
			ss=text_words(text.decode(encoding), stop_words=stop_words)#.decode(encoding))#text.decode('cp1251').split()#
		else:
			ss=text_words(unicode(text,'utf-8'), stop_words=stop_words)
		s.node_list=dict()
		s.node_property=dict()
		s.edge_list=dict()
		s.edge_property=dict()
		_S=None
		try:
			s.add_node(ss[0].lower())
			_S=ss[0].lower()
		except(IndexError):
			return None
		s.node_list=dict()
		s.node_property=dict()
		s.edge_list=dict()
		s.edge_property=dict()
		s.add_properties('node',weight=1,textPositionFirst=-1,textPositionLast=-1,textPositionAvg=0,edges_in=0,edges_out=0,sweight=1.0)
		s.add_properties('edge',weight=1,textPositionFirst=-1,textPositionLast=-1,textPositionAvg=0,sweight=1.0,is_tree_edge=False)
		s.node[_S]['weight']=1
		s.node[_S]['textPositionFirst']=1
		s.node[_S]['textPositionAvg']=1
		s.node[_S]['textPositionLast']=1
		t=0
		for tt in ss:
			t+=1
			try:
				ss[t]=ss[t]
			except(IndexError):
				break
			#print(t,' ',ss.ii)##########################
			s.add_node(ss[t])
			s._add_node(ss[t],'weight',1,1)
			if not (s.node[ss[t]].get('textPositionFirst')):
				s.node[ss[t]]['textPositionFirst']=t+1
			s._add_node(ss[t],'textPositionAvg',t+1,t+1)
			s.node[ss[t]]['textPositionLast']=t+1
			
			s.add_edge(ss[t-1],ss[t])
			s._add_edge(ss[t-1],ss[t])
			if not (s.edge[ss[t-1]][ss[t]].get('textPositionFirst')):
				s.edge[ss[t-1]][ss[t]]['textPositionFirst']=t
			s._add_edge(ss[t-1],ss[t],'textPositionAvg',1+t,t+1)
			s.edge[ss[t-1]][ss[t]]['textPositionLast']=t
		for v in s.node.keys():
			s.node[v]['textPositionAvg']/=float(s.node[v]['weight'])
			s.node[v]['edges_out']=len(s.edge[v])
			s.node[v]['edges_in']=0
			s.node[v]['sweight']=1.0/s.node[v]['weight']
		for e in s.edge:
			for ee in s.edge[e]:
				s.edge[e][ee]['textPositionAvg']/=float(s.edge[e][ee]['weight'])
				s.node[ee]['edges_in']+=1
				s.edge[e][ee]['is_tree_edge']=s.node[e]['textPositionFirst']<s.node[ee]['textPositionFirst']
				s.edge[e][ee]['sweight']=1.0/s.edge[e][ee]['weight']
		s.sort_edge()
		s.sort_node()
	
	def add_properties(s,type,**property):
		if (type=='node'):
			pAr=s.node_property
		else:
			pAr=s.edge_property
		for p in property:
			#print(p)################################
			pAr[p]=property[p]
	
	def _add_node(s,n,prop='weight',val=1,def_val=1):
		# type: (str, str, int, int) -> None
		if (s.node[n].get(prop)):
			s.node[n][prop]+=val
		else:
			s.node[n][prop]=def_val
	
	def _add_edge(s,n,nn,prop='weight',val=1,def_val=1):
		if (s.edge[n][nn].get(prop)):
			s.edge[n][nn][prop]+=val
		else:
			s.edge[n][nn][prop]=def_val
	
	def sort_node(s,prop=None):
		for p in s.node_property: 
			def f(x,y):
				if (s.node[x][p]<s.node[y][p]):
					return 1
				if (s.node[x][p]>s.node[y][p]):
					return -1
				return 0
			s.node_list[p]=s.node.keys()
			s.node_list[p].sort(cmp=f)
		
	def sort_edge(s,prop=None):
		for p in s.edge_property:
			def f(x,y):
				if (s.edge[x[0]][x[1]][p]<s.edge[y[0]][y[1]][p]):
					return 1
				if (s.edge[x[0]][x[1]][p]>s.edge[y[0]][y[1]][p]):
					return -1
				return 0
			s.edge_list[p]=s.edges()
			s.edge_list[p].sort(cmp=f)
	
	def get_morphem_absolut_graph(s):
		kAr=s.node.keys()
		import subprocess as sp
		p=sp.Popen([s.path+'\mystem.exe','-l','-e utf8','--format','json'],stdout=sp.PIPE,stdin=sp.PIPE, stderr=sp.STDOUT)
		mystrem_stdout=p.communicate(input=' '.join(kAr).encode('utf8'))[0]
		import json
		jsonRes=json.JSONDecoder().decode(mystrem_stdout)
		p.kill()
		absltM=dict()
		for i in range(len(s.node)):
			try:
				absltM[kAr[i]]=jsonRes[i]['analysis'][0]['lex']
				#print(absltM[kAr[i]])
			except:
				absltM[kAr[i]]=kAr[i]
		tgAbs=text_graph('')
		tgAbs.add_properties('node',weight=1,textPositionFirst=-1,textPositionLast=-1,textPositionAvg=0,edges_in=0,edges_out=0,sweight=1.0,morphCount=1)
		tgAbs.add_properties('edge',weight=1,textPositionFirst=-1,textPositionLast=-1,textPositionAvg=0,sweight=1.0,is_tree_edge=False)
		for k in kAr:
			tgAbs.add_node(absltM[k])
			tgAbs._add_node(absltM[k],'morphCount',1,1)
			tgAbs._add_node(absltM[k],'weight',s.node[k]['weight'],s.node[k]['weight'])
			if (tgAbs.node[absltM[k]].get('textPositionFirst')):
				tgAbs.node[absltM[k]]['textPositionFirst']=min(s.node[k]['textPositionFirst'],tgAbs.node[absltM[k]]['textPositionFirst'])
			else:
				tgAbs.node[absltM[k]]['textPositionFirst']=s.node[k]['textPositionFirst']
			if (tgAbs.node[absltM[k]].get('textPositionLast')):
				tgAbs.node[absltM[k]]['textPositionLast']=max(s.node[k]['textPositionLast'], tgAbs.node[absltM[k]]['textPositionLast'])
			else:
				tgAbs.node[absltM[k]]['textPositionLast']=s.node[k]['textPositionLast']
			tgAbs._add_node(absltM[k],'textPositionAvg',s.node[k]['textPositionAvg']*s.node[k]['weight'],s.node[k]['textPositionAvg']*s.node[k]['weight'])

		for k in s.edge.keys():
			for kk in s.edge[k]:
				tgAbs.add_edge(absltM[k],absltM[kk])
				tgAbs._add_edge(absltM[k],absltM[kk],'weight',s.edge[k][kk]['weight'],s.edge[k][kk]['weight'])
				if (tgAbs.edge[absltM[k]][absltM[kk]].get('textPositionFirst')):
					tgAbs.edge[absltM[k]][absltM[kk]]['textPositionFirst']=min(s.edge[k][kk]['textPositionFirst'],tgAbs.edge[absltM[k]][absltM[kk]]['textPositionFirst'])
				else:
					tgAbs.edge[absltM[k]][absltM[kk]]['textPositionFirst']=s.edge[k][kk]['textPositionFirst']
				if (tgAbs.edge[absltM[k]][absltM[kk]].get('textPositionLast')):
					tgAbs.edge[absltM[k]][absltM[kk]]['textPositionLast']=max(s.edge[k][kk]['textPositionLast'], tgAbs.edge[absltM[k]][absltM[kk]]['textPositionLast'])
				else:
					tgAbs.edge[absltM[k]][absltM[kk]]['textPositionLast']=s.edge[k][kk]['textPositionLast']
				tgAbs._add_edge(absltM[k],absltM[kk],'textPositionAvg',s.edge[k][kk]['textPositionAvg']*s.edge[k][kk]['weight'],s.edge[k][kk]['textPositionAvg']*s.edge[k][kk]['weight'])
		
		for v in tgAbs.node.keys():
			tgAbs.node[v]['textPositionAvg']/=float(tgAbs.node[v]['weight'])
			tgAbs.node[v]['edges_out']=len(tgAbs.edge[v])
			tgAbs.node[v]['edges_in']=0
			tgAbs.node[v]['sweight']=1.0/tgAbs.node[v]['weight']
		for e in tgAbs.edge:
			for ee in tgAbs.edge[e]:
				tgAbs.edge[e][ee]['textPositionAvg']/=float(tgAbs.edge[e][ee]['weight'])
				tgAbs.node[ee]['edges_in']+=1
				tgAbs.edge[e][ee]['is_tree_edge']=tgAbs.node[e]['textPositionFirst']<tgAbs.node[ee]['textPositionFirst']
				tgAbs.edge[e][ee]['sweight']=1.0/tgAbs.edge[e][ee]['weight']
		tgAbs.sort_edge()
		tgAbs.sort_node()
		return tgAbs
	
	def get(s,_type,key):
		if (_type=='node'):
			return s.node[key]
		else:
			return s.edge[key[0]][key[1]]
	
	def find(s,_type,prop,val):
		if (_type=='node'):
			r = s.number_of_nodes()
			lists=s.node_list[prop]
		else:
			r = s.number_of_edges()
			lists=s.edge_list[prop]
		l = 0
		while r - l > 1:
			m = (l + r) // 2
			if val > s.get(_type,lists[m])[prop]:
				r = m
			else:
				l = m
		if((l<len(lists)-1) and (((s.get(_type,lists[l])[prop] - s.get(_type,lists[l+1])[prop]) // 2) + s.get(_type,lists[l+1])[prop] > val)):
			l+=1
		return lists[l]


class sentence_graph(text_graph):
	def __init__(self, text, fromFile=0, stop_words=('-')):
		W = ur'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯA-Z'
		w = W+ur'a-zабвгдеёжзийклмнопрстуфхцчшщъыьэюя'

		nx.DiGraph.__init__(self)
		if (fromFile):
			with open(text) as f:
				text = f.read()
		try:
			encoding = \
			chardet.detect(text[:289] + ' ' + text[len(text) / 2 - 144:len(text) / 2 + 144] + ' ' + text[-289:])[
				'encoding']
		except(TypeError):
			encoding = 'utf-8'
			print('Error: Encoding not detected, utf-8 selected\n')
		sentence_pattern = re.compile(ur'.*?[\.\.\.|\.|\!|\?|\n\n](?=[^' + w + ur']*?([' + W + ur']))', flags=(re.U | re.S))
		if (encoding):
			sents = text_words(re.sub(ur'\s+', u' ', text.decode(encoding)+u' . A'), stop_words=(' ', '.', '\n', '\r\n',),
							   words_pattern=sentence_pattern)
			#wrd = text_words(text.decode(encoding),
			#				 stop_words=stop_words)  # .decode(encoding))#text.decode('cp1251').split()#
		else:
			sents = text_words(re.sub(ur'\s+', u' ', unicode(text,'utf-8')+u' . A'), stop_words=(' ', '.','\n', '\r\n',),
							   words_pattern=sentence_pattern)
			#wrd = text_words(unicode(text, 'utf-8'), stop_words=stop_words)
		self.node_list = dict()
		self.node_property = dict()
		self.edge_list = dict()
		self.edge_property = dict()
		_S = None
		wrd = text_words(sents[0], stop_words=stop_words)
		try:
			self.add_node(wrd[0].lower())
			_S = wrd[0].lower()
		except(IndexError):
			return None
		self.node_list = dict()
		self.node_property = dict()
		self.edge_list = dict()
		self.edge_property = dict()
		self.add_properties('node', weight=1, textPositionFirst=-1, textPositionLast=-1, textPositionAvg=0, edges_in=0,
							edges_out=0, sweight=1.0, sentCount=1, PositionFirstSent=1, PositionAvgSent= 1.0, PositionLastSent=1)
		self.add_properties('edge', weight=1, textPositionFirst=-1, textPositionLast=-1, textPositionAvg=0, sweight=1.0,
							is_tree_edge=False, PositionFirstSent=1, PositionAvgSent= 1.0, PositionLastSent=1)
		self.node[_S]['weight'] = 1
		self.node[_S]['sentCount'] = 1
		self.node[_S]['textPositionFirst'] = 1
		self.node[_S]['textPositionAvg'] = 1
		self.node[_S]['textPositionLast'] = 1

		self.node[_S]['PositionFirstSent'] = 1
		self.node[_S]['PositionAvgSent'] = 1
		self.node[_S]['PositionLastSent'] = 1

		self.sentence_words = dict()

		sn = 0
		self.sentence_words[sn]=set()
		words_count = self.compute_stats_text_words(wrd, sn, 1)
		for snt in sents:
			sn += 1
			try:
				sents.__getitem__(sn)
			except(IndexError):
				break
			self.sentence_words[sn]=set()
			wrd = text_words(snt, stop_words=stop_words)
			words_count = self.compute_stats_text_words(wrd, sn, words_count)

		# TODO compute right stats for words in sentences. e.g. Avg position in sent
		if 1:
			return
		for v in self.node.keys():
			try:
				self.node[v]['textPositionAvg'] /= float(self.node[v]['weight'])
			except KeyError:
				print(v)
				continue
			self.node[v]['PositionAvgSent'] /= float(self.node[v]['weight'])
			self.node[v]['edges_out'] = len(self.edge[v])
			self.node[v]['edges_in'] = 0
			self.node[v]['sweight'] = 1.0 / self.node[v]['weight']
		for e in self.edge:
			for ee in self.edge[e]:
				self.edge[e][ee]['textPositionAvg'] /= float(self.edge[e][ee]['weight'])
				try:
					self.node[ee]['edges_in'] += 1
				except KeyError:
					print(e, ' ', ee)
					continue
				self.edge[e][ee]['is_tree_edge'] = self.node[e]['textPositionFirst'] < self.node[ee]['textPositionFirst']
				self.edge[e][ee]['sweight'] = 1.0 / self.edge[e][ee]['weight']
		self.sort_edge()
		self.sort_node()

	def compute_stats_text_words(self, wrd, sn, glbPos=0):
		# type: (text_words, int, int) -> int
		t = 0
		for tt in wrd:
			t += 1
			glbPos += 1
			try:
				wrd[t] = wrd[t]
			except(IndexError):
				break
			# TODO add stats for count of word repeating in diff sentences: sentCount
			self.add_node(wrd[t])
			self._add_node(wrd[t], 'weight', 1, 1)
			if not (self.node[wrd[t]].get(	'textPositionFirst')):
				self.node[wrd[t]][			'textPositionFirst'] = 	glbPos + 1
			if not (self.node[wrd[t]].get(	'PositionFirstSent')):
				self.node[wrd[t]][			'PositionFirstSent'] = 	t + 1
			self._add_node(wrd[t], 			'textPositionAvg', 		glbPos + 1, glbPos + 1)
			self.node[wrd[t]][				'textPositionLast'] = 	glbPos + 1
			self._add_node(wrd[t], 			'PositionAvgSent', 		t + 1, t + 1)
			self.node[wrd[t]][				'PositionLastSent'] = 	t + 1
			self.add_edge(wrd[t - 1], wrd[t])
			self._add_edge(wrd[t - 1], wrd[t])
			if not (self.edge[wrd[t - 1]][wrd[t]].get(	'textPositionFirst')):
				self.edge[wrd[t - 1]][wrd[t]][			'textPositionFirst'] = 	glbPos
			self._add_edge(wrd[t - 1], wrd[t], 			'textPositionAvg', 		1 + glbPos, glbPos + 1)
			self.edge[wrd[t - 1]][wrd[t]][				'textPositionLast'] = 	glbPos
			if not (self.edge[wrd[t - 1]][wrd[t]].get(	'PositionFirstSent')):
				self.edge[wrd[t - 1]][wrd[t]][			'PositionFirstSent'] = 	t
			self._add_edge(wrd[t - 1], wrd[t], 			'PositionAvgSent', 		1 + t, t + 1)
			self.edge[wrd[t - 1]][wrd[t]][				'PositionLastSent'] = 	t

			self.sentence_words[sn].add(wrd[t])

		return glbPos




class separate_graph(text_graph):
	def __init__(s,text,separating='(\.|;|\n\n)',fromFile=0):
		nx.DiGraph.__init__(s)
		if (fromFile):
			with open(text) as f:
				ss=f.read()#words_pattern=u'[a-zA-Zа-яёА-ЯЁ\-]+'
		encoding=chardet.detect(text[:289]+' '+text[len(text)/2-144:len(text)/2+144]+' '+text[-289:])['encoding']
		if (encoding=='utf-8'):
			ss=text_words(text,words_pattern=u'([a-zA-Zа-яёА-ЯЁ\-]+|'+separating+')',stop_words=stop_words)
		else:
			ss=text_words(text.decode(encoding),words_pattern=u'([a-zA-Zа-яёА-ЯЁ\-]+|'+separating+')',stop_words=stop_words)#.decode(encoding))#text.decode('cp1251').split()#
		s.node_list=dict()
		s.node_property=dict()
		s.edge_list=dict()
		s.edge_property=dict()
		_S=None
		r=re.compile(separating)
		try:
			s.add_node(ss[0].lower())
			_S=ss[0].lower()
		except:
			return None
		s.node_list=dict()
		s.node_property=dict()
		s.edge_list=dict()
		s.edge_property=dict()
		s.add_properties('node',weight=1,textPositionFirst=-1,textPositionLast=-1,textPositionAvg=0,edges_in=0,edges_out=0,sweight=1.0)
		s.add_properties('edge',weight=1,textPositionFirst=-1,textPositionLast=-1,textPositionAvg=0,sweight=1.0,is_tree_edge=False)
		s.node[_S]['weight']=1
		s.node[_S]['textPositionFirst']=1
		s.node[_S]['textPositionAvg']=1
		s.node[_S]['textPositionLast']=1
		t=0
		for tt in ss:
			t+=1
			try:
				ss[t]=ss[t]
			except(IndexError):
				break
			#print(t,' ',ss.ii)##########################

			s.add_node(ss[t])
			s._add_node(ss[t],'weight',1,1)
			if not (s.node[ss[t]].get('textPositionFirst')):
				s.node[ss[t]]['textPositionFirst']=t+1
			s._add_node(ss[t],'textPositionAvg',t+1,t+1)
			s.node[ss[t]]['textPositionLast']=t+1
			
			m=r.match(ss[t])
			#if (m.end - m.start()==len(ss[t])):
				#########################
			
			s.add_edge(ss[t-1],ss[t])
			s._add_edge(ss[t-1],ss[t])
			if not (s.edge[ss[t-1]][ss[t]].get('textPositionFirst')):
				s.edge[ss[t-1]][ss[t]]['textPositionFirst']=t
			s._add_edge(ss[t-1],ss[t],'textPositionAvg',1+t,t+1)
			s.edge[ss[t-1]][ss[t]]['textPositionLast']=t
		for v in s.node.keys():
			s.node[v]['textPositionAvg']/=float(s.node[v]['weight'])
			s.node[v]['edges_out']=len(s.edge[v])
			s.node[v]['edges_in']=0
			s.node[v]['sweight']=1.0/s.node[v]['weight']
		for e in s.edge:
			for ee in s.edge[e]:
				s.edge[e][ee]['textPositionAvg']/=float(s.edge[e][ee]['weight'])
				s.node[ee]['edges_in']+=1
				s.edge[e][ee]['is_tree_edge']=s.node[e]['textPositionFirst']<s.node[ee]['textPositionFirst']
				s.edge[e][ee]['sweight']=1.0/s.edge[e][ee]['weight']
		s.sort_edge()
		s.sort_node()

def f():
	text = 'D:/Users/DAN85_000/Desktop/py/tg/corpus/1.txt'
	sg = sentence_graph(text, 1,stop_words=(u'в', u'но', u'и', u'на', u'из', u'то',
                                            u'к', u'а', u'что', u'-',u'не', u'с', u'о'))
	kn = sg.node.keys()
	return sg

def all_pairs_in_sent(sg):
	# type: (sentence_graph) -> None
	words=None
	res = []
	for sn in range(len(sg.sentence_words)):
		words = sg.sentence_words[sn].copy()
		res.append(dict())
		res[sn][(u'_', u'_')] = 0
		for sw in range(len(words)):
			w = words.pop()
			for w2 in words:
				if sg.edge.has_key(w):
					if sg.edge[w].has_key(w2):
						res[sn][(w,w2)] = sg.edge[w][w2]['weight']
					else:
						res[sn][(u'_',u'_')] +=1
				if sg.edge.has_key(w2):
					if sg.edge[w2].has_key(w):
						res[sn][(w2,w)] = sg.edge[w2][w]['weight']
					else:
						res[sn][(u'_',u'_')] +=1
	return res




if __name__=='__main__':
	sg=f()
	rp = all_pairs_in_sent(sg)
	i=0
	for r in rp:
		def _f(x,y):
			if r[x]>r[y]:
				return 1
			elif r[x]<r[y]:
				return -1
			else:
				return 0
		ar = r.keys()
		ar.sort(cmp=_f)#lambda x,y: 1 if r[x]>r[y] else -1 if r[x]<r[y] else 0)
		i+=1
		print(i)
		for k in ar:
			print(u'%s %s: %i'%(k[0],k[1],r[k]))
	pass