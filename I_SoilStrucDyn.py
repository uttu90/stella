import numpy as np
import config
import calculate

time = 0

S_TrampMax = 100
S_RelBulkDensity = [I_BD_BDRefVegNow]

S_Compaction = np.multiply((1.3 - S_RelBulkDensity[time]), C_TrampComp)/S_TrampMax
S_SplashErosion = 0 * np.divide(np.multiply(G_SurfaceCover, S_RainAtSoilStructure),
                                I_RainDuration,
                                out=np.zeros_like(G_SurfaceCover),
                                where=I_RainDuration!=0)
S_StructureFormation = 0 * np.multiply(S_RelBulkDensity, G_SurfaceCover)
S_RippingSurface = 0

calculate.update(S_RelBulkDensity,
                 inflow=S_SplashErosion + S_StructureFormation + S_RippingSurface,
                 outflow=S_Compaction,
                 dt=config.dt)
