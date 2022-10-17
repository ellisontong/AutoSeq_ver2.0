###############################################################################
#Auto-sequencer tool, by Ellison Tong
###############################################################################
import pandas as pd
import numpy as np
import random
import tkinter as tk
from tkinter import * #loads everything in tkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfile
root = tk.Tk()

### FUNCTIONS(setup) #########################################################
def opening_setup():
    ####general set up
    root.geometry("1200x500")
    root.title("ICP-MS Auto-Sequencer Tool by Ellison Tong: 2021-10-15")
    my_font1=('times', 11, 'bold')
    l1 = tk.Label(root, text = 'ICP-MS Auto-Sequencer Tool by Ellison Tong', width=50, font=my_font1)
    l1.grid(row=0, column=0)
    ####create menu item
    my_menu= Menu(root)
    root.config(menu=my_menu)
    file_menu = Menu(my_menu)
    my_menu.add_cascade(label="Menu", menu=file_menu) #put it on screen 
    file_menu.add_command(label="About", command=menu_about)
    file_menu.add_command(label="How to Use", command=menu_how)
    file_menu.add_command(label="Technical Information", command=menu_tech)
def menu_about():
    top = Toplevel()
    top.geometry("1000x90")
    my_font1=('times', 11, 'bold')
    about_text_0=Label(top, text="About", font=my_font1).grid(row=0, sticky=W)
    about_text_1=Label(top, text="The Auto-Sequencer Tool was made by Ellison Tong on 2021-10-15.").grid(row=1, sticky=W)
    about_text_2=Label(top, text="This tool was made to speed up the sequencing process on MassHunter for ICP-MS 7000 series by allowing a user to sequence multiple sample batches at once. ").grid(row=2, sticky=W)
    about_text_3=Label(top, text="This tool will ask a user to upload multiple excel files (containing a list of sample names in the first column) and then it generates a matrix to copy and paste into MassHunter.").grid(row=3, sticky=W)
def menu_how():
    top = Toplevel()
    top.geometry("1000x300")
    my_font1=('times', 11, 'bold')
    how_text_0=Label(top, text="How to Use", font=my_font1).grid(row=0, sticky=W)
    how_text_1=Label(top, text="1. Lauch autoseq.py").grid(row=1, sticky=W)
    how_text_2=Label(top, text="2. Upload the appropriate* Excel files into the program by clicking on the upload buttons. A 'File Explorer' window should open.").grid(row=2, sticky=W) 
    how_text_3=Label(top, text="3. Select the target Excel file and click 'open' on the file explorer window. The order of the uploaded files should follow the order** of the ICP-MS machine.") .grid(row=3, sticky=W)
    how_text_3=Label(top, text="     - Do not skip numbers when uploading files e.g. uploading files in the slots 1,2,4 is not allowed, instead use 1,2,3").grid(row=4, sticky=W)
    how_text_4=Label(top, text="4. For each uploaded Excel file select which type of analyses it is by clicking on the drop down menus next to the upload buttons.").grid(row=5, sticky=W)
    how_text_5=Label(top, text="5. Fill in the required information on starting position*** and number of uploaded files by using their respective drop-down menus.").grid(row=6, sticky=W)
    how_text_6=Label(top, text="     - This program assumes that batches of samples are placed consecutively").grid(row=7, sticky=W) 
    how_text_7=Label(top, text="6. Click on the 'Confirm' button (any opened old verions of AutoSeqResults.xlsx will cause the program to not work).").grid(row=8, sticky=W)
    how_text_8=Label(top, text="7. Open up AutoSeqResults.xlsx then copy and paste the generated matrix. Note: Double-check that AutoSeqResults.xlsx has been recently updated before copying matrix to clipboard").grid(row=9, sticky=W)
    how_text_9=Label(top, text="For all terms marked by an asterick please refer to the menu option 'Technical Information'.").grid(row=10, sticky=W)
def menu_tech():
    top = Toplevel()
    top.geometry("1200x300")
    my_font1=('times', 11, 'bold')
    tech_text_0=Label(top, text="Technical Information", font=my_font1).grid(row=0, sticky=W)
    tech_text_1=Label(top, text="ICP-MS Software = ICP-MS MassHunter Software by Aligent").grid(row=1, sticky=W)
    tech_text_2=Label(top, text="ICP-MS Hardware = ICP-MS 7000 series by Aligent").grid(row=2, sticky=W)
    tech_text_3=Label(top, text="*Appropriate Excel files = Excel files that contain a column with sample names in the first column").grid(row=3, sticky=W)
    tech_text_4=Label(top, text="**Correct Order of the ICP-MS machine = Batches of samples should follow the numerical order of the ICP-MS machine. The numerical order of the tray begins at tray 1 and ends with tray 4.").grid(row=4, sticky=W) 
    tech_text_5=Label(top, text="    Tray 1 = {1101,1102,...,1111,1112}, {1201,1202,...,1211,1212}, {1301,1302,...,1311,1312}, {1401,1402,...,1411,1412}, {1501,1502,...,1511,1512}.").grid(row=5, sticky=W)
    tech_text_6=Label(top, text="    Tray 2 = {2101,2102,...,2111,2112}, {2201,2202,...,2211,2212}, {2301,2302,...,2311,2312}, {2401,2402,...,2411,2412}, {2501,2502,...,2511,2512}.").grid(row=6, sticky=W)
    tech_text_7=Label(top, text="    Tray 3 = {3101,3102,...,3111,3112}, {3201,3202,...,3211,3212}, {3301,3302,...,3311,3312}, {3401,3402,...,3411,3412}, {3501,3502,...,3511,3512}.").grid(row=7, sticky=W)
    tech_text_8=Label(top, text="    Tray 4 = {4101,4102,...,4111,4112}, {4201,4202,...,4211,4212}, {4301,4302,...,4311,4312}, {4401,4402,...,4411,4412}, {4501,4502,...,4511,4512}.").grid(row=8, sticky=W)
    tech_text_9=Label(top, text="    E.g. If a batch has five samples in it and starts at postion 3512, therefore the batch will occupy positions 3512, 4101, 4102, 4013, and 4104 in respective order.").grid(row=9, sticky=W)
    tech_text_10=Label(top, text="***Starting Position = The position of the very first sample to be analyzed").grid(row=10, sticky=W)

### FUNCTIONS(homescreen buttons) ############################################
def button_upload_files(): #puts up upload file buttons
    b1 = tk.Button(root, text = 'Upload File 1', width = 20, command=lambda:upload_file_1())
    b1.grid(row=1, column=0)
    b2 = tk.Button(root, text = 'Upload File 2', width = 20, command=lambda:upload_file_2())
    b2.grid(row=2, column=0)
    b3 = tk.Button(root, text = 'Upload File 3', width = 20, command=lambda:upload_file_3())
    b3.grid(row=3, column=0)
    b4 = tk.Button(root, text = 'Upload File 4', width = 20, command=lambda:upload_file_4())
    b4.grid(row=4, column=0)
    b5 = tk.Button(root, text = 'Upload File 5', width = 20, command=lambda:upload_file_5())
    b5.grid(row=5, column=0)
    b6 = tk.Button(root, text = 'Upload File 6', width = 20, command=lambda:upload_file_6())
    b6.grid(row=6, column=0)
    b7 = tk.Button(root, text = 'Upload File 7', width = 20, command=lambda:upload_file_7())
    b7.grid(row=7, column=0)
    b8 = tk.Button(root, text = 'Upload File 8', width = 20, command=lambda:upload_file_8())
    b8.grid(row=8, column=0)
    b9 = tk.Button(root, text = 'Upload File 9', width = 20, command=lambda:upload_file_9())
    b9.grid(row=9, column=0)
    b10 = tk.Button(root, text = 'Upload File 10', width = 20, command=lambda:upload_file_10())
    b10.grid(row=10, column=0)
