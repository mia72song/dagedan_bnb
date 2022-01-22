from werkzeug.routing import BaseConverter

#定義一個正則轉換器
class ReConverter(BaseConverter):
    def __init__(self, url_map, regex):
        #調用父類的初始化方法
        super().__init__(url_map)       
        #將正規表達法的參數傳入類別屬性，flask用此屬性進行路由的配對
        self.regex = regex