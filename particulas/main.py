from easymunk import Arbiter, Body, Vec2d, ShapeFilter, pyxel as phys
import pyxel
import random

FPS = 30
WIDTH, HEIGHT = 256, 196
SCREEN = Vec2d(WIDTH, HEIGHT)


class Particles:
    def __init__(self, space):
        self.particles = []
        self.space = space

    def draw(self, camera=pyxel):
        for p in self.particles:
            x, y = p.position
            if random.random() < 0.45:
                camera.rect(x, y, 3, 3, self.get_color(p.duration))
            else:
                camera.pset(x, y, self.get_color(p.duration))

    def update(self):
        for p in self.particles.copy():
            p.velocity = p.velocity.rotated(random.uniform(-5, 5))
            p.duration -= 1
            if p.duration <= 0:
                self.particles.remove(p)
                p.detach()

    def emmit(self, position, velocity):
        p = self.space.create_circle(
            radius=1,
            mass=0.1,
            moment=float("inf"),
            position=position,
            velocity=velocity,
            filter=ShapeFilter(group=1),
        )
        p.duration = 105 - random.expovariate(1 / 10)
        p.velocity_func = self.update_velocity
        self.particles.append(p)

    def update_velocity(self, body, gravity, damping, dt):
        body.update_velocity(body, -gravity / 2, 0.99, dt)

    def get_color(self, t):
        if t > 95:
            return pyxel.COLOR_DARKBLUE
        elif t > 80:
            return pyxel.COLOR_NAVY
        elif t > 65:
            return pyxel.COLOR_LIGHTBLUE
        elif t > 40:
            return pyxel.COLOR_CYAN
        elif t > 25:
            return pyxel.COLOR_WHITE
        else:
            return pyxel.COLOR_GRAY


class Particlesflare:
    def __init__(self, space):
        self.particles = []
        self.space = space

    def draw(self, camera=pyxel):
        for p in self.particles:
            x, y = p.position
            r = p.radius
            if random.random() < 0.45:
                camera.rect(x, y, 4, 4, self.get_color(p.duration))
            else:
                camera.pset(x, y, self.get_color(p.duration))

    def update(self):
        for p in self.particles.copy():
            p.velocity = p.velocity.rotated(random.uniform(-5, 5))
            p.duration -= 1
            if p.duration <= 0:
                self.particles.remove(p)
                p.detach()

    def emmit_end(self, position, velocity):
        p = self.space.create_circle(
            radius=15,
            mass=0.1,
            moment=float("inf"),
            position=position,
            velocity=velocity,
            filter=ShapeFilter(group=1),
        )
        p.duration = 55 - random.expovariate(1 / 10)
        p.velocity_func = self.update_velocity
        self.particles.append(p)

    def emmit_flare(self, position, velocity):
        p = self.space.create_circle(
            radius=1,
            mass=0.1,
            moment=float("inf"),
            position=position,
            velocity=velocity,
            filter=ShapeFilter(group=1),
        )
        p.duration = 205 - random.expovariate(1 / 10)
        p.velocity_func = self.update_velocity
        self.particles.append(p)

    def update_velocity(self, body, gravity, damping, dt):
        body.update_velocity(body, -gravity / 2, 0.99, dt)

    def get_color(self, t):
        if t > 95:
            return pyxel.COLOR_YELLOW
        elif t > 80:
            return pyxel.COLOR_ORANGE
        elif t > 65:
            return pyxel.COLOR_RED
        elif t > 40:
            return pyxel.COLOR_ORANGE
        elif t > 25:
            return pyxel.COLOR_YELLOW
        else:
            return pyxel.COLOR_GRAY

class Particlesexplosion:
    def __init__(self, space):
        self.particles = []
        self.space = space

    def draw(self, camera=pyxel):
        for p in self.particles:
            x, y = p.position
            r = p.radius
            if random.random() < 0.45:
                camera.rect(x, y, 3, 3, self.get_color(p.duration))
            else:
                camera.pset(x, y, self.get_color(p.duration))

    def update(self):
        for p in self.particles.copy():
            p.velocity = p.velocity.rotated(random.uniform(-5, 5))
            p.duration -= 1
            if p.duration <= 0:
                self.particles.remove(p)
                p.detach()

    def emmit(self, position, velocity):
        p = self.space.create_circle(
            radius=1,
            mass=0.1,
            moment=float("inf"),
            position=position,
            velocity=velocity,
            filter=ShapeFilter(group=1),
        )
        p.duration = 105 - random.expovariate(1 / 10)
        p.velocity_func = self.update_velocity
        self.particles.append(p)

    def update_velocity(self, body, gravity, damping, dt):
        body.update_velocity(body, -gravity / 2, 0.99, dt)

    def get_color(self, t):
        if t > 95:
            return pyxel.COLOR_RED
        elif t > 80:
            return pyxel.COLOR_YELLOW
        elif t > 65:
            return pyxel.COLOR_PURPLE
        elif t > 40:
            return pyxel.COLOR_RED
        elif t > 25:
            return pyxel.COLOR_YELLOW
        else:
            return pyxel.COLOR_GRAY


