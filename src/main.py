__author__ = 'Nick Hirakawa'

from parse import *
from query import QueryProcessor
import operator

def main():
	qp = QueryParser(filename='../text/queries.txt')
	cp = CorpusParser(filename='../text/corpus.txt')
	qp.parse()
	queries = qp.get_queries()
	cp.parse()
	out=open('../text/result.txt','w')
	corpus = cp.get_corpus()
	proc = QueryProcessor(queries, corpus)
	results = proc.run()
	qid = 0
	for result in results:
		sorted_x = sorted(result.iteritems(), key=operator.itemgetter(1))
		sorted_x.reverse()
		index = 0
		#这里可指定输出topK个
		for i in sorted_x[:10]:
			out.write(str(qid)+'\t'+str(index)+'\t'+i[0]+'\t'+str(i[1])+'\n')
			index += 1
		qid += 1


if __name__ == '__main__':
	main()