def button_file_num(): #ask about total number of files
    global dd_entry_num
    how_many = Label(root, text ="How many files?")
    how_many.grid(row=11, column=0)
    dd_entry_num = StringVar()
    options_list_num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    dd_entry_num.set(options_list_num[0]) #default option
    drop_ten = OptionMenu(root, dd_entry_num, *options_list_num) # called dd_menu_1
    drop_ten.grid(row=11, column=1)
def button_analysis_type(): #ask about analysis type for each file
    global dd_menu_1
    dd_menu_1 = StringVar()
    options_list = ["SALM", "TCLP"]
    dd_menu_1.set(options_list[0]) #default option
    drop_1 = OptionMenu(root, dd_menu_1, *options_list) # called dd_menu_1
    drop_1.grid(row=1, column=1)
    
    global dd_menu_2
    dd_menu_2 = StringVar()
    options_list = ["SALM", "TCLP"]
    dd_menu_2.set(options_list[0]) #default option
    drop_2 = OptionMenu(root, dd_menu_2, *options_list) 
    drop_2.grid(row=2, column=1)
    
    global dd_menu_3
    dd_menu_3 = StringVar()
    options_list = ["SALM", "TCLP"]
    dd_menu_3.set(options_list[0]) #default option
    drop_3 = OptionMenu(root, dd_menu_3, *options_list)
    drop_3.grid(row=3, column=1)
    
    global dd_menu_4
    dd_menu_4 = StringVar()
    options_list = ["SALM", "TCLP"]
    dd_menu_4.set(options_list[0]) #default option
    drop_4 = OptionMenu(root, dd_menu_4, *options_list)
    drop_4.grid(row=4, column=1)
    
    global dd_menu_5
    dd_menu_5 = StringVar()
    options_list = ["SALM", "TCLP"]
    dd_menu_5.set(options_list[0]) #default option
    drop_5 = OptionMenu(root, dd_menu_5, *options_list)
    drop_5.grid(row=5, column=1)
    
    global dd_menu_6
    dd_menu_6 = StringVar()
    options_list = ["SALM", "TCLP"]
    dd_menu_6.set(options_list[0]) #default option
    drop_6 = OptionMenu(root, dd_menu_6, *options_list)
    drop_6.grid(row=6, column=1)
    
    global dd_menu_7
    dd_menu_7 = StringVar()
    options_list = ["SALM", "TCLP"]
    dd_menu_7.set(options_list[0]) #default option
    drop_7 = OptionMenu(root, dd_menu_7, *options_list)
    drop_7.grid(row=7, column=1)
    
    global dd_menu_8
    dd_menu_8 = StringVar()
    options_list = ["SALM", "TCLP"]
    dd_menu_8.set(options_list[0]) #default option
    drop_8 = OptionMenu(root, dd_menu_8, *options_list)
    drop_8.grid(row=8, column=1)
    
    global dd_menu_9
    dd_menu_9 = StringVar()
    options_list = ["SALM", "TCLP"]
    dd_menu_9.set(options_list[0]) #default option
    drop_9 = OptionMenu(root, dd_menu_9, *options_list)
    drop_9.grid(row=9, column=1)
    
    global dd_menu_10
    dd_menu_10 = StringVar()
    options_list = ["SALM", "TCLP"]
    dd_menu_10.set(options_list[0]) #default option
    drop_10 = OptionMenu(root, dd_menu_10, *options_list)
    drop_10.grid(row=10, column=1)
def button_start_point(): #asks about starting position
    where_start_label = Label(root, text ="Starting position?")
    where_start_label.grid(row=12, column=0)
    global dd_menu_start 
    dd_menu_start = IntVar()
    global sample_positions_list
    sample_positions_list = [1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1210, 1211, 1212, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2111, 2112, 2201, 2202, 2203, 2204, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2212, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2308, 2309, 2310, 2311, 2312, 2401, 2402, 2403, 2404, 2405, 2406, 2407, 2408, 2409, 2410, 2411, 2412, 2501, 2502, 2503, 2504, 2505, 2506, 2507, 2508, 2509, 2510, 2511, 2512, 3101, 3102, 3103, 3104, 3105, 3106, 3107, 3108, 3109, 3110, 3111, 3112, 3201, 3202, 3203, 3204, 3205, 3206, 3207, 3208, 3209, 3210, 3211, 3212, 3301, 3302, 3303, 3304, 3305, 3306, 3307, 3308, 3309, 3310, 3311, 3312, 3401, 3402, 3403, 3404, 3405, 3406, 3407, 3408, 3409, 3410, 3411, 3412, 3501, 3502, 3503, 3504, 3505, 3506, 3507, 3508, 3509, 3510, 3511, 3512, 4101, 4102, 4103, 4104, 4105, 4106, 4107, 4108, 4109, 4110, 4111, 4112, 4201, 4202, 4203, 4204, 4205, 4206, 4207, 4208, 4209, 4210, 4211, 4212, 4301, 4302, 4303, 4304, 4305, 4306, 4307, 4308, 4309, 4310, 4311, 4312, 4401, 4402, 4403, 4404, 4405, 4406, 4407, 4408, 4409, 4410, 4411, 4412, 4501, 4502, 4503, 4504, 4505, 4506, 4507, 4508, 4509, 4510, 4511, 4512]
    dd_menu_start.set(sample_positions_list[0]) #default option
    drop_start = OptionMenu(root, dd_menu_start, *sample_positions_list)
    drop_start.grid(row=12, column=1)    
def button_confirm(): #buttons: upload confirmation, generate output
    confirm_button = tk.Button(root, text = "Confirm and Proceed", bg='yellow', command=lambda:output_results())
    confirm_button.grid(row=14, column=0)

