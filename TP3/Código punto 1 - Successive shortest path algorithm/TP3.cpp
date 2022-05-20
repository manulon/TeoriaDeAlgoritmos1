#include <vector>
#include <iostream>
#include <queue>
#include "Algorithms.h"
#include "Graph.h"
#include "File_Reader.h"

Graph build_graph_using_csv(std::string fn){
    File_Reader file(fn);
    return file.read_file_and_build_graph();
}

int main(int argc, char const *argv[]) {
    Algorithms a;
    Graph g = build_graph_using_csv(argv[1]);
    std::vector<int> v = a.min_cost_flow(g.total_nodes, g.edges, INF, g.s, g.t);
    printf("Costo: %i, Flow: %i\n", v[0], v[1]);
    return 0;
}
