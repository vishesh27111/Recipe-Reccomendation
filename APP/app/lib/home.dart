// ignore: unused_import
import 'dart:convert';

// import 'package:flaskapi/function.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

// ignore: unused_import
import 'function.dart';

class Home extends StatefulWidget {
  const Home({key}) : super(key: key);

  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  String url = 'http://10.0.2.2:5000/yolo/detection';
  var data;
  String output = 'Detecting Output';
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("RecipeR")),
      body: Column(
        children: <Widget>[
          // TextField(
          //   onChanged: (value) {
          //     url = 'http://10.0.2.2:5000/yolo/detection' + value.toString();
          //   },
          // ),
          // ignore: deprecated_member_use
          RaisedButton(
              // child: Text('Detect Ingridients'),
              onPressed: () async {
                data = await fetchdata(url);
                var decoded = jsonDecode(data) as Map;
                var itemId;
                String ingridents = '';
                setState(() {
                  for (itemId in decoded.keys) {
                    output = decoded[itemId]['item'];
                    ingridents = ingridents + ' ' + output;
                  }
                  output = ingridents;
                });
              },
              child: Text(
                'Detect Ingredients',
                style: TextStyle(fontSize: 20),
              )),

          // ignore: deprecated_member_use
          RaisedButton(
            child: Text('BigBasket'),
            onPressed: null,
          ),
          // ignore: deprecated_member_use
          RaisedButton(
            child: Text('Recommendar1'),
            onPressed: null,
          ),
          // ignore: deprecated_member_use
          RaisedButton(
            child: Text('Recommendar2'),
            onPressed: null,
          ),
        ],
      ),
    );
  }
}
