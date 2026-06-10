amount=int(input("enter the amount"))
gst=int(input("enter the gst"))
def mygst(amount,gst):
    cgst=(amount*gst)/100
    cal=amount+cgst
    return cal
ans=mygst(amount,gst)
print(ans)
    