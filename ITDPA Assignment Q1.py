import heapq

class Patient:
    def __init__(self, name, surname, id_number):
        self.name = name
        self.surname = surname
        self.id_number = id_number

    #Print
    def print_info(self):
        print(f"Patient Name: {self.name} {self.surname}, ID: {self.id_number}")


class Scheduler:
    def __init__(self):
        self.patients = []  #Priority queue for patient scheduling
        self.consultations = []  #Stores patient consultation details

    #Add
    def add_patient(self, patient, priority):
        heapq.heappush(self.patients, (-priority, patient))

    #Next
    def get_next_patient(self):
        #If there is a patient then return
        if self.patients:
            priority, patient = heapq.heappop(self.patients)
            return patient
        else:
            print("No patients in the schedule.")
            return None

    #Print
    def print_waiting_patients(self):
        #Only print if there are patients
        if not self.patients:
            print("No patients are waiting.")
        else:
            print("Patients waiting:")
            for priority, patient in sorted(self.patients, reverse=True):
                print(f"Priority {abs(priority)}: {patient.name} {patient.surname}")

    #Save file
    def save_consultation(self, patient, status):
        with open('consultations.txt', 'a') as file:
            file.write(f"Patient: {patient.name} {patient.surname}, ID: {patient.id_number}, Status: {status}\n")
        self.consultations.append((patient, status))

    #Read file
    def read_consultations(self):
        #Try except
        try:
            with open('consultations.txt', 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("No consultation records found.")

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    #Add
    def add(self, priority, patient):
        heapq.heappush(self.queue, (-priority, patient))

    #Return
    def pop(self):
        if self.queue:
            return heapq.heappop(self.queue)[1]
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    #Print
    def print_queue(self):
        #Only print if there are patients
        if self.queue:
            print("Patients waiting in queue:")
            for priority, patient in sorted(self.queue, reverse=True):
                print(f"{patient.name} {patient.surname} (Priority {abs(priority)})")
        else:
            print("No patients in the queue.")


def main_menu():
    scheduler = Scheduler()
    
    #Keep running until exit is selected
    while True:
        print("\n--- Emergency Room Scheduler ---")
        print("1. Add Patient")
        print("2. Get Next Patient")
        print("3. Print Waiting Patients")
        print("4. Save Consultation")
        print("5. View Consultation Records")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter patient's name: ")
            surname = input("Enter patient's surname: ")
            id_number = input("Enter patient's ID number: ")
            priority = int(input("Enter patient's priority level (1-5): "))

            patient = Patient(name, surname, id_number)

            scheduler.add_patient(patient, priority)
            print(f"Patient {name} {surname} added with priority {priority}.")
        
        elif choice == '2':
            next_patient = scheduler.get_next_patient()

            if next_patient:
                next_patient.print_info()
        
        elif choice == '3':
            scheduler.print_waiting_patients()
        
        elif choice == '4':
            patient_name = input("Enter patient's name for consultation: ")
            consultation_status = input("Enter consultation status: ")
            
            patient = Patient(patient_name, "qwerty", "0000")  #Placeholder

            scheduler.save_consultation(patient, consultation_status)
            print("Saved.")
        
        elif choice == '5':
            scheduler.read_consultations()
        
        elif choice == '6':
            print("Have a great day. Goodbye.")
            break
        
        else:
            print("Invalid choice. Try again.")

#Main menu
if __name__ == "__main__":
    main_menu()

