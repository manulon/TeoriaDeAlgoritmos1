#ifndef INDEX_IS_NOT_OPEN_EXCEPTION
#define INDEX_IS_NOT_OPEN_EXCEPTION

#include "FileIsNotOpenException.h"
#include <iostream>

class IndexIsNotOpenException : public FileIsNotOpenException {
    public:
        virtual const char* what() override {
            return "No se puede ingresar al archivo index \n";
        }
};

#endif