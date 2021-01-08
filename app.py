# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:40:41 2020
@author: win10
"""
#StreamLit Krish Naik
#https://www.youtube.com/watch?v=M1uyH-DzjGE
#pip install pymongo

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

class Package(BaseModel):
    name: str
    number: int
    description: str


@app.post('/package/{priority}')
async def setPackageDetails(package:Package):
    return {
        **package.dict(),
        "asanka":32
    }



@app.get('/')
async def index():
    return {'message': 'Hello, World'}



@app.get('/name/{number}')
async def get_name(number : int, name: Optional[str],age : int):
    return {'Welcome To Krish Youtube Channel': f'{name}'}


from pymongo import MongoClient

# creation of object MongoClient
client = MongoClient()

# Connect with the portnumber and host
client = MongoClient("mongodb+srv://asanka:asanka96@cluster0.pelc0.mongodb.net/test")

# Access database
mydatabase = client['Students989']

# Access collection of the database
collection = mydatabase['studentscores']
data = [
    {"user": "Krish", "subject": "Database", "score": 80},
    {"user": "Amit", "subject": "JavaScript", "score": 90},
    {"user": "Amit", "title": "Database", "score": 85},
    {"user": "Krish", "title": "JavaScript", "score": 75},
    {"user": "Amit", "title": "Data Science", "score": 60},
    {"user": "Krish", "title": "Data Science", "score": 95}]

collection.insert_many(data)

