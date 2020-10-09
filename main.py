from model.check import Classify
crop1 = 472.45276
cropfi = {}
cropfi['x1'] = 472.45276
cropfi['y1'] = 531.41583
cropfi['x2'] = 752.09204
cropfi['y2'] = 1119.4039
print(cropfi)
crop = {'x1': 472.45276, 'y1': 531.41583, 'x2': 752.09204, 'y2': 1119.4039}
print(crop)
predict = Classify("./top_long.pt")
prediction = predict.predict("./1.jpg", cropfi)

if prediction == 0:
    print('hoodie')
if prediction == 1:
    print ('long blouse')
if prediction == 2:
    print ('long_shirt')
if prediction == 3:
    print ('long_tee')
if prediction == 4:
    print ('sweater')
if prediction == 5:
    print ('turtleneck')
if prediction == 6:
    print ('leather')
if prediction == 7:
    print ('parka')
if prediction == 8:
    print ('trench_coat')
