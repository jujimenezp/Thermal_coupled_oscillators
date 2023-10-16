#include "coupled.hpp"

int main(int argc, char** argv){
    double t_end=std::stod(argv[3]), dt=std::stod(argv[2]);
    int t_imp=5;
    double k=4, f=1-exp(-dt*4.01), T=1./4;
    double x0=-11, x1=11;
    double c_x0=-10, c_x1=10;

    bool bonded=false;
    double thres_bond=4, thres_unbond=4, dist, F;

    double interval = t_end/16;
    double interval2 = t_end-interval;
    double sep = 2;


    // particle(double Ri, double xi, double c_xi, double yi, double c_yi, double vxi, double vyi, double Fxi, double Fyi)
    std::vector<particle> bs{particle(3, x0, c_x0, 0, 0, 0, 0, 0, 0), particle(3, x1, c_x1, 0, 0, 0, 0, 0, 0)};
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

        //Protocols
        if(t <= interval){
            bs[0].c_x = c_x0 - t*(c_x0+sep/2)/interval;
            bs[1].c_x = c_x1 - t*(c_x1-sep/2)/interval;
        }
        else if(t > interval2){
            bs[0].c_x = -sep/2 + (t-interval2)*(c_x0+sep/2)/interval;
            bs[1].c_x = sep/2 + (t-interval2)*(c_x1-sep/2)/interval;
        }
    }
    file.close();
    gsl_rng_free(r);
    return 0;
}
