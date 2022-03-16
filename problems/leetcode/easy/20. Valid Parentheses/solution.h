//
// Created by kouz on 2022/03/13.
//

#ifndef CORE_SV_SOLUTION_H
#define CORE_SV_SOLUTION_H

#include<iostream>
#include<stack>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        for (const auto &item: s) {
            if (isOpenBracket(item)) {
                stack.push(item);
                continue;
            }
            if (isCloseBracket(item) && !stack.empty() && isMatchWith(stack.top(), item)) {
                stack.pop();
                continue;
            }
            return false;
        }
        return stack.empty();
    }

private:
    bool isOpenBracket(const char &item) {
        return item == '(' ||
               item == '{' ||
               item == '[';
    }

    bool isCloseBracket(const char &item) {
        return item == ')' ||
               item == '}' ||
               item == ']';
    }

    bool isMatchWith(const char &top, const char &item) {
        return (top == '(' && item == ')') ||
                (top == '{' && item == '}') ||
                (top == '[' && item == ']');
    }
};

#endif //CORE_SV_SOLUTION_H
