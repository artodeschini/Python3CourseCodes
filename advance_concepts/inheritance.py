class A:
    def run(self):
        print("basic run")

    def jump(self):
        print("basic jump")


class B(A):
    def run(self):
        print("run like this")


class C(A):
    def jump(self):
        print("jump like bunny")


class D(B,C):
    pass


d = D()
d.run()
d.jump()