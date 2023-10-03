
#include <iostream>
#include <string>
#include <vector>

class Book {

    public:
        std::string title;
        std::string author;
        int pages;

        Book(std::string x, std::string y, int z) {
            title = x;
            author = y;
            pages = z;
        }
        void showBook() {
            std::cout << " titulo " << title << " autor: " << author << " pages " << pages << std::endl;
        }    
};

class Library {
    public:
        std::vector<Book> books = {};
        std::string name;
        Library(std::x) {
            name = x;
        }

};


int main() {

    Book kevin("Harry", "Kevin",250);
    kevin.showBook();


    return 1;
}