class Particlesbarrer:
    def __init__(self, space):
        self.particles = []
        self.space = space

    def draw(self, camera=pyxel):
        for p in self.particles:
            x, y = p.position
            r = p.radius
            if random.random() < 0.55:
                camera.rect(x, y, 4, 4, self.get_color(p.duration))
            else:
                camera.pset(x, y, self.get_color(p.duration))

    def update(self):
        for p in self.particles.copy():
            p.velocity = p.velocity.rotated(random.uniform(-5, 5))
            p.duration -= 1
            if p.duration <= 0:
                self.particles.remove(p)
                p.detach()

    def emmit(self, position, velocity):
        p = self.space.create_circle(
            radius=1,
            mass=0.1,
            moment=float("inf"),
            position=position,
            velocity=velocity,
            filter=ShapeFilter(group=1),
        )
        p.duration = 55 - random.expovariate(1 / 10)
        p.velocity_func = self.update_velocity
        self.particles.append(p)

    def update_velocity(self, body, gravity, damping, dt):
        body.update_velocity(body, -gravity / 2, 0.99, dt)

    def get_color(self, t):
        if t > 95:
            return pyxel.COLOR_WHITE
        elif t > 80:
            return pyxel.COLOR_GRAY
        elif t > 65:
            return pyxel.COLOR_WHITE
        elif t > 40:
            return pyxel.COLOR_GRAY
        elif t > 25:
            return pyxel.COLOR_WHITE
        else:
            return pyxel.COLOR_GRAY

