#include "rand_lf.hpp"

int main(int argc, char** argv){
    double t_end=std::stod(argv[3]), dt=std::stod(argv[2]);
    int t_imp=20;
    double k=0.5;
    // particle(double Ri, double xi, double yi, double vxi, double vyi, double Fxi, double Fyi)
    //particle b(3, 0, 0, 0, 0, 0, 0);
    std::vector<particle> bs = {5000, particle(3, 0, 0, 0, 0, 0, 0)};
    double SEED=std::stoi(argv[1]);
    gsl_rng * r = gsl_rng_alloc(gsl_rng_mt19937);
    gsl_rng_set(r,SEED);

    // lf_integrator(double dti, double fi, double Ti)
    lf_integrator osc(dt,0.5,1);
    //osc.update_F(bs,k);
    osc.initialize_v(bs);

    std::ofstream file("results/trajectories.dat");
    //file <<"t" << "\tx" << "\tvx" <<"\n";
    for(double t=0; t < t_end; t+=dt){
        //osc.update_F(bs,k);
        if(int(t/dt)%t_imp == 0){
            file << t;
            for(int i=0; i < bs.size(); i++){
                file << "\t" << bs[i].x;
                //file <<"\t"<< bs[i].x <<"\t"<< bs[i].vx;
            }
        file << "\n";
        osc.update_v1(bs);
        osc.impulse_Dv(bs, r);
        osc.update_x(bs);
        osc.update_v2(bs);
        }
    }
    file.close();
    gsl_rng_free(r);
    return 0;
}
