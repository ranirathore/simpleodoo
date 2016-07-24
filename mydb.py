from openerp.osv import osv, fields

class testtable(osv.osv):
    _name = "mytable"
    _columns = {
                'name':fields.char("Full Name"),
                'contact_no':fields.char("Contact No"),
                "email":fields.char("Email Address")   
                }
