#entry for cron

VAR='/scripts/update_pull.py'
#DIR="$(dirname "${VAR}")" ;

FILE="$(basename "${VAR}")"

echo "[${FILE}]"

sudo chmod +x FILE

crontab -l > mycron

echo "00 01 * * * "${FILE}" " >> mycron

crontab mycron

rm mycron