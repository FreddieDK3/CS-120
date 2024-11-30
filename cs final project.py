from random import randint
import json

reg = {
    "data": {
        "appointments": [
            {
                "booking_time": "2024-11-17 19:58:49",
                "doctor": "Dr. Smith",
                "id": 1,
                "patient": {
                    "email": "ckalenga@gsumail.gram.edu",
                    "name": "Chinyemba Kalenga"
                },
                "status": "scheduled",
                "time": "09:00"
            },
            {
                "booking_time": "2024-11-18 15:33:09",
                "doctor": "Dr. Smith",
                "id": 2,
                "patient": {
                    "email": "mali2@gsumail.gram.edu",
                    "name": "mr al"
                },
                "status": "scheduled",
                "time": "10:00"
            }
        ],
        "meta": {
            "timestamp": "2024-11-20T15:53:34.133126",
            "total": 2
        }
    },
    "status": "success"
}
dic = {"1":1,"2":1,"3":1}
sq = {"1":["Kalenga","UTH","Software Engineer"],"2":["Ali","UTH","Software Engineer"]}
#ppl = {}

def grant_access(x):
    if x == "1":
        file = open("insurance_payment_report.json","r")
        line = eval(file.read())
        print("Patient Details:")
        print(f"Patient ID: {line['Patient_ID']}")
        print(f"Patient Name: {line['Patient_Name']}")
        print(f"Doctor ID: {line['Doctor_ID']}")
        print(f"Doctor Name: {line['Doctor_Name']}")

        print("\nDiagnosis:")
        for diagnosis in line["Diagnosis"]:
            print(f"  - CPT Code: {diagnosis['CPT_Code']}")
            print(f"    CPT Description: {diagnosis['CPT_Description']}")
            print(f"    Condition Name: {diagnosis['Condition_Name']}")
            print(f"    ICD10 Code: {diagnosis['ICD10_Code']}")
            print(f"    ICD10 Description: {diagnosis['ICD10_Description']}")
            print(f"    Price: ${diagnosis['Price']:.2f}")

        print("\nPrescribed Drugs:")
        for drug in line["Prescribed_Drugs"]:
            print(f"  - {drug}")

        print("\nPayment Details:")
        for key, value in line["Payment_Details"].items():
            print(f"  {key}: ${value:.2f}")

        print("\nRejections:")
        for rejection in line["Rejections"]:
            print(f"  - {rejection}")
    
def diagnostics(id):
    if id == "1":
        print(reg[0][0][0][0:3])
    elif id == "2":
        print(reg[0][0][1][0:3])

def insuarance(id):
    file = open("eye_patient_info.csv","r")
    lines = file.splitlines()
    if id == "1":
        header = lines[0].split(",") 
        first_patient = lines[1].split(",")  
        print("First Patient Information:")
        for key, value in zip(header, first_patient):
            print(f"{key}: {value}")
    elif id == "2":
        header = lines[0].split(",") 
        first_patient = lines[2].split(",") 
        print("Second Patient Information:")
        for key, value in zip(header, second_patient):
            print(f"{key}: {value}")
    file.close()

def doctor(id):
    files = open("health_data.json","r")
    line = files.read()
    if id == "1":
        health_info = line[0]["health_data"]
        print("Health Data for the First Person:")
        for key, value in health_info.items():
            print(f"{key.replace('-', ' ').capitalize()}: {', '.join(value)}")
    elif id == "2":
        health_info_second =files[1]["health_data"]
        print("Health Data for the Second Person:")
        for key, value in health_info_second.items():
            print(f"{key.replace('-', ' ').capitalize()}: {', '.join(value)}")
    files.close()
    files.close()

def pharmacy(id):
    file = open("diagnosis_results.csv","r")
    lines = file.splitlines()
    reader = csv.DictReader(lines)
    first_patient = next(reader)

    if id == "1":
        first_patient = next(reader)
        print("Patient Info:")
        for key, value in first_patient.items():
            print(f"{key}: {value}")
    elif id == "2":
        next(reader)
        second_patient = next(reader)
        print("Patient Info:")
        for key, value in second_patient.items():
            print(f"{key}: {value}")
            health_info_second = data[1]["health_data"]
    file.close()
    
def send_email(mail,num):
    # Email sender and receiver details
    sender_email = "your_email@example.com"
    receiver_email = mail
    password = "your_email_password"

    # Create the email content
    subject = "OTP"
    body = num

    # Create a MIMEMultipart object
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the email body
    message.attach(MIMEText(body, "plain"))

    # Set up the server and send the email
    try:
        # Connect to the server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Use the appropriate SMTP server
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, password)  # Login to the email account
            server.sendmail(sender_email, receiver_email, message.as_string())  # Send the email

        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")    


