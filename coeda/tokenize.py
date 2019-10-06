#!/usr/bin/env python3
# coding:utf8

import json


class Chunk:
	""" Chunk class """

	def __init__(self, data: dict):
		self.chunk = data["chunk_info"]
		self.id = data["chunk_info"]["id"]
		self.head = data["chunk_info"]["head"]
		self.dep = data["chunk_info"]["dep"]
		self.chunk_head = data["chunk_info"]["chunk_head"]
		self.chunk_func = data["chunk_info"]["chunk_func"]
		self.links = data["chunk_info"]["links"]
		self.tokens = [token for token_json in data["tokens"] for token in [Token(token_json)]]
		self.form = "".join([token.form for token in self.tokens])

	def get_chunk_head_token(self):
		return self.tokens[self.chunk_head]

	def get_chunk_func_token(self):
		return self.tokens[self.chunk_func]

	def __str__(self):
		return (json.dumps({
			"chunk_info": self.chunk,
			"tokens": [token.to_dict() for token in self.tokens]}, ensure_ascii=False))

	def __repr__(self):
		return self.__str__()

	def to_json(self):
		return self.__repr__()


class Token:
	""" Token class """

	def __init__(self, data: dict):
		self.form = data["form"]
		self.lemma = data["lemma"]
		self.kana = data["kana"]
		self.id = data["id"]
		self.pos = data["pos"]
		self.features = data["features"]
		self.dependency_labels = data["dependency_labels"] if "dependency_labels" in data else {}
		self.attributes = data["attributes"]

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		return json.dumps(self.to_dict(), ensure_ascii=False)

	def to_json(self):
		return self.__repr__()

	def to_dict(self):
		return {
			"id": self.id,
			"form": self.form,
			"lemma": self.lemma,
			"kana": self.kana,
			"pos": self.pos,
			"feautes": self.features,
			"dependency_labels": self.dependency_labels,
			"attributes": self.attributes
		}
