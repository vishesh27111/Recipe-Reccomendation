import 'dart:convert';

import 'package:flaskapi/function.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

class Home extends StatefulWidget {
  const Home({Key? key}) : super(key: key);

  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  String url = 'http://10.0.0.2:5000/yolo/detection';
  var data;
  String output = 'Initial';
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('f')),
      body: Center(
        child: Column(children: [
          TextButton(
              onPressed: () async {
                data = await jsonDecode(fetchdata(url));
                setState(() {
                  output = data['0']['item'];
                });
              },
              child: Text('recommend recipe:')),
          Text(output)
        ]),
      ),
    );
  }
}
