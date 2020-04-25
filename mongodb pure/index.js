const express=require('express');

const mongoose=require('mongoose');

const app=express();

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: false }));


mongoose 
    .connect(
        'mongodb://mongo:27017/',
        { useNewUrlParser:true}
    )
    .then(() => console.log('mongo connected'))
    .catch(err => console.log(err))

app.get('/createuser',(req,res)=>{

    db().collection('users').insertOne({
        name:"v"
    }).then(data=>{
        res.send(data)
    });

});

app.get('/getuser',(req,res)=>{

    db().collection('users').findOne({
        name:"ven"
    }).then(data=>{
        res.send(data);
    });


});

app.get('/updateuser',(req,res)=>{

    db().collection('users').update({
        name:"ven"
    },{
        $set:{name:"diljfejfiepwjf"}
    }).then(data=>{
        res.send(data)
    });

});

app.get('/deleteuser',(req,res)=>{

    db().collection('users').deleteOne({
        name:"v"
    }).then(data=>{
        res.send(data)
    });

});



app.listen(3000,()=>{
    console.log("server is started");
})



