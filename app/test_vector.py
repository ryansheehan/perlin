import unittest
from vector import (
    _approx_eq,
    Vector2,
    Vector2Add,
    Vector2Sub,
    Vector2Scale,
    Vector2Dot,
    Vector2Length,
    Vector2LengthSq,
    Vector2Normal,
    Vector3,
    Vector3Add,
    Vector3Sub,
    Vector3Scale,
    Vector3Dot,
    Vector3Length,
    Vector3LengthSq,
    Vector3Normal
)


class TestVector2(unittest.TestCase):
    def test_Vector2Right(self):
        x = Vector2.Right()
        v = Vector2(1., 0.)
        self.assertEqual(x.x, v.x)
        self.assertEqual(x.y, v.y)

    def test_Vector2Up(self):
        y = Vector2.Up()
        v = Vector2(0., 1.)
        self.assertEqual(y.x, v.x)
        self.assertEqual(y.y, v.y)

    def test_Vector2Left(self):
        x = Vector2.Left()
        v = Vector2(-1., 0.)
        self.assertEqual(x.x, v.x)
        self.assertEqual(x.y, v.y)

    def test_Vector2Down(self):
        y = Vector2.Down()
        v = Vector2(0., -1.)
        self.assertEqual(y.x, v.x)
        self.assertEqual(y.y, v.y)

    def test_Vector2Zero(self):
        zero = Vector2.Zero()
        self.assertEqual(zero.x, 0.)
        self.assertEqual(zero.y, 0.)

    def test_Vector2One(self):
        one = Vector2.One()
        self.assertEqual(one.x, 1.)
        self.assertEqual(one.y, 1.)

    def test_Vector2__iter__(self):
        v = Vector2.One()
        for e in v:
            self.assertEqual(e, 1.)

    def test_Vector2__getitem__(self):
        v = Vector2(1., 2.)
        self.assertEqual(v[0], 1.)
        self.assertEqual(v['x'], 1.)
        self.assertEqual(v[1], 2.)
        self.assertEqual(v['y'], 2.)

    def test_Vector2__add__(self):
        a = Vector2(1., 2.)
        b = Vector2(4., 5.)
        c = a + b
        self.assertEqual(c.x, 5.)
        self.assertEqual(c.y, 7.)

    def test_Vector2__sub__(self):
        a = Vector2(4., 5.)
        b = Vector2(1., 2.)
        c = a - b
        self.assertEqual(c.x, 3.)
        self.assertEqual(c.y, 3.)

    def test_Vector2__mul__Vector2(self):
        a = Vector2(2., 2.)
        b = Vector2(1., 2.)
        c = a * b
        r = 2. * 1. + 2. * 2.
        self.assertEqual(c, r)

    def test_Vector2__mul__scalar(self):
        a = Vector2(1., 2.)
        b = 3.
        c = a * b
        self.assertEqual(c.x, 3.)
        self.assertEqual(c.y, 6.)

    def test_Vector2__eq__(self):
        a = Vector2.One()
        b = Vector2(1., 1.)
        c = a == b
        self.assertTrue(c)

    def test_Vector2_getters(self):
        v = Vector2(1., 2.)
        self.assertEqual(v.x, 1.)
        self.assertEqual(v.y, 2.)

    def test_Vector2_setters(self):
        v = Vector2.Zero()
        v.x = 1.
        v.y = 2.
        self.assertEqual(v.x, 1.)
        self.assertEqual(v.y, 2.)

    def test_Vector2_length(self):
        v = Vector2.Random()
        l = v.length
        self.assertTrue(_approx_eq(l, 1., 0.000000001))

    def test_Vector2_length_sq(self):
        v = Vector2.Random()
        v = v * 2.
        l = v.length_sq
        self.assertTrue(_approx_eq(l, 4., 0.000000001))

    def test_Vector2_normal(self):
        v = Vector2.Right() * 2.
        n = v.normal
        self.assertTrue(n == Vector2.Right())
        l = n.length
        self.assertTrue(_approx_eq(l, 1.))

        v = Vector2.Zero()
        n = v.normal
        self.assertTrue(n == Vector2.Zero())
        l = n.length
        self.assertTrue(_approx_eq(l, 0.))

    def test_Vector2_Normalize(self):
        v = Vector2.Right() * 2.
        v.Normalize()
        self.assertTrue(v == Vector2.Right())
        self.assertTrue(_approx_eq(v.length, 1.))
        v = Vector2.Zero()
        v.Normalize()
        self.assertTrue(v == Vector2.Zero())
        self.assertTrue(_approx_eq(v.length, 0.))

    def test_Vector2Add(self):
        a = Vector2(1., 2.)
        b = Vector2(2., 4.)
        c = Vector2Add(a, b)
        self.assertEqual(c.x, 3.)
        self.assertEqual(c.y, 6.)

    def test_Vector2Sub(self):
        a = Vector2(2., 4.)
        b = Vector2(1., 2.)
        c = Vector2Sub(a, b)
        self.assertEqual(c.x, 1.)
        self.assertEqual(c.y, 2.)

    def test_Vector2Dot(self):
        a = Vector2(1., 2.)
        b = Vector2(2., 4.)
        c = Vector2Dot(a, b)
        self.assertEqual(c, 2 + 8)

    def test_Vector2Scale(self):
        v = Vector2(1., 2.)
        sv = v * 3.
        self.assertEqual(sv.x, 3.)
        self.assertEqual(sv.y, 6.)

    def test_Vector2Length(self):
        v = Vector2.Random()
        l = Vector2Length(v)
        self.assertTrue(_approx_eq(l, 1., 0.000000001))

    def test_Vector2LengthSq(self):
        v = Vector2(1., 2.)
        l = Vector2LengthSq(v)
        self.assertEqual(l, 5.)

    def test_Vector2Normal(self):
        v = Vector2.Right() * 3.
        n = Vector2Normal(v)
        self.assertTrue(n == Vector2.Right())
        self.assertTrue(_approx_eq(n.length, 1.))
        v = Vector2.Zero()
        n = Vector2Normal(v)
        self.assertTrue(n == Vector2.Zero())
        self.assertTrue(_approx_eq(n.length, 0.))


