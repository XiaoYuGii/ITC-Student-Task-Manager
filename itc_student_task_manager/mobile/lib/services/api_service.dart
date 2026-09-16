import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import '../models/task.dart';
class ApiService {
  // Android emulator -> host computer. For a real phone, replace with your PC's LAN IP.
  static const base='http://10.0.2.2:8000/api';
  static Future<String?> _token() async=>(await SharedPreferences.getInstance()).getString('token');
  static Future<bool> login(String u,String p) async { final r=await http.post(Uri.parse('$base/login/'),body:{'username':u,'password':p}); if(r.statusCode==200){final sp=await SharedPreferences.getInstance(); await sp.setString('token',jsonDecode(r.body)['token']); return true;} return false; }
  static Future<bool> register(String u,String p) async { final r=await http.post(Uri.parse('$base/register/'),body:{'username':u,'password':p}); if(r.statusCode==201){final sp=await SharedPreferences.getInstance(); await sp.setString('token',jsonDecode(r.body)['token']); return true;} return false; }
  static Future<Map<String,String>> _headers() async=>{'Content-Type':'application/json','Authorization':'Token ${await _token()}'};
  static Future<List<Task>> tasks() async {final r=await http.get(Uri.parse('$base/tasks/'),headers:await _headers()); if(r.statusCode!=200) throw Exception('Could not load tasks'); return (jsonDecode(r.body) as List).map((x)=>Task.fromJson(x)).toList();}
  static Future<void> create(Map<String,dynamic> data) async {final r=await http.post(Uri.parse('$base/tasks/'),headers:await _headers(),body:jsonEncode(data)); if(r.statusCode!=201) throw Exception('Create failed');}
  static Future<void> update(Task t) async {final r=await http.put(Uri.parse('$base/tasks/${t.id}/'),headers:await _headers(),body:jsonEncode(t.toJson())); if(r.statusCode!=200) throw Exception('Update failed');}
  static Future<void> delete(int id) async {final r=await http.delete(Uri.parse('$base/tasks/$id/'),headers:await _headers()); if(r.statusCode!=204) throw Exception('Delete failed');}
  static Future<void> logout() async=>(await SharedPreferences.getInstance()).remove('token');
}
