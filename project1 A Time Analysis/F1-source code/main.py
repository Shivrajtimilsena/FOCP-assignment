import os
import argparse
from tabulate import tabulate

# ============================
# Tabulate Functions Section
# ============================

def generate_race_info_table(location, overall_average, fastest_driver_info, fastest_time): #generate table  that contains location overall average fastestdriver info fastest time.
    headers = ["Race Location", "Overall Average Lap Time", "Fastest Driver", "Fastest Lap Time"]
    table = [
        [location, f"{overall_average:.3f}s", f"{fastest_driver_info['name']} ({fastest_driver_info['team']})", f"{fastest_time:.3f}s"]
    ]
    return tabulate(table, headers=headers, tablefmt="heavy_grid") #return the table as astring in table format

def generate_results_f1_table(drivers, results):
    headers = ["Driver Code", "Name", "Team", "Fastest Lap", "Average Lap"]
    table = []

    sorted_results = sorted(                  #sort the result based on the fastest lap time in descending order
         results.items(),    
         key=lambda x: x[1]['fastest'],
         reverse=True
    ) 
    #   upload driver dta to the table 
    for code, stats in sorted_results:
        driver_info = drivers.get(code, {"name": "Unknown", "team": "Unknown"}) #get drivers details from the disctionaly call drivers using driver code
        table.append([ 
            code,   #driver code
            driver_info['name'],  #driver real namae
            driver_info['team'],  #drivers team name
            f"{stats['fastest']:.3f}",  #fastest lap times formatted to 3 decimals
            f"{stats['average']:.3f}"   #average lap times formatted to 3 decimals
        ])

    return tabulate(table, headers=headers, tablefmt="heavy_grid")  #return the table as a string

# ============================
# File Handling Functions
# ============================

def read_drivers(file_path): #read the drivers file and return
    drivers = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    code = parts[1]
                    name = parts[2]
                    team = parts[3]
                    drivers[code] = {"name": name, "team": team}
    except Exception as e:
        print(f"Error reading drivers file: {e}")
        exit(1)  # Exit if the drivers file can't be read
    return drivers

def load_lap_data(file_path):     #read lap file and return the race location and a dictionary of laptime for each drivers.
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            location = lines[0].strip()     #the first line is the race location
            lap_times = {}
            for line in lines[1:]: #skip the first line (race location)
                code = line[:3]    # extract the driver cde (first 3 letters)
                try:
                    time = float(line[3:].strip())    #sort the result based on the fastest lap time in descending order
                except ValueError:
                    print(f"Skipping invalid lap time: {line.strip()}")   #skip any invalid lap times or invalid data in lap files.
                    continue
                if code not in lap_times:
                    lap_times[code] = []            #Create an entry for the driver if not already present
                lap_times[code].append(time)        #Append the lap times to the driver's list
            return location, lap_times
    except Exception as e:
        print(f"Error reading lap times file: {e}")
        exit(1)        #Exit if the lap times file cannot be read

def analyze_times(lap_times):  #analyzie the lap times for each drivers and return the result including the fastest lap and average lap time. also return the fastest driver and the overall average lap time.
    results = {}                
    overall_times = []             #list for overall times to calculate th overall average
    fastest_time = float('inf')    #start with an extremely high fastest time.
    fastest_driver = None          #variable to store the fastest driver code
    
    for driver, times in lap_times.items():    #Check if this drivers has the fastest lap so far.
        fastest = min(times)  
        average = sum(times) / len(times)  
        results[driver] = {"fastest": fastest, "average": average}
        overall_times.extend(times)  
        
        if fastest < fastest_time:
            fastest_time = fastest
            fastest_driver = driver

    overall_average = sum(overall_times) / len(overall_times)        #Calculate the verall average lap time.
    return results, overall_average, fastest_driver, fastest_time

# ============================
# Terminal-Based Workflow
# ============================

def main():
    """
    The main function to parse command line arguments, read data files, analyzie lap time. and display results.
    """
    parser = argparse.ArgumentParser(description="F1 Timing Analysis")   #Parse command line arguments
    parser.add_argument("lap_files", help="Paths to the lap times files (e.g., 'lap_times_race1.txt')", nargs='+')
    args = parser.parse_args()

    lap_files = args.lap_files

    if not lap_files:
        print("Error: No lap times files provided.")  
        return
    
    #automatically read drivers files
    drivers_file = "f1_drivers.txt"        # Path to the drivers file
    if not os.path.exists(drivers_file):
        print("Error: Drivers file not found.")  #check if the drivers file exits
        return

    drivers = read_drivers(drivers_file)  #read the drivers data

    overall_results = {}
    combined_lap_times = []

    for lap_file in lap_files:
        if not os.path.exists(lap_file):
            print(f"Error: Lap times file '{lap_file}' not found.")  
            continue

        location, lap_times = load_lap_data(lap_file)     #parse the lap times file
        
        #analyze the lp time to calculate the fastest and average alp times.
        results, overall_average, fastest_driver, fastest_time = analyze_times(lap_times)

        print(f"Processing File: {lap_file}")
        
        #display race information in tabular format
        fastest_driver_info = drivers.get(fastest_driver, {"name": "Unknown", "team": "Unknown"})
        print("\n-------------------------------- Race Information -----------------------------------")
        print(generate_race_info_table(location, overall_average, fastest_driver_info, fastest_time))

        #Generate and display the result table (sort by fastest lap in descending order)
        print("\n--------------- Results (Fastest & Average Laps in Descending Order): ---------------")
        print(generate_results_f1_table(drivers, results))

        overall_results.update(results)
        combined_lap_times.extend([time for times in lap_times.values() for time in times])

    if combined_lap_times:
        combined_overall_average = sum(combined_lap_times) / len(combined_lap_times)
        print(f"\nThe overall average lap time across all files is {combined_overall_average:.3f}s")
    else:
        print("\nNo lap times found across files.")

if __name__ == "__main__":
    main()    #Run the main function when the script is executed
