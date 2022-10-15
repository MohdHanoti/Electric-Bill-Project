from Bill import bill

def bill_data():
    print('''
    *****************************************************
    ** welcome to elictrical bill program ***************
    ** this program will calculate your bill ************
    ** all you need to do is providing us with your KW **
    ''')
    while True:
        name=input(" >> enter your name please: ")
        KW=float(input (" >> enter your power consumbtion in KW : "))
        if type(name) != str or type(KW) != float:
            print (type(name),type(KW))
            print(" $$ name must be of only charectors and KW must be a number $$")
        else :
            break    

    bill.set_name(name)
    bill.set_KW(KW)
    bill.update_Taxes()
    
    print (f"""
         _________________________________________________________________________
        |                        {name} bill                                      
        |_________________________________________________________________________|
        | Name                   |     {name}                                       
        |_________________________________________________________________________|
        | Elictrical consumbtion |   {KW} KW                                      
        | ________________________________________________________________________|
        | Price/KW               |   {bill.get_elictric_price()} JD               
        |_________________________________________________________________________|
        |                              Taxes :                                    |
        |-------------------------------------------------------------------------|                     
        | Televesion tax         |   {bill.Taxes["Televesion tax"]} JD            
        | Trash tax              |   {bill.Taxes['Trash tax']} JD                 
        | Collector rent         |   {bill.Taxes['collector rent']} JD            
        | Other taxes            |   {bill.Taxes['other taxes']} JD               
        |_________________________________________________________________________|
        |                                                                         |
        | Total price            |   {bill.get_final_price()} JD                   
        |_________________________________________________________________________|
        """)                                                                    

bill_data()