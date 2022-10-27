import pandas
import statistics
import plotly.figure_factory as ff

df = pandas.read_csv('StudentsPerformance.csv')

mathList = df['math score'].tolist()
readingList = df['reading score'].tolist()
writingList = df['writing score'].tolist()

mathMean = statistics.mean(mathList)
readingMean = statistics.mean(readingList)
writingMean = statistics.mean(writingList)

mathStDev = statistics.stdev(mathList)
readingStDev = statistics.stdev(readingList)
writingStDev = statistics.stdev(writingList)

#math
math_first_st_dev_start = mathMean - mathStDev
math_first_st_dev_end = mathMean + mathStDev
math_second_st_dev_start = mathMean - (2 * mathStDev)
math_second_st_dev_end = mathMean + (2 * mathStDev)
math_third_st_dev_start = mathMean - (3 * mathStDev)
math_third_st_dev_start = mathMean + (3 * mathStDev)

math_first_st_dev_result = [result for result in mathList if result > math_first_st_dev_start and result < math_first_st_dev_end]
math_second_st_dev_result = [result for result in mathList if result > math_second_st_dev_start and result < math_second_st_dev_end]
math_third_st_dev_result = [result for result in mathList if result > math_third_st_dev_start and result < math_third_st_dev_end]

math_first_st_dev_percentage = (len(math_first_st_dev_result)/len(mathList)) * 100;
math_second_st_dev_percentage = (len(math_second_st_dev_result)/len(mathList)) * 100;
math_third_st_dev_percentage = (len(math_third_st_dev_result)/len(mathList)) * 100;

print("Math: ")
print("First stdev: ", math_first_st_dev_percentage)
print("Second stdev: ", math_second_st_dev_percentage)
print("Third stdev: ", math_third_st_dev_percentage)

#reading
reading_first_st_dev_start = readingMean - readingStDev
reading_first_st_dev_end = readingMean + readingStDev
reading_second_st_dev_start = readingMean - (2 * readingStDev)
reading_second_st_dev_end = readingMean + (2 * readingStDev)
reading_third_st_dev_start = readingMean - (3 * readingStDev)
reading_third_st_dev_start = readingMean + (3 * readingStDev)

reading_first_st_dev_result = [result for result in readingList if result > reading_first_st_dev_start and result < reading_first_st_dev_end]
reading_second_st_dev_result = [result for result in readingList if result > reading_second_st_dev_start and result < reading_second_st_dev_end]
reading_third_st_dev_result = [result for result in readingList if result > reading_third_st_dev_start and result < reading_third_st_dev_end]

reading_first_st_dev_percentage = (len(reading_first_st_dev_result)/len(readingList)) * 100;
reading_second_st_dev_percentage = (len(reading_second_st_dev_result)/len(readingList)) * 100;
reading_third_st_dev_percentage = (len(reading_third_st_dev_result)/len(readingList)) * 100;

print("\nReading: ")
print("First stdev: ", reading_first_st_dev_percentage)
print("Second stdev: ", reading_second_st_dev_percentage)
print("Third stdev: ", reading_third_st_dev_percentage)

#writing
writing_first_st_dev_start = writingMean - writingStDev
writing_first_st_dev_end = writingMean + writingStDev
writing_second_st_dev_start = writingMean - (2 * writingStDev)
writing_second_st_dev_end = writingMean + (2 * writingStDev)
writing_third_st_dev_start = writingMean - (3 * writingStDev)
writing_third_st_dev_start = writingMean + (3 * writingStDev)

writing_first_st_dev_result = [result for result in writingList if result > writing_first_st_dev_start and result < writing_first_st_dev_end]
writing_second_st_dev_result = [result for result in writingList if result > writing_second_st_dev_start and result < writing_second_st_dev_end]
writing_third_st_dev_result = [result for result in writingList if result > writing_third_st_dev_start and result < writing_third_st_dev_end]

writing_first_st_dev_percentage = (len(writing_first_st_dev_result)/len(writingList)) * 100;
writing_second_st_dev_percentage = (len(writing_second_st_dev_result)/len(writingList)) * 100;
writing_third_st_dev_percentage = (len(writing_third_st_dev_result)/len(writingList)) * 100;

print("\nWriting: ")
print("First stdev: ", writing_first_st_dev_percentage)
print("Second stdev: ", writing_second_st_dev_percentage)
print("Third stdev: ", writing_third_st_dev_percentage)

display = [mathList, readingList, writingList]
labels = ['Math Score', 'Reading Score', 'Writing Score']

fig = ff.create_distplot(display, labels, show_hist=False, colors=['lime', 'deeppink', 'teal'])
fig.show()
