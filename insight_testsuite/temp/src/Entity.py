from datetime import datetime

class Entity:
    def __init__(self, cmte_id, zip_code, date, amount, other):
      self.cmte_id = cmte_id
      self.zip_code = zip_code[0:5]
      self.transaction_date = date
      self.transaction_amount =  int(amount) if len(amount)>0 else amount
      self.other_id = other

    def validate(self):
        if(self.other_id == "" and self.cmte_id!="" and self.transaction_amount!=""):
            return True
        return False

    def validate_zip_code(self):
        if(len(self.zip_code)!=5):
            return False
        return self.validate()

    def validate_date(self):
        try:
            self.transaction_date = datetime.strptime(self.transaction_date , '%m%d%Y')
            return self.validate()
        except:
            return False
