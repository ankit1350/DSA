#include <iostream>
#define SIZE 5
using namespace std;

class Hash {
private:
    int ht[SIZE];

public:
    Hash() {
        for (int i = 0; i < SIZE; i++) {
            ht[i] = -1;   // initialize table as empty
        }
    }

    void insert() {
        int key, loc, ans, cnt;
        do {
            cout << "Enter key to insert: ";
            cin >> key;

            loc = key % SIZE;
            if (ht[loc] == -1) {
                ht[loc] = key;
            } else {
                cnt = 0;
                int start = loc;
                while (ht[loc] != -1 && cnt < SIZE) {
                    loc = (loc + 1) % SIZE;  // linear probing
                    cnt++;
                }
                if (cnt < SIZE) {
                    ht[loc] = key;
                } else {
                    cout << "Hash table is full. Cannot insert " << key << endl;
                }
            }

            cout << "Do you want to insert more keys? (1 = yes / 0 = no): ";
            cin >> ans;
        } while (ans == 1);
    }

    void display() {
        cout << "\nHash Table:\n";
        for (int i = 0; i < SIZE; i++) {
            cout << i << " --> " << ht[i] << endl;
        }
    }
};

int main() {
    Hash h;
    h.insert();
    h.display();
    return 0;
}
