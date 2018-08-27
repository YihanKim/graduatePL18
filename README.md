# CS520 Theory of Programming Languages, Fall 2018, KAIST 

This is a webpage of the course "CS520 Theory of Programming Languages", which is offered at the KAIST CS department in the fall of 2018. The webpage will contain links to course-related materials and announcements.

CS520 is an advanced graduate-level course on the theories of programming languages. Its goal is to expose students to rigorous mathematical foundations for programming languages and systems, and mathematical techniques for formally reasoning about  programs written in those languages. The course will largely follow Reynolds's textbook "Theories of Programming Languages", which provides good mathematical treatment of a wide range of programming constructs through axiomatic, denotational and operational semantics. 

The prerequisite of the course is CS320, the undergraduate-level programming-language course offered at KAIST, or a similar course. The course will be heavy in math, and we expect students to be comfortable with doing and reading rigorous mathematical proofs. 

## 1. Important Announcements

#### [27 August] Planned cancelling and addition of lectures.

Because of Hongseok's business, there will be no lectures on the following days.

1. 09/06 - NO LECTURE. SETTA'18.
2. 10/04 - NO LECTURE. PROBPROG'18.
3. 12/04, 12/06 - NO LECTURES. NIPS'18.

This is in addition to the cancelling of lectures due to national holidays and KAIST undergraduate admission. 

To cover cancelled lectures, we schedule two additional lectures:

1. 10/18 (Thu) - LECTURE FROM 9:30 TO 11:30. Recursively-Defined Domains (Tennent Ch10). 
2. 11/30 (Fri) - LECTURE FROM 4 TO 6. The Simple Type System (Ch15). 

Note that the 18th of October is in the period of the mid-term exam. The university allocated the 9:00-11:45 slot on 10/18 for the mid-term exam of this course. Instead of having a mid-term exam, we will have a 2-hour lecture on that day.

## 2. Logistics

#### Evaluation

* Final exam (40%). Homework (30%). Two critical reviews (30%).

#### Teaching Staffs

