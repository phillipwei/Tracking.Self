python 3 (?)

pip install:
pip install Flask
pip install Flask-Script
pip install Flask-Babel
pip install Flask-Login
pip install Flask-Mail
pip install Flask-SqlAlchemy
pip install Flask-WTF
pip install python-dateutil
pip install celery
  
p3 Flask-WTF
http://stackoverflow.com/questions/18297041/im-not-able-to-import-flask-wtf-textfield-and-booleanfield

sqlite3 installation

* backfill

http://stackoverflow.com/questions/5785117/run-powershell-command-using-csv-as-input



$csv = import-csv weight_data.csv
foreach ($line in $csv) { 
  $params = @{datetime='';qty=''};
  curl -uri localhost:5000/api/weight -method post -body $params
}


graphing:
timeline
http://www.simile-widgets.org/timeline/

vc
http://www.visualcomplexity.com/vc/
flot
raphael
d3

https://plot.ly/
http://www.win-vector.com/blog/2014/01/the-extra-step-graphs-for-communication-versus-exploration/
http://www.brendangregg.com/FlameGraphs/cpuflamegraphs.html

https://github.com/blog/1093-introducing-the-new-github-graphs
http://dygraphs.com/

http://mbostock.github.io/protovis/

nvd3
vega

http://www.nytimes.com/interactive/2011/05/31/business/economy/case-shiller-index.html?_r=0



/api/weight
/api/activity
/api/intake
/api/thoughts

/app
/weight