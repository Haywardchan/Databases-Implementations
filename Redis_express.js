// Run npm i redis to install the redis package for caching data
const { rejects } = require('assert')
const Redis = require('redis')
const express = require('express')
const cors = require('cors')
const redisClient = Redis.createClient()//pass {url:<url>} for the production instance
redisClient.on('error', err => console.log('Redis Client Error', err))
async() => await redisClient.connect()
const DEFAULT_TTL = 60 * 60
const app = express()
app.use(cors())

redisClient.SETEX('key', DEFAULT_TTL, 'value')

function getOrSetCache(key, cb){
    return new Promise((resolve, reject) => {
        redisClient.GET(key, async (error, data) => {
            if (error) return reject(error)
            if (data != null) return resolve(JSON.parse(data))
            const freshData = await cb()
            redisClient.SETEX(key, DEFAULT_TTL, JSON.stringify(freshData))
            resolve(freshData)
        })
    })
}
app.listen(3000)