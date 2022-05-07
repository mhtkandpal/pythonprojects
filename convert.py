#convert it to according to handwriting

import pywhatkit as pw

txt="hello my name is mohit kandpal ,learning as python devloper every day and creating a 2 project per day to learn"

pw.text_to_handwriting(txt,"name.png",[0,0,138])
print("  END  ")