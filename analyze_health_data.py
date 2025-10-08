#!/usr/bin/env python3

"""
Health Sensor Data Analysis Script

Complete the TODO sections to analyze health sensor data using NumPy.
This script demonstrates basic NumPy operations for data loading, statistics,
filtering, and report generation.
"""

import numpy as np


def load_data(filename):
    """Load CSV data using NumPy.
    
    Args:
        filename: Path to CSV file
        
    Returns:
        NumPy structured array with all columns
    """
    # This code is provided because np.genfromtxt() is not covered in the lecture
    dtype = [('patient_id', 'U10'), ('timestamp', 'U20'), 
             ('heart_rate', 'i4'), ('blood_pressure_systolic', 'i4'),
             ('blood_pressure_diastolic', 'i4'), ('temperature', 'f4'),
             ('glucose_level', 'i4'), ('sensor_id', 'U10')]
    
    data = np.genfromtxt(filename, delimiter=',', dtype=dtype, skip_header=1)
    return data


def calculate_statistics(data):
    """Calculate basic statistics for numeric columns.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with statistics
    """
    # TODO: Calculate average heart rate using data['heart_rate'].mean()
    # TODO: Calculate average systolic BP using data['blood_pressure_systolic'].mean()
    # TODO: Calculate average glucose level using data['glucose_level'].mean()
    # TODO: Return as dictionary with keys: 'avg_heart_rate', 'avg_systolic_bp', 'avg_glucose'
    avg_hr_rate = data['heart_rate'].mean()
    avg_sys_bp = data['blood_pressure_systolic'].mean()
    avg_glu_lvl = data['glucose_level'].mean()
    return {
        "avg_hr_rate" : f'{avg_hr_rate:.1f}',
        "avg_sys_bp" : f'{avg_sys_bp:.1f}',
        "avg_glu_lvl" : f'{avg_glu_lvl:.1f}'
    }


def find_abnormal_readings(data):
    """Find readings with abnormal values.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with counts
    """
    # TODO: Count readings where heart rate > 90 using boolean indexing
    # Example: high_hr_count = len(data[data['heart_rate'] > 90])
    # Or: high_hr_count = (data['heart_rate'] > 90).sum()
    
    # TODO: Count readings where systolic BP > 130 using boolean indexing
    # Example: high_bp_count = len(data[data['blood_pressure_systolic'] > 130])
    
    # TODO: Count readings where glucose > 110 using boolean indexing
    # Example: high_glucose_count = len(data[data['glucose_level'] > 110])
    
    # TODO: Return dictionary with keys: 'high_heart_rate', 'high_blood_pressure', 'high_glucose'
    high_hr_count = len(data[data['heart_rate'] > 90])
    high_bp_count = len(data[data['blood_pressure_systolic'] > 130])
    high_glucose_count = len(data[data['glucose_level'] > 110])
    return {
        "high_hr_count":high_hr_count,
        "high_bp_count":high_bp_count,
        "high_glucose_count":high_glucose_count
    }
                        


def generate_report(stats, abnormal, total_readings):
    """Generate formatted analysis report.
    
    Args:
        stats: Dictionary of statistics
        abnormal: Dictionary of abnormal counts
        total_readings: Total number of readings
        
    Returns:
        Formatted string report
    """
    # TODO: Create a formatted report string using f-strings
    # TODO: Include all statistics with proper formatting using .1f for decimals
    # Example: f"Heart Rate: {stats['avg_heart_rate']:.1f} bpm"
    # TODO: Include section headers and labels for readability
    # TODO: Include total_readings, all averages, and all abnormal counts
    report = (
        f'Health Sensor Data Analysis Report\n'
        f'_____________________________________\n'
        f'Dataset Summary:\n'
        f'- Total readings:{total_readings} \n'
        f'Average Measurements:\n'
        f'- Systolic Blood Pressure: {stats['avg_sys_bp']} \n'
        f'- Heart Rate: {stats['avg_hr_rate']} \n'
        f'- Glucose Level: {stats['avg_glu_lvl']} \n'
        f'Abnormal Readings:\n'
        f'- Heart Rate > 90 : {abnormal['high_hr_count']}\n'
        f'- Systolic BP >130 : {abnormal['high_bp_count']}\n'
        f'- Glucose > 110 : {abnormal['high_glucose_count']}\n'
    )
    return report

def save_report(report, filename):
    """Save report to file.
    
    Args:
        report: Report string
        filename: Output filename
    """
    # TODO: Write the report to a file using open() with 'w' mode
    # Example: with open(filename, 'w') as f:
    #              f.write(report)
    with open(filename, 'w') as f:
        f.write(report)


def main():
    """Main execution function."""
    # TODO: Load the data from 'health_data.csv' using load_data()
    # TODO: Calculate statistics using calculate_statistics()
    # TODO: Find abnormal readings using find_abnormal_readings()
    # TODO: Calculate total readings using len(data)
    # TODO: Generate report using generate_report()
    # TODO: Save to 'output/analysis_report.txt' using save_report()
    # TODO: Print success message
    data = load_data('health_data.csv')
    stats = calculate_statistics(data)
    abnormal = find_abnormal_readings(data)
    total_read = len(data)
    report = generate_report(stats,abnormal,total_read)
    save_report(report,'output/analysis_report.txt')
    print("Sucess! report saved to output")


if __name__ == "__main__":
    main()