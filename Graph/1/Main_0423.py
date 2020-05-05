from collections import defaultdict
from ast import literal_eval
import sys

class SC:
    def __init__(self, test_file_name, result_file_name):
        self.test_file = test_file_name
        self.result_file = result_file_name
        self.graph = defaultdict(set)

    def read_edgefile(self, test_file_name, delimiter=','):
        graph = defaultdict(set)
        with open(test_file_name, 'r') as f:
            for line in f:
                s = line.strip().split(delimiter)
                graph[int(s[0])].add(int(s[1]))
        return graph

    def simple_cycles(self, graph, limit):
        def _unblock(thisnode, blocked, B):
            stack = set([thisnode])
            while stack:
                node = stack.pop()
                if node in blocked:
                    blocked.remove(node)
                    stack.update(B[node])
                    B[node].clear()
        sccs = [scc for scc in self.strongly_connected_components(graph)
                if len(scc) > 1]
        while sccs:
            scc = sccs.pop()
            startnode = scc.pop()
            path = [startnode]
            blocked = set()
            closed = set()
            blocked.add(startnode)
            B = defaultdict(set)
            stack = [(startnode,list(graph[startnode]))]
            while stack:
                thisnode, nbrs = stack[-1]
                if nbrs and len(path) <= limit:
                    nextnode = nbrs.pop()
                    if len(blocked) > limit:
                        pass
                    if nextnode == startnode: # can not use is
                        yield path[:]
                        closed.update(path)
                    elif nextnode not in blocked:
                        path.append(nextnode)
                        stack.append((nextnode, list(graph[nextnode])))
                        closed.discard(nextnode)
                        blocked.add(nextnode)
                        continue
                # if not nbrs or len(path) > limit: # 20200422
                else:
                    if thisnode in closed:
                        _unblock(thisnode, blocked, B)
                    else:
                        if thisnode in graph:
                            for nbr in graph[thisnode]:
                                if thisnode not in B[nbr]:
                                    B[nbr].add(thisnode)
                    stack.pop()
                    path.pop()
            self.remove_node(graph, startnode)
            # done processing this node
            H = self.subgraph(graph, set(scc))  # make smaller to avoid work in SCC routine
            sccs.extend(scc for scc in self.strongly_connected_components(H)
                        if len(scc) > 1)

    def strongly_connected_components(self, graph):
        preorder = {}
        lowlink = {}
        scc_found = set()
        scc_queue = []
        i = 0     # Preorder counter
        key_copy = tuple(graph.keys())    # Feel free to use any iterable collection
        for source in key_copy:    #graph:
            if source not in scc_found:
                queue = [source]
                while queue:
                    v = queue[-1]
                    if v not in preorder:
                        i = i + 1
                        preorder[v] = i
                    done = True
                    for w in graph[v]:
                        if w not in preorder:
                            queue.append(w)
                            done = False
                            break
                    if done:
                        lowlink[v] = preorder[v]
                        for w in graph[v]:
                            if w not in scc_found:
                                if preorder[w] > preorder[v]:
                                    lowlink[v] = min([lowlink[v], lowlink[w]])
                                else:
                                    lowlink[v] = min([lowlink[v], preorder[w]])
                        queue.pop()
                        if lowlink[v] == preorder[v]: # can use is
                            scc = {v}
                            while scc_queue and preorder[scc_queue[-1]] > preorder[v]:
                                k = scc_queue.pop()
                                scc.add(k)
                            scc_found.update(scc)
                            yield scc
                        else:
                            scc_queue.append(v)

    def remove_node(self, graph, target):
        del graph[target]
        for nbrs in graph.values():
            nbrs.discard(target)

    def subgraph(self, graph, vertices):
        sub = defaultdict(set)
        for v in vertices:
            sub[v] = graph[v] & vertices
        return sub
        # return {v: graph[v] & vertices for v in vertices}

    def get_result(self):
        G = self.read_edgefile(test_file, delimiter=',')
        cycles_result = []
        for cycle in self.simple_cycles(G, 7):
            if len(cycle) != 2:
                i = cycle.index(min(cycle))
                cycles_result.append(cycle[i:] + cycle[:i])
        cycles_result.sort(key=lambda x:(len(x),x[0]))
        f = open(result_file, 'w')
        f.writelines(str(len(cycles_result))+'\n')
        f.writelines(map(lambda x : ','.join([str(elem) for elem in x]) +'\n', cycles_result))
        f.close()


def print_help_and_exit():
    print("usage:python3 main.py train_data.txt test_data.txt predict.txt [debug]")
    sys.exit(-1)


def parse_args():
    debug = False
    if len(sys.argv) is 2:
        if sys.argv[1] is 'debug':
            print("test mode")
            debug = True
        else:
            print_help_and_exit()
    return debug

if __name__ == "__main__":
    debug = parse_args()
    test_file = "/data/test_data.txt"
    result_file = "/projects/student/result.txt"
    sc = SC(test_file, result_file)
    sc.get_result()

    if debug:
        answer_file ="/projects/student/answer.txt"
        f_a = open(answer_file, 'r')
        f_r = open(result_file, 'r')
        a = []
        r = []
        lines = f_a.readlines()
        for line in lines:
            a.append(line.strip())
        f_a.close()

        lines = f_r.readlines()
        for line in lines:
            r.append(line.strip())
        f_r.close()

        print("answer lines:%d" % (len(a)))
        print("rusult lines:%d" % (len(r)))

        errline = 0
        for i in range(len(a)):
            if a[i] != r[i]:
                errline += 1

        accuracy = (len(a)-errline)/len(a)
        print("accuracy:%f" %(accuracy))