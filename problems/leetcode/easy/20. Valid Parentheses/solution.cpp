#include<iostream>
#include "solution.h"

using namespace std;

int main(int argc, char *argv[]) {
    bool isValid = Solution().isValid("()");
    string result = isValid ? "true" : "false";

    cout << result << endl;

    return 0;
}