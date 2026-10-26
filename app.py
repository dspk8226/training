from fastapi import FastAPI, HTTPException
from models import Student
from repository import StudentRepository

app=FastAPI(
    title="Student Marks Services (SMS)",
    version="1.0"
)

repo=StudentRepository()

@app.get("/")
def home():
    return {"message": "Student Marks services"}

#create

@app.post("/students",response_model=Student)
def create_student(student: Student):
    try:
        return repo.create(student)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    


#read all
@app.get("/students",response_model=list[Student])
def get_all():
    return repo.get_all()


#read one
@app.get("/students/{student_id}",response_model=Student)
def get_one(student_id:int):
    student=repo.get(student_id)

    if student is None:
        raise HTTPException(status_code=404, detail="student not found")

    return student



#update
@app.put("/students/{student_id}",response_model=Student)
def upt(student_id:int,student:Student):
    updated=repo.update(student_id,student)

    if updated is None:
        raise HTTPException(status_code=404, detail="student not found")

    return updated



#delete
@app.delete("/students/{student_id}")
def delet(student_id:int):
    deleted=repo.delete(student_id)

    if deleted is None:
        raise HTTPException(status_code=404, detail="student not found")

    return {"message": "student deleted successfully"}
    

    