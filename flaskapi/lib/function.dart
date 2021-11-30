import 'package:http/http.dart' as http;

fetchdata(String url1) async {
  http.Response response = await http.get(Uri.parse(url1));
  return response.body;
}

fetchdata2(String url2) async {
  http.Response response = await http.get(Uri.parse(url2));
  return response.body;
}

fetchdata3(String url3) async {
  http.Response response = await http.get(Uri.parse(url3));
  return response.body;
}
