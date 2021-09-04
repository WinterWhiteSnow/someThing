from flask import Flask, render_template, request, redirect, send_file


app = Flask(__name__)

@app.route("/")
def home():
	word = request.args
	word = list(word.values())
	if word:
		porduct = word[0]
		mini = word[1]
		maxi = word[2]
		url = 	f"http://browse.auction.co.kr/m/search?keyword={porduct}&f=p:{mini}%5e{maxi}&s=8"
		print(url)		
	else:
		word=None
		url =None	
	return render_template("main.html", word=word, url=url)

app.run(host="0.0.0.0", port="5000", debug=True)
# if __name__ == "__main__":
#     app.run()