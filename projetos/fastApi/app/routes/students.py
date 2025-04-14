from fastapi import APIRouter, HTTPException
from app.models.students_data import students  

router = APIRouter()

@router.get("/students/{id}", tags=["Students"])
def get_student_by_id(id: int) -> dict:
    student = students.get(id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