#
# MOON LANDER (SISTEMA DE PARTÍCULAS)
#
class Game:
    PLAYER_SHAPE = [(0, 6), (-3, -3), (+3, -3)]
    PLAYER_SHAPE_END = [(0, 0), (-3, -3), (3, -3)]
    BASE_SHAPE = (25, 5)
    PLAYER_SPEED = 90
    PLAYER_COLOR = pyxel.COLOR_GRAY
    BASE_COLOR = pyxel.COLOR_ORANGE
    GRAVITY = Vec2d(0, -25)
    THRUST = -3 * GRAVITY
    ANGULAR_VELOCITY = 180
    FLOOR_STEP = 30
    FLOOR_DY = 15
    FLOOR_N = 42
    PLAYER_COL_TYPE = 1
    BASE_COL_TYPE = 2
    FLOOR_COL_TYPE = 3
    MAX_IMPULSE = 30

    def __init__(self):
        self.space = space = phys.space(
            gravity=self.GRAVITY,
            camera=phys.Camera(flip_y=True),
            friction=1,
        )
        self.landed = False
        self.victory = False

        # Cria jogador
        self.player = space.create_poly(
            self.PLAYER_SHAPE,
            mass=1,
            moment=2,
            position=SCREEN / 2,
            friction=1.0,
            collision_type=self.PLAYER_COL_TYPE,
            filter=ShapeFilter(group=1),
        )
        self.particles = Particles(space)
        self.particlesflare = Particlesflare(space)
        self.particlesexplosion = Particlesexplosion(space)
        self.particlesbarrer = Particlesbarrer(space)


        # Cria base
        dx = random.uniform(-WIDTH, WIDTH)
        self.base = space.create_box(
            self.BASE_SHAPE,
            position=self.player.position + (dx, -0.45 * HEIGHT),
            friction=1.0,
            collision_type=self.BASE_COL_TYPE,
            body_type=Body.STATIC,
        )

        # Cria chão
        shape = list(self.base.shapes)[0]
        bb = shape.cache_bb()
        self.make_floor(bb.right, bb.bottom, self.FLOOR_STEP, self.FLOOR_DY)
        self.make_floor(bb.left, bb.bottom, -self.FLOOR_STEP, self.FLOOR_DY)

        # Escuta colisões entre base/chão e jogador
        space.collision_handler(
            self.PLAYER_COL_TYPE, self.BASE_COL_TYPE, post_solve=self.on_land
        )
        self.space.collision_handler(
            self.PLAYER_COL_TYPE, self.FLOOR_COL_TYPE, begin=self.on_collision
        )

    def on_collision(self, arb: Arbiter):
        self.landed = True
        self.victory = False
        return True

    def on_land(self, arb: Arbiter):
        if not self.landed:
            self.victory = arb.total_impulse.length < self.MAX_IMPULSE
        self.landed = True

    def make_floor(self, x, y, step, dy):
        body = self.space.static_body

        a = Vec2d(x, y)
        for _ in range(self.FLOOR_N):
            b = a + (step, random.uniform(-dy, dy))
            body.create_segment(a, b, 1, collision_type=self.FLOOR_COL_TYPE)
            a = b

    def update(self):

        if not self.landed:
            if pyxel.btn(pyxel.KEY_LEFT):
                self.player.angular_velocity = +self.ANGULAR_VELOCITY

                # Propulsor Lateral

                for _ in range(1):
                    self.particles.emmit(
                        position=self.player.local_to_world((3, -3)),
                        velocity=-random.uniform(40, 60) * self.player.rotation_vector.perpendicular(),
                    )
            elif pyxel.btn(pyxel.KEY_RIGHT):
                self.player.angular_velocity = -self.ANGULAR_VELOCITY

                # Propulsor Lateral

                for _ in range(1):
                    self.particles.emmit(
                        position=self.player.local_to_world(((-3), -3)),
                        velocity=-random.uniform(40, 60) * self.player.rotation_vector.perpendicular(),
                    )
            else:
                self.player.angular_velocity = 0.0

            if pyxel.btn(pyxel.KEY_UP):
                self.player.apply_force_at_local_point(4 * self.THRUST)

                for _ in range(3):
                    self.particles.emmit(
                        position=self.player.local_to_world((random.uniform(-2, 2), -3)),
                        velocity=-random.uniform(70, 100) * self.player.rotation_vector.perpendicular(),
                    )

            # Barreira do som;

            if 200 < self.player.velocity.y < 202 or 200 < self.player.velocity.x < 202 or -200 < self.player.velocity.y < -202 or -200 < self.player.velocity.x < -202:
                for _ in range(100):
                    self.particlesbarrer.emmit(
                        position=self.player.local_to_world((random.uniform(0, 0), -3)),
                        velocity=60 * self.player.rotation_vector.perpendicular().rotated(random.uniform(0, 360)),
                    )

            # Barreira do som (extra);

            if 700 < self.player.velocity.y < 702 or 700 < self.player.velocity.x < 702 or -700 < self.player.velocity.y < -702 or -700 < self.player.velocity.x < -702:
                for _ in range(100):
                    self.particlesbarrer.emmit(
                        position=self.player.local_to_world((random.uniform(0, 0), -3)),
                        velocity=100 * self.player.rotation_vector.perpendicular().rotated(random.uniform(0, 360)),
                    )

            # Idéia de tiro;

            if pyxel.btnp(pyxel.KEY_SPACE):
                for _ in range(1):
                    self.particlesflare.emmit_flare(
                        position=self.player.local_to_world((random.uniform(0, 0), -3)),
                        velocity=-random.uniform(-700, -700) * self.player.rotation_vector.perpendicular(),
                    )

            # Fogos de artificio ou Tiro Especial;

            if pyxel.btnp(pyxel.KEY_F):
                for _ in range(2):
                    for _ in range(80):
                        self.particlesexplosion.emmit(
                             position=self.player.local_to_world((random.uniform(0, 0), -3)),
                             velocity=-random.uniform(-150, -150) * self.player.rotation_vector.perpendicular().rotated(random.uniform(0, 360)),
                        )

            # Sistemas de Flares;

            if pyxel.btnp(pyxel.KEY_DOWN):
                for _ in range(3):
                    self.particlesflare.emmit_flare(
                        position=self.player.local_to_world((random.uniform(3, -3), -3)),
                        velocity=-random.uniform(-60, 60) * self.player.rotation_vector.perpendicular(),
                    )

        # Fogo, Fumaça e explosão;

        elif self.landed:
            if self.victory:
                self.base.color = self.BASE_COLOR
            else:
                if self.player.mass == 1:
                    for _ in range(100):
                        self.particlesexplosion.emmit(
                            position=self.player.local_to_world((random.uniform(0, 0), -3)),
                            velocity=80 * self.player.rotation_vector.perpendicular().rotated(random.uniform(0, 360)),
                        )
                for _ in range(8):
                    self.particlesflare.emmit_end(
                        position=self.player.local_to_world((random.uniform(2, -2), -3)),
                        velocity=-random.uniform(-40, -70) * self.player.rotation_vector.perpendicular(),
                    )
                self.player = self.space.create_poly(
                    self.PLAYER_SHAPE_END,
                    mass=0.1,
                    moment=2,
                    position=self.player.position,
                    friction=1.0,
                    collision_type=self.PLAYER_COL_TYPE,
                    filter=ShapeFilter(group=1),
                )

        dt = 1 / FPS
        self.particles.update()
        self.particlesflare.update()
        self.particlesexplosion.update()
        self.particlesbarrer.update()
        self.space.step(dt, sub_steps=4)
        self.space.camera.follow(self.player.position)

    def draw(self):
        pyxel.cls(0)
        camera = self.space.camera
        camera.draw(self.space.static_body)
        camera.draw(self.base)
        self.particles.draw(camera)
        self.particlesflare.draw(camera)
        self.particlesexplosion.draw(camera)
        self.particlesbarrer.draw(camera)
        camera.draw(self.player)

        if self.landed:
            msg = "PARABENS!" if self.victory else "PERDEU :("
            x = WIDTH / 2 - len(msg) * pyxel.FONT_WIDTH / 2
            pyxel.text(x, HEIGHT // 2 - 20, msg, pyxel.COLOR_RED)


game = Game()
pyxel.init(WIDTH, HEIGHT, fps=FPS)
pyxel.mouse(True)
pyxel.run(game.update, game.draw)
