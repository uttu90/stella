import numpy as np
import config
import calculate

time = 0

C_DailyIntake = 1
C_DailyTrampFrac = 1
C_CattleSale = 0

C_StockingRate = [0]

C_TrampComp = C_DailyTrampFrac * G_Grazing / C_DailyIntake
C_DeathRate = C_StockingRate[time] * C_DailyIntake - G_GrassAll

C_Destoking = min(C_StockingRate[time], C_CattleSale + C_DeathRate)
C_Stocking = 0 * C_StockingRate[time]
calculate.update(C_StockingRate, inflow=C_Stocking, outflow=C_Destoking, dt=config.dt)
