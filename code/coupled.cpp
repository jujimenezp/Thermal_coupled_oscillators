#include "coupled.hpp"

int main(int argc, char** argv){
    double t_end=std::stod(argv[3]), dt=std::stod(argv[2]);
    int t_imp=5, N=1000;
    double k=4, k_coupled=4, f=1-exp(-dt*4.001), T=4;
    double c_x[2]={-3, 3};

    double thres_bond=12, thres_unbond=12;
    double sep = 18;
    double x0=-(k*c_x[1]+2*k_coupled*thres_bond/2)/(k+2*k_coupled), x1=(k*c_x[1]+2*k_coupled*thres_bond/2)/(k+2*k_coupled);

    double v[2] = {-6./4800, 6./4800};
    double t_eq = 100;

    double t1 = (-sep/2 - c_x[0])/v[0] + t_eq;

    double W1=0, c_x_prev=0;

    //std::ofstream file("results/coupled_pos.dat");
    //std::ofstream file2("results/coupled_w.dat");
    std::ofstream file("results/hist_work_v6_4800.dat");

    std::vector<double> Fs(t_end/dt,0);
    std::vector<double> Ws(t_end/dt,0);
    std::vector<double> x_cs(t_end/dt,c_x[0]);

    for(int i=1; i <= N; i++){
        W1=0;
        // particle(double Ri, double xi, double c_xi, double yi, double c_yi, double vxi, double vyi, double Fxi, double Fyi)
        std::vector<particle> bs{particle(3, x0, c_x[0], 0, 0, 0, 0, 0, 0), particle(3, x1, c_x[1], 0, 0, 0, 0, 0, 0)};
        //double SEED=std::stoi(argv[1]);
        double SEED=i;
        gsl_rng * r = gsl_rng_alloc(gsl_rng_mt19937);
        gsl_rng_set(r,SEED);

        // lf_integrator(double dti, double fi, double Ti)
        lf_integrator osc(dt,f,T);
        osc.update_F(bs,k);
        osc.initialize_v(bs);

        //file <<"t" << "\tx1" << "\tx2" <<"\n";
        for(double t=0; t < t_end; t+=dt){
            // if(int(t/dt)%t_imp == 0){
            //     file << t;
            //     for(int i=0; i < bs.size(); i++){
            //         file << "\t" << bs[i].x;
            //         file2 << bs[i].c_x << "\t" << -k*(bs[i].x-bs[i].c_x) <<"\t"<< W1 <<"\t";
            //         //file <<"\t"<< bs[i].x <<"\t"<< bs[i].vx;
            //     }
            //     file << "\n"; file2 << "\n";
            // }
            osc.update_F(bs,k);
            osc.check_bonded(bs,k_coupled,thres_bond,thres_unbond);

            osc.update_v1(bs);
            osc.impulse_Dv(bs, r);
            osc.update_x(bs, k);
            osc.update_v2(bs);

            //Protocols
            c_x_prev=bs[0].c_x;
            if(t>t_eq && t <= t1){
                bs[0].c_x = c_x[0] + v[0]*(t-t_eq);
                bs[1].c_x = c_x[1] + v[1]*(t-t_eq);
            }
            else if(t > t_end-t1 && t <= t_end - t_eq){
                bs[0].c_x = -sep/2 + v[1]*(t+t1-t_end);
                bs[1].c_x = sep/2 + v[0]*(t+t1-t_end);
            }

            W1 += -k*(bs[0].x-bs[0].c_x)*(bs[0].c_x-c_x_prev);

            if(int(t/dt)%t_imp == 0){
                Fs[floor(t/(dt*t_imp))] += -k*(bs[0].x-bs[0].c_x);
                Ws[floor(t/(dt*t_imp))] += W1;
                x_cs[floor(t/(dt*t_imp))] = bs[0].c_x;
            }

            if(floor(t/dt) == floor((t_eq+2400.)/dt)){
                file << W1 <<"\t";
            }
            else if(floor(t/dt) == floor(5000./dt)){
                file << W1 <<"\t";
            }
            else if(floor(t/dt) == floor(9950./dt)){
                file << W1 <<"\n";
            }

        }
        gsl_rng_free(r);
    }
    file.close();
    //file2.close();

    std::ofstream avg_file("results/avg_w.dat");
    for(int i=0; i < Ws.size(); i++){
        avg_file << x_cs[i] << "\t" <<Fs[i]/N << "\t" <<Ws[i]/N << "\n";
    }
    avg_file.close();

    return 0;
}
