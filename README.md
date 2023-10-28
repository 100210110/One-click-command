# One-click-command
# 这是干什么的
这是帮助生成我的世界一键命令方块的一段代码
一次即可执行多条代码，为开发地图或您在游玩多个地图多个服务器时需要同一份指令设置（如地毯端的设置多个存档不互通）

# 如何使用
需要pyperclip库，使用pip install puperclip安装，用来直接复制结果

运行后会提示你添加指令，每添加一条指令回车一次即可，如果全部指令添加完毕，直接回车结束输入阶段

此时会让你选择模式
模式1复制的命令可以粘贴到命令方块里，执行效果就是你输入的那些命令；
模式2会先询问你命令的作用，这会被写到命令方块名字里。之后复制的命令，粘贴命令方块里执行后，会给予你一个特殊的命令方块，这个命令方块放出来即可执行一串预设指令，适合保存物品栏跨存档使用

以下是一个示例
# 获取放下即执行的创造优化命令方块
指令中包含了一些地毯端的优化
禁用生成、锁定时间天气，优化、假人等等
summon falling_block ~ ~1 ~ {Time:1,BlockState:{Name:redstone_block},Passengers:[{id:armor_stand,Health:0,Passengers:[{id:falling_block,Time:1,BlockState:{Name:activator_rail},Passengers:[
{id:command_block_minecart,Command:'gamerule commandBlockOutput false'},
{id:command_block_minecart,Command:'data merge block ~ ~-2 ~ {auto:0}'},
{id:command_block_minecart,Command:'carpet setDefault creativeNoClip true'},
{id:command_block_minecart,Command:'carpet setDefault language zh_cn'},
{id:command_block_minecart,Command:'carpet setDefault fillLimit 1000000'},
{id:command_block_minecart,Command:'carpet setDefault smoothClientAnimations true'},
{id:command_block_minecart,Command:'gamerule doMobSpawning false'},
{id:command_block_minecart,Command:'gamerule doDaylightCycle false'},
{id:command_block_minecart,Command:'time set noon'},
{id:command_block_minecart,Command:'gamerule doWeatherCycle false'},
{id:command_block_minecart,Command:'carpet setDefault antiCheatDisabled true'},
{id:command_block_minecart,Command:'carpet setDefault antiSpamDisabled true'},
{id:command_block_minecart,Command:'carpet setDefault accurateBlockPlacement true'},
{id:command_block_minecart,Command:'carpet setDefault creativeNoItemCooldown true'},
{id:command_block_minecart,Command:'carpet setDefault creativeOpenContainerForcibly true'},
{id:command_block_minecart,Command:'carpet setDefault defaultLoggers mobcaps'},
{id:command_block_minecart,Command:'carpet setDefault syncServerMsptMetricsData true'},
{id:command_block_minecart,Command:'carpet setDefault persistentLoggerSubscription true'},
{id:command_block_minecart,Command:'carpet setDefault fastRedstoneDust true'},
{id:command_block_minecart,Command:'carpet setDefault lagFreeSpawning true'},
{id:command_block_minecart,Command:'carpet setDefault ctrlQCraftingFix true'},
{id:command_block_minecart,Command:'carpet setDefault entityBrainMemoryUnfreedFix true'},
{id:command_block_minecart,Command:'carpet setDefault openFakePlayerInventory true'},
{id:command_block_minecart,Command:'carpet setDefault fakePlayerResident true'},
{id:command_block_minecart,Command:'say 初始化完成'},
{id:command_block_minecart,Command:'setblock ~ ~1 ~ command_block{auto:1,Command:"fill ~ ~ ~ ~ ~-3 ~ air"}'},
{id:command_block_minecart,Command:'kill @e[type=command_block_minecart,distance=..1]'}
]}]}]}
# 获取放下即执行的创造优化命令方块
可以保存物品栏中以备多存档使用
/give @p command_block{display:{Name:'{"text":"创造用一键命令","color":"gold","bold":true,"italic":false}'},BlockEntityTag:{Command:"summon falling_block ~ ~1 ~ {Time:1,BlockState:{Name:redstone_block},
Passengers:[{id:armor_stand,Health:0,
Passengers:[{id:falling_block,Time:1,BlockState:{Name:activator_rail},
Passengers:[
{id:command_block_minecart,Command:'gamerule commandBlockOutput false'},
{id:command_block_minecart,Command:'data merge block ~ ~-2 ~ {auto:0}'},
{id:command_block_minecart,Command:'carpet setDefault creativeNoClip true'},
{id:command_block_minecart,Command:'carpet setDefault language zh_cn'},
{id:command_block_minecart,Command:'carpet setDefault fillLimit 1000000'},
{id:command_block_minecart,Command:'carpet setDefault smoothClientAnimations true'},
{id:command_block_minecart,Command:'gamerule doMobSpawning false'},
{id:command_block_minecart,Command:'gamerule doDaylightCycle false'},
{id:command_block_minecart,Command:'time set noon'},
{id:command_block_minecart,Command:'gamerile doWeatherCycle false'},
{id:command_block_minecart,Command:'carpet setDefault antiCheatDisabled true'},
{id:command_block_minecart,Command:'carpet setDefault antiSpamDisabled true'},
{id:command_block_minecart,Command:'carpet setDefault accurateBlockPlacement true'},
{id:command_block_minecart,Command:'carpet setDefault creativeNoItemCooldown true'},
{id:command_block_minecart,Command:'carpet setDefault creativeOpenContainerForcibly true'},
{id:command_block_minecart,Command:'carpet setDefault defaultLoggers mobcaps'},
{id:command_block_minecart,Command:'carpet setDefault syncServerMsptMetricsData true'},
{id:command_block_minecart,Command:'carpet setDefault persistentLoggerSubscription true'},
{id:command_block_minecart,Command:'carpet setDefault fastRedstoneDust true'},
{id:command_block_minecart,Command:'carpet setDefault lagFreeSpawning true'},
{id:command_block_minecart,Command:'carpet setDefault ctrlQCraftingFix true'},
{id:command_block_minecart,Command:'carpet setDefault entityBrainMemoryUnfreedFix true'},
{id:command_block_minecart,Command:'carpet setDefault openFakePlayerInventory true'},
{id:command_block_minecart,Command:'carpet setDefault fakePlayerResident true'},
{id:command_block_minecart,Command:'say 创造设置初始化完成'},
{id:command_block_minecart,Command:'setblock ~ ~1 ~ command_block{auto:1,Command:\"fill ~ ~ ~ ~ ~-3 ~ air\"}'},
{id:command_block_minecart,Command:'kill @e[type=command_block_minecart,distance=..1]'}]}]}]}
",auto:1b}}

# 生存一键
一些优化选项，也包含创造穿墙等不会影响生存模式的选项，（总之无影响就一道优化了）
summon falling_block ~ ~1 ~ {Time:1,BlockState:{Name:redstone_block},
Passengers:[
{id:armor_stand,Health:0,
Passengers:[
{id:falling_block,Time:1,BlockState:{Name:activator_rail},
Passengers:[
{id:command_block_minecart,Command:'gamerule commandBlockOutput false'},
{id:command_block_minecart,Command:'data merge block ~ ~-2 ~ {auto:0}'},
{id:command_block_minecart,Command:'carpet setDefault creativeNoClip true'},
{id:command_block_minecart,Command:'carpet setDefault language zh_cn'},
{id:command_block_minecart,Command:'carpet setDefault fillLimit 1000000'},
{id:command_block_minecart,Command:'carpet setDefault xpNoCooldown true'},
{id:command_block_minecart,Command:'carpet setDefault antiCheatDisabled true'},
{id:command_block_minecart,Command:'carpet setDefault antiSpamDisabled true'},
{id:command_block_minecart,Command:'carpet setDefault accurateBlockPlacement true'},
{id:command_block_minecart,Command:'carpet setDefault creativeNoItemCooldown true'},
{id:command_block_minecart,Command:'carpet setDefault creativeOpenContainerForcibly true'},
{id:command_block_minecart,Command:'carpet setDefault defaultLoggers mobcaps'},
{id:command_block_minecart,Command:'carpet setDefault syncServerMsptMetricsData true'},
{id:command_block_minecart,Command:'carpet setDefault persistentLoggerSubscription true'},
{id:command_block_minecart,Command:'carpet setDefault fastRedstoneDust true'},
{id:command_block_minecart,Command:'carpet setDefault lagFreeSpawning true'},
{id:command_block_minecart,Command:'carpet setDefault ctrlQCraftingFix true'},
{id:command_block_minecart,Command:'carpet setDefault entityBrainMemoryUnfreedFix true'},
{id:command_block_minecart,Command:'carpet setDefault openFakePlayerInventory true'},
{id:command_block_minecart,Command:'carpet setDefault fakePlayerResident true'},
{id:command_block_minecart,Command:'say 生存设置初始化完成'},
{id:command_block_minecart,Command:'setblock ~ ~1 ~ command_block{auto:1,Command:"fill ~ ~ ~ ~ ~-3 ~ air"}'},
{id:command_block_minecart,Command:'kill @e[type=command_block_minecart,distance=..1]'}]}]}]}
# 获取放下即执行的生存优化命令方块
可以保存物品栏中以备多存档使用
/give @p command_block{display:{Name:'{"text":"生存用一键命令","color":"light_purple","bold":true,"italic":false}'},BlockEntityTag:{Command:"
summon falling_block ~ ~1 ~ {Time:1,BlockState:{Name:redstone_block},
Passengers:[{id:armor_stand,Health:0,
Passengers:[{id:falling_block,Time:1,BlockState:{Name:activator_rail},
Passengers:[
{id:command_block_minecart,Command:'gamerule commandBlockOutput false'},
{id:command_block_minecart,Command:'data merge block ~ ~-2 ~ {auto:0}'},
{id:command_block_minecart,Command:'carpet setDefault creativeNoClip true'},
{id:command_block_minecart,Command:'carpet setDefault language zh_cn'},
{id:command_block_minecart,Command:'carpet setDefault fillLimit 1000000'},
{id:command_block_minecart,Command:'carpet setDefault xpNoCooldown true'},
{id:command_block_minecart,Command:'carpet setDefault antiCheatDisabled true'},
{id:command_block_minecart,Command:'carpet setDefault antiSpamDisabled true'},
{id:command_block_minecart,Command:'carpet setDefault accurateBlockPlacement true'},
{id:command_block_minecart,Command:'carpet setDefault creativeNoItemCooldown true'},
{id:command_block_minecart,Command:'carpet setDefault creativeOpenContainerForcibly true'},
{id:command_block_minecart,Command:'carpet setDefault defaultLoggers mobcaps'},
{id:command_block_minecart,Command:'carpet setDefault syncServerMsptMetricsData true'},
{id:command_block_minecart,Command:'carpet setDefault persistentLoggerSubscription true'},
{id:command_block_minecart,Command:'carpet setDefault fastRedstoneDust true'},
{id:command_block_minecart,Command:'carpet setDefault lagFreeSpawning true'},
{id:command_block_minecart,Command:'carpet setDefault ctrlQCraftingFix true'},
{id:command_block_minecart,Command:'carpet setDefault entityBrainMemoryUnfreedFix true'},
{id:command_block_minecart,Command:'carpet setDefault openFakePlayerInventory true'},
{id:command_block_minecart,Command:'carpet setDefault fakePlayerResident true'},
{id:command_block_minecart,Command:'say 生存设置初始化完成'},
{id:command_block_minecart,Command:'setblock ~ ~1 ~ command_block{auto:1,Command:\"fill ~ ~ ~ ~ ~-3 ~ air\"}'},
{id:command_block_minecart,Command:'kill @e[type=command_block_minecart,distance=..1]'}]}]}]}
",auto:1b}}


