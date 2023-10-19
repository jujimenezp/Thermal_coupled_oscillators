#include "coupled.hpp"

int main(int argc, char** argv){
    double t_end=std::stod(argv[3]), dt=std::stod(argv[2]);
    int t_imp=5;
    double k=4, k_coupled=4, f=1-exp(-dt*4.01), T=1./4;
    double x0=-10, x1=10;
    double c_x[2]={-10, 10};

    double thres_bond=0, thres_unbond=0;
    double sep = 0;

    double v[2] = {9./100, -9./100};
    double t1 = (-sep/2 -c_x[0])/v[0];
    double W1=0, c_x_prev=0;


    // particle(double Ri, double xi, double c_xi, double yi, double c_yi, double vxi, double vyi, double Fxi, double Fyi)
    std::vector<particle> bs{particle(3, x0, c_x[0], 0, 0, 0, 0, 0, 0), particle(3, x1, c_x[1], 0, 0, 0, 0, 0, 0)};
    double SEED=std::stoi(argv[1]);
    gsl_rng * r = gsl_rng_alloc(gsl_rng_mt19937);
    gsl_rng_set(r,SEED);

    // lf_integrator(double dti, double fi, double Ti)
    lf_integrator osc(dt,f,T);
    osc.update_F(bs,k);
    osc.initialize_v(bs);

    std::ofstream file("results/coupled_pos.dat");
    std::ofstream file2("results/coupled_w.dat");
    //file <<"t" << "\tx1" << "\tx2" <<"\n";
    for(double t=0; t < t_end; t+=dt){
        if(int(t/dt)%t_imp == 0){
            file << t;
            for(int i=0; i < bs.size(); i++){
                file << "\t" << bs[i].x;
                file2 << bs[i].c_x << "\t" << k*(bs[i].x-bs[i].c_x) <<"\t"<< W1 <<"\t";
                //file <<"\t"<< bs[i].x <<"\t"<< bs[i].vx;
            }
        file << "\n"; file2 << "\n";
        }
        osc.update_F(bs,k);
        osc.check_bonded(bs,k_coupled,thres_bond,thres_unbond);

        osc.update_v1(bs);
        osc.impulse_Dv(bs, r);
        osc.update_x(bs, k);
        osc.update_v2(bs);

        //Protocols
        c_x_prev=bs[0].c_x;
        if(t <= t1){
            bs[0].c_x = c_x[0] + v[0]*t;
            bs[1].c_x = c_x[1] + v[1]*t;
        }
        else if(t > t_end-t1){
            bs[0].c_x = -sep/2 + v[1]*(t+t1-t_end);
            bs[1].c_x = sep/2 + v[0]*(t+t1-t_end);
        }
        W1 += k*(bs[0].x-bs[0].c_x)*(bs[0].c_x-c_x_prev);
    }
    file.close();
    file2.close();
    gsl_rng_free(r);
    return 0;
}
