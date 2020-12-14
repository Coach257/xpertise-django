from flask import Flask, request, jsonify


app=Flask(__name__)

@app.route('/api/v1/search_author',methods=['POST'])
def search_author():
    from scholarly import scholarly
    author_name=request.POST.get('author_name')
    author = next(scholarly.search_author(author_name))
    res = {'affiliation': author.affiliation,
           'email': author.email,
           'id': author.id,
           'interests': author.interests,
           'name': author.name,
           'url_picture': author.url_picture}
    return jsonify(res)

@app.route('/api/v1/search_paper',methods=['POST'])
def search_author():
    from scholarly import scholarly
    paper_name=request.POST.get('paper_name')
    paper=next(scholarly.search_pubs(paper_name))
    res = {
            'url':paper.bib['url'],
            'venue': paper.bib['venue'],
            'abstract': paper.bib['abstract']}
    return jsonify(res)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)

