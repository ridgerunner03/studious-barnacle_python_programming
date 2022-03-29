"""
This file will be a GUI that will enable the user
to unzip a file within a folder or series of folders.
"""


import tkinter as tk
from PIL import Image, ImageTk
import os



## align exceptions from B3 and B4.

logo = Image.open('cotton_logo.png')
sm_logo = logo.resize((175,175))


root = tk.Tk()

canvas = tk.Canvas(root, width=1000, height=500)
canvas.grid(columnspan=4, rowspan=4)

logo = Image.open('cotton_logo.png')
sm_logo = ImageTk.PhotoImage(sm_logo)
logo_label = tk.Label(image=sm_logo)
logo_label.image = sm_logo
logo_label.grid(column=0, row=0)

#1 define working_dir
def set_working_dir():
    print("Hello World!")

B1 = tk.Button(root,text = "Set Working Directory", command = set_working_dir)

B1.grid(column=0, row=2)


#2 set up folders
def setup_folders():
    working_dir = os.getcwd() #this will change to the user selected directory in final

    hold_dir = '/1_Holding_Folder/'
    test_dir = '/2_Testing_Folder/'
    del_dir = '/3_To_Be_Deleted/'
    except_dir = '/4_Transfer_Exceptions/'

    hold_loc = working_dir + hold_dir
    test_loc = working_dir + test_dir
    del_loc = working_dir + del_dir
    err_loc = working_dir + except_dir

    os.makedirs(hold_loc)
    os.makedirs(test_loc)
    os.makedirs(del_loc)
    os.makedirs(err_loc)

B2 = tk.Button(root,text = "SetUp Folders", command = setup_folders)

B2.grid(column=1, row=2)


#3 zipper
def unzipper():
    import os
    import zipfile
    import shutil

    move_count = 0
    holding_duplicate = 0
    testing_duplicate = 0
    del_duplicate = 0
    except_duplicate = 0
    zip_error = 0

    for root, dirs, files in os.walk("./1_Holding_Folder/", topdown=True):
        for name in files:
            f_name = name[0:15]
            working_dir = os.getcwd() #this will change to the user selected directory in final
            hold_dir = '/1_Holding_Folder/'
            test_dir = '/2_Testing_Folder/'
            del_dir = '/3_To_Be_Deleted/'
            except_dir = '/4_Transfer_Exceptions/'

            hold_loc = working_dir + hold_dir
            test_loc = working_dir + test_dir
            del_loc = working_dir + del_dir
            err_loc = working_dir + except_dir

            hold_ext = working_dir + hold_dir + name
            test_ext = working_dir + test_dir + f_name
            err_ext = working_dir + except_dir + name
  
            if not os.path.exists(test_ext):  
                if not os.path.exists(err_ext):
                    if name.endswith(".zip"):
                        os.makedirs(test_ext)
                        try: # unzipping 
                            z_file = zipfile.ZipFile(hold_ext)
                            z_file.extractall(test_ext)
                        except:
                            
                            #add some sort of exception count here
                            top_zip = tk.Toplevel()
                            top_zip.geometry("300x300")
                            top_zip.title("Information Report")
                            top_zip= tk.Label(top_zip,text="zipping error encountered. Unable to unzip file {}.".format(name))
                            zip_error +=1
                            top_zip.grid()
                            continue
                                      
                        try: # moving zip file to the delete folder

                            shutil.move(hold_ext, del_loc)
                            move_count +=1
                        except:
                            
                            #add some sort of exception count here
                            top_zip = tk.Toplevel()
                            top_zip.geometry("300x300")
                            top_zip.title("Information Report")
                            top_zip= tk.Label(top_zip,text="Unable to move file {} to folder 3.".format(name))
                            del_duplicate +=1
                            top_zip.grid()
                            continue
                    else:
                        shutil.move(hold_ext, err_loc)
                        zip_error +=1
                        continue
                else:
                    except_duplicate +=1
                    continue

            else: # if file DOES already exist in test_ext
                shutil.move(hold_ext, err_loc)
                testing_duplicate +=1
                continue
                
            total_f = move_count + holding_duplicate + testing_duplicate + del_duplicate + except_duplicate + zip_error      
            
        top = tk.Toplevel()
        top.geometry("300x300")
        top.title("Information Report")
        top= tk.Label(top,text="Files moved sucessfully:  {mc}\n\
Testing folder duplicate encountered: {td}\
Non-zip files encountered: {ze}\n\
Exception folder duplicate encountered:  {ed}\n\
Delete folder duplicate encountered:  {dd}\n\
------------------------------------------\n\
Total files processed:  {tf}".format(mc=move_count,hd=holding_duplicate,td=testing_duplicate,dd=del_duplicate,ed=except_duplicate,ze=zip_error,tf=total_f))

        top.grid()
    
