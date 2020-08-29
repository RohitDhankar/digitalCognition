# Generated by Django 2.2.6 on 2019-10-21 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='csv_document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='_DataBaseFile_')),
                ('csv_file_name', models.CharField(blank=True, max_length=255)),
                ('dataset_name', models.CharField(blank=True, max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('unq_id_nameField', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='data_table_10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField()),
                ('f2', models.TextField()),
                ('f3', models.TextField()),
                ('f4', models.TextField()),
                ('f5', models.TextField()),
                ('f6', models.TextField()),
                ('f7', models.TextField()),
                ('f8', models.TextField()),
                ('f9', models.TextField()),
                ('f10', models.TextField()),
                ('f11', models.TextField()),
                ('f12', models.TextField()),
                ('f13', models.TextField()),
                ('f14', models.TextField()),
                ('f15', models.TextField()),
                ('f16', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='data_table_11',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField()),
                ('f2', models.TextField()),
                ('f3', models.TextField()),
                ('f4', models.TextField()),
                ('f5', models.TextField()),
                ('f6', models.TextField()),
                ('f7', models.TextField()),
                ('f8', models.TextField()),
                ('f9', models.TextField()),
                ('f10', models.TextField()),
                ('f11', models.TextField()),
                ('f12', models.TextField()),
                ('f13', models.TextField()),
                ('f14', models.TextField()),
                ('f15', models.TextField()),
                ('f16', models.TextField()),
                ('f17', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='data_table_12',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField()),
                ('f2', models.TextField()),
                ('f3', models.TextField()),
                ('f4', models.TextField()),
                ('f5', models.TextField()),
                ('f6', models.TextField()),
                ('f7', models.TextField()),
                ('f8', models.TextField()),
                ('f9', models.TextField()),
                ('f10', models.TextField()),
                ('f11', models.TextField()),
                ('f12', models.TextField()),
                ('f13', models.TextField()),
                ('f14', models.TextField()),
                ('f15', models.TextField()),
                ('f16', models.TextField()),
                ('f17', models.TextField()),
                ('f18', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='data_table_13',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField()),
                ('f2', models.TextField()),
                ('f3', models.TextField()),
                ('f4', models.TextField()),
                ('f5', models.TextField()),
                ('f6', models.TextField()),
                ('f7', models.TextField()),
                ('f8', models.TextField()),
                ('f9', models.TextField()),
                ('f10', models.TextField()),
                ('f11', models.TextField()),
                ('f12', models.TextField()),
                ('f13', models.TextField()),
                ('f14', models.TextField()),
                ('f15', models.TextField()),
                ('f16', models.TextField()),
                ('f17', models.TextField()),
                ('f18', models.TextField()),
                ('f19', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='data_table_14',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField()),
                ('f2', models.TextField()),
                ('f3', models.TextField()),
                ('f4', models.TextField()),
                ('f5', models.TextField()),
                ('f6', models.TextField()),
                ('f7', models.TextField()),
                ('f8', models.TextField()),
                ('f9', models.TextField()),
                ('f10', models.TextField()),
                ('f11', models.TextField()),
                ('f12', models.TextField()),
                ('f13', models.TextField()),
                ('f14', models.TextField()),
                ('f15', models.TextField()),
                ('f16', models.TextField()),
                ('f17', models.TextField()),
                ('f18', models.TextField()),
                ('f19', models.TextField()),
                ('f20', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='data_table_15',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField()),
                ('f2', models.TextField()),
                ('f3', models.TextField()),
                ('f4', models.TextField()),
                ('f5', models.TextField()),
                ('f6', models.TextField()),
                ('f7', models.TextField()),
                ('f8', models.TextField()),
                ('f9', models.TextField()),
                ('f10', models.TextField()),
                ('f11', models.TextField()),
                ('f12', models.TextField()),
                ('f13', models.TextField()),
                ('f14', models.TextField()),
                ('f15', models.TextField()),
                ('f16', models.TextField()),
                ('f17', models.TextField()),
                ('f18', models.TextField()),
                ('f19', models.TextField()),
                ('f20', models.TextField()),
                ('f21', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='data_table_16',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField()),
                ('f2', models.TextField()),
                ('f3', models.TextField()),
                ('f4', models.TextField()),
                ('f5', models.TextField()),
                ('f6', models.TextField()),
                ('f7', models.TextField()),
                ('f8', models.TextField()),
                ('f9', models.TextField()),
                ('f10', models.TextField()),
                ('f11', models.TextField()),
                ('f12', models.TextField()),
                ('f13', models.TextField()),
                ('f14', models.TextField()),
                ('f15', models.TextField()),
                ('f16', models.TextField()),
                ('f17', models.TextField()),
                ('f18', models.TextField()),
                ('f19', models.TextField()),
                ('f20', models.TextField()),
                ('f21', models.TextField()),
                ('f22', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='data_table_17',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField()),
                ('f2', models.TextField()),
                ('f3', models.TextField()),
                ('f4', models.TextField()),
                ('f5', models.TextField()),
                ('f6', models.TextField()),
                ('f7', models.TextField()),
                ('f8', models.TextField()),
                ('f9', models.TextField()),
                ('f10', models.TextField()),
                ('f11', models.TextField()),
                ('f12', models.TextField()),
                ('f13', models.TextField()),
                ('f14', models.TextField()),
                ('f15', models.TextField()),
                ('f16', models.TextField()),
                ('f17', models.TextField()),
                ('f18', models.TextField()),
                ('f19', models.TextField()),
                ('f20', models.TextField()),
                ('f21', models.TextField()),
                ('f23', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='data_table_1a',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField(blank=True)),
                ('f2', models.TextField(blank=True)),
                ('f3', models.TextField(blank=True)),
                ('f4', models.TextField(blank=True)),
                ('f5', models.TextField(blank=True)),
                ('f6', models.TextField(blank=True)),
                ('f7', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='data_table_1b',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField(blank=True)),
                ('f2', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='data_table_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField(blank=True)),
                ('f2', models.TextField(blank=True)),
                ('f3', models.TextField(blank=True)),
                ('f4', models.TextField(blank=True)),
                ('f5', models.TextField(blank=True)),
                ('f6', models.TextField(blank=True)),
                ('f7', models.TextField(blank=True)),
                ('f8', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='data_table_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField()),
                ('f2', models.TextField()),
                ('f3', models.TextField()),
                ('f4', models.TextField()),
                ('f5', models.TextField()),
                ('f6', models.TextField()),
                ('f7', models.TextField()),
                ('f8', models.TextField()),
                ('f9', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='data_table_4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField()),
                ('f2', models.TextField()),
                ('f3', models.TextField()),
                ('f4', models.TextField()),
                ('f5', models.TextField()),
                ('f6', models.TextField()),
                ('f7', models.TextField()),
                ('f8', models.TextField()),
                ('f9', models.TextField()),
                ('f10', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='data_table_5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField()),
                ('f2', models.TextField()),
                ('f3', models.TextField()),
                ('f4', models.TextField()),
                ('f5', models.TextField()),
                ('f6', models.TextField()),
                ('f7', models.TextField()),
                ('f8', models.TextField()),
                ('f9', models.TextField()),
                ('f10', models.TextField()),
                ('f11', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='data_table_6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField()),
                ('f2', models.TextField()),
                ('f3', models.TextField()),
                ('f4', models.TextField()),
                ('f5', models.TextField()),
                ('f6', models.TextField()),
                ('f7', models.TextField()),
                ('f8', models.TextField()),
                ('f9', models.TextField()),
                ('f10', models.TextField()),
                ('f11', models.TextField()),
                ('f12', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='data_table_7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField()),
                ('f2', models.TextField()),
                ('f3', models.TextField()),
                ('f4', models.TextField()),
                ('f5', models.TextField()),
                ('f6', models.TextField()),
                ('f7', models.TextField()),
                ('f8', models.TextField()),
                ('f9', models.TextField()),
                ('f10', models.TextField()),
                ('f11', models.TextField()),
                ('f12', models.TextField()),
                ('f13', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='data_table_8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField()),
                ('f2', models.TextField()),
                ('f3', models.TextField()),
                ('f4', models.TextField()),
                ('f5', models.TextField()),
                ('f6', models.TextField()),
                ('f7', models.TextField()),
                ('f8', models.TextField()),
                ('f9', models.TextField()),
                ('f10', models.TextField()),
                ('f11', models.TextField()),
                ('f12', models.TextField()),
                ('f13', models.TextField()),
                ('f14', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='data_table_9',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.TextField()),
                ('f2', models.TextField()),
                ('f3', models.TextField()),
                ('f4', models.TextField()),
                ('f5', models.TextField()),
                ('f6', models.TextField()),
                ('f7', models.TextField()),
                ('f8', models.TextField()),
                ('f9', models.TextField()),
                ('f10', models.TextField()),
                ('f11', models.TextField()),
                ('f12', models.TextField()),
                ('f13', models.TextField()),
                ('f14', models.TextField()),
                ('f15', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='eda_inputs_MatchSimilarText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuzziness', models.CharField(blank=True, max_length=255)),
                ('str_to_compare_with', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='eda_inputs_search_and_replace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset_name', models.CharField(blank=True, max_length=255)),
                ('form_input_new_column', models.CharField(blank=True, max_length=255)),
                ('django_form_input_operation_type', models.CharField(blank=True, max_length=255)),
                ('column_name', models.CharField(blank=True, max_length=255)),
                ('str_search', models.CharField(blank=True, max_length=255)),
                ('str_replace', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='model_10_col_names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='model_11_col_names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='model_12_col_names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='model_13_col_names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='model_14_col_names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='model_15_col_names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='model_16_col_names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='model_17_col_names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='model_1_col_names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(blank=True, max_length=200)),
                ('f2', models.CharField(blank=True, max_length=200)),
                ('f3', models.CharField(blank=True, max_length=200)),
                ('f4', models.CharField(blank=True, max_length=200)),
                ('f5', models.CharField(blank=True, max_length=200)),
                ('f6', models.CharField(blank=True, max_length=200)),
                ('f7', models.CharField(blank=True, max_length=200)),
                ('f8', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='model_1b_col_names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='model_2_col_names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='model_3_col_names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='model_4_col_names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='model_5_col_names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='model_6_col_names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='model_7_col_names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='model_8_col_names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='model_9_col_names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='model_init_lnkd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.TextField(blank=True)),
                ('Org_Name', models.TextField(blank=True)),
                ('Geo_City', models.TextField(blank=True)),
                ('Geo_Country', models.TextField(blank=True)),
                ('college', models.TextField(blank=True)),
                ('university', models.TextField(blank=True)),
                ('createdStr_lnkd', models.TextField(blank=True)),
                ('SearchPortal', models.TextField(blank=True)),
                ('TimeStamp', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='model_scrape_lnkd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.TextField(blank=True)),
                ('Middle_Name', models.TextField(blank=True)),
                ('Last_Name', models.TextField(blank=True)),
                ('LinkdeIn', models.TextField(blank=True)),
                ('Organization', models.TextField(blank=True)),
                ('designation', models.TextField(blank=True)),
                ('college', models.TextField(blank=True)),
                ('university', models.TextField(blank=True)),
                ('City', models.TextField(blank=True)),
                ('Country', models.TextField(blank=True)),
                ('TimeStamp', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='model_ScrapeTracxn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Org_NAME', models.TextField(blank=True)),
                ('Org_URL', models.TextField(blank=True)),
                ('Org_NAME_Others', models.TextField(blank=True)),
                ('Org_URL_Others', models.TextField(blank=True)),
                ('TimeStamp', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='model_SearchTracxn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initSearchStr', models.TextField(blank=True)),
                ('initSearchStrTracxn', models.TextField(blank=True)),
                ('SearchPortal', models.TextField(blank=True)),
                ('TimeStamp', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='news_startup_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ORG_Name', models.TextField(blank=True)),
                ('ORG_URL', models.TextField(blank=True)),
                ('ENG_Levl', models.TextField(blank=True)),
                ('LinkedIn_URL', models.TextField(blank=True)),
                ('ORG_Image', models.TextField(blank=True)),
                ('REG_Coy', models.TextField(blank=True)),
                ('COY_Stage', models.TextField(blank=True)),
                ('ORG_Industry', models.TextField(blank=True)),
                ('ORG_Sector', models.TextField(blank=True)),
                ('ORG_loca', models.TextField(blank=True)),
                ('ORG_AboutMe', models.TextField(blank=True)),
                ('TimeStamp', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='pvbonds_csv_document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pvBonds_csv_file', models.FileField(upload_to='_DataBaseFile_')),
                ('pvBonds_csv_file_name', models.CharField(blank=True, max_length=255)),
                ('pvBonds_dataset_name', models.CharField(blank=True, max_length=255)),
                ('pvBonds_uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('pvBonds_unq_id_nameField', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SqlQueryStr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit_records', models.TextField(blank=True)),
                ('table_name', models.TextField(blank=True)),
                ('new_table_name', models.TextField(blank=True)),
                ('table_col1_name', models.TextField(blank=True)),
                ('table_col1_type', models.TextField(blank=True)),
                ('table_col2_name', models.TextField(blank=True)),
                ('table_col2_type', models.TextField(blank=True)),
                ('table_col3_name', models.TextField(blank=True)),
                ('table_col3_type', models.TextField(blank=True)),
                ('table_col4_name', models.TextField(blank=True)),
                ('table_col4_type', models.TextField(blank=True)),
                ('table_col5_name', models.TextField(blank=True)),
                ('table_col5_type', models.TextField(blank=True)),
                ('table_col6_name', models.TextField(blank=True)),
                ('table_col6_type', models.TextField(blank=True)),
                ('sql_query_input', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='temp_colIndex_for_Eda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_index_from_dataTables_js', models.CharField(blank=True, max_length=255)),
                ('colIndx_js_to_py_pvBonds', models.CharField(blank=True, max_length=255)),
                ('col_SAIR_Value', models.CharField(blank=True, max_length=255)),
                ('col_couponValue', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='temp_dataSetName_dfFromEDA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp_dataset_name', models.CharField(blank=True, max_length=255)),
                ('counter_for_dfFromEDA', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='temp_dataSetName_for_EDALanding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset_name', models.CharField(blank=True, max_length=255)),
                ('pvBondsTempDataSetName', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='temp_tableName_forMerge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp_tableName', models.CharField(blank=True, max_length=255)),
                ('temp_tableName1', models.CharField(blank=True, max_length=255)),
                ('new_merged_tableName', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
