class Bill:
    Taxes={
        "Televesion tax":1,
        "Trash tax":0,
        "fuel price deferince":0,
        "collector rent":0.2,
        "other taxes":0
    }

    def __init__(self,name='',KW=0):
        self.name=name
        self.KW=KW

    def update_Taxes(self):
        Bill.Taxes["other taxes"]=self.KW/1000
        if self.KW>200:
            Bill.Taxes["Trash tax"]=1.66+0.005*(self.KW-200)




    def get_elictric_price(self):
        value=0
        price=0
        if self.KW <0:
            return "Please enter a positive power consumbtion in K"
        if self.KW >=0 and self.KW<=160:
            value=0.033
            price=value*self.KW
            return price
        elif self.KW >=161 and self.KW<=300:
            value=0.072
            price=0.033*160+value*(self.KW-160)
            return price
        elif self.KW >=301 and self.KW<=500:
            value=0.086
            price=0.033*160+0.072*140+value*(self.KW-300)
            return price
        elif self.KW >=501 and self.KW<=600:
            value=0.114
            price=0.033*160+0.072*140+0.086*200+value*(self.KW-500)
            return price
        elif self.KW >=601 and self.KW<=750:
            value=0.158
            price=0.033*160+0.072*140+0.086*200+0.114*100+value*(self.KW-600)
            return price
        elif self.KW >=751 and self.KW<=1000:
            value=0.188
            price=0.033*160+0.072*140+0.086*200+0.114*100+0.158*150+value*(self.KW-750)
            return price
        else:
            value=0.265
            price=0.033*160+0.072*140+0.086*200+0.114*100+0.158*150+0.188*250+value*(self.KW-1000)
            return price

    def get_final_price(self):
        self.update_Taxes()
        additional_taxes=0
        for i in Bill.Taxes:
            additional_taxes+=Bill.Taxes[i]
        total_price=self.get_elictric_price()+additional_taxes
        return total_price
   

    def __str__(self):
        return f"""
        welcome {self.name} to the elictrical bill program
        Your elictrical consumbtion is {self.KW} KW
        and your elictrical consumbtion price is {self.get_elictric_price()} JD
        taxes :{Bill.Taxes}

        and your total price is {self.get_final_price()} JD

        """

EX=Bill("mohammad",300)
print (EX)            