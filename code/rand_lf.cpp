#include "rand_lf.hpp"

int main(int argc, char** argv){
    double t_end=10, dt=0.01;
    double k=0.5;
    particle b(3, 3, 0, 1, 0, 0, 0);
    std::vector<particle> bs = {b};

    lf_integrator osc(dt);
    osc.update_F(bs,k);
    osc.initialize_v(bs);

    std::ofstream file("results/oscillator.dat");
    file <<"t" << "\tx" << "\ty" << "\n";
    for(double t=0; t < t_end; t+=dt){
        osc.update_x(bs);
        osc.update_F(bs,k);
        osc.update_v(bs);
        file << t <<"\t"<< bs[0].x <<"\t"<< bs[0].y <<"\t"<<bs[0].vx <<"\t"<< bs[0].Fx << "\n";
    }
    file.close();

    return 0;
}
