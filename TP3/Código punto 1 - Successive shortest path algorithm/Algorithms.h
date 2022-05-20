#ifndef ALGORITHMS_H
#define ALGORITHMS_H

#include <vector>
#include "Edge.h"

const int INF = 1e9;

class Algorithms{
private:
    std::vector<std::vector<int>> adj;
    std::vector<std::vector<int>> cost;
    std::vector<std::vector<int>> capacity;

public:
    Algorithms();
    void shortest_paths(int n, int v0, std::vector<int>& d, std::vector<int>& p);
    std::vector<int> min_cost_flow(int N, std::vector<Edge> edges, int K, int s, int t);
    ~Algorithms();
};


#endif
