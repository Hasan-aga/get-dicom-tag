## intro
some series are medical scans that include more than one body part, we need to find if there is a metadata tag that identifies such series.

## analysis
there is a tag that seems to do what we want:
```
Body Part Examined Attribute
Tag	(0018,0015)
Type	Optional (3)
Keyword	BodyPartExamined
Value Multiplicity	1
Value Representation	Code String (CS)
Example Values	
BREAST
ABDOMEN
CHEST
```

## plan
we could use dicom validator `dcmvalidate` to scan for this tag across out dataset.
we will need an iod to scan against.

## implementation
using this command:
```
./dcmvalidate --iod ~/work/body-analysis/dicomdir-iod.xml ~/work/body-analysis/OneDrive_1_7-24-2023/HA-1056/
```
we can test for the existing of our tag, we use this iod:
```
<?xml version="1.0" encoding="UTF-8"?>
<IOD xml-space="preserved">
  <DataElement keyword="BodyPartExamined" tag="00180015" vr="CS" type="3" vm="1"/>
</IOD>
```
## resutls
1.	HA-1097/20760 -> ok: KRANIUM
2. HA-882/390/390/ -> ok: NORO_BA_BOYUN
3. HA-1056/18738/1.2.752.24.7.1180089009.21927124/ADC_1.2.840.9999.123068363843992055865827148931819878862/ -> ok: KRANIYM
4. HA-1056/18739/1.2.752.24.7.1180089009.21927124/ADC_1.2.840.9999.123068363843992055865827148931819878862 -> ok: kranium
5. HA-1109/21387/RAW -> ok: brain
6.