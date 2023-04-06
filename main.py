from Instance import Instance, shared_instances
from Memory import GetDataModel,float_to_hex,SetupOptimizations, FreeOptimizations, getPropertyFuncs, write_str, nameMap, GetRenderJob
from Players import Players #useful to manipulate players instance
from Player import Player
import time
from Exploit import roblox

class Job():
    def __init__(self, addr = 0) -> None:
        self.addr = addr
    def GetName(self) -> str:
        return roblox.ReadNormalString(roblox.DRP(self.addr) + 0x10)
    
class TaskScheduler():
    def __init__(self) -> None:
        self.addr = roblox.DRP(roblox.getAddressFromName("RobloxPlayerBeta.exe+3DE457C"))
    def getJobs(self) -> list[Job]:
        schduler_start = roblox.DRP(self.addr + 0x134)
        schduler_end = roblox.DRP(self.addr + 0x138)
        returned = []
        while schduler_start != schduler_end:
            returned.append(Job(roblox.DRP(schduler_start)))
            schduler_start += 8




#SetupOptimizations()
#RenderJob = GetRenderJob()
#roblox.Program.write_bool(RenderJob+0x154, True) #Disable renderjob
#localPlayer = Players.GetLocalPlayerChar(workspace)
#humanoid = localPlayer.FindFirstChild("Humanoid")
#humanoid.SetProperty("Sit", 1)
#FreeOptimizations() # free the memory
