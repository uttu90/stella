import numpy as np
import config
import calculate

time = 0

G_GrassStandingBiomass = [1]
G_SurfaceLitter = [0]
G_SurfManure = [0]

G_GrassLitConv = 1
G_GrassMortFrac = 0.03
G_GrazingManConv = 0.1
G_SurfLitDecFrac = 0.03
G_SurfManureDecFrac = 0.01
G_TramplingMultiplier = 0
G_WUE = 0.04


G_GrassFract_Biomass = np.zeros(config.LANDCOVERTYPE)
G_GrowthRate = G_WUE * np.multiply(D_ActEvapTransp, G_GrassFract_Biomass)
G_GrassAll = np.sum(G_GrassStandingBiomass[time])
G_Grazing = 0 if G_GrassAll == 0 else C_StockingRate * C_DailyIntake * G_GrassFract_Biomass / G_GrassAll
G_LeafMortality = G_GrassStandingBiomass[time] * G_GrassMortFrac + G_Grazing * G_TramplingMultiplier
G_LitterDeposition = G_LeafMortality * G_GrassLitConv
calculate.update(G_GrassStandingBiomass, inflow=G_GrowthRate, outflow=G_Grazing + G_LeafMortality, dt=config.dt)

G_Incorporation_DecaySurfLit = G_SurfaceLitter[time] * G_SurfLitDecFrac
calculate.update(G_SurfaceLitter, inflow=G_LitterDeposition, outflow=G_Incorporation_DecaySurfLit, dt=config.dt)

G_FaecesProd = G_Grazing * G_GrazingManConv
G_Incorporation_DecayManure = G_SurfManure[time] * G_SurfManureDecFrac
calculate.update(G_SurfManure, inflow=G_FaecesProd, outflow=G_Incorporation_DecayManure, dt=config.dt)

G_SurfaceCover = G_GrassStandingBiomass[time] + G_SurfaceLitter[time] + G_SurfManure[time]
