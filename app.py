from flask import Flask, render_template
import COVID19Py as cov


def getdata():
    covid19 = cov.COVID19()
    data = covid19.getAll()

    india_data = data['locations'][131]

    stats = list(india_data['latest'].items())

    date = india_data['last_updated'][:10]

    time = india_data['last_updated'][11:19]
    return stats, date, time

app = Flask(__name__)


@app.route('/')
def hello():
    stats, date, time = getdata()
    return render_template("index.html", cases = stats, date = date, time = time)

if __name__ == '__main__':
    app.run(debug = True)