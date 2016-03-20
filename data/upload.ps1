$csv = import-csv weight_data.csv
foreach ($line in $csv) { 
  write-host $line.Date $line.Morning $line.Evening;
  if($line.Morning) {
    $params = @{datetime=$line.Date+' 08:00AM';qty=$line.Morning};
    curl -uri http://localhost:5000/api/weight -method post -body $params
  }
  if($line.Evening) {
    $params = @{datetime=$line.Date+' 10:00PM';qty=$line.Evening};
    curl -uri http://localhost:5000/api/weight -method post -body $params
  }
}

# write-host instead of write-output if you know; write-output is for piping