a = input("x(E) or Paitient(P), or Create new user(new):\n")
if a == "E":
    # Open the JSON file and load its content
    with open("employee.json", "r") as file:
        line = json.load(file)  # Parse JSON into a Python object

    # Get user input
    user = input("Enter department Doctor(D), Pharmacy(P), Vitals(V), or Insurance(I):\n").strip().upper()
    id = input("Enter your ID:\n").strip()
    pw = input("Enter your password:\n").strip()

    # Check if the provided ID and password exist in the JSON data
    if any(employee.get("ID") == id and employee.get("Password") == pw for employee in line):
        # Check the department and call the appropriate function
        m = input("Enter Patient ID:\n").strip()
        if user == "D":
            doctor(m)
        elif user == "P":
            pharmacy(m)
        elif user == "I":
            insuarance(m)
        elif user == "V":
            diagnostics(m)
        else:
            print("Invalid department input.")
    else:
        print("Invalid ID or password.")

elif a == "P":
    id = input("Enter patient ID:\n")
    if id in dic:
        b = input("Security question(Q) or OTP(O):\n")
        if b == "Q":
            s = input("Mother's maiden name:\n")
            t = input("Hospital of birth:\n")
            u = input("Occupation:\n")
            if [s,t,u]==sq[id]:
                grant_access(id)
        elif b == "O":
                num = randint(1000,9999)
                if id == "1":
                    send_email(reg["data"]['appointments'][0]["patient"]["email"],num)
                elif id == "2":
                    send_email(reg["data"]['appointments'][1]["patient"]["email"],num)
                you = input("Enter OTP:\n")
                if str(num)==you:
                    grant_access(id)
                else:
                    print("Incorect.")
        else:
            print("Invalid input.")
    else:
        print("Invalid ID.")

elif a == "new":
    # Open the file and load the JSON data
    with open("employee.json", "r") as file:
        line = json.load(file)  # Parse JSON into a Python object (e.g., dict or list)

    # Get user input
    b = input("Doctor(D), Pharmacy(P), Vitals(V), Patient(T), or Insurance(I):\n").strip().upper()

    if b == "D":
        c = input("Enter ID:\n").strip()
        d = input("Enter password:\n").strip()

        # Check if the ID already exists in the data
        if any(employee.get("ID") == c for employee in line):
            print("ID already exists.")
        else:
            # Append the new ID and password as a dictionary
            line.append({"ID": c, "Password": d})
            print("New ID added successfully.")

            # Save the updated data back to the file
            with open("employee.json", "w") as file:
                json.dump(line, file, indent=4)
    elif b == "P":
        c = input("Enter ID:\n").strip()
        d = input("Enter password:\n").strip()

        # Check if the ID already exists in the data
        if any(employee.get("ID") == c for employee in line):
            print("ID already exists.")
        else:
            # Append the new ID and password as a dictionary
            line.append({"ID": c, "Password": d})
            print("New ID added successfully.")

            # Save the updated data back to the file
            with open("employee.json", "w") as file:
                json.dump(line, file, indent=4)
    elif b == "V":
        c = input("Enter ID:\n").strip()
        d = input("Enter password:\n").strip()

        # Check if the ID already exists in the data
        if any(employee.get("ID") == c for employee in line):
            print("ID already exists.")
        else:
            # Append the new ID and password as a dictionary
            line.append({"ID": c, "Password": d})
            print("New ID added successfully.")

            # Save the updated data back to the file
            with open("employee.json", "w") as file:
                json.dump(line, file, indent=4)
    elif b == "T":
        c = input("Enter ID:\n").strip()
        d = input("Enter password:\n").strip()

        # Check if the ID already exists in the data
        if any(employee.get("ID") == c for employee in line):
            print("ID already exists.")
        else:
            # Append the new ID and password as a dictionary
            line.append({"ID": c, "Password": d})
            print("New ID added successfully.")

            # Save the updated data back to the file
            with open("employee.json", "w") as file:
                json.dump(line, file, indent=4)
    elif b == "I":
        c = input("Enter ID:\n").strip()
        d = input("Enter password:\n").strip()

        # Check if the ID already exists in the data
        if any(employee.get("ID") == c for employee in line):
            print("ID already exists.")
        else:
            # Append the new ID and password as a dictionary
            line.append({"ID": c, "Password": d})
            print("New ID added successfully.")

            # Save the updated data back to the file
            with open("employee.json", "w") as file:
                json.dump(line, file, indent=4)
    file.close()
else:
    print("Invalid input.")
