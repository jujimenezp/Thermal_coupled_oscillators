#include "coupled.hpp"

int main(int argc, char** argv){
    double t_end=std::stod(argv[3]), dt=std::stod(argv[2]);
    int t_imp=5;
    double k=4, f=1-exp(-dt*6), T=1;
    double c_x0=-5, c_x1=5;

    bool bonded=false;
    double thres_bond=0.8, thres_unbond=2, dist, F;

    // particle(double Ri, double xi, double c_xi, double yi, double c_yi, double vxi, double vyi, double Fxi, double Fyi)
    std::vector<particle> bs{particle(3, -6, c_x0, 0, 0, 0, 0, 0, 0), particle(3, 6, c_x1, 0, 0, 0, 0, 0, 0)};
    double SEED=std::stoi(argv[1]);
    gsl_rng * r = gsl_rng_alloc(gsl_rng_mt19937);
    gsl_rng_set(r,SEED);

    // lf_integrator(double dti, double fi, double Ti)
    lf_integrator osc(dt,f,T);
    osc.update_F(bs,k);
    osc.initialize_v(bs);

    std::ofstream file("results/coupled.dat");
    //file <<"t" << "\tx" << "\tvx" <<"\n";
    for(double t=0; t < t_end; t+=dt){
        if(int(t/dt)%t_imp == 0){
            file << t;
            for(int i=0; i < bs.size(); i++){
                file << "\t" << bs[i].x;
                //file <<"\t"<< bs[i].x <<"\t"<< bs[i].vx;
            }
        file << "\n";
        }
        osc.update_F(bs,k);
        osc.check_bonded(bs,k,thres_bond,thres_unbond);

        osc.update_v1(bs);
        osc.impulse_Dv(bs, r);
        osc.update_x(bs);
        osc.update_v2(bs);

        bs[0].c_x = c_x0 + t*0.1;
        bs[1].c_x = c_x1 + -t*0.1;
    }
    file.close();
    gsl_rng_free(r);
    return 0;
}
