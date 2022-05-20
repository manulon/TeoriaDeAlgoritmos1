#ifndef FILE_IS_NOT_OPEN_EXCEPTION_H
#define FILE_IS_NOT_OPEN_EXCEPTION_H

#include <exception>

class FileIsNotOpenException : public std::exception {
    public:
        virtual const char* what(){
            return "No se abrio un archivo \n";
        }
};
#endif