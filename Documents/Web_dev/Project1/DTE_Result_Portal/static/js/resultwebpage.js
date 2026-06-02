const students = {
  "203CS23008": {
    name: "B C YASHAS",
    internal: 239,
    theory: 52,
    practical: 99,
    grade:"A+",
    sgpa:10.00,
  },
  "203CS23011": {
    name: "BHARATH S",
    internal: 207,
    theory: 4,
    practical: 60,
    grade:"F",
    sgpa:0.00,
  },
  "203CS23039": {
    name: "PAVAN GOWDA R",
    internal: 225,
    theory: 27,
    practical: 80,
    grade:"A",
    sgpa:9.00,
  },
  "203CS23048": {
    name: "RISHI P",
    internal: 195,
    theory: 29,
    practical: 60,
    grade:"F",
    sgpa:0.00,
  }
};

const regno = localStorage.getItem("regno");



const student = students[regno];



document.getElementById("Name").innerHTML = student.name;
document.getElementById("regno").innerHTML = regno;
document.getElementById("intermarks").innerHTML = student.internal;
document.getElementById("theorymarks").innerHTML = student.theory;
document.getElementById("practmarks").innerHTML = student.practical;
document.getElementById("grade").innerHTML = student.grade;
document.getElementById("sgpa").innerHTML = student.sgpa;

document.getElementById("totalMarks").innerHTML=marksSum();
function marksSum(){
  let result=student.internal+student.theory+student.practical
  return result;
}