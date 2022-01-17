class tuple_to_list:
    def tuple_to_list(self,tuple_in): #  *agrs指的是输入的数据类型为元组
        list_out = []                  #建立一个空列表
        for i in tuple_in:
            lt = list(i)               #把元组类型全部变成列表类型
            list_out.append(lt)        #把输出填充到列表list_out中
        return list_out