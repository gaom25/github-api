psql -U postgres postgres -f scripts/create_data_base.sql

python git4nstats/manage.py migrate --settings=git4nstats.settings.development