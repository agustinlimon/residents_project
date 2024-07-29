from residents_app.models import Resident, Building, Contract
from django.core.management.base import BaseCommand
import pandas as pd

#! Command to populate the database with the data from the Excel file
class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        # Read the Excel file
        file_path = './residents_import.xlsx'
        excel_data = pd.ExcelFile(file_path)
        
        # Populate the Resident table
        residents_data = excel_data.parse('Resident table')
        for _, row in residents_data.iterrows():
            Resident.objects.create(
                tenantid=row['tenantid'],
                resident_fname=row['resident_fname'],
                resident_lname=row['resident_lname'],
                resident_program=row['resident_program'],
                last_effective_action=row['last_effective_action'],
                last_effective_date=row['last_effective_date'],
                resident_phonenumber=row['resident_phonenumber'],
                resident_email=row['resident_email'],
                resident_address=row['resident_address'],
                resident_status=row['resident_status'],
                unitid=row['unitid'],
                resident_amp=row['resident_amp']
            )

        # Populate the Contract table
        contracts_data = excel_data.parse('Contracts table')
        for _, row in contracts_data.iterrows():
            Contract.objects.create(
                contractid=row['contractid'],
                contract_effectivedate=row['contract_effectivedate'],
                contract_type=row['contract_type'],
                contract_address=row['contract_address'],
                tenantid=row['tenantid'],
                contract_status=row['contract_status'],
                contract_phone_number=row.get('contract_phone_number'),
                contract_email=row['contract_email'],
                contract_amp=row.get('contract_amp'),
                contract_last_recert=row['contract_last_recert'],
                contract_packet_sent=row['contract_packet_sent'],
                contract_packet_received=row['contract_packet_received'],
                contract_rent_det_letter_sent=row['contract_rent_det_letter_sent'],
                contract_unit=row['contract_unit'],
                contract_building=row['contract_building'],
                contract_program=row['contract_program'],
                contract_rent=row['contract_rent'],
                contract_process_status=row['contract_process_status']
            )

        # Populate the Building table
        buildings_data = excel_data.parse('buildings table')
        for _, row in buildings_data.iterrows():
            Building.objects.create(
                buildingid=row['buildingid'],
                housingid=row['housingid'],
                number_of_units=row['number_of_units'],
                building_name=row['building_name'],
                building_address=row['building_address'],
                ampid=row['ampid']
            )
