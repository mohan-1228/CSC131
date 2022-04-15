

class BMI:
    

    def __init__(self, name="UNKNOWN", gender="UNKNOWN", dob="UNKNOWN", ppsn="TESTING", weight=0.0, height=0.0):
        """Setting class attributes."""
        self.Name = name
        self.gender = gender
        self.dob = dob
        self.ppsn = ppsn
        self.weight = weight
        self.height = height

    def bmi(self):
        """creating method to calculate body mass index, returns float
        BMI= weight(kg) / ( height(m)*height(m) )
        Example:
        >>> Patient(weight=75, height=1.7).calculate_bmi()
        25.95155709342561
        """

        return float(self.weight / (self.height * self.height))

    def status(self):
        """Analyse the patient's BMI:
        < 16 underweight, < 25 healthy, < 30 overweight, 30+ obese
        >>> Patient(height=1.83, weight=89).bmi_analysis()
        'overweight'
        """
        bmi = self.bmi()
        if bmi < 16:
            Status = "underweight"
        elif bmi < 25:
            Status = "healthy"
        elif bmi < 30:
            Status = "overweight"
        else:
            Ststus = "obese"
        return Status

    def generate_report(self):
        """"Creating method to generate report to file containing patient details and BMI results."""
        report_file = open(self.ppsn, "w")
        print("PATIENT REPORT", file=report_file)
        print("-" * 30, "\n", file=report_file)
        print("Patient name:\t", self.name, file=report_file)
        print("Patient gender:\t", self.gender, file=report_file)
        print("Patient dob: \t", self.dob, file=report_file)
        print("Patient PPSN:\t", self.ppsn, file=report_file)
        print("Patient weight:\t", self.weight, "kg", file=report_file)
        print("Patient height:\t", self.height, "m", file=report_file)
        print("Patient BMI: \t", round(self.bmi(), 1), file=report_file)
        print("BMI Analysis: \t", self.Status(), file=report_file)
        report_file.close()



from BMI import BMI

def main():
    bmi1=BMI("John Doe",18,145,70)
    print("The BMI for ",bmi1.get_Name(), " is ",bmi1.get_BMI(),bmi1.get_Status())
    bmi2=BMI("Sue Doe",19,103,68)
    print("The BMI for ",bmi2.get_Name(), " is ",bmi2.get_BMI(),bmi2.get_Status())
    bmi3=BMI("Pete Doe",50,217,70)
    print("The BMI for ",bmi3.get_Name(), " is ",bmi3.get_BMI(),bmi3.get_Status())
 
main()
