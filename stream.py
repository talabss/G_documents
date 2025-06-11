import math
import streamlit as st
"""
Write a function that takes the lengths of the two shorter sides of a right triangle as
its parameters. Return the hypotenuse of the triangle, computed using Pythagorean
theorem, as the function’s result. Include a main program that reads the lengths of
the shorter sides of a right triangle from the user, uses your function to compute the
length of the hypotenuse, and displays the result.
"""
st.title("hypotenus")
adj = st.number_input("enter your adjacent value", value = 0)
opp = st.number_input("enter your adjacent value", value = 0)
def hyp(a,b):
    hyp = math.sqrt(math.pow,(a,2) + math.pow,(b,2))
    return (hyp)
st.write(hyp(adj, opp))


















'''
st.markdown("HELLO")
st.markdown("# HELLO")
st.markdown("## HELLO")
st.markdown("###### HELLO")
'''
























'''
power = math.pow(3,0)

cosine = math.cos(45)
inv_cos = math.acos(0.5253219888177297)

st.write(cosine)

print(power)



add = sum({207, 38, 43, 81, 611})
print(add)


#list
fruits = ["mango", "apple"]
num = [1,2,3,4,5,6]

add2 = sum(num)
print(add2)
'''