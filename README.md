# Wayfair-to-Fishbowl-CSV-Converter
Program that converts Wayfair CSV order files into a single CSV file that can be imported as Sales Orders in Fishbowl Inventory

Fishbowl Inventory can be a little finicky regarding the formatting of csv files for import, and I hope this script can save
some other Fishbowl users headaches!

Note: You will need to set up a WayfairIn and a FishbowlOut folder in the directory where you plan to run this program. 

The program will read all .csv files in the WayfairIn directory and write them to a single new .csv file in the FishbowlOut 
directory. The program then clears all of the files from the WayfairIn directory to avoid duplication later. 

You now have a .csv file in the FishbowlOut directory that can be easily imported using Fishbowl Inventory's native import
feature!

Note that this script will format the import .csv for both regular inventory items an Kit items, however due to limitation 
in how Fishbowl Inventory handles the import of Kit Item data off of a .csv file, some additional manual work may need to be done to make sure that the Kit items populate correctly on the Fishbowl Sales Order and include their component parts. 
