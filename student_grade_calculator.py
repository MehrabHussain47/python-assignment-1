student = input()

marks_1 = int(input())
marks_2 = int(input())
marks_3 = int(input())

print(f"Student Name: {student}")

total_marks = marks_1 + marks_2 + marks_3
avg_marks = total_marks / 3

print(f"Total Marks: {total_marks}")
print(f"Average: {avg_marks:.2f}")

if avg_marks >= 80 and avg_marks <= 100:
  print("Grade: A+")
elif avg_marks >= 70 and avg_marks < 80:
  print("Grade: A")
elif avg_marks >= 60 and avg_marks < 70:
  print("Grade: B")
elif avg_marks >= 50 and avg_marks < 60:
  print("Grade: C")
elif avg_marks >= 0 and avg_marks < 50:
  print("Grade: F")
else:
  print("Grade: Invalid Grade")
