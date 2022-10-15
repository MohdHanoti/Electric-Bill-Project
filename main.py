from Bill import bill

def bill_data():
    print('''
    *****************************************************
    ******** welcome to elictrical bill program *********
    ******* this program will calculate your bill *******
    ** all you need to do is providing us with your KW **
    *****************************************************
    ''')
    while True:
        """this to force the user to input a number in kw"""
        try:
            name=input(" >> enter your name please: ")
            KW= float(input (" >> enter your power consumbtion in KW : "))
            break
        
        except ValueError:
            print(" Err: Power consumbtion must be a number!")
       
    
       

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

        ** Thanks for using our applecation!
        > Bye 
        """)                                                                    

bill_data()