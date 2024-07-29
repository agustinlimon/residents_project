from django.db import models

class Resident(models.Model):
    tenantid = models.CharField(max_length=20)
    resident_fname = models.CharField(max_length=100)
    resident_lname = models.CharField(max_length=100)
    resident_program = models.CharField(max_length=100)
    last_effective_action = models.IntegerField()
    last_effective_date = models.CharField(max_length=100)
    resident_phonenumber = models.CharField(max_length=15)
    resident_email = models.EmailField()
    resident_address = models.TextField()
    resident_status = models.CharField(max_length=20)
    unitid = models.CharField(max_length=20)
    resident_amp = models.IntegerField()

    def __str__(self):
        return f"{self.resident_fname} {self.resident_lname}"

class Contract(models.Model):
    contractid = models.IntegerField()
    contract_effectivedate = models.CharField(max_length=100)
    contract_type = models.CharField(max_length=100)
    contract_address = models.TextField()
    tenantid = models.CharField(max_length=20)
    contract_status = models.CharField(max_length=100)
    contract_phone_number = models.CharField(max_length=15, null=True, blank=True)
    contract_email = models.EmailField()
    contract_amp = models.IntegerField(null=True, blank=True)
    contract_last_recert = models.CharField(max_length=100)
    contract_packet_sent = models.CharField(max_length=100)
    contract_packet_received = models.CharField(max_length=100)
    contract_rent_det_letter_sent = models.CharField(max_length=100)
    contract_unit = models.IntegerField()
    contract_building = models.IntegerField()
    contract_program = models.CharField(max_length=100)
    contract_rent = models.DecimalField(max_digits=10, decimal_places=2)
    contract_process_status = models.CharField(max_length=100)

    def __str__(self):
        return f"Contract {self.contractid}"

class Building(models.Model):
    buildingid = models.IntegerField()
    housingid = models.IntegerField()
    number_of_units = models.IntegerField()
    building_name = models.CharField(max_length=100)
    building_address = models.TextField()
    ampid = models.IntegerField()

    def __str__(self):
        return self.building_name
