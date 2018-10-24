from flask import Flask,request, make_response,redirect, render_template
app= Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"),404

@app.errorhandler(500)
def internal(e):
	return render_template("500.html")

@app.route('/')

def index():
	return render_template("index.html")
	
@app.route("/user/<name>")
def user(name):
	return render_template("user.html", blabla = name)

@app.route("/user/")
def noUser():
	
	return render_template("user.html")
@app.route('/req')
def req():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {0}</p><p>HTTP method is: {1}</p><p></p>'.format(user_agent, request.method)
	
@app.route('/resp')
def resp():
	r = make_response('<h1>Šaljemo kolačiće!</h1>')
	r.set_cookie('odgovor', '42')
	return r

@app.route('/redir')
def redir():
    return redirect('https://hr.wikipedia.org')
	
@app.route('/eurhr/<iznos>')
def pretvEu(iznos):
	hrk=float(iznos)*7.62
	return "Iznos je %.2f"%(hrk)

@app.route("/comments/")
def comments():
	comments=["odlicno","ne razumijem", "nije lose", "uzasno je", "moze i gore"]
	return render_template("comments.html", comments=comments)

