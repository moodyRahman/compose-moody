from jenkinsapi.jenkins import Jenkins
from flask import *

app = Flask(__name__)
jenkins_url = 'http://localhost:8080'
server = Jenkins(jenkins_url, username='moody', password='angrr')

@app.route("/")
def home():
    out = []
    for name, instance in server.get_jobs():
        build = instance.get_last_completed_build()
        job = {
            "recent_build":str(build),
            "status":build.get_status(),
            "timestamp":build.get_timestamp()
            
        }
        out.append(job)
    return out

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8081)