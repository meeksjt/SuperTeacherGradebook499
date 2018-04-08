from GlobalVariables import *


class GradeScale(object):

    def __init__(self, gs_uuid):
        self.grade_dict = {}
        self.grade_scale_uuid = gs_uuid

        # If you made it here, the GradeScale database table already exists.
        # Now you want to find this GradeScale's row in the table.
        # So use 'SELECT * where UUID = courseUUID', but check that the row doesn't return anything.
        # If it doesn't return, add a row.

    def _reload(self):
        pass

    def set_grade_scale(self,a,b,c,d):
        self.grade_dict['A'] = a
        self.grade_dict['B'] = b
        self.grade_dict['C'] = c
        self.grade_dict['D'] = d
        ##******** DATABASE STUFF
        #Save this stuff to the database table for grade scales.
        #Remember to use the Course UUID to find your entry on the table.

    # The following functions just return a letter grade.
    def get_A_bottom_score(self):
        return self.grade_dict['A']

    def get_B_bottom_score(self):
        return self.grade_dict['B']

    def get_C_bottom_score(self):
        return self.grade_dict['C']

    def get_D_bottom_score(self):
        return self.grade_dict['D']