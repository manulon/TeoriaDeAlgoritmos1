#ifndef FILE_READER_H
#define FILE_READER_H

#include <string>
#include <fstream>
#include <map>
#include "Edge.h"
#include "Graph.h"

class File_Reader {
private:
    std::ifstream myfile_index;   

public:
    File_Reader
    (const std::string& index);
    Graph read_file_and_build_graph();
    ~File_Reader();
};

#endif