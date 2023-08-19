#include <functional>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>


#ifndef RAND_LF_H_
#define RAND_LF_H_

class particle{
    public:
        double R;
        double x,y;
        double vx,vy;
        std::function<double(std::vector<double> args)> Fx;
        std::function<double(std::vector<double> args)> Fy;
        particle(double Ri, double xi, double yi, double vxi, double vyi,
                 std::function<double(std::vector<double> args)> Fxi,
                 std::function<double(std::vector<double> args)> Fyi)
        {R=Ri; x=xi; y=yi; vx=vxi; vy=vyi; Fx=Fxi; Fy=Fyi;}
        void update_F(){
                
        }
};

class lf_integrator{
    public:
        double dt;
        std::vector<particle> particles;

        lf_integrator(std::vector<particle> p_i, double dti)
        {particles=p_i; dt=dti;}
        void initialize_v(std::vector<double> args);
        void update_F();
        void update_v(std::vector<double> args);
        void update_x();
};

void lf_integrator::initialize_v(std::vector<double> args){
        for(auto &p: particles){
                p.vx += 0.5*dt*p.Fx(args);
                p.vy += 0.5*dt*p.Fy(args);
        }
}

void lf_integrator::update_v(std::vector<double> args){
        for(auto &p: particles){
                p.vx += dt*p.Fx(args);
                p.vy += dt*p.Fy(args);
        }
}

void lf_integrator::update_x(){
        for(auto &p: particles){
                p.vx += dt*p.vx;
                p.vy += dt*p.vy;
        }
}

#endif // RAND_LF_H_
