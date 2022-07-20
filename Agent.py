# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
from colorsys import TWO_THIRD
from PIL import Image
from PIL import ImageChops
import numpy as np
import time

import cv2 

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints 
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self,problem):

        if problem.problemType == '3x3':
             
            figureA = cv2.imread(problem.figures["A"].visualFilename)
            figureB = cv2.imread(problem.figures["B"].visualFilename)
            figureC = cv2.imread(problem.figures["C"].visualFilename)
            figureD = cv2.imread(problem.figures["D"].visualFilename)
            figureE = cv2.imread(problem.figures["E"].visualFilename)
            figureF = cv2.imread(problem.figures["F"].visualFilename)
            figureG = cv2.imread(problem.figures["G"].visualFilename)
            figureH = cv2.imread(problem.figures["H"].visualFilename)

            one = cv2.imread(problem.figures["1"].visualFilename)
            two = cv2.imread(problem.figures["2"].visualFilename)
            three = cv2.imread(problem.figures["3"].visualFilename)
            four = cv2.imread(problem.figures["4"].visualFilename)
            five = cv2.imread(problem.figures["5"].visualFilename)
            six = cv2.imread(problem.figures["6"].visualFilename)
            seven = cv2.imread(problem.figures["7"].visualFilename)
            eight = cv2.imread(problem.figures["8"].visualFilename)

            
            dpr_A = np.sum(figureA == 0)/np.sum(figureA)
            dpr_B = np.sum(figureB == 0)/np.sum(figureB)
            dpr_C = np.sum(figureC == 0)/np.sum(figureC)
            dpr_D = np.sum(figureD == 0)/np.sum(figureD)
            dpr_E = np.sum(figureE == 0)/np.sum(figureE)
            dpr_F = np.sum(figureF == 0)/np.sum(figureF)
            dpr_G = np.sum(figureG == 0)/np.sum(figureG)
            dpr_H = np.sum(figureH == 0)/np.sum(figureH)

  

            choices = [one,two,three,four,five,six,seven,eight]

            if abs(1-((dpr_A+dpr_B)/dpr_C))<0.06 and abs(1-((dpr_D+dpr_E)/dpr_F))<0.06:
                print("Yes")
                result_DPR = dpr_G+dpr_H
                print(result_DPR)
                number = 0 
                answer = -1
                for choice in choices:
                    number +=1
                    DPR_Choice = np.sum(choice == 0)/np.sum(choice) 
                    print("Choice:", DPR_Choice)
                    print("how close:", abs(1-(DPR_Choice/result_DPR)))
                    if abs(1-(DPR_Choice/result_DPR))<0.06:
                        print("right now")
                        answer = number
                        return number 
            elif abs(1-((dpr_A+dpr_D)/dpr_G))<0.06 and abs(1-((dpr_B+dpr_E)/dpr_H))<0.06:
                print("Yes")
                result_DPR = dpr_C+dpr_F
                print(result_DPR)
                number = 0 
                answer = -1
                for choice in choices:
                    number +=1
                    DPR_Choice = np.sum(choice == 0)/np.sum(choice) 
                    print("Choice:", DPR_Choice)
                    print("how close:", abs(1-(DPR_Choice/result_DPR)))
                    if abs(1-(DPR_Choice/result_DPR))<0.06:
                        print("right now")
                        answer = number
                        return number 
            else:
                DPRRow1 = dpr_B + dpr_A + dpr_C
                DPRRow2 = dpr_D + dpr_E + dpr_F
                RowAVG = (DPRRow1 + DPRRow2)/2
                DPRColumn1 = dpr_A + dpr_D + dpr_G
                DPRColumn2 = dpr_B+dpr_E+dpr_H
                ColumnAVG = (DPRColumn1+DPRColumn2)/2
        

                smallest_diff = 100000000000
                answer = -1
                number = 0
                for choice in choices:
                    number+=1
                    DPR_Choice = np.sum(choice == 0)/np.sum(choice) 
                    Choice_row = dpr_C+dpr_F+DPR_Choice
                    choice_column = dpr_G + dpr_H + DPR_Choice
                    row_diff = abs(RowAVG - Choice_row)
                    column_diff = abs(ColumnAVG - choice_column)
                    diff_total = row_diff + column_diff
                    if diff_total < smallest_diff:
                        smallest_diff = diff_total
                        answer = number

        
            return answer



            

        else:
            A = problem.figures["A"]
            B = problem.figures["B"]
            C = problem.figures["C"]

            one = problem.figures["1"]
            two = problem.figures["2"]
            three = problem.figures["3"]
            four = problem.figures["4"]
            five = problem.figures["5"]
            six = problem.figures["6"]

            row1 = [A,B]
            column1 = [A,C]
            figures =[A,B,C]
            choices = [one,two,three,four,five,six,]

            if list(A.getdata()) == list(B.getdata()):
                if list(A.getdata()) == list(C.getdata()):
                    for choice in choices:
                        if list(A.getdata()) == list(choice.getdata()):
                            answer = choice
                else:
                    for choice in choices:
                        if list(C.getdata()) == list(choice.getdata()):
                            answer = choice
            elif list(A.getdata()) == list(C.getdata()):
                for choice in choices:
                    if list(B.getdata()) == list(choice.getdata()):
                        answer = choice
            else:
                    row = (np.sum(A == 0))+(np.sum(B == 0))
                    column = (np.sum(A==0))+(np.sum(C==0))

                    smallest_diff = 100000000000
                    for choice in choices:
                        Choice_row = np.sum(C ==0) + np.sum(choice ==0)
                        choice_column = np.sum(B ==0) +np.sum(choice ==0)
                        row_diff = abs(row - Choice_row)
                        column_diff = abs(column - choice_column)
                        diff_total = row_diff + column_diff
                        if diff_total <= smallest_diff:
                            smallest_diff = diff_total
                            answer = choice
                    
                            if np.array_equal(answer,one) :
                                return 1
                            if np.array_equal(answer,two):
                                return 2
                            if np.array_equal(answer,three):
                                return 3
                            if np.array_equal(answer,four):
                                return 4
                            if np.array_equal(answer,five):
                                return 5
                            if np.array_equal(answer,six):
                                return 6
                            if np.array_equal(answer,seven):
                                return 7
                            if np.array_equal(answer,eight):
                                return 8
                            else:
                                return -1 


            '''DPRRow = find_DPR(A)+find_DPR(B)
            DPRColumn = find_DPR(A)+find_DPR(C)

            smallest_diff = 100000000000
            for choice in choices:
                Choice_row = find_DPR(C)+find_DPR(choice)
                choice_column = find_DPR(B) +find_DPR(choice)
                row_diff = abs(DPRRow - Choice_row)
                column_diff = abs(DPRColumn - choice_column)
                diff_total = row_diff + column_diff
                if diff_total < smallest_diff:
                    smallest_diff = diff_total
                    answer = choice'''

        def find_DPR(img):
            pic = cv2.imread(img)
            percentage = np.sum(pic == 0) / np.sum(pic)
            return percentage


        '''def same_image(img1, img2):
            np.sum(B ==0) == np
            if diff.getbbox():
                return False
            else:
                return True'''



        

  


    