B3 = tk.Button(root,text = "Unzip Files", command = unzipper)

B3.grid(column=2, row=2)

#4 exceptions back to holding
def err_folder():
    import os
    import shutil

    move_count = 0
    holding_duplicate = 0
    testing_duplicate = 0
    del_duplicate = 0
    except_duplicate = 0
    zip_error = 0

    for root, dirs, files in os.walk("./4_Transfer_Exceptions/", topdown=True):
        for name in files:
            f_name = name[0:15]
            working_dir = os.getcwd() #this will change to the user selected directory in final
            hold_dir = '/1_Holding_Folder/'
            test_dir = '/2_Testing_Folder/'
            del_dir = '/3_To_Be_Deleted/'
            except_dir = '/4_Transfer_Exceptions/'

            hold_loc = working_dir + hold_dir
            test_loc = working_dir + test_dir
            del_loc = working_dir + del_dir
            err_loc = working_dir + except_dir

            hold_ext = working_dir + hold_dir + name
            test_ext = working_dir + test_dir + f_name
            err_ext = working_dir + except_dir + name


           # FINAL VERSION NEEDS TO DELETE ALL FILES IN THE DELETE FOLDER AND EXCEPTION FOLDER BEFORE STARTING 
            # Do we want to use regex to enable unzip otherwise send file to exception folder

            if not os.path.exists(test_ext):
                if not os.path.exists(hold_ext):
                    if name.endswith(".zip"):
                        #if r'(\D{2}.\W\D{2}.\w{2}.\d{2}: (eg. 22.S01.FIN.0001): else:err_ext

                        try: # moving zip file to the delete folder

                            shutil.move(err_ext, hold_loc)
                            move_count +=1
                        except:
                            top_zip = tk.Toplevel()
                            top_zip.geometry("300x300")
                            top_zip.title("Information Report")
                            top_zip= tk.Label(top_zip,text="Unable to move file {} to folder 1".format(name))
                            holding_duplicate +=1
                            top_zip.grid()
                            continue
                    else:
                        zip_error +=1
                        continue
                else:
                    holding_duplicate +=1
                    continue
            else:
                testing_duplicate +=1
                continue
        
        total_f = move_count + holding_duplicate + testing_duplicate + del_duplicate + except_duplicate + zip_error      
            
            
        top = tk.Toplevel()
        top.geometry("300x300")
        top.title("Information Report")
        top= tk.Label(top,text="Files moved successfully:  {mc}\n\
Holding folder duplciate encountered: {hd}\n\
Non-zip files encounterd: {ze}\n\
Exception folder duplicate encountered:  {ed}\n\
Duplicate files encountered encountered:  {td}\n\
-----------------------------------------------\n\
Total files processed:  {tf}".format(mc=move_count,hd=holding_duplicate,td=testing_duplicate,dd=del_duplicate,ed=except_duplicate,ze=zip_error,tf=total_f))

        top.grid()

B4 = tk.Button(root,text = "Reset Exception Folder", command = err_folder)

B4.grid(column=3, row=2)

root.mainloop()

# Known Error: if the same file is in the holding folder and any two other folders the program will not work.
# A single file will not show up in multiple places on the information report.
# As soon as a file triggers any single exception the program will move on to the next file
# even if that file could have triggered more than one exception.
