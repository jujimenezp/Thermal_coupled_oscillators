#include <fstream>
#include <gsl/gsl_rng.h>
#include <gsl/gsl_randist.h>

double gauss_dist(gsl_rng *r, double sigma){
    double eta= gsl_ran_gaussian(r,sigma);
    return eta;
}

int main(int argc, char** argv){
    int SEED=std::stoi(argv[1]);
    double g,sigma=std::stoi(argv[3]), samples=std::stoi(argv[2]);
    gsl_rng * r = gsl_rng_alloc(gsl_rng_mt19937);
    gsl_rng_set(r, SEED);

    std::ofstream file("results/gauss.dat");
    for(int i=0; i < samples; i++){
        g=gauss_dist(r, sigma);
        file << g << "\n";
    }
    file.close();
    gsl_rng_free(r);
    return 0;
}
