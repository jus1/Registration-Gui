from Tkinter import *

import ttk

from PIL import Image, ImageTk


root = Tk()
root.title("Uniondale Knights Registration V1.0")
root.geometry("700x480")
##############################################################################
var1 = Label(root, text="                                   First Name: ")# First name label and entry widget
var1.grid(column=1, row=20, rowspan=1, sticky=W)

var2 = Entry(root, width=30)
var2.grid(column=5, row=20, rowspan=1, sticky=W)
##############################################################################

var3 = Label(root, text="                                   Last Name: ") #Last name label and entry widget
var3.grid(column=1, row=40, rowspan=1)

var4 = Entry(root, width=30)
var4.grid(column=5, row=40, rowspan=1, sticky=W)
##############################################################################
var3aa = Label(root, text="                                          Team: ")#Team age label and drop down list
var3aa.grid(column=1, row=50)


varAge = ttk.Combobox(root, width=2)
varAge.insert(0, "6")
varAge['values'] = ('6','7','8','9','10','11','12','13')
varAge.grid(column=5, row=50, columnspan=1, sticky=W)
##############################################################################
dobday = ttk.Combobox(root, width=2)                                           #Date of birth Day of month drop down list
dobday.insert(0, "01")
dobday['values'] = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13','14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26','27','28','29','30','31')
dobday.grid(column=5, row=60, columnspan=1, sticky=E)
################################################################################
dobyear = ttk.Combobox(root, width=4)                                           #Date of birth Year dropdown list
dobyear.insert(0, "2003")
dobyear['values'] = ('2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011')
dobyear.grid(column=6, row=60, columnspan=1, sticky=W)


dob = Label(root, text="                              Date Of Birth: ")        # Date of birth label
dob.grid(column=1, row=60)


dob9 = Label(root, text="                                                                Day/Year: ") #Day/Year label
dob9.grid(column=5, row=60, sticky=W)

dobmonth = ttk.Combobox(root, width=11)                                          #Date of birth Month dropdown list
dobmonth.insert(0, "January")
dobmonth['values'] = ('January','February','March','April','May','June','July','August','September','October','November','December')
dobmonth.grid(column=5, row=60, columnspan=1, sticky=W)
###############################################################################
addy = Label(root, text="                                      Address: ")      #Address label and Entry widget
addy.grid(column=1, row=70, rowspan=1)

addy1 = Entry(root, width=30)
addy1.grid(column=5, row=70, rowspan=1, sticky=W)
##############################################################################
cityVar = Label(root, text="                                             City: ") #City label and Entry widget
cityVar.grid(column=1, row=80, rowspan=1)

city = Entry(root, width=18)
city.grid(column=5, row=80, sticky=W)
##############################################################################
state = Label(root, text="State: ")                                            #State dropdown list
state.grid(column=5, row=80, sticky=E)

state1 = ttk.Combobox(root, width=3)
state1.insert(0, "NY")
state1['values'] = ('NY')
state1.grid(column=6, row=80, columnspan=1, sticky=W)

state = Label(root, text="Zipcode: ")                                      #zipcode label and entry list
state.grid(column=7, row=80, sticky=W)

zip = Entry(root, width=5)
zip.grid(column=7, row=80, columnspan=1, sticky=E)

################################################################################
school = Label(root, text="                                         Phone: ") #Phone label and entry widget
school.grid(column=1, row=90)

school1 = Entry(root, width=13)
school1.insert(0, "(516)485-4444")
school1.grid(column=5, row=90, sticky=W)

##################################################################################
district = Label(root, text="                            Parent Name: ")         #Parent label
district.grid(column=1, row=100)

district = Label(root, text="                                                               Relationship: ") #relationship drop list label
district.grid(column=5, row=100, sticky=W)


district1 = Entry(root, width=30)                                                    #parent entry
district1.grid(column=5, row=100, sticky=W)


relat = ttk.Combobox(root, width=11)
relat.insert(0, "Mother")
relat['values'] = ('Mother','Father','Aunt','Uncle','Grandmother','Grandfather','Sister', 'Brother')    #relationship dropdown list
relat.grid(column=5, row=100, columnspan=1, sticky=E)
#################################################################################
district = Label(root, text="                                          Email: ")
district.grid(column=1, row=110)

district1 = Entry(root, width=30)
district1.grid(column=5, row=110, sticky=W)
#################################################################################

district0 = Label(root, text="                           School Name: ")
district0.grid(column=1, row=120)

district10 = Entry(root, width=30)
district10.grid(column=5, row=120, sticky=W)
################################################################################

district = Label(root, text="                           School District: ")
district.grid(column=1, row=130)

district1 = Entry(root, width=30)
district1.grid(column=5, row=130, sticky=W)
###############################################################################
district = Label(root, text="Has your child ever played in the NCYFL before? (Check box if Yes)")
district.grid(column=5, row=140, sticky=W)

check = Checkbutton(root)
check.grid(column=6, row=140, sticky=W)

var3aa = Label(root, text="                            If Yes, Where: ")
var3aa.grid(column=1, row=150)

ncyfl = Entry(root, width=30)
ncyfl.grid(column=5, row=150, sticky=W)

var3aa1 = Label(root, text="When:")
var3aa1.grid(column=5, row=150, sticky=E)

year = ttk.Combobox(root, width=4)
year.insert(0, "2011")
year['values'] = ('2011','2012','2013','2014','2015')
year.grid(column=6, row=150, columnspan=1, sticky=E)
##############################################################################
district = Label(root, text="Are you interested in Volunteering?                              (Check if Yes)")
district.grid(column=5, row=160, sticky=W)

check = Checkbutton(root)
check.grid(column=6, row=160, sticky=W)

###############################################################################
district = Label(root, text="What role are you interested in?")
district.grid(column=5, row=170, sticky=W)


relat1 = ttk.Combobox(root, width=18)
relat1['values'] = ('Team Mother','General Volunteer', 'Assistant Coach', 'Head Coach')
relat1.grid(column=5, row=170, columnspan=1, sticky=E)

###############################################################################
button = Button(root, text="    Submit    ", font="Arial 24", padx=10, pady=10)
button.grid(column=5, row=210, sticky=W)

check = Checkbutton(root, text="I have verified all information is correct.")
check.grid(column=5, row=209, sticky=W)

################################################################################
image = Image.open("knights_logo_teams.jpg")
photo = ImageTk.PhotoImage(image)

label9 = Label(image=photo)
label9.image = photo # keep a reference!
label9.grid(column=5, row=210, sticky=E)

root.mainloop()
def pull():
    var2.get()
    var4.get()
    varAge.get()
    dobmonth.get()
    dobday.get()
    dobyear.get()
