from pydantic import BaseModel

class C1(BaseModel):
    a: int | None

class C2(C1):
    b: int | None

c_1 = C1(a=1)
c_1.a = None

c_2 = C2(a=1, b=2)

c_2.a = None
c_2.b = None
