#include <omp.h>
#include <stdio.h>
#include <math.h>

#define N 100000000

int main() {
    double sum = 0.0;
    double t0 = omp_get_wtime();

    #pragma omp parallel for reduction(+:sum)
    for (long i = 0; i < N; i++) {
        sum += sqrt((double)i);
    }

    double t1 = omp_get_wtime();
    printf("Soma: %.3f, Tempo: %.3fs, Threads: %d\n", sum, t1-t0, omp_get_max_threads());
    return 0;
}
