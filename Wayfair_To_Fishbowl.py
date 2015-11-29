#! Python 2.7

import csv
import os
from os import listdir
import os.path

Path = os.getcwd()
Filenames = listdir(os.path.join(Path, 'WayfairIn/'))

with open(os.path.join(Path, 'FishbowlOut/SalesOrder_Wayfair.csv'), 'wb') as o:
    writer = csv.writer(o, delimiter=',', dialect=csv.excel)

    for orders in Filenames:
        if not orders.endswith('.csv'):
            continue
        else:
            with open(os.path.join(Path, 'WayfairIn/', orders), 'U') as i:
                reader = csv.reader(i, delimiter='|')

                Kit = ['List the FishBowl part numbers of your Kits here']

                for row in reader:
                    if row[0] == 'IH':
                        SONum = row[1]
                        ShipToName = row[3]
                        ShipToAddress = row[4]
                        ShipToCity = row[6]
                        ShipToState = row[7]
                        ShipToZip = row[8]
                        Date = row[2]
                        writer.writerow(['SO', SONum, '20', 'Wayfair - eCommerce', 'Wayfair - eCommerce', 'Attn:Accounts Payable',
                                        '177 Huntington Avenue, Suite 6000', 'Boston', 'MA', '02115', 'UNITED STATES', ShipToName,
                                        ShipToAddress, ShipToCity, ShipToState, ShipToZip, 'UNITED STATES', 'FedEx', 'NONE',
                                        '30', '', '', Date, 'admin', 'Prepaid & Billed', 'Net 30', 'Origin', '', 'None', 'Main'])

                    elif row[0] == 'ID':
                        ProductNumber = row[1]
                        ProductQuantity = row[2]
                        ProductPrice = row[3]
                        Note = row[6]
                        if ProductNumber in Kit:
                            writer.writerow(['Item', '80', ProductNumber, ProductQuantity, 'ea', ProductPrice, 'FALSE', Note,
                                            '', '', 'FALSE', 'TRUE'])
                        else:
                            writer.writerow(['Item', '10', ProductNumber, ProductQuantity, 'ea', ProductPrice, 'FALSE', Note,
                                            '', '', 'FALSE', 'FALSE'])

to_be_deleted = os.path.join(Path, 'WayfairIn/')
filelist = os.listdir(to_be_deleted)
for filename in filelist:
    os.remove(to_be_deleted + "/" + filename)