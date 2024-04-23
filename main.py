from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/dcc-database"
db = SQLAlchemy(app)

class purchase(db.Model):
    sno = db.Column(db.String(10), primary_key=True)
    ref= db.Column(db.String(20), nullable=False)
    j_date = db.Column(db.String(30), nullable=False)
    purchase_date = db.Column(db.String(30), nullable=False)
    exp_date = db.Column(db.String(30))
    purchaser_name = db.Column(db.String(120), nullable=False)
    prefix = db.Column(db.String(10), nullable=False)
    bond_no = db.Column(db.String(10), nullable=False)
    denominations = db.Column(db.String(40), nullable=False)
    branch_code = db.Column(db.String(8), nullable=False)
    issue = db.Column(db.String(14), nullable=False)
    status = db.Column(db.String(20), nullable=False)

class redemption(db.Model):
    sno = db.Column(db.String(10), primary_key=True)
    encashment_date = db.Column(db.String(40), nullable=False)
    encashment = db.Column(db.String(120), nullable=False)
    account_no = db.Column(db.String(30), nullable=False)
    prefix = db.Column(db.String(30))
    bond_no = db.Column(db.String(10), nullable=False)
    denominations = db.Column(db.String(40), nullable=False)
    branch_code = db.Column(db.String(8), nullable=False)
    pay_teller = db.Column(db.String(20), nullable=False)

@app.route('/search', methods=['GET'])
def search():
    table = request.args.get('table')
    column = request.args.get('column')
    query = request.args.get('query')

    if table == 'purchase':
        model = purchase
    elif table == 'redemption':
        model = redemption

    if column:
        results = model.query.filter(getattr(model, column).contains(query)).all()
    else:
        results = model.query.filter(
            db.or_(
                purchase.sno.contains(query),
                purchase.ref.contains(query),
                purchase.j_date.contains(query),
            )
        ).all()

    purchase_results = []
    redemption_results = []
    for result in results:
        if isinstance(result, purchase):
            purchase_results.append(result)
        elif isinstance(result, redemption):
            redemption_results.append(result)

    return render_template("search.html", purchase_results=purchase_results, redemption_results=redemption_results)

@app.route('/')
def index():
    parties = db.session.query(redemption.encashment).distinct().all()
    companies = purchase.query.with_entities(purchase.purchaser_name).distinct().all()
    return render_template('index.html', companies=companies, parties=parties)

if __name__ == '__main__':
    app.run(debug=True)

