import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'screens/login_screen.dart'; import 'screens/task_screen.dart';
void main() async{WidgetsFlutterBinding.ensureInitialized();final token=(await SharedPreferences.getInstance()).getString('token');runApp(App(hasToken:token!=null));}
class App extends StatelessWidget{final bool hasToken;const App({super.key,required this.hasToken});Widget build(c)=>MaterialApp(debugShowCheckedModeBanner:false,title:'ITC Task Manager',theme:ThemeData(useMaterial3:true,colorSchemeSeed:Colors.indigo),home:hasToken?const TaskScreen():const LoginScreen());}
