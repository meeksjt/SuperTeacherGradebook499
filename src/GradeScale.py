from GlobalVariables import *


class GradeScale(object):

    def __init__(self, gs_uuid):
        self.grade_dict = {}
        self.grade_scale_uuid = gs_uuid+"_GradeScale"
        self.grade_dict['A'] = 12
        self.grade_dict['B'] = 23
        self.grade_dict['C'] = 23
        self.grade_dict['D'] = 465

        # If you made it here, the GradeScale database table already exists.
        # Now you want to find this GradeScale's row in the table.
        # So use 'SELECT * where UUID = courseUUID', but check that the row doesn't return anything.
        # If it doesn't return, add a row.
        cursor.execute("CREATE TABLE IF NOT EXISTS `" + str(self.grade_scale_uuid) + "` (`A`	TEXT,`B`	TEXT,`C`	TEXT,`D`	TEXT);")


        connection.commit()

        self.__reload()

    def __reload(self):
        #query = "UPDATE " + self.tableName + " SET email = '" + str(self.email) + "' WHERE uuid = '" + str(self.uuid) + "';"
        #print(query)
        #connection.execute(("UPDATE '" + str(self.grade_scale_uuid) + "' VALUES('" + str(self.grade_dict["A"]) + "','" + str(self.grade_dict["B"]) + "', '" + str(self.grade_dict["C"]) + "', '" + str(self.grade_dict["D"]) + "')"))
        cursor.execute("SELECT * FROM `" + self.grade_scale_uuid + "`")
        results = cursor.fetchall()
        if results:
            for row in results:
                self.set_grade_scale(row[0], row[1], row[2], row[3])
        else:
            connection.execute(("INSERT INTO '" + str(self.grade_scale_uuid) + "' VALUES('90','80', '70', '60')"))
            connection.commit()


    def set_grade_scale(self,a,b,c,d):
        self.grade_dict['A'] = a
        self.grade_dict['B'] = b
        self.grade_dict['C'] = c
        self.grade_dict['D'] = d

        query = "UPDATE `" + self.grade_scale_uuid + "` SET `A` = '" + str(self.grade_dict['A']) + "';"
        #print(query)
        cursor.execute(query)
        query = "UPDATE `" + self.grade_scale_uuid + "` SET `B` = '" + str(self.grade_dict['B']) + "';"
        #print(query)
        cursor.execute(query)
        query = "UPDATE `" + self.grade_scale_uuid + "` SET `C` = '" + str(self.grade_dict['C']) + "';"
        #print(query)
        cursor.execute(query)
        query = "UPDATE `" + self.grade_scale_uuid + "` SET `D` = '" + str(self.grade_dict['D']) + "';"
        #print(query)
        cursor.execute(query)
        connection.commit()

        ##******** DATABASE STUFF
        #Save this stuff to the database table for grade scales.
        #Remember to use the Course UUID to find your entry on the table.

    #The following functions just return a letter grade.
    def get_A_bottom_score(self):
        return self.grade_dict['A']

    def get_B_bottom_score(self):
        return self.grade_dict['B']

    def get_C_bottom_score(self):
        return self.grade_dict['C']

    def get_D_bottom_score(self):
        return self.grade_dict['D']

if __name__ == "__main__":
    print("This is a test.")
    testGradeScale = GradeScale("StacysMom")
    testGradeScale.set_grade_scale(1,2,3,4)