#ifndef UTILS_H
#define UTILS_H

std::vector<std::string> split(std::string str, char pattern) {
    
    int posInit = 0;
    int posFound = 0;
    std::string splitted;
    std::vector<std::string> results;
    
    while(posFound >= 0){
        posFound = str.find(pattern, posInit);
        splitted = str.substr(posInit, posFound - posInit);
        posInit = posFound + 1;
        results.push_back(splitted);
    }

    return results;
}

#endif