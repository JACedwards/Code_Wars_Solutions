def reverse(st):

    x = st.split()
    print(x)
    x.reverse()
    print(x)
    x = ' '.join(x)
    return x


print(reverse("Hi There."))