# Step 2: The Counter
attack_count = 0

# Step 3: Opening two files at once
with open("auth_audit.log", "r") as log_file:
    with open("brute_report.txt", "w") as report_file:
        
        # Step 4: The Loop (The Conveyor Belt)
        for line in log_file:
            
            # Step 5: The Signature Search
            if "Failed password" in line:
                
                # Step 6: Save the finding to your report
                report_file.write(line)
                
                # Step 7: Increment the counter
                attack_count += 1

# Final Step: Print the summary
print(f"Audit Complete. Found {attack_count} failed login attempts.")
