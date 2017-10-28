class Entity:
    def __init__(self, cmte_id, zip_code, date, amount, other):
      self.cmte_id = cmte_id
      self.zip_code = zip_code[0:5]
      self.transction_date = date
      self.transction_amount = amount
      self.other_id = other

    def validate_other_id(self):
        if(self.other_id == ""):
            return True
        return False

    def validate_zip_code(self):
        if(len(self.zip_code)!=5):
            return False
        return True
