class ExpenseLogHelper(object):
    EXPENSE_MAP = {
            "meal" => 1,
            "grocery" => 2,
    }
    
    
    def getExpenseTypeFromName(self, expense_name: str):

        if expense.lower in expense_map:
            return expense_map[expense.lower]:
        return False