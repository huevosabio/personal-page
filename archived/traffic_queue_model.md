Title: Understanding MATSim's queuing model.
Date: 2016-07-20 14:30
Tags: research, queuing theory, amod, transportation 	
Author: Ramon Dario Iglesias
Summary: Notes on how Matsim models traffic behavior and how it compares to our original model.

I'm currently working in optimal coordination/control of fleets of autonomous
vehicles (also known as Autonomous Mobility on Demand, or AMoD) as part of the [Autonomous System Laboratory][ASL].
In [our last paper][RI-FR-RZ-MP:16], we modeled the operation AMoD systems as a [BCMP queuing network][BCMP].
The goal was to model the system stochastically and find an open-loop control policy that would minimize congestion while
keeping the system in balance (balance we define as having equal level-of-service at all stations/regions).
Indeed, the BCMP approach allowed us to find an asymptotically optimal solution that can be efficiently calculated.
However, we made significant assumptions in the system, and we now want to port this approach to more realistic scenarios.

Currently, there are several different simulation software tools with varying use cases and degrees of accuracy (for brevity I'll omit enumerating them). We chose [MATSim][MATSim] for its extensibility, having the right scale (capable of modeling hundreds of thousands of vehicles), and the fact that it is FOSS. The extensibility was a key requirements, since we want to be able to model our own algorithms within the simulation software, and it is likely that we will need to expand the core simulation to include future research, e.g., public transportation or the smart grid. The scale makes it very attractive as our goal is to control larges fleets of autonomous vehicles.
Being open source allows us to check the source code anytime to fully understand how it works internally, instead of treating it as a black box. This is key because the assumptions we make for our algorithms must be compatible with those made for simulation.

Thus, for the next several days, I'll be reviewing the core modeling aspects of MATSim, comparing them with our models and find a practical (and tractable) way to make both as equivalent as possible. Let's start with the queuing model.


As it turns out, MATSim gets its large-scale modeling capabilities by modeling traffic as a queue instead of  modeling the individual, local interaction between cars. This allows the simulation [to be more efficient][NC:05] while being able to track each vehicle individually. Luckily, our BCMP approach is also based on queues. The task is then to compare how different they actually are, and whether we can port their approach into a [BCMP network][BCMP].

After some light skimming of several sources, it turns out that the queue model they use is based on [Gawron's model][CG:98]. The key idea is this. Each road link is a First-In-First-Out (FIFO) queue. When a vehicle arrives to the beginning of a queue, the model uses a "vehicle delay function" (VDF) to estimate the minimum time it will take the vehicle to cross the road $T_0$. Thus, the ETA of at the end of the road is $t_0 + T_0$. Now, the vehicle is placed on a queue once it has spent at least $T_0$ time, and the queue releases $N \leq N_{max}$ vehicles at each time step. Here $N_{max}$ is the flow capacity, that is, the number of vehicles per unit time the queue is able to process. Vehicles who are ready to leave the queue but whose turn has not come (because of the cap on how many vehicles may leave at a given time step) remain in the queue until their time has come. In this fashion, the queue grows until it reaches a capacity $C$, and while the queue is of size $C$, new vehicles attempting to enter the road will be rejected, and placed back in their original roads. This way, spillback behavior is emulated.

From a first glance, this sort of model does not seem to be reflected in traditional queuing theory, much less in BCMP. First of all the release of vehicles, or the "service rate" in traditional queuing theory, is not quite stochastic. This should be easy to bypass since BCMP formulations give ample room for how the distribution of the service rates should be (in fact, much of the metrics can be estimated by using only the means). More worrisome is the fact that we are dealing with finite capacity queues. Often, this means that there are packet loss, however, in our case we can't just lose vehicles. Assuming infinite capacity might be a serious deviation from the simulation model, bypassing the spillback phenomenon.

Luckily, there has been some work in this area in these two papers: [M/G/c/K finite queues][JMS:07], where a finite queue with the purpose of simulating traffic is presented; and [optimal routing in state-dependent queues][JMS:07], where the author tackles the issue of routing with the aforementioned queues. Allegedly, networks of these queues can be represented in product form. Perhaps we could expand our findings in the BCMP paper to a network of finite-buffer queues, and make it comparable to the queues that MATSim uses.


[ASL]: http://asl.stanford.edu "Autonomous Systems Laboratory"

[RI-FR-RZ-MP:16]: http://arxiv.org/abs/1607.04357 "A BCMP Network Approach to Modeling and Controlling Autonomous Mobility-on-Demand Systems"

[CG:98]: http://www.worldscientific.com/doi/abs/10.1142/S0129183198000303 "An Iterative Algorithm to Determine the Dynamic User Equilibrium in a Traffic Simulation Model"

[NC:05]: http://e-collection.library.ethz.ch/eserv/eth:28009/eth-28009-02.pdf "Large-scale parallel graph-based simulations"

[PJF:10]: http://www.matsim.org/sites/default/files/scenarios/paper_presented_at_southern_african_transport_conference_2010.pdf "Agent-based transport simulation versus equilibrium assignment for private vehicle traffic in Gauteng"

[MATSimBook]: http://www.matsim.org/the-book "The MATSim Book"

[BCMP]: https://en.wikipedia.org/wiki/BCMP_network "Wikpedia: BCMP Network"

[JMS:07]: http://www.utpjournals.press/doi/abs/10.3138/infor.45.4.257 "Multi-server, finite waiting room, M/G/c/K optimization models"

[JMS:11]: http://www.utpjournals.press/doi/abs/10.3138/infor.49.1.045 "Optimal routing in closed queueing networks with state dependent queues"
