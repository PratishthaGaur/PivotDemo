from flask import Flask, render_template, Response, request,jsonify
import pandas as pd
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/data', methods = ['GET', 'POST'])
def data():
    # return "Successful"
    if request.method=='POST':
        file = request.files['csvfile']
        data=[]
        # with open(file) as file:
        #     csvfile=csv.reader(file)
        #     for row in csvfile:
        #         data.append(row)
        data = pd.read_csv(file)
        data=data.pivot_table(index="CD_NAME")
        # return "Success"

            # convert DataFrame to CSV string
        csv = data.to_csv(index=False)

            # create a response object with CSV string as content
        response = Response(
                csv,
                mimetype='text/csv',
                headers={'Content-Disposition': 'attachment; filename=data.csv'}
        )

        return response

    else:
        return "Not Successful"




if __name__ == '__main__':
    app.run()
