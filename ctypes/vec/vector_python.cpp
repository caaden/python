#include <vector>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

extern "C" {
    //constructor
    vector<int>* new_vector() {
        return new vector<int>;
    }
    
    //destructor
    void delete_vector(vector<int>* v) {
        cout << "destructor called in c++." << v << endl;
        delete v;
    }
    //c wrapper for size
    int vector_size(vector<int>* v) {
        return v->size();
    } 
    //c wrapper for get
    int vector_get(vector<int>* v, int i) {
        return v->at(i);
    }
    //c wrapper for pushback
    void vector_pushback(vector<int>* v, int i) {
        v->push_back(i);
    }
}

int main(void){
    cout<<"Hello World"<<endl;
    return 0;
}