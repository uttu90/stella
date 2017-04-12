import numpy as np
import config
import calculate

time = 0

#Initialization
D_CumInflowtoLake = [0]
D_CumTotRiverFlow = [np.zeros((config.SUBCATCHMENT, config.OBSPOINT))]
D_StreamsSurfQ = [np.zeros((config.SUBCATCHMENT, config.OBSPOINT))]
D_TotRiverFlowNoDelay = [np.zeros((config.SUBCATCHMENT, config.OBSPOINT))]


D_RiverFlowtoLake = np.sum(D_RivLakeSameDay, axis=0) + np.sum(D_RivInflLake, axis=0)
D_GWtoLake = np.sum(D_GWLakeSub)
D_RestartL = O_Reset_ * D_CumInflowtoLake[time]/config.dt

D_RoutingTime = np.divide(I_RoutingDistance, (np.multiply(I_RivFlowTimeNow, I_RoutVeloc_m_per_s)*3.6*24*I_Tortuosity))
I_ReleaseFract = np.minimummin(1, np.divide(I_RiverflowDispersalFactor,
                                            D_RoutingTime,
                                            out=np.ones((config.SUBCATCHMENT, config.OBSPOINT)),
                                            where=D_RoutingTime>0))
D_TotalStreamInflow = (D_SurfaceFlow + np.multiply(D_GWaDisch, (1-D_FracGWtoLake)) + np.sum(D_SoilDischarge, axis=0)) + np.multiply(D_SubCResOutflow, (1-I_DaminThisStream_))
D_SurfFlowObspoint = np.multiply(D_RoutingTime>=1, D_TotalStreamInflow)
D_DirectSurfFkowObsPoint = np.multiply(np.multiply(D_RoutingTime>=0, D_RoutingTime<1), np.multiply(D_TotalStreamInflow*(1-I_ReleaseFrac)))
D_RiverDirect = np.multiply(np.multiply(D_RoutingTime>0, D_RoutingTime<1), np.multiply((1-D_FeedingIntoLake_), np.multiply(D_TotalStreamInflow, (I_ReleaseFrac))))
D_RivInfLake = np.multiply(np.multiply(I_ReleaseFrac, D_TotRiverFlowNoDelay), D_FeedingIntoLake_)
D_SurfFlowRiver = np.multiply(D_RoutingTime>1, D_RoutingTime)
D_CurrRivFlow = np.sum(D_StreamsSurfQ, axis=0)+np.sum(D_TotRiverFlowNoDelay, axis=0)

calculate.update(D_CumInflowtoLake, inflow=D_RiverFlowtoLake + D_GWtoLake, outflow=D_RestartL, dt=config.dt)
calculate.update(D_CumTotRiverFlow, inflow=D_RiverDelay + D_RiverDirect, outflow=D_RestartR, dt=config.dt)
calculate.update(D_TotRiverFlowNoDelay, inflow=D_SurfFlowRiver+D_DirectSurfFkowObsPoint, outflow=D_RiverDelay+D_RivInflLake, dt=config.dt)
calculate.update_conveyor(D_StreamsSurfQ, inflow=D_SurfFlowObsPoint, outflow=D_SurfFlowRiver, time=time, dt=config.dt)