### FUNCTIONS (df manipulation) ###############################################
def tclp_compute(incoming_df, start_of_batch, end_of_batch): ##Alter dataframe so it results in the right output
    ##builds around column taken from original excel sheet. Adds columns and default entries
    incoming_df.insert(0, "Sample_Type", 'defaultTYPE') 
    incoming_df.insert(2, "Comment", 'defaultCOMMENT')
    incoming_df.insert(3, "Vial_num", 0) #fills it with zeros
    incoming_df.insert(4, "Total_Dilution", 0)
    incoming_df = incoming_df.rename(columns = {'LabNumber' : 'Sample_Name'}) #change name of one column
    
    ##Insert values into all the columns based on sample name
    incoming_df = incoming_df.assign(Sample_Type='Sample')
    incoming_df = incoming_df.assign(Comment='TCLP')
    incoming_df = incoming_df.assign(Total_Dilution ='10')
    # need to change dilution to 5x for BS sample
    incoming_df.loc[incoming_df['Sample_Name'].str.contains('BS1'), 'Total_Dilution'] = '5'
    
    ##input position info into dataframe, generate sub-list and input it into incoming_df 
    vial_num_list = sample_positions_list[start_of_batch:end_of_batch+1]    
    incoming_df['Vial_num'] = vial_num_list #turn a list into a column

    ###rearrnage rows using shoot up method
    ##shoot rows to top in following order = DUP1, BS1, BLK1, BLK2
    ##product should have the following order BLK2, BLK1, BS1, 3 rinses, DUP1, samples, MS1, 3 rinses
    ##this program assumes that the first sample is the source of DUP1 and the last sample is the source of MS1
    ##drop duplicates at end
    
    #move DUP1 row
    move_2_top_dup1 = incoming_df[incoming_df['Sample_Name'].str.contains('DUP1')]
    df = pd.concat([move_2_top_dup1, incoming_df], ignore_index=True)
    #move BS row
    move_2_top_BS1 = incoming_df[incoming_df['Sample_Name'].str.contains('BS1')]
    df = pd.concat([move_2_top_BS1, df], ignore_index=True)
    #move BLK1
    move_2_top_BLK1 = incoming_df[incoming_df['Sample_Name'].str.contains('BLK1')]
    df = pd.concat([move_2_top_BLK1, df], ignore_index=True)
    #move BLK2
    move_2_top_BLK2 = incoming_df[incoming_df['Sample_Name'].str.contains('BLK2')]
    df = pd.concat([move_2_top_BLK2, df], ignore_index=True)
    # deltes duplicates but keeps rinse duplicates
    df = df[~df['Sample_Name'].duplicated() | df['Sample_Name'].eq('Rinse')] 
    
    ##breaks df into 2 groups of rows in order to add rinses in the right places
    ##assumes index is in proper numerical order i.e. 1,2,3,...,9,10
    
    #Make A group - made up of the first 3 rows (BLK2, BLK1, BS1) of df followed by 3 rinses
    A_tclp_group = df.loc[0:2]
    for x in range(3): #Add 3 rinse row
          A_tclp_group = A_tclp_group.append({'Sample_Type' : 'Sample',
                          'Sample_Name' : 'Rinse',
                          'Comment' : '-',
                          'Vial_num' : 0,
                          'Total_Dilution' : 0} , 
                          ignore_index=True)
    
    #Make B group - made up of DUP1, then non-QC rows (the samples), then MS, then followed by rinses
    # kicks out certain samples from incoming_df, AKA uses an inversion (the tilde symbol)
    B_tclp_group0 = df[df["Sample_Name"].str.contains('DUP1')]
    B_tclp_group1 = incoming_df[~incoming_df["Sample_Name"].str.contains('BLK1')] 
    B_tclp_group2 = B_tclp_group1[~B_tclp_group1["Sample_Name"].str.contains('BLK2')]
    B_tclp_group3 = B_tclp_group2[~B_tclp_group2["Sample_Name"].str.contains('BS1')]
    B_tclp_group4 = B_tclp_group3[~B_tclp_group3["Sample_Name"].str.contains('DUP1')]
    B_tclp_group = pd.concat([B_tclp_group0, B_tclp_group4], ignore_index=True)
    for x in range(3): #Add 3 rinse rows
         B_tclp_group = B_tclp_group.append({'Sample_Type' : 'Sample',
                         'Sample_Name' : 'Rinse',
                         'Comment' : '-',
                         'Vial_num' : 0,
                         'Total_Dilution' : 0} , 
                         ignore_index=True)
         
    ##combine AB groups to make final output, randomizes rinse position
    df_final_tclp = pd.concat([A_tclp_group, B_tclp_group])
    #randomly selects vials 4 or 5 for rinse samples
    df_final_tclp.Vial_num = df_final_tclp.apply(lambda x: np.random.randint(4, 5+1) if x.Sample_Name == 'Rinse' and x.Sample_Type == 'Sample' else x.Vial_num, axis=1)
    #reset index
    df_final_tclp.reset_index(inplace = True)
    return df_final_tclp
def salm_compute(incoming_df, start_of_batch, end_of_batch): ##Alter dataframe so it results in the right output
    
    ##builds around column taken from original excel sheet. Adds columns and default entries
    incoming_df.insert(0, "Sample_Type", 'defaultTYPE') 
    incoming_df.insert(2, "Comment", 'defaultCOMMENT')
    incoming_df.insert(3, "Vial_num", 0) #fills it with zeros
    incoming_df.insert(4, "Total_Dilution", 0)
    incoming_df = incoming_df.rename(columns = {'LabNumber' : 'Sample_Name'}) #change name of one column

    ##Insert values into all the columns based on sample name
    incoming_df = incoming_df.assign(Sample_Type='Sample')
    incoming_df = incoming_df.assign(Comment='SALM')
    incoming_df = incoming_df.assign(Total_Dilution ='50')
    # need to change dilution to 10x for BS sample
    incoming_df.loc[incoming_df['Sample_Name'].str.contains('BS1'), 'Total_Dilution'] = '10'
    
    ##input position info into dataframe, generate sub-list and input it into incoming_df 
    vial_num_list = sample_positions_list[start_of_batch:end_of_batch+1]    
    incoming_df['Vial_num'] = vial_num_list #turn a list into a column

    ###rearrnage rows using shoot up method
    ##shoot rows to top in following order = dup, SRM, BS1, BLK1, BLK3
    ##product should have the following order BLK3, BLK1, BS1, SRM1, DUP1, all samples, BLK2, CCB, CCV, rinses
    ##drop duplicates at end
    #move DUP1 row
    move_2_top_dup1 = incoming_df[incoming_df['Sample_Name'].str.contains('DUP1')]
    df = pd.concat([move_2_top_dup1, incoming_df], ignore_index=True)
    #move SRM row
    move_2_top_SRM1 = incoming_df[incoming_df['Sample_Name'].str.contains('SRM1')]
    df = pd.concat([move_2_top_SRM1, df], ignore_index=True)
    #move BS row
    move_2_top_BS1 = incoming_df[incoming_df['Sample_Name'].str.contains('BS1')]
    df = pd.concat([move_2_top_BS1, df], ignore_index=True)
    #move BLK1
    move_2_top_BLK1 = incoming_df[incoming_df['Sample_Name'].str.contains('BLK1')]
    df = pd.concat([move_2_top_BLK1, df], ignore_index=True)
    #move BLK3
    move_2_top_BLK3 = incoming_df[incoming_df['Sample_Name'].str.contains('BLK3')]
    df = pd.concat([move_2_top_BLK3, df], ignore_index=True)
    # deltes duplicates but keeps rinse duplicates
    df = df[~df['Sample_Name'].duplicated() | df['Sample_Name'].eq('Rinse')] 

    ##breaks df into 4 groups of rows in order to add rinses and CCB/CCV in the right places
    ##assumes index is in proper numerical order i.e. 1,2,3,...,9,10
    
    #Make A group - made up of the first 3 rows (BLK3, BLK1, BS1) of df followed by rinses
    A_salm_group = df.loc[0:2]
    for x in range(1): #Add 1 rinse row
         A_salm_group = A_salm_group.append({'Sample_Type' : 'Sample',
                         'Sample_Name' : 'Rinse',
                         'Comment' : '-',
                         'Vial_num' : 0,
                         'Total_Dilution' : 0} , 
                         ignore_index=True)
    
    #Make B group - made up of the SRM row of df followed by rinses and then the dup
    B_salm_group = df.loc[3:3]
    for x in range(3): #Add 3 rinse rows
         B_salm_group = B_salm_group.append({'Sample_Type' : 'Sample',
                         'Sample_Name' : 'Rinse',
                         'Comment' : '-',
                         'Vial_num' : 0,
                         'Total_Dilution' : 0} , 
                         ignore_index=True)
    dup_row = incoming_df[incoming_df['Sample_Name'].str.contains('DUP1')]
    B_salm_group = B_salm_group.append(dup_row)
    
    #Make C group - made up of the non-QC rows (the samples) of df followed by rinses
    # kicks out non-QC samples from incoming_df, AKA uses an inversion (the tilde symbol)
    C_salm_group1 = incoming_df[~incoming_df["Sample_Name"].str.contains('BLK1')] 
    C_salm_group2 = C_salm_group1[~C_salm_group1["Sample_Name"].str.contains('BLK2')]
    C_salm_group3 = C_salm_group2[~C_salm_group2["Sample_Name"].str.contains('BLK3')]
    C_salm_group4 = C_salm_group3[~C_salm_group3["Sample_Name"].str.contains('SRM1')]
    C_salm_group5 = C_salm_group4[~C_salm_group4["Sample_Name"].str.contains('BS1')]
    C_salm_group = C_salm_group5[~C_salm_group5["Sample_Name"].str.contains('DUP1')]
    for x in range(3): #Add 3 rinse rows
         B_salm_group = B_salm_group.append({'Sample_Type' : 'Sample',
                         'Sample_Name' : 'Rinse',
                         'Comment' : '-',
                         'Vial_num' : 0,
                         'Total_Dilution' : 0} , 
                         ignore_index=True)       
         
    #Make D group - has BLK2, CCB, CCV and rinses
    D_salm_group = incoming_df[incoming_df["Sample_Name"].str.contains('BLK2')]
    #add CCB and CCV
    D_salm_group = D_salm_group.append({'Sample_Type' : 'CCB',
                        'Sample_Name' : 'CCB',
                        'Comment' : '-',
                        'Vial_num' : 1405,
                        'Total_Dilution' : 0} , 
                        ignore_index=True)
    D_salm_group = D_salm_group.append({'Sample_Type' : 'CCV',
                        'Sample_Name' : 'CCV',
                        'Comment' : '-',
                        'Vial_num' : 1411,
                        'Total_Dilution' : 0} , 
                        ignore_index=True)
    for x in range(8): #Add rinse rows to bottom of D group
         D_salm_group = D_salm_group.append({'Sample_Type' : 'Sample',
                         'Sample_Name' : 'Rinse',
                         'Comment' : '-',
                         'Vial_num' : 0,
                         'Total_Dilution' : 0} , 
                         ignore_index=True) 
         
    ##combine ABCD groups to make final output, randomizes rinse position
    df_final_salm = pd.concat([A_salm_group, B_salm_group, C_salm_group, D_salm_group])
    #randomly selects vials 4 or 5 for rinse samples
    df_final_salm.Vial_num = df_final_salm.apply(lambda x: np.random.randint(4, 5+1) if x.Sample_Name == 'Rinse' and x.Sample_Type == 'Sample' else x.Vial_num, axis=1)
    #reset index
    df_final_salm.reset_index(inplace = True)
    return df_final_salm
