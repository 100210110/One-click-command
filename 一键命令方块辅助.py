from pyperclip import copy


i = 1
commands = "summon falling_block ~ ~1 ~ {Time:1,BlockState:{Name:redstone_block},\nPassengers:[{id:armor_stand,Health:0,\nPassengers:[{id:falling_block,Time:1,BlockState:{Name:activator_rail},\nPassengers:["
end_of_command = "\n{id:command_block_minecart,Command:\'setblock ~ ~1 ~ command_block{auto:1,Command:\"fill ~ ~ ~ ~ ~-3 ~ air\"}\'},\n{id:command_block_minecart,Command:\'kill @e[type=command_block_minecart,distance=..1]\'}]}]}]}"




# 输入并添加新指令到列表
def input_command(new_command): 
    global i
    global commands
    commands += f"\n{{id:command_block_minecart,Command:'{new_command}'}},"
    print(f"新指令已添加，为第{i}条执行\n")
    i += 1   


# 输出并复制最终指令
def get_command(ending_command):
    print(ending_command)
    copy(ending_command)
    print(f"\n<指令已复制到剪贴板>\n")


# 输出并复制获取方块指令
def get_block(ending_command):
    ending_command = ending_command.replace("\\", "\\\\")
    ending_command = ending_command.replace("\"", "\\\"")
    item_name = input("命令方块主要作用是: ")
    get_block_command = f"/give @p command_block{{display:{{Name:'{{\"text\":\"{item_name}\",\"color\":\"gold\",\"bold\":true,\"italic\":false}}'}},BlockEntityTag:{{Command:\"{ending_command}\",auto:1b}}}}"
    print(get_block_command)
    copy(get_block_command)
    print(f"\n<指令已复制到剪贴板>\n")



# 主函数
def main():
    # 循环输入新指令
    while True:    
        new_command = input(f"输入第{i}条命令: ")
        if not new_command:
            print(f"输入为空，结束指令\n")
            break
        input_command(new_command)
        ending_command = commands + end_of_command
    # 选择获得一次指令还是保存为命令方块
    while True:
        try:
            mode = int(input("请选择: 1.获得一次性指令; 2.保存至命令方块"))
            if mode == 1:
                get_command(ending_command)
            elif mode == 2:
                get_block(ending_command)
            else:
                print(f"超出范围\n")
                continue
            break
        except Exception as e:
            print(f"非法输入，抛出异常:{e}\n")



if __name__ == "__main__":
    main()
    input("按任意键结束")
