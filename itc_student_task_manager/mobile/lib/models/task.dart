class Task {
  final int id; String title, description, status, priority; String? dueDate;
  Task({required this.id,required this.title,required this.description,required this.status,required this.priority,this.dueDate});
  factory Task.fromJson(Map<String,dynamic> j)=>Task(id:j['id'],title:j['title'],description:j['description']??'',status:j['status'],priority:j['priority'],dueDate:j['due_date']);
  Map<String,dynamic> toJson()=>{'title':title,'description':description,'status':status,'priority':priority,'due_date':dueDate};
}
