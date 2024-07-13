from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('govstack_api', '0004_seeds'),
    ]

    operations = [
        migrations.RunSQL(
            """
            INSERT INTO "tblInsuree" (
                "InsureeID", "AuditUserID", "CHFID", "CardIssued", "CurrentAddress", "CurrentVillage", "DOB",
                "Education", "Email", "FamilyID", "Gender", "GeoLocation", "HFID", "InsureeUUID", "IsHead",
                "LastName", "LegacyID", "Marital", "OtherNames", "Phone", "PhotoDate", "PhotoID",
                "Profession", "Relationship", "RowID", "TypeOfId", "ValidityFrom", "ValidityTo",
                "Vulnerability", "isOffline", "passport", "Source", "SourceVersion", "JsonExt"
            ) VALUES
            (147, 1, '070707055', false, '900', null, '2005-10-16', null, '', 1, 'F', '0.0 0.0', null,
             '4d908777-50ff-44c3-81f2-48f27517c799', false, 'TPA', null, null, 'Targeted Poverty Alleviation', 'package',
             '2018-03-27', 271, null, 7, null, null, '2018-03-27 06:43:32.393000 +00:00', null, null, false, '', null, null, null),
            (148, 1, '070707055', false, '1234.5', null, '2005-10-16', null, '', 1, 'F', '0.0 0.0', null,
             '4d908777-50ff-44c3-81f2-48f27517c788', false, 'UBI', null, null, 'Universal basic income', 'package',
             '2018-03-27', 271, null, 7, null, null, '2018-03-27 06:43:32.393000 +00:00', null, null, false, '', null, null, null),
            (149, 1, '070707055', false, '750', null, '2005-10-16', null, '', 1, 'F', '0.0 0.0', null,
             '4d908777-50ff-44c3-81f2-48f27517c777', false, 'SP', null, null, 'Social pension', 'package',
             '2018-03-27', 271, null, 7, null, null, '2018-03-27 06:43:32.393000 +00:00', null, null, false, '', null, null, null),
            (150, 1, '070707055', false, '500', null, '2005-10-16', null, '', 1, 'F', '0.0 0.0', null,
             '4d908777-50ff-44c3-81f2-48f27517c766', false, 'CFS', null, null, 'Child and Family support', 'package',
             '2018-03-27', 271, null, 7, null, null, '2018-03-27 06:43:32.393000 +00:00', null, null, false, '', null, null, null);
            """,
            reverse_sql="""
            DELETE FROM "tblInsuree" WHERE "InsureeID" IN (147, 148, 149, 150);
            """
        ),
    ]