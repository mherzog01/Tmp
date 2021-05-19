import glob
import os

targ_root = r'C:\Tmp\Work3'

while True:
    lot_number = input("Enter lot number: ")
    lot_number = lot_number.strip().upper()
    if lot_number[:2] != 'RH':
        print(f'Lot number {lot_number} does not begin with RH')
        continue
    if len(lot_number) != 8:
        print(f'Lot number {lot_number} must be 8 characters long')
        continue
    if not lot_number[2:].isnumeric():
        print(f'Last characters of lot number {lot_number} must be numeric')
        continue
    
    targ_dir = os.path.join(targ_root,lot_number)
    if os.path.exists(targ_dir):
        ans = input(f'The folder {targ_dir} already exists.  Move files anyway? y/n: ')
        if ans.strip().lower() != 'y':
            continue
    else:
        print(f'Created new folder {targ_dir}')
        os.mkdir(targ_dir)
        
    files_to_move = [o for o in glob.glob(os.path.join(targ_root,'*')) if os.path.isfile(o)]
    print(f'Found {len(files_to_move)} files')
    
    for cur_file in files_to_move:
        cur_basename = os.path.basename(cur_file)

        # Parse date from file and use only a cleaned up version of that
        # Assume original format is xxxxxxxxxxxxxxxxxxxxxxxxxxxx
        new_basename = cur_basename


        new_file = os.path.join(targ_dir,new_basename)
        print(f'Moving {cur_file} to {new_file}')
        os.rename(cur_file,new_file)
        
    print('Process complete')
    print