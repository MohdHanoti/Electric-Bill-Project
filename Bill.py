class Bill:
    """
    App helps you to know the total financial value with taxes for the electricity bill
    """
    Taxes={
        "Televesion tax":1,
        "Trash tax":0,
        "fuel price deferince":0,
        "collector rent":0.2,
        "other taxes":0
    }

    def __init__(self):
         self.city = None
         self.KW = None
        
    def set_name(self,name):
        self.name=name

    def set_KW(self,KW):
        self.KW=KW        

    def update_Taxes(self):
        """
        Here, the value of the tax imposed will change according to the value of amount of KW consumption
        """
        Bill.Taxes["other taxes"]=self.KW/1000
        if self.KW>200:
            Bill.Taxes["Trash tax"]=1.66+0.005*(self.KW-200)




    def get_elictric_price(self):
        """
        Here, the value of the bill will be calculated according to the amount of KW are used
        """
        value=0
        price=0
        if self.KW <0:
            return "Please enter a positive power consumbtion in KW"
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
        """
        Here, will get the final price of the electricity bill with taxes
        """
        self.update_Taxes()
        additional_taxes=0
        for i in Bill.Taxes:
            additional_taxes+=Bill.Taxes[i]
        total_price=self.get_elictric_price()+additional_taxes
        return total_price
   
    def get_data(self):
        """This function is bult for the test porpose and if the programer wanted to use the progrem from this module"""
        self.update_Taxes()
        return f"""
        welcome {self.name} to the elictrical bill program
        Your elictrical consumbtion is {self.KW} KW
        and your elictrical consumbtion price is {self.get_elictric_price()} JD
        taxes :{Bill.Taxes}

        and your total price is {self.get_final_price()} JD

        """

    def __str__(self):
        return f"welcome {self.name} to the elictrical bill program"
  

bill=Bill() # general call
            