def find_end_plus_start(df_find_position, where_start_idx):
    row_amount = len(df_find_position.index) #find how many rows are, don't count tittle row
    where_end_idx = where_start_idx + (row_amount - 1) #don't count tittle row
    return where_end_idx
def prelim_clean(raw_data): #common to all analyses
    not_raw_data = raw_data.drop_duplicates(subset=['LabNumber'])
    not_raw_data = not_raw_data[['LabNumber']] #keep only first column from the raw data
    return not_raw_data

### FUNCTIONS(button functions) ##############################################

def upload_file_1(): 
    file_1 = filedialog.askopenfilename()
    if(file_1):
        my_str_1 = tk.StringVar()
        my_str_1.set(file_1)
        fob_1 = open(file_1, 'r')
        path_1 = tk.Label(root, textvariable=my_str_1, fg='blue')
        path_1.grid(row=1, column=2) 
        global df_1
        df_1 = pd.read_excel(file_1)
        return df_1  
def upload_file_2(): 
    file_2 = filedialog.askopenfilename()
    if(file_2):
        my_str_2 = tk.StringVar()
        my_str_2.set(file_2)
        fob_2 = open(file_2, 'r')
        path_2 = tk.Label(root, textvariable=my_str_2, fg='blue')
        path_2.grid(row=2, column=2) 
        global df_2
        df_2 = pd.read_excel(file_2)
        return df_2       
def upload_file_3(): 
    file_3 = filedialog.askopenfilename()
    if(file_3):
        my_str_3 = tk.StringVar()
        my_str_3.set(file_3)
        fob_3 = open(file_3, 'r')
        path_3 = tk.Label(root, textvariable=my_str_3, fg='blue')
        path_3.grid(row=3, column=2) 
        global df_3
        df_3 = pd.read_excel(file_3)
        return df_3       
def upload_file_4(): 
    file_4 = filedialog.askopenfilename()
    if(file_4):
        my_str_4 = tk.StringVar()
        my_str_4.set(file_4)
        fob_4 = open(file_4, 'r')
        path_4 = tk.Label(root, textvariable=my_str_4, fg='blue')
        path_4.grid(row=4, column=2) 
        global df_4
        df_4 = pd.read_excel(file_4)
        return df_4       
def upload_file_5(): 
    file_5 = filedialog.askopenfilename()
    if(file_5):
        my_str_5 = tk.StringVar()
        my_str_5.set(file_5)
        fob_5 = open(file_5, 'r')
        path_5 = tk.Label(root, textvariable=my_str_5, fg='blue')
        path_5.grid(row=5, column=2) 
        global df_5
        df_5 = pd.read_excel(file_5)
        return df_5       
def upload_file_6(): 
    file_6 = filedialog.askopenfilename()
    if(file_6):
        my_str_6 = tk.StringVar()
        my_str_6.set(file_6)
        fob_6 = open(file_6, 'r')
        path_6 = tk.Label(root, textvariable=my_str_6, fg='blue')
        path_6.grid(row=6, column=2) 
        global df_6
        df_6 = pd.read_excel(file_6)
        return df_6       
def upload_file_7(): 
    file_7 = filedialog.askopenfilename()
    if(file_7):
        my_str_7 = tk.StringVar()
        my_str_7.set(file_7)
        fob_7 = open(file_7, 'r')
        path_7 = tk.Label(root, textvariable=my_str_7, fg='blue')
        path_7.grid(row=7, column=2) 
        global df_7
        df_7 = pd.read_excel(file_7)
        return df_7    
def upload_file_8(): 
    file_8 = filedialog.askopenfilename()
    if(file_8):
        my_str_8 = tk.StringVar()
        my_str_8.set(file_8)
        fob_8 = open(file_8, 'r')
        path_8 = tk.Label(root, textvariable=my_str_8, fg='blue')
        path_8.grid(row=8, column=2) 
        global df_8
        df_8 = pd.read_excel(file_8)
        return df_8       
def upload_file_9(): 
    file_9 = filedialog.askopenfilename()
    if(file_9):
        my_str_9 = tk.StringVar()
        my_str_9.set(file_9)
        fob_9 = open(file_9, 'r')
        path_9 = tk.Label(root, textvariable=my_str_9, fg='blue')
        path_9.grid(row=9, column=2) 
        global df_9
        df_9 = pd.read_excel(file_9)
        return df_9       
def upload_file_10(): 
    file_10 = filedialog.askopenfilename()
    if(file_10):
        my_str_10 = tk.StringVar()
        my_str_10.set(file_10)
        fob_10 = open(file_10, 'r')
        path_10 = tk.Label(root, textvariable=my_str_10, fg='blue')
        path_10.grid(row=10, column=2) 
        global df_10
        df_10 = pd.read_excel(file_10)
        return df_10       

