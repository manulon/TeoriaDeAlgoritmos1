#include "File_Reader.h"
#include "Utils.h"

#include <vector>
#include <iostream>

File_Reader:: File_Reader (const std::string& index): myfile_index(index){}

Graph File_Reader:: read_file_and_build_graph(){
    std::string line;
    std::vector<std::string> results;
    Graph graph;

    graph.total_nodes = 0;

    for(int i = 0; i < 2; i++) {
        getline(this->myfile_index,line);
        graph.map.insert({line.c_str(), graph.total_nodes});
        if(i == 0) {
            graph.s = graph.map.at(line.c_str());
        } 
        else {
            graph.t = graph.map.at(line.c_str());
        }
        graph.total_nodes++;
    }
    
    while ( getline(this->myfile_index,line) ){
        Edge e;
        results = split(line.c_str(), ',');
        std::string from = results[0].c_str();
        std::string to = results[1].c_str();
        if ( graph.map.find(from) == graph.map.end() ) {
            graph.map.insert({from, graph.total_nodes});
            graph.total_nodes++;
        }  
        if ( graph.map.find(to) == graph.map.end() ) {
            graph.map.insert({to, graph.total_nodes});
            graph.total_nodes++;
        } 
        e.from = graph.map.at(from);
        e.to = graph.map.at(to);
        e.cost = atoi(results[2].c_str());
        e.capacity = atoi(results[3].c_str());
        graph.edges.push_back(e);
    }

    return graph;
}

File_Reader:: ~File_Reader(){
    this->myfile_index.close();
}
