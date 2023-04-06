from Instance import Instance, shared_instances
from Memory import GetDataModel,float_to_hex,SetupOptimizations, FreeOptimizations, getPropertyFuncs, write_str, nameMap, GetRenderJob
from Players import Players #useful to manipulate players instance
from Player import Player
import time
from Exploit import roblox
DataModel = Instance(GetDataModel())
workspace = DataModel.GetChildren()[0]
Players = Players(DataModel.FindFirstChild("Players"))
shared_instances["Workspace"] = workspace

SetupOptimizations()
RenderJob = GetRenderJob()
roblox.Program.write_bool(RenderJob+0x154, True) #Disable renderjob
FreeOptimizations() # free the memory
