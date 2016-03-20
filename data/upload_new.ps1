$csv = import-csv weight_data_new.csv
foreach ($line in $csv) { 
  write-host $line.Date $line.Qty;
  $params = @{datetime=$line.Date;qty=$line.Qty};
  curl -uri http://localhost:5000/api/weight -method post -body $params;
  read-host;
}

# write-host instead of write-output if you know; write-output is for piping