## FUNCTIONS(output results, from confirm button) #############################
def output_results():
    
    global start_position_ultimate
    global dd_menu_start
    global start_position_ultimate_idx
    global sample_positions_list

    
    #checks position information 
    start_position_ultimate = dd_menu_start.get() 
    start_position_ultimate_idx = sample_positions_list.index(start_position_ultimate)

    
    #outputs results to excel named "AutoSeqResults". Each dataframe is dependant of the conditions of subsequent dataframes
    if dd_entry_num.get() == "1":
        data_1a = prelim_clean(df_1)
        data_1a_end_idx = find_end_plus_start(data_1a, start_position_ultimate_idx)
        if dd_menu_1.get() == "SALM":
             df_all_1 = salm_compute(data_1a, start_position_ultimate_idx, data_1a_end_idx)
        if dd_menu_1.get() == "TCLP":
             df_all_1 = tclp_compute(data_1a, start_position_ultimate_idx, data_1a_end_idx)
        dataframe_all = df_all_1
        
    if dd_entry_num.get() == "2":
        data_1a = prelim_clean(df_1)
        data_1a_end_idx = find_end_plus_start(data_1a, start_position_ultimate_idx)
        if dd_menu_1.get() == "SALM":
             df_all_1 = salm_compute(data_1a, start_position_ultimate_idx, data_1a_end_idx)
        if dd_menu_1.get() == "TCLP":
             df_all_1 = tclp_compute(data_1a, start_position_ultimate_idx, data_1a_end_idx)        
        data_2a = prelim_clean(df_2) 
        data_2a_start_idx = 1 + data_1a_end_idx
        data_2a_end_idx = find_end_plus_start(data_2a, data_2a_start_idx)
        if dd_menu_2.get() == "SALM":
            df_all_2 = salm_compute(data_2a, data_2a_start_idx, data_2a_end_idx)        
        if dd_menu_2.get() == "TCLP":
            df_all_2 = tclp_compute(data_2a, data_2a_start_idx, data_2a_end_idx)              
        dataframe_all = pd.concat([df_all_1, df_all_2], axis=0)
        
    if dd_entry_num.get() == "3":
        data_1a = prelim_clean(df_1)
        data_1a_end_idx = find_end_plus_start(data_1a, start_position_ultimate_idx)
        if dd_menu_1.get() == "SALM":
             df_all_1 = salm_compute(data_1a, start_position_ultimate_idx, data_1a_end_idx)
        if dd_menu_1.get() == "TCLP":
             df_all_1 = tclp_compute(data_1a, start_position_ultimate_idx, data_1a_end_idx)
        data_2a = prelim_clean(df_2) 
        data_2a_start_idx = 1 + data_1a_end_idx
        data_2a_end_idx = find_end_plus_start(data_2a, data_2a_start_idx)
        if dd_menu_2.get() == "SALM":
            df_all_2 = salm_compute(data_2a, data_2a_start_idx, data_2a_end_idx) 
        if dd_menu_2.get() == "TCLP":
            df_all_2 = tclp_compute(data_2a, data_2a_start_idx, data_2a_end_idx) 
        data_3a = prelim_clean(df_3) 
        data_3a_start_idx = 1 + data_2a_end_idx
        data_3a_end_idx = find_end_plus_start(data_3a, data_3a_start_idx)
        if dd_menu_3.get() == "SALM":
            df_all_3 = salm_compute(data_3a, data_3a_start_idx, data_3a_end_idx)
        if dd_menu_3.get() == "TCLP":
            df_all_3 = tclp_compute(data_3a, data_3a_start_idx, data_3a_end_idx)
        dataframe_all = pd.concat([df_all_1, df_all_2, df_all_3], axis=0)

    if dd_entry_num.get() == "4":
        data_1a = prelim_clean(df_1)
        data_1a_end_idx = find_end_plus_start(data_1a, start_position_ultimate_idx)
        if dd_menu_1.get() == "SALM":
             df_all_1 = salm_compute(data_1a, start_position_ultimate_idx, data_1a_end_idx)
        if dd_menu_1.get() == "TCLP":
             df_all_1 = tclp_compute(data_1a, start_position_ultimate_idx, data_1a_end_idx)
        data_2a = prelim_clean(df_2) 
        data_2a_start_idx = 1 + data_1a_end_idx
        data_2a_end_idx = find_end_plus_start(data_2a, data_2a_start_idx)
        if dd_menu_2.get() == "SALM":
            df_all_2 = salm_compute(data_2a, data_2a_start_idx, data_2a_end_idx) 
        if dd_menu_2.get() == "TCLP":
            df_all_2 = tclp_compute(data_2a, data_2a_start_idx, data_2a_end_idx) 
        data_3a = prelim_clean(df_3) 
        data_3a_start_idx = 1 + data_2a_end_idx
        data_3a_end_idx = find_end_plus_start(data_3a, data_3a_start_idx)
        if dd_menu_3.get() == "SALM":
            df_all_3 = salm_compute(data_3a, data_3a_start_idx, data_3a_end_idx)
        if dd_menu_3.get() == "TCLP":
            df_all_3 = tclp_compute(data_3a, data_3a_start_idx, data_3a_end_idx)        
        data_4a = prelim_clean(df_4) 
        data_4a_start_idx = 1 + data_3a_end_idx
        data_4a_end_idx = find_end_plus_start(data_4a, data_4a_start_idx)
        if dd_menu_4.get() == "SALM":
            df_all_4 = salm_compute(data_4a, data_4a_start_idx, data_4a_end_idx)
        if dd_menu_4.get() == "TCLP":
            df_all_4 = tclp_compute(data_4a, data_4a_start_idx, data_4a_end_idx)
        dataframe_all = pd.concat([df_all_1, df_all_2, df_all_3, df_all_4], axis=0)

    if dd_entry_num.get() == "5":
        data_1a = prelim_clean(df_1)
        data_1a_end_idx = find_end_plus_start(data_1a, start_position_ultimate_idx)
        if dd_menu_1.get() == "SALM":
             df_all_1 = salm_compute(data_1a, start_position_ultimate_idx, data_1a_end_idx)
        if dd_menu_1.get() == "TCLP":
             df_all_1 = tclp_compute(data_1a, start_position_ultimate_idx, data_1a_end_idx)
        data_2a = prelim_clean(df_2) 
        data_2a_start_idx = 1 + data_1a_end_idx
        data_2a_end_idx = find_end_plus_start(data_2a, data_2a_start_idx)
        if dd_menu_2.get() == "SALM":
            df_all_2 = salm_compute(data_2a, data_2a_start_idx, data_2a_end_idx) 
        if dd_menu_2.get() == "TCLP":
            df_all_2 = tclp_compute(data_2a, data_2a_start_idx, data_2a_end_idx) 
        data_3a = prelim_clean(df_3) 
        data_3a_start_idx = 1 + data_2a_end_idx
        data_3a_end_idx = find_end_plus_start(data_3a, data_3a_start_idx)
        if dd_menu_3.get() == "SALM":
            df_all_3 = salm_compute(data_3a, data_3a_start_idx, data_3a_end_idx)
        if dd_menu_3.get() == "TCLP":
            df_all_3 = tclp_compute(data_3a, data_3a_start_idx, data_3a_end_idx)
        data_4a = prelim_clean(df_4) 
        data_4a_start_idx = 1 + data_3a_end_idx
        data_4a_end_idx = find_end_plus_start(data_4a, data_4a_start_idx)
        if dd_menu_4.get() == "SALM":
            df_all_4 = salm_compute(data_4a, data_4a_start_idx, data_4a_end_idx)
        if dd_menu_4.get() == "TCLP":
            df_all_4 = tclp_compute(data_4a, data_4a_start_idx, data_4a_end_idx)
        data_5a = prelim_clean(df_5) 
        data_5a_start_idx = 1 + data_4a_end_idx
        data_5a_end_idx = find_end_plus_start(data_5a, data_5a_start_idx)
        if dd_menu_5.get() == "SALM":
            df_all_5 = salm_compute(data_5a, data_5a_start_idx, data_5a_end_idx)
        if dd_menu_5.get() == "TCLP":
            df_all_5 = tclp_compute(data_5a, data_5a_start_idx, data_5a_end_idx)
        dataframe_all = pd.concat([df_all_1, df_all_2, df_all_3, df_all_4, df_all_5], axis=0)
        
    if dd_entry_num.get() == "6":
        data_1a = prelim_clean(df_1)
        data_1a_end_idx = find_end_plus_start(data_1a, start_position_ultimate_idx)
        if dd_menu_1.get() == "SALM":
             df_all_1 = salm_compute(data_1a, start_position_ultimate_idx, data_1a_end_idx)
        if dd_menu_1.get() == "TCLP":
             df_all_1 = tclp_compute(data_1a, start_position_ultimate_idx, data_1a_end_idx)
        data_2a = prelim_clean(df_2) 
        data_2a_start_idx = 1 + data_1a_end_idx
        data_2a_end_idx = find_end_plus_start(data_2a, data_2a_start_idx)
        if dd_menu_2.get() == "SALM":
            df_all_2 = salm_compute(data_2a, data_2a_start_idx, data_2a_end_idx) 
        if dd_menu_2.get() == "TCLP":
            df_all_2 = tclp_compute(data_2a, data_2a_start_idx, data_2a_end_idx) 
        data_3a = prelim_clean(df_3) 
        data_3a_start_idx = 1 + data_2a_end_idx
        data_3a_end_idx = find_end_plus_start(data_3a, data_3a_start_idx)
        if dd_menu_3.get() == "SALM":
            df_all_3 = salm_compute(data_3a, data_3a_start_idx, data_3a_end_idx)
        if dd_menu_3.get() == "TCLP":
            df_all_3 = tclp_compute(data_3a, data_3a_start_idx, data_3a_end_idx)
        data_4a = prelim_clean(df_4) 
        data_4a_start_idx = 1 + data_3a_end_idx
        data_4a_end_idx = find_end_plus_start(data_4a, data_4a_start_idx)
        if dd_menu_4.get() == "SALM":
            df_all_4 = salm_compute(data_4a, data_4a_start_idx, data_4a_end_idx)
        if dd_menu_4.get() == "TCLP":
            df_all_4 = tclp_compute(data_4a, data_4a_start_idx, data_4a_end_idx)
        data_5a = prelim_clean(df_5) 
        data_5a_start_idx = 1 + data_4a_end_idx
        data_5a_end_idx = find_end_plus_start(data_5a, data_5a_start_idx)
        if dd_menu_5.get() == "SALM":
            df_all_5 = salm_compute(data_5a, data_5a_start_idx, data_5a_end_idx)
        if dd_menu_5.get() == "TCLP":
            df_all_5 = tclp_compute(data_5a, data_5a_start_idx, data_5a_end_idx)
        data_6a = prelim_clean(df_6) 
        data_6a_start_idx = 1 + data_5a_end_idx
        data_6a_end_idx = find_end_plus_start(data_6a, data_6a_start_idx)
        if dd_menu_6.get() == "SALM":
            df_all_6 = salm_compute(data_6a, data_6a_start_idx, data_6a_end_idx)
        if dd_menu_6.get() == "TCLP":
            df_all_6 = tclp_compute(data_6a, data_6a_start_idx, data_6a_end_idx)
        dataframe_all = pd.concat([df_all_1, df_all_2, df_all_3, df_all_4, df_all_5, df_all_6], axis=0)

    if dd_entry_num.get() == "7":
        data_1a = prelim_clean(df_1)
        data_1a_end_idx = find_end_plus_start(data_1a, start_position_ultimate_idx)
        if dd_menu_1.get() == "SALM":
             df_all_1 = salm_compute(data_1a, start_position_ultimate_idx, data_1a_end_idx)
        if dd_menu_1.get() == "TCLP":
             df_all_1 = tclp_compute(data_1a, start_position_ultimate_idx, data_1a_end_idx)
        data_2a = prelim_clean(df_2) 
        data_2a_start_idx = 1 + data_1a_end_idx
        data_2a_end_idx = find_end_plus_start(data_2a, data_2a_start_idx)
        if dd_menu_2.get() == "SALM":
            df_all_2 = salm_compute(data_2a, data_2a_start_idx, data_2a_end_idx) 
        if dd_menu_2.get() == "TCLP":
            df_all_2 = tclp_compute(data_2a, data_2a_start_idx, data_2a_end_idx) 
        data_3a = prelim_clean(df_3) 
        data_3a_start_idx = 1 + data_2a_end_idx
        data_3a_end_idx = find_end_plus_start(data_3a, data_3a_start_idx)
        if dd_menu_3.get() == "SALM":
            df_all_3 = salm_compute(data_3a, data_3a_start_idx, data_3a_end_idx)
        if dd_menu_3.get() == "TCLP":
            df_all_3 = tclp_compute(data_3a, data_3a_start_idx, data_3a_end_idx)
        data_4a = prelim_clean(df_4) 
        data_4a_start_idx = 1 + data_3a_end_idx
        data_4a_end_idx = find_end_plus_start(data_4a, data_4a_start_idx)
        if dd_menu_4.get() == "SALM":
            df_all_4 = salm_compute(data_4a, data_4a_start_idx, data_4a_end_idx)
        if dd_menu_4.get() == "TCLP":
            df_all_4 = tclp_compute(data_4a, data_4a_start_idx, data_4a_end_idx)
        data_5a = prelim_clean(df_5) 
        data_5a_start_idx = 1 + data_4a_end_idx
        data_5a_end_idx = find_end_plus_start(data_5a, data_5a_start_idx)
        if dd_menu_5.get() == "SALM":
            df_all_5 = salm_compute(data_5a, data_5a_start_idx, data_5a_end_idx)
        if dd_menu_5.get() == "TCLP":
            df_all_5 = tclp_compute(data_5a, data_5a_start_idx, data_5a_end_idx)
        data_6a = prelim_clean(df_6) 
        data_6a_start_idx = 1 + data_5a_end_idx
        data_6a_end_idx = find_end_plus_start(data_6a, data_6a_start_idx)
        if dd_menu_6.get() == "SALM":
            df_all_6 = salm_compute(data_6a, data_6a_start_idx, data_6a_end_idx)
        if dd_menu_6.get() == "TCLP":
            df_all_6 = tclp_compute(data_6a, data_6a_start_idx, data_6a_end_idx)
        data_7a = prelim_clean(df_7) 
        data_7a_start_idx = 1 + data_6a_end_idx
        data_7a_end_idx = find_end_plus_start(data_7a, data_7a_start_idx)
        if dd_menu_7.get() == "SALM":
            df_all_7 = salm_compute(data_7a, data_7a_start_idx, data_7a_end_idx)    
        if dd_menu_7.get() == "TCLP":
            df_all_7 = tclp_compute(data_7a, data_7a_start_idx, data_7a_end_idx)    
        dataframe_all = pd.concat([df_all_1, df_all_2, df_all_3, df_all_4, df_all_5, df_all_6, df_all_7], axis=0)

    if dd_entry_num.get() == "8":
        data_1a = prelim_clean(df_1)
        data_1a_end_idx = find_end_plus_start(data_1a, start_position_ultimate_idx)
        if dd_menu_1.get() == "SALM":
             df_all_1 = salm_compute(data_1a, start_position_ultimate_idx, data_1a_end_idx)
        if dd_menu_1.get() == "TCLP":
             df_all_1 = tclp_compute(data_1a, start_position_ultimate_idx, data_1a_end_idx)
        data_2a = prelim_clean(df_2) 
        data_2a_start_idx = 1 + data_1a_end_idx
        data_2a_end_idx = find_end_plus_start(data_2a, data_2a_start_idx)
        if dd_menu_2.get() == "SALM":
            df_all_2 = salm_compute(data_2a, data_2a_start_idx, data_2a_end_idx) 
        if dd_menu_2.get() == "TCLP":
            df_all_2 = tclp_compute(data_2a, data_2a_start_idx, data_2a_end_idx) 
        data_3a = prelim_clean(df_3) 
        data_3a_start_idx = 1 + data_2a_end_idx
        data_3a_end_idx = find_end_plus_start(data_3a, data_3a_start_idx)
        if dd_menu_3.get() == "SALM":
            df_all_3 = salm_compute(data_3a, data_3a_start_idx, data_3a_end_idx)
        if dd_menu_3.get() == "TCLP":
            df_all_3 = tclp_compute(data_3a, data_3a_start_idx, data_3a_end_idx)
        data_4a = prelim_clean(df_4) 
        data_4a_start_idx = 1 + data_3a_end_idx
        data_4a_end_idx = find_end_plus_start(data_4a, data_4a_start_idx)
        if dd_menu_4.get() == "SALM":
            df_all_4 = salm_compute(data_4a, data_4a_start_idx, data_4a_end_idx)
        if dd_menu_4.get() == "TCLP":
            df_all_4 = tclp_compute(data_4a, data_4a_start_idx, data_4a_end_idx)
        data_5a = prelim_clean(df_5) 
        data_5a_start_idx = 1 + data_4a_end_idx
        data_5a_end_idx = find_end_plus_start(data_5a, data_5a_start_idx)
        if dd_menu_5.get() == "SALM":
            df_all_5 = salm_compute(data_5a, data_5a_start_idx, data_5a_end_idx)
        if dd_menu_5.get() == "TCLP":
            df_all_5 = tclp_compute(data_5a, data_5a_start_idx, data_5a_end_idx)
        data_6a = prelim_clean(df_6) 
        data_6a_start_idx = 1 + data_5a_end_idx
        data_6a_end_idx = find_end_plus_start(data_6a, data_6a_start_idx)
        if dd_menu_6.get() == "SALM":
            df_all_6 = salm_compute(data_6a, data_6a_start_idx, data_6a_end_idx)
        if dd_menu_6.get() == "TCLP":
            df_all_6 = tclp_compute(data_6a, data_6a_start_idx, data_6a_end_idx)
        data_7a = prelim_clean(df_7) 
        data_7a_start_idx = 1 + data_6a_end_idx
        data_7a_end_idx = find_end_plus_start(data_7a, data_7a_start_idx)
        if dd_menu_7.get() == "SALM":
            df_all_7 = salm_compute(data_7a, data_7a_start_idx, data_7a_end_idx)    
        if dd_menu_7.get() == "TCLP":
            df_all_7 = tclp_compute(data_7a, data_7a_start_idx, data_7a_end_idx)    
        data_8a = prelim_clean(df_8) 
        data_8a_start_idx = 1 + data_7a_end_idx
        data_8a_end_idx = find_end_plus_start(data_8a, data_8a_start_idx)
        if dd_menu_8.get() == "SALM":
            df_all_8 = salm_compute(data_8a, data_8a_start_idx, data_8a_end_idx) 
        if dd_menu_8.get() == "TCLP":
            df_all_8 = tclp_compute(data_8a, data_8a_start_idx, data_8a_end_idx) 
        dataframe_all = pd.concat([df_all_1, df_all_2, df_all_3, df_all_4, df_all_5, df_all_6, df_all_7, df_all_8], axis=0)

    if dd_entry_num.get() == "9":
        data_1a = prelim_clean(df_1)
        data_1a_end_idx = find_end_plus_start(data_1a, start_position_ultimate_idx)
        if dd_menu_1.get() == "SALM":
             df_all_1 = salm_compute(data_1a, start_position_ultimate_idx, data_1a_end_idx)
        if dd_menu_1.get() == "TCLP":
             df_all_1 = tclp_compute(data_1a, start_position_ultimate_idx, data_1a_end_idx)
        data_2a = prelim_clean(df_2) 
        data_2a_start_idx = 1 + data_1a_end_idx
        data_2a_end_idx = find_end_plus_start(data_2a, data_2a_start_idx)
        if dd_menu_2.get() == "SALM":
            df_all_2 = salm_compute(data_2a, data_2a_start_idx, data_2a_end_idx) 
        if dd_menu_2.get() == "TCLP":
            df_all_2 = tclp_compute(data_2a, data_2a_start_idx, data_2a_end_idx) 
        data_3a = prelim_clean(df_3) 
        data_3a_start_idx = 1 + data_2a_end_idx
        data_3a_end_idx = find_end_plus_start(data_3a, data_3a_start_idx)
        if dd_menu_3.get() == "SALM":
            df_all_3 = salm_compute(data_3a, data_3a_start_idx, data_3a_end_idx)
        if dd_menu_3.get() == "TCLP":
            df_all_3 = tclp_compute(data_3a, data_3a_start_idx, data_3a_end_idx)
        data_4a = prelim_clean(df_4) 
        data_4a_start_idx = 1 + data_3a_end_idx
        data_4a_end_idx = find_end_plus_start(data_4a, data_4a_start_idx)
        if dd_menu_4.get() == "SALM":
            df_all_4 = salm_compute(data_4a, data_4a_start_idx, data_4a_end_idx)
        if dd_menu_4.get() == "TCLP":
            df_all_4 = tclp_compute(data_4a, data_4a_start_idx, data_4a_end_idx)
        data_5a = prelim_clean(df_5) 
        data_5a_start_idx = 1 + data_4a_end_idx
        data_5a_end_idx = find_end_plus_start(data_5a, data_5a_start_idx)
        if dd_menu_5.get() == "SALM":
            df_all_5 = salm_compute(data_5a, data_5a_start_idx, data_5a_end_idx)
        if dd_menu_5.get() == "TCLP":
            df_all_5 = tclp_compute(data_5a, data_5a_start_idx, data_5a_end_idx)
        data_6a = prelim_clean(df_6) 
        data_6a_start_idx = 1 + data_5a_end_idx
        data_6a_end_idx = find_end_plus_start(data_6a, data_6a_start_idx)
        if dd_menu_6.get() == "SALM":
            df_all_6 = salm_compute(data_6a, data_6a_start_idx, data_6a_end_idx)
        if dd_menu_6.get() == "TCLP":
            df_all_6 = tclp_compute(data_6a, data_6a_start_idx, data_6a_end_idx)
        data_7a = prelim_clean(df_7) 
        data_7a_start_idx = 1 + data_6a_end_idx
        data_7a_end_idx = find_end_plus_start(data_7a, data_7a_start_idx)
        if dd_menu_7.get() == "SALM":
            df_all_7 = salm_compute(data_7a, data_7a_start_idx, data_7a_end_idx)    
        if dd_menu_7.get() == "TCLP":
            df_all_7 = tclp_compute(data_7a, data_7a_start_idx, data_7a_end_idx)    
        data_8a = prelim_clean(df_8) 
        data_8a_start_idx = 1 + data_7a_end_idx
        data_8a_end_idx = find_end_plus_start(data_8a, data_8a_start_idx)
        if dd_menu_8.get() == "SALM":
            df_all_8 = salm_compute(data_8a, data_8a_start_idx, data_8a_end_idx) 
        if dd_menu_8.get() == "TCLP":
            df_all_8 = tclp_compute(data_8a, data_8a_start_idx, data_8a_end_idx) 
        data_9a = prelim_clean(df_9) 
        data_9a_start_idx = 1 + data_8a_end_idx
        data_9a_end_idx = find_end_plus_start(data_9a, data_9a_start_idx)
        if dd_menu_9.get() == "SALM":
            df_all_9 = salm_compute(data_9a, data_9a_start_idx, data_9a_end_idx) 
        if dd_menu_9.get() == "TCLP":
            df_all_9 = tclp_compute(data_9a, data_9a_start_idx, data_9a_end_idx) 
        dataframe_all = pd.concat([df_all_1, df_all_2, df_all_3, df_all_4, df_all_5, df_all_6, df_all_7, df_all_8, df_all_9], axis=0)
  
    if dd_entry_num.get() == "10":
        data_1a = prelim_clean(df_1)
        data_1a_end_idx = find_end_plus_start(data_1a, start_position_ultimate_idx)
        if dd_menu_1.get() == "SALM":
             df_all_1 = salm_compute(data_1a, start_position_ultimate_idx, data_1a_end_idx)
        if dd_menu_1.get() == "TCLP":
             df_all_1 = tclp_compute(data_1a, start_position_ultimate_idx, data_1a_end_idx)
        data_2a = prelim_clean(df_2) 
        data_2a_start_idx = 1 + data_1a_end_idx
        data_2a_end_idx = find_end_plus_start(data_2a, data_2a_start_idx)
        if dd_menu_2.get() == "SALM":
            df_all_2 = salm_compute(data_2a, data_2a_start_idx, data_2a_end_idx) 
        if dd_menu_2.get() == "TCLP":
            df_all_2 = tclp_compute(data_2a, data_2a_start_idx, data_2a_end_idx) 
        data_3a = prelim_clean(df_3) 
        data_3a_start_idx = 1 + data_2a_end_idx
        data_3a_end_idx = find_end_plus_start(data_3a, data_3a_start_idx)
        if dd_menu_3.get() == "SALM":
            df_all_3 = salm_compute(data_3a, data_3a_start_idx, data_3a_end_idx)
        if dd_menu_3.get() == "TCLP":
            df_all_3 = tclp_compute(data_3a, data_3a_start_idx, data_3a_end_idx)
        data_4a = prelim_clean(df_4) 
        data_4a_start_idx = 1 + data_3a_end_idx
        data_4a_end_idx = find_end_plus_start(data_4a, data_4a_start_idx)
        if dd_menu_4.get() == "SALM":
            df_all_4 = salm_compute(data_4a, data_4a_start_idx, data_4a_end_idx)
        if dd_menu_4.get() == "TCLP":
            df_all_4 = tclp_compute(data_4a, data_4a_start_idx, data_4a_end_idx)
        data_5a = prelim_clean(df_5) 
        data_5a_start_idx = 1 + data_4a_end_idx
        data_5a_end_idx = find_end_plus_start(data_5a, data_5a_start_idx)
        if dd_menu_5.get() == "SALM":
            df_all_5 = salm_compute(data_5a, data_5a_start_idx, data_5a_end_idx)
        if dd_menu_5.get() == "TCLP":
            df_all_5 = tclp_compute(data_5a, data_5a_start_idx, data_5a_end_idx)
        data_6a = prelim_clean(df_6) 
        data_6a_start_idx = 1 + data_5a_end_idx
        data_6a_end_idx = find_end_plus_start(data_6a, data_6a_start_idx)
        if dd_menu_6.get() == "SALM":
            df_all_6 = salm_compute(data_6a, data_6a_start_idx, data_6a_end_idx)
        if dd_menu_6.get() == "TCLP":
            df_all_6 = tclp_compute(data_6a, data_6a_start_idx, data_6a_end_idx)
        data_7a = prelim_clean(df_7) 
        data_7a_start_idx = 1 + data_6a_end_idx
        data_7a_end_idx = find_end_plus_start(data_7a, data_7a_start_idx)
        if dd_menu_7.get() == "SALM":
            df_all_7 = salm_compute(data_7a, data_7a_start_idx, data_7a_end_idx)    
        if dd_menu_7.get() == "TCLP":
            df_all_7 = tclp_compute(data_7a, data_7a_start_idx, data_7a_end_idx)    
        data_8a = prelim_clean(df_8) 
        data_8a_start_idx = 1 + data_7a_end_idx
        data_8a_end_idx = find_end_plus_start(data_8a, data_8a_start_idx)
        if dd_menu_8.get() == "SALM":
            df_all_8 = salm_compute(data_8a, data_8a_start_idx, data_8a_end_idx) 
        if dd_menu_8.get() == "TCLP":
            df_all_8 = tclp_compute(data_8a, data_8a_start_idx, data_8a_end_idx) 
        data_9a = prelim_clean(df_9) 
        data_9a_start_idx = 1 + data_8a_end_idx
        data_9a_end_idx = find_end_plus_start(data_9a, data_9a_start_idx)
        if dd_menu_9.get() == "SALM":
            df_all_9 = salm_compute(data_9a, data_9a_start_idx, data_9a_end_idx) 
        if dd_menu_9.get() == "TCLP":
            df_all_9 = tclp_compute(data_9a, data_9a_start_idx, data_9a_end_idx)
        
        data_10a = prelim_clean(df_10) 
        data_10a_start_idx = 1 + data_9a_end_idx
        data_10a_end_idx = find_end_plus_start(data_10a, data_10a_start_idx)
        if dd_menu_10.get() == "SALM":
            df_all_10 = salm_compute(data_10a, data_10a_start_idx, data_10a_end_idx)             
        if dd_menu_10.get() == "TCLP":
            df_all_10 = tclp_compute(data_10a, data_10a_start_idx, data_10a_end_idx)             
        dataframe_all = pd.concat([df_all_1, df_all_2, df_all_3, df_all_4, df_all_5, df_all_6, df_all_7, df_all_8, df_all_9, df_all_10], axis=0)
    
    #need to delete index and need better label
    dataframe_all.drop('index', inplace=True, axis=1)
    writer = pd.ExcelWriter('AutoSeqResults.xlsx') # create excel writer object
    dataframe_all.to_excel(writer) # write dataframe to excel
    writer.save() #save excel, make sure that the output file has been recently updated!
    finished_label = tk.Label(root, text = 'Results computed. \nSee the Excel file AutoSeqResults.xlsx. \nReopen program to refresh.')
    finished_label.configure(foreground="blue")
    finished_label.grid(row=16, column=0)

### MAIN CODE #################################################################

#opening format
opening_setup()

#buttons
button_file_num()
button_start_point()
button_analysis_type()
button_upload_files()
button_confirm()

root.mainloop()   
###############################################################################