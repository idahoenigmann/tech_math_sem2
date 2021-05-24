//
// Created by ida on 24.05.21.
//
#include </home/ida/technische_mathematik/tech_math_sem2/extern/pybind11/include/pybind11/pybind11.h>

float f(n, a, x_0) {
    float res = x_0;
    for (int i{}, i < n, i++) {
        res = 0.5 * (res + a / res);
    }
    return res;
}

PYBIND11_MODULE(wrap, m) {
    m.doc() = "c++ module for problem 3";

    m.def("f", &f, "computes sequence described in problem 3")
}

