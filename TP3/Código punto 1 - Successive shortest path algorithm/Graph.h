#ifndef GRAPH_H
#define GRAPH_H

#include <string>
#include <vector>
#include <map>
#include "Edge.h"

struct Graph
{
    int s;
    int t;
    int total_nodes;
    std::map<std::string, int> map;
    std::vector<Edge> edges;
};

#endif