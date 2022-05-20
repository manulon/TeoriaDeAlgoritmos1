#include <vector>
#include <iostream>
#include <queue>
#include "File_Reader.h"
#include "Edge.h"
#include "Algorithms.h"

Algorithms:: Algorithms(): 
adj(), cost(), capacity() {}

void Algorithms:: shortest_paths(int n, int v0, std::vector<int>& d, std::vector<int>& p) {
    d.assign(n, INF);
    d[v0] = 0;
    std::vector<bool> inq(n, false);
    std::queue<int> q;
    q.push(v0);
    p.assign(n, -1);

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        inq[u] = false;
        for (int v : this->adj[u]) {
            if (this->capacity[u][v] > 0 && d[v] > d[u] + this->cost[u][v]) {
                d[v] = d[u] + this->cost[u][v];
                p[v] = u;
                if (!inq[v]) {
                    inq[v] = true;
                    q.push(v);
                }
            }
        }
    }
}

std::vector<int> Algorithms:: min_cost_flow(int N, std::vector<Edge> edges, int K, int s, int t) {
    this->adj.assign(N, std::vector<int>());
    this->cost.assign(N, std::vector<int>(N, 0));
    this->capacity.assign(N, std::vector<int>(N, 0));
    for (Edge e : edges) {
        this->adj[e.from].push_back(e.to);
        this->adj[e.to].push_back(e.from);
        this->cost[e.from][e.to] = e.cost;
        this->cost[e.to][e.from] = -e.cost;
        this->capacity[e.from][e.to] = e.capacity;
    }

    int flow = 0;
    int cost = 0;
    std::vector<int> d, p;
    while (flow < K) {
        shortest_paths(N, s, d, p);
        if (d[t] == INF)
            break;

        int f = K - flow;
        int cur = t;
        while (cur != s) {
            f = std::min(f, this->capacity[p[cur]][cur]);
            cur = p[cur];
        }

        flow += f;
        cost += f * d[t];
        cur = t;
        while (cur != s) {
            this->capacity[p[cur]][cur] -= f;
            this->capacity[cur][p[cur]] += f;
            cur = p[cur];
        }
    }

    std::vector<int> final_result;
    final_result.push_back(cost);
    final_result.push_back(flow);
    return final_result;
}

Algorithms:: ~Algorithms(){}

