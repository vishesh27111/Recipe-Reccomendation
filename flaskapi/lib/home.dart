import 'dart:convert';

import 'package:flaskapi/function.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

import 'function.dart';

class Home extends StatefulWidget {
  const Home({key}) : super(key: key);

  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  String url1 = 'http://127.0.0.1:5000/yolo/detection';
  String url2 = 'http://127.0.0.1:5000/recommender/content';
  String url3 =
      'http://127.0.0.1:5000/self_order/get_shopping_list/<string:item_id>';
  var data;
  String output1 = 'Detecting Output';
  String output2 = 'recipes';
  String output3 = 'self odering';
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
          backgroundColor: Colors.blue.shade900, title: Text('Recipe R app')),
      body: Center(
        child: Container(
          color: Colors.white,
          padding: EdgeInsets.all(100),
          child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                RaisedButton(
                    color: Colors.blue.shade900,
                    onPressed: () async {
                      data = await fetchdata(url1);
                      var decoded = jsonDecode(data) as Map;
                      var itemId;
                      String ingridents = '';
                      setState(() {
                        for (itemId in decoded.keys) {
                          output1 = decoded[itemId]['item'];
                          ingridents = ingridents + ' ' + output1;
                        }
                        output1 = ingridents;
                      });
                    },
                    child: Text('Detect Ingredients',
                        style: TextStyle(fontSize: 20, color: Colors.white))),
                Text(
                  output1,
                  style: TextStyle(fontSize: 10, color: Colors.black87),
                ),
                RaisedButton(
                    color: Colors.blue.shade900,
                    onPressed: () async {
                      data = await fetchdata2(url2);
                      var decoded = jsonDecode(data) as Map;
                      var itemId;
                      String recipe = '';
                      setState(() {
                        for (itemId in decoded.keys) {
                          output2 = decoded[itemId];
                          recipe = recipe + ' ' + output2;
                        }
                        output2 = recipe;
                      });
                    },
                    child: Text(
                      'Recommend recipe',
                      style: TextStyle(fontSize: 20, color: Colors.white),
                    )),
                Text(
                  output2,
                  style: TextStyle(fontSize: 10, color: Colors.black87),
                ),
                RaisedButton(
                    color: Colors.blue.shade900,
                    onPressed: () async {
                      data = await fetchdata3(url3);
                      var decoded = jsonDecode(data) as Map;
                      var itemId;
                      String message = '';
                      setState(() {
                        for (itemId in decoded.keys) {
                          output3 = decoded[itemId];
                          message = message + ' ' + output3;
                        }
                        output3 = message;
                      });
                    },
                    child: Text(
                      'order',
                      style: TextStyle(fontSize: 20, color: Colors.white),
                    )),
                Text(
                  output3,
                  style: TextStyle(fontSize: 10, color: Colors.black87),
                )
              ]),
        ),
      ),
    );
  }
}
