from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models import db, Post

post_route = Blueprint('post_route', __name__)
@post_route.route('/posts', methods=['GET'])
@post_route.route('/post/<int:id>', methods=['GET'])
#@jwt_required
def getpost(id=None):
    if request.method == 'GET':
        if id is not None:
            post = Post.query.get(id)
            if post:
                return jsonify(post.serialize()), 200
            else:
                return jsonify({"error":"Post no encontrado"}), 404
        else:
            posts = Post.query.all()
            posts = list(map(lambda post:post.serialize(), posts))
            return jsonify(posts), 200

@post_route.route('/posts', methods=['POST'])
#@jwt_required
def postpost():
    content = request.json.get('content')
    user = request.json.get('user')
    #image = request.json.get('image')
    #user_id = request.json.get('user_id')
    if not user:
        return jsonify({"error": "Usuario es obligatorio"}), 422
    if not content:
        return jsonify({"error": "Contenido es obligatorio"}), 422
    #if not image:
    #    return jsonify({"error": "Imagen es obligatoria"}), 422
    #if not user_id:
    #    return jsonify({"error": "Inserte su id de usuario"}), 422
    post = Post()
    post.content = content
    post.user = user
    #post.image = image
    #post.user_id = user_id
    db.session.add(post)
    db.session.commit()
    return jsonify({
        "post": post.serialize(),
        "success": "Post creado exitósamente"
        }), 201

@post_route.route('/post/<int:id>', methods=['PUT'])
#@jwt_required
def updatepost(id):
    if request.method == 'PUT':
        post = Post.query.get(id)
        post.content = request.json.get('content')
        db.session.commit()
        return jsonify({
            "post": post.serialize(),
            "success": "Post editado exitósamente"
        }), 201

@post_route.route('/post/<int:id>', methods=['DELETE'])
#@jwt_required
def deletepost(id):
    if request.method == 'DELETE':
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
        return jsonify({"success":"Post borrado exitósamente"}), 200
