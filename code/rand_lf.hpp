#include <functional>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <gsl/gsl_rng.h>


#ifndef RAND_LF_H_
#define RAND_LF_H_

class particle{
    private:
    public:
        double R;
        double x,y;
        double vx,vy;
        double Fx,Fy;

        particle(double Ri, double xi, double yi, double vxi, double vyi,
                 double Fxi, double Fyi)
        {R=Ri; x=xi; y=yi; vx=vxi; vy=vyi; Fx=Fxi; Fy=Fyi;}
        void reset_F(){Fx=Fy=0;}
        void add_F(double Fx0, double Fy0);
};

void particle::add_F(double Fx0, double Fy0){
        Fx+=Fx0;
        Fy+=Fy0;
}

class lf_integrator{
    public:
        double dt;
        lf_integrator(double dti){dt=dti;}
        void initialize_v(std::vector<particle> &particles);
        void update_F(std::vector<particle> &particles, double k);
        void update_v(std::vector<particle> &particles);
        void update_x(std::vector<particle> &particles);
};

void lf_integrator::initialize_v(std::vector<particle> &particles){
        for(auto &p: particles){
                p.vx += 0.5*dt*p.Fx;
                p.vy += 0.5*dt*p.Fy;
        }
}

void lf_integrator::update_F(std::vector<particle> &particles, double k){
        double F;
        for(auto &p: particles){
                p.reset_F();
                F=-k*p.x;
                p.add_F(F,0);
        }
}

void lf_integrator::update_v(std::vector<particle> &particles){
        for(auto &p: particles){
                p.vx += dt*p.Fx;
                p.vy += dt*p.Fy;
        }
}

void lf_integrator::update_x(std::vector<particle> &particles){
        for(auto &p: particles){
                p.x += dt*p.vx;
                p.y += dt*p.vy;
        }
}

#endif // RAND_LF_H_