* Lecturer: [Prof Hongseok Yang](https://cs.kaist.ac.kr/people/view?idx=552&kind=faculty&menu=160) (email: hongseok00@gmail.com, office hour: 6:00pm - 7:00pm on Tuesday at the room 3403 in the E3-1 building)
* TA: Hyoungjin Lim (email: lmkmkr@kaist.ac.kr)
* TA: Hangyeol Yu (email: yhk1344@kaist.ac.kr)

#### Place and Time

* Place: room 111 in the N1 building
* Time: 10:30am - 11:45am on Tuesday and Thursday from 28 August 2018 until 13 December 2018.
* Final exam: 9:00am - 11:00am on 13 December 2018 (Thursday) at the room 202 in the E11 building.

#### Online Discussion

* We will use KLMS. 

## 3. Homework

Submit your solutions by putting them in the homework submission box in the third floor of the E3-1 building.

## 4. Tentative Plan

* 08/28 - Introduction ([slides](https://github.com/hongseok-yang/graduatePL18/blob/master/Lectures/Lecture1/Lecture1.pdf)). Predicate Logic (Ch1) ([note1](https://github.com/hongseok-yang/graduatePL18/blob/master/Lectures/Lecture2/note1.jpg) [note2](https://github.com/hongseok-yang/graduatePL18/blob/master/Lectures/Lecture2/note2.jpg), [note3](https://github.com/hongseok-yang/graduatePL18/blob/master/Lectures/Lecture2/note3.jpg), [note4](https://github.com/hongseok-yang/graduatePL18/blob/master/Lectures/Lecture2/Lecture4.jpg)).
* 08/30 - Predicate Logic (Ch1).
* 09/04 - The Simple Imperative Language (Ch2).
* __**09/06 - NO LECTURE. SETTA'18.**__
* 09/11 - The Simple Imperative Language (Ch2).
* 09/13 - Program Specification and Their Proofs (Ch3).
* 09/18 - Failure, Input-Output, and Continuation (Ch5).
* 09/20 - Failure, Input-Output, and Continuation (Ch5).
* __**09/25 - NO LECTURE. Chuseok.**__
* 09/27 - Transition Semantics (Ch6).
* 10/02 - Transition Semantics (Ch6).
* __**10/04 - NO LECTURE. PROBPROG'18.**__
* __**10/09 - NO LECTURE. Hangle Proclamation Day.**__
* 10/11 - An Introduction to Category Theory (Tennent Ch8).
* __**10/16 - NO LECTURE. Midterm Exam.**__
* __**10/18 - LECTURE FROM 9:30 TO 11:30.**__ Recursively-Defined Domains (Tennent Ch10). 
* 10/23 - The Lambda Calculus (Ch10).
* 10/25 - The Lambda Calculus (Ch10). 
* 10/30 - An Eager Functional Language (Ch11).
* 11/01 - An Eager Functional Language (Ch11).
* 11/06 - Continuation in a Functional Language (Ch12).
* 11/08 - Continuation in a Functional Language (Ch12).
* 11/13 - Iswim-like Languages (Ch13).
* 11/15 - Iswim-like Languages (Ch13).
* 11/20 - A Normal-Order Language (Ch14).
* 11/22 - A Normal-Order Language (Ch14).
* 11/27 - The Simple Type System (Ch15).
* __**11/29 - NO LECTURE. KAIST Undergraduate Admission.**__
* __**11/30 - LECTURE FROM 4 TO 6.**__ The Simple Type System (Ch15). 
* __**12/04, 12/06 - NO LECTURES. NIPS'18.**__
* __**12/11, 12/13 - NO LECTURES. Final Exam.**__

## 5. Studying Materials

We will mainly follow Reynolds's book, but study the materials appearing in Chapters 8 and 9 of Tennent's book.

* Main Textbook 1 : Theories of Programming Languages, John C Reynolds, Cambridge University Press, 1998. 
* Main Textbook 2 : Semantics of Programming Languages, Robert D. Tennent, Prentice Hall, 1991. Chapters 8 and 10 only.

In addition to the two books above, the following books will have further information about the topics covered in the course. In particular, Gunter's book goes deep into the domain theory, and Pierce's book into the type theory.

* Auxiliary Textbook 1 : Semantics of Programming Languages: Structures and Techniques, Carl A. Gunter, MIT Press, 1992.
* Auxiliary Textbook 2 : Types and Programming Languages, Benjamin C. Pierce, MIT Press, 2002.
* Auxiliary Textbook 3 : Formal Semantics of Programming Languages: an Introduction, Glynn Winskel, MIT Press, 1993.

The following classic papers or their recent reprints contain deep insight into some of topics that we study throughout the course.

* John C. Reynolds, [Definitional Interpreters for Higher-Order Programming Languages](https://doi.org/10.1023/A:1010027404223), Higher-Order and Symbolic Computation, 1998. 
* Luis Damas and Robin Milner, [Principal Type-Schemes for Functional Programs](http://delivery.acm.org/10.1145/590000/582176/p207-damas.pdf?ip=143.248.139.205&id=582176&acc=ACTIVE%20SERVICE&key=0EC22F8658578FE1%2E7500FBAD1E9579D9%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&__acm__=1535179405_6f0967c345266d3a1429bb43f9add160), POPL 1982.

## 5. Two Critial Reviews

One important part of this course is to study assigned reading materials and write reviews about them. It accounts for the 30% of the total marks of this course. In order to get full marks, a student has to show in his or her write-up that she or he has thought hard about the materials and gone beyond the simple understanding of them. Here are the details of this assignments.

1. There are two assignments for this critical review.
2. First assignment.
   1. Deadline: __**midnight of the 26th of October in 2018 (Friday).**__
   2. Material: Chapter 7 of Reynolds's ''Theories of Programming Languagues.'' This chapter is about nondeterminism and guarded commands.
3. Second assignment.
   1. Deadline: __**midnight of the 3rd of December in 2018 (Monday).**__
   2. Material: Wadler's [Monads for Functional Programming](http://homepages.inf.ed.ac.uk/wadler/papers/marktoberdorf/baastad.pdf) (Advanced Functional Programming 1995), and Moggi's [Computational Lambda-Calculus and Monads](http://www.disi.unige.it/person/MoggiE/ftp/lics89.ps.gz) (LICS 1989).
4. A review should have three pages or less.