class TestVector3(unittest.TestCase):
    def test_Vector3Right(self):
        x = Vector3.Right()
        v = Vector3(1., 0., 0.)
        self.assertEqual(x.x, v.x)
        self.assertEqual(x.y, v.y)
        self.assertEqual(x.z, v.z)

    def test_Vector3Up(self):
        y = Vector3.Up()
        v = Vector3(0., 1., 0.)
        self.assertEqual(y.x, v.x)
        self.assertEqual(y.y, v.y)
        self.assertEqual(y.z, v.z)

    def test_Vector3Backward(self):
        z = Vector3.Backward()
        v = Vector3(0., 0., 1.)
        self.assertEqual(z.x, v.x)
        self.assertEqual(z.y, v.y)
        self.assertEqual(z.z, v.z)

    def test_Vector3Left(self):
        x = Vector3.Left()
        v = Vector3(-1., 0., 0.)
        self.assertEqual(x.x, v.x)
        self.assertEqual(x.y, v.y)
        self.assertEqual(x.z, v.z)

    def test_Vector3Down(self):
        y = Vector3.Down()
        v = Vector3(0., -1., 0.)
        self.assertEqual(y.x, v.x)
        self.assertEqual(y.y, v.y)
        self.assertEqual(y.z, v.z)

    def test_Vector3Forward(self):
        z = Vector3.Forward()
        v = Vector3(0., 0., -1.)
        self.assertEqual(z.x, v.x)
        self.assertEqual(z.y, v.y)
        self.assertEqual(z.z, v.z)

    def test_Vector3Zero(self):
        zero = Vector3.Zero()
        self.assertEqual(zero.x, 0.)
        self.assertEqual(zero.y, 0.)
        self.assertEqual(zero.z, 0.)

    def test_Vector3One(self):
        one = Vector3.One()
        self.assertEqual(one.x, 1.)
        self.assertEqual(one.y, 1.)
        self.assertEqual(one.z, 1.)

    def test_Vector3__iter__(self):
        v = Vector3.One()
        for e in v:
            self.assertEqual(e, 1.)

    def test_Vector3__getitem__(self):
        v = Vector3(1., 2., 3.)
        self.assertEqual(v[0], 1.)
        self.assertEqual(v['x'], 1.)
        self.assertEqual(v['r'], 1.)
        self.assertEqual(v[1], 2.)
        self.assertEqual(v['y'], 2.)
        self.assertEqual(v['g'], 2.)
        self.assertEqual(v[2], 3.)
        self.assertEqual(v['z'], 3.)
        self.assertEqual(v['b'], 3.)

    def test_Vector3__add__(self):
        a = Vector3(1., 2., 3.)
        b = Vector3(4., 5., 6.)
        c = a + b
        self.assertEqual(c.x, 5.)
        self.assertEqual(c.y, 7.)
        self.assertEqual(c.z, 9.)

    def test_Vector3__sub__(self):
        a = Vector3(4., 5., 6.)
        b = Vector3(1., 2., 3.)
        c = a - b
        self.assertEqual(c.x, 3.)
        self.assertEqual(c.y, 3.)
        self.assertEqual(c.z, 3.)

    def test_Vector3__mul__Vector3(self):
        a = Vector3(2., 2., 2.)
        b = Vector3(1., 2., 3.)
        c = a * b
        r = 2. * 1. + 2. * 2. + 2. * 3.
        self.assertEqual(c, r)

    def test_Vector3__mul__scalar(self):
        a = Vector3(1., 2., 3.)
        b = 3.
        c = a * b
        self.assertEqual(c.x, 3.)
        self.assertEqual(c.y, 6.)
        self.assertEqual(c.z, 9.)

    def test_Vector3__eq__(self):
        a = Vector3.One()
        b = Vector3(1., 1., 1.)
        c = a == b
        self.assertTrue(c)

    def test_Vector3_getters(self):
        v = Vector3(1., 2., 3.)
        self.assertEqual(v.x, 1.)
        self.assertEqual(v.r, 1.)
        self.assertEqual(v.y, 2.)
        self.assertEqual(v.g, 2.)
        self.assertEqual(v.z, 3.)
        self.assertEqual(v.b, 3.)

    def test_Vector3_setters(self):
        v = Vector3.Zero()
        v.x = 1.
        v.y = 2.
        v.z = 3.
        self.assertEqual(v.x, 1.)
        self.assertEqual(v.y, 2.)
        self.assertEqual(v.z, 3.)
        v.r = 2.
        v.g = 4.
        v.b = 6.
        self.assertEqual(v.r, 2.)
        self.assertEqual(v.g, 4.)
        self.assertEqual(v.b, 6.)

    def test_Vector3_length(self):
        v = Vector3.Random()
        l = v.length
        self.assertTrue(_approx_eq(l, 1., 0.000000001))

    def test_Vector3_length_sq(self):
        v = Vector3.Random()
        v = v * 2.
        l = v.length_sq
        self.assertTrue(_approx_eq(l, 4., 0.000000001))

    def test_Vector3_normal(self):
        v = Vector3.Right() * 2.
        n = v.normal
        self.assertTrue(n == Vector3.Right())
        l = n.length
        self.assertTrue(_approx_eq(l, 1.))

        v = Vector3.Zero()
        n = v.normal
        self.assertTrue(n == Vector3.Zero())
        l = n.length
        self.assertTrue(_approx_eq(l, 0.))

    def test_Vector3_Normalize(self):
        v = Vector3.Right() * 2.
        v.Normalize()
        self.assertTrue(v == Vector3.Right())
        self.assertTrue(_approx_eq(v.length, 1.))
        v = Vector3.Zero()
        v.Normalize()
        self.assertTrue(v == Vector3.Zero())
        self.assertTrue(_approx_eq(v.length, 0.))

    def test_Vector3Add(self):
        a = Vector3(1., 2., 3.)
        b = Vector3(2., 4., 6.)
        c = Vector3Add(a, b)
        self.assertEqual(c.x, 3.)
        self.assertEqual(c.y, 6.)
        self.assertEqual(c.z, 9.)

    def test_Vector3Sub(self):
        a = Vector3(2., 4., 6.)
        b = Vector3(1., 2., 3.)
        c = Vector3Sub(a, b)
        self.assertEqual(c.x, 1.)
        self.assertEqual(c.y, 2.)
        self.assertEqual(c.z, 3.)

    def test_Vector3Dot(self):
        a = Vector3(1., 2., 3.)
        b = Vector3(2., 4., 6.)
        c = Vector3Dot(a, b)
        self.assertEqual(c, 2 + 8 + 18)

    def test_Vector3Scale(self):
        v = Vector3(1., 2., 3.)
        sv = v * 3.
        self.assertEqual(sv.x, 3.)
        self.assertEqual(sv.y, 6.)
        self.assertEqual(sv.z, 9.)

    def test_Vector3Length(self):
        v = Vector3.Random()
        l = Vector3Length(v)
        self.assertTrue(_approx_eq(l, 1., 0.000000001))

    def test_Vector3LengthSq(self):
        v = Vector3(1., 2., 3.)
        l = Vector3LengthSq(v)
        self.assertEqual(l, 14.)

    def test_Vector3Normal(self):
        v = Vector3.Right() * 3.
        n = Vector3Normal(v)
        self.assertTrue(n == Vector3.Right())
        self.assertTrue(_approx_eq(n.length, 1.))
        v = Vector3.Zero()
        n = Vector3Normal(v)
        self.assertTrue(n == Vector3.Zero())
        self.assertTrue(_approx_eq(n.length, 0.))

if __name__ == '__main__':
    unittest.main()
