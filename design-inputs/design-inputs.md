# Rough Basic Requirements
    - User Management
        - Admin
        - Doctor
        - Pharmacist

    - Patient
        - Personal Details
        - Consultation History
        - Prescription History
        - Treatment History
        - Vitals Timeline (Weight, Height, Pressure etc)
        - Discharge Summary

   - Billing

   - Inventory
     - Clinic Inventory
          - Medicinies
          - Non Medical
   
     - Kitchen Inventory

   - Human Resource Management
     - Payroll Management
     - Leave Management
     
   - Reminders
     - Utility Bills
         - Electricity
         - Water
         - Waste
         - Internet
         - Cable TV
         - Cooking Gas
         - License renewal
         - Rent

   - Expense Tracker

   - PR


# User Flow
    - /admin
    - /ayuh/home
        - /ayuh/admin [admin]
          - /ayuh/admin/staff
            - /ayuh/admin/staff/list
            - /ayuh/admin/staff/create
            - /ayuh/admin/staff/{staff-id}/update
            - /ayuh/admin/staff/{staff-id}/delete
            - /ayuh/admin/staff/{staff-id}/document?type=[experience|offer]
            - /ayuh/admin/staff/{staff-id}/holiday/overview
            - /ayuh/admin/staff/{staff-id}/holiday/create
            - /ayuh/admin/staff/{staff-id}/holiday/update
            - /ayuh/admin/staff/{staff-id}/holiday/delete
            - /ayuh/admin/staff/{staff-id}/salary-slip/create
            - /ayuh/admin/staff/{staff-id}/salary-slip/{slip-id}/update
            - /ayuh/admin/staff/{staff-id}/salary-slip/{slip-id}/delete
          - /ayuh/admin/to-do-list
            - /ayuh/admin/to-do-list/list
            - /ayuh/admin/to-do-list/create
            - /ayuh/admin/to-do-list/{item-id}/update
            - /ayuh/admin/to-do-list/{item-id}/delete
          - /ayuh/admin/expense-tracker
        - /ayuh/patient
          - /ayuh/patient/add
          - /ayuh/patient/{patient-id}/update
          - /ayuh/patient/{patient-id}/vitals/list
          - /ayuh/patient/{patient-id}/vitals/add
          - /ayuh/patient/{patient-id}/vitals/{observation-id}/update
          - /ayuh/patient/{patient-id}/consultation-history
          - /ayuh/patient/{patient-id}/treatment-history
          - /ayuh/patient/{patient-id}/prescription-history
          - /ayuh/patient/{patient-id}/feedback-history
        - /ayuh/consultation
          - /ayuh/consultation/list
          - /ayuh/consultation/add
          - /ayuh/consultation/{consultation-id}/update
          - /ayuh/consultation/{consultation-id}/delete
          - /ayuh/consultation/{consultation-id}/prescriptions
          - /ayuh/consultation/{consultation-id}/bill
          - /ayuh/consultation/{consultation-id}/feedback
        - /ayuh/admission
          - /ayuh/admission/list
          - /ayuh/admission/add
          - /ayuh/admission/{admission-id}/update
          - /ayuh/admission/{admission-id}/delete
          - /ayuh/admission/{admission-id}/treatments
          - /ayuh/admission/{admission-id}/bill
          - /ayuh/admission/{admission-id}/discharge-summary
          - /ayuh/admission/{admission-id}/feedback
        - /ayuh/inventory
          - /ayuh/inventory/clinical
            - /ayuh/inventory/clinical/list
            - /ayuh/inventory/clinical/create
            - /ayuh/inventory/clinical/{inventory-id}/update
          - /ayuh/inventory/non-clinical
            - /ayuh/inventory/non-clinical/list
            - /ayuh/inventory/non-clinical/create
            - /ayuh/inventory/non-clinical/{inventory-id}/update
   