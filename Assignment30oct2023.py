#Program 1:

#Find the maximum and minimum elements in a tuple.

my_tuple = (15, 8, 25, 36, 42, 10)

Minimum_tuple= min(my_tuple)
maximumm_tuple= max(my_tuple)

print(Minimum_tuple)
print(maximumm_tuple)

#Program 2:

#Find the intersection and union of two sets.

#Intersection
set1 = {1, 2, 3, 4, 5}

set2 = {3, 4, 5, 6, 7}

Commonelements = set1 & set2

print(Commonelements)

Intersection = set1.intersection(set2)
print(Intersection)

Union=set1.union(set2)
print(Union)

#Program 3:

#Remove duplicate elements from a list.

my_list = [1, 2, 2, 3, 4, 4, 5]

print("the old list is ", my_list)
new_list = list(set(my_list))

print(new_list)

#list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print("The original list is : " + str(test_list))

res = []
for i in test_list:
    if i not in res:
        res.append(i)
print(res)

#Convert to Dict JSON Response and Print and Booking Id AND checkin and Checkout Data

Bookinfo= {

"bookingid": 2384,

"booking": {

"firstname": "PRAMOD",

"lastname": "Dutta",

"totalprice": 432,

"depositpaid": False,

"bookingdates": {

"checkin": "2022-01-01",

"checkout": "2022-01-01"

},

"additionalneeds": "Lunch"

}

}
print(type(Bookinfo))
print("Booking id is" ,Bookinfo["bookingid"])

print("Checkin:", Bookinfo["booking"]["bookingdates"]["checkin"])
print("Checkout:", Bookinfo["booking"]["bookingdates"]["